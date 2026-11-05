#!/usr/bin/env bash
# Instala el entorno de inferencia sin modificar el Python del sistema.
set -euo pipefail

REPO_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"

if [[ "${1:-}" == "--help" || "${1:-}" == "-h" ]]; then
    cat <<'HELP'
Uso: bash install_server.sh

Variables opcionales:
  PYTHON_BIN       Intérprete preferido (predeterminado: python3).
  VENV_DIR         Ruta del entorno (predeterminado: .venv-server en el repo).
  TORCH_INDEX_URL  Índice de ruedas PyTorch para una variante CUDA concreta.

Si Python falta o es anterior a 3.10, instala Python 3.11 mediante uv.
Si falta uv, descarga su instalador oficial (requiere curl).
Con driver NVIDIA 535 selecciona CUDA 11.8, salvo TORCH_INDEX_URL explícito.
Requiere Linux, acceso a Internet y un controlador NVIDIA
compatible para ejecutar el servidor con su configuración CUDA predeterminada.
HELP
    exit 0
fi
if [[ $# -ne 0 ]]; then
    echo "Argumento desconocido. Consulta: bash install_server.sh --help" >&2
    exit 2
fi

PYTHON_BIN="${PYTHON_BIN:-python3}"
VENV_DIR="${VENV_DIR:-$REPO_DIR/.venv-server}"
if [[ "$VENV_DIR" != /* ]]; then
    VENV_DIR="$PWD/$VENV_DIR"
fi
if ! command -v "$PYTHON_BIN" >/dev/null || ! "$PYTHON_BIN" -c \
    'import sys; sys.exit(0 if sys.version_info >= (3, 10) else 1)'; then
    echo "Python >= 3.10 no disponible en $PYTHON_BIN; preparando Python 3.11 con uv."
    if command -v uv >/dev/null; then
        UV_BIN="$(command -v uv)"
    elif [[ -x "$HOME/.local/bin/uv" ]]; then
        UV_BIN="$HOME/.local/bin/uv"
    else
        command -v curl >/dev/null || {
            echo "Se necesita curl para instalar uv. En Ubuntu: sudo apt install curl" >&2
            exit 1
        }
        UV_INSTALLER="$(mktemp)"
        trap 'rm -f -- "$UV_INSTALLER"' EXIT
        curl --proto '=https' --tlsv1.2 -LsSf https://astral.sh/uv/install.sh -o "$UV_INSTALLER"
        UV_INSTALL_DIR="$HOME/.local/bin" UV_NO_MODIFY_PATH=1 sh "$UV_INSTALLER"
        UV_BIN="$HOME/.local/bin/uv"
    fi
    "$UV_BIN" python install 3.11
    PYTHON_BIN="$("$UV_BIN" python find --managed-python 3.11)"
fi
echo "Python seleccionado: $PYTHON_BIN"

if [[ -z "${TORCH_INDEX_URL:-}" ]] && command -v nvidia-smi >/dev/null; then
    NVIDIA_DRIVER="$(nvidia-smi --query-gpu=driver_version --format=csv,noheader 2>/dev/null || true)"
    if [[ "$NVIDIA_DRIVER" == 535.* ]]; then
        TORCH_INDEX_URL="https://download.pytorch.org/whl/cu118"
        echo "Driver NVIDIA 535 detectado: usando PyTorch con CUDA 11.8."
    fi
fi

if ! "$PYTHON_BIN" -m venv "$VENV_DIR"; then
    echo "No se pudo crear el entorno. En Ubuntu/Debian instala python3-venv y vuelve a ejecutar este script." >&2
    exit 1
fi

VENV_PYTHON="$VENV_DIR/bin/python"
export USE_TORCH=1 USE_TF=0
"$VENV_PYTHON" -m pip install --upgrade pip
if [[ -n "${TORCH_INDEX_URL:-}" ]]; then
    "$VENV_PYTHON" -m pip install 'torch>=2.6,<3' --index-url "$TORCH_INDEX_URL"
fi
"$VENV_PYTHON" -m pip install -r "$REPO_DIR/requirements-server.txt"
"$VENV_PYTHON" -m pip check

cd -- "$REPO_DIR"
"$VENV_PYTHON" - <<'PY'
import torch
import transformers
import peft
import accelerate
import bitsandbytes
from qwen_gpsr.runtime.server import QwenRequestHandler

print(f"PyTorch: {torch.__version__} | Transformers: {transformers.__version__}")
print(f"CUDA de PyTorch: {torch.version.cuda} | GPU disponible: {torch.cuda.is_available()}")
if torch.cuda.is_available():
    for index in range(torch.cuda.device_count()):
        print(f"GPU {index}: {torch.cuda.get_device_name(index)}")
    # Comprueba que se puede ejecutar una operación en la GPU.
    print(f"Prueba CUDA: {torch.ones(1, device='cuda').sum().item()}")
else:
    print("Dependencias instaladas; CUDA no está disponible. Revisa el controlador NVIDIA y la variante de PyTorch antes de iniciar el servidor en cuda:0.")
PY

printf '\nEntorno instalado. Para iniciar:\n'
printf 'cd %q\n' "$REPO_DIR"
printf 'source %q\n' "$VENV_DIR/bin/activate"
printf 'USE_TORCH=1 USE_TF=0 python3 server.py --host 127.0.0.1 --port 8008\n'
echo "El adaptador debe estar en models/nl2cd_qwen7b; el modelo base se descarga en el primer arranque."
