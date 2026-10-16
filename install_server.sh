#!/usr/bin/env bash
# Instala el entorno de inferencia sin modificar el Python del sistema.
set -euo pipefail

REPO_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"

if [[ "${1:-}" == "--help" || "${1:-}" == "-h" ]]; then
    cat <<'HELP'
Uso: bash install_server.sh

Variables opcionales:
  PYTHON_BIN       Intérprete Python >= 3.10 (predeterminado: python3).
  VENV_DIR         Ruta del entorno (predeterminado: .venv-server en el repo).
  TORCH_INDEX_URL  Índice de ruedas PyTorch para una variante CUDA concreta.

Requiere Linux, Python con venv, acceso a Internet y un controlador NVIDIA
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
command -v "$PYTHON_BIN" >/dev/null || {
    echo "No se encontró $PYTHON_BIN. Instala Python 3.10 o posterior." >&2
    exit 1
}
"$PYTHON_BIN" -c 'import sys; sys.exit(0 if sys.version_info >= (3, 10) else "Se requiere Python >= 3.10")'

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
