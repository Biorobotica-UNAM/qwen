# Limpieza y revisión documental — 4 de noviembre de 2026

## Alcance

Se revisaron README principal, documentación del planificador, programas de
campaña, guía, cuaderno de desarrollo, protocolo final, informe consolidado y
suite automatizada. El repositorio ya contenía cambios locales; se conservaron.
No se alteraron campañas, respuestas, referencias, pesos ni informes históricos.

## Material retirado

Se retiró `legacy/`: `generator.py`, `egpsr_commands.py`, `gpsr_commands_v1.py`,
`llm.py` y su README. Su documentación los identificaba como prototipos ajenos al
flujo vigente; la búsqueda de referencias en Python y Markdown no encontró
consumidores activos fuera de esa carpeta. El generador soportado sigue siendo
`qwen_gpsr.generation.generate_dataset`. Se actualizaron los enlaces del README.

Respaldo local recuperable: `/tmp/qwen_limpieza_20261104_legacy.tar.gz`.
Los archivos también estaban versionados en Git. El respaldo temporal no es un
artefacto de reproducción ni debe asumirse permanente.

Se eliminaron cachés Python y pytest del código activo. Se regeneran al ejecutar
Python; los patrones de exclusión ya estaban en `.gitignore`.

## Pruebas que se conservan

No se identificaron pruebas automatizadas sin relación con el producto final.
El tamaño o el uso de respuestas simuladas no hacen prescindible una prueba:
los servidores simulados permiten comprobar fallos sin cargar pesos ni usar API.

| Archivos en `tests/` | Aporte al experimento |
|---|---|
| `test_dataset_quality.py`, `test_evaluate_model.py` | Contrato del corpus, cobertura, métricas y artefactos de evaluación |
| `test_experiments.py` | Campañas, control real CLIPS, aislamiento, límites, reanudación, huellas, recursos y denominadores |
| `test_server_metadata.py`, `test_runtime_paths.py`, `test_model_variant.py` | Identidad de configuración, rutas independientes del directorio y selección correcta 3B/7B |
| `test_planner_test_node.py`, `test_planning_protocol.py`, `test_completion_contract.py` | Esquema, interacción, destinos y cierre del plan |
| `test_clips_cleanup.py` | Reutilización de CLIPS y liberación de recursos en campañas largas |
| `test_gpt_request_pacing.py` | Pausas fuera de latencia y parada ante límites del proveedor |

Se conservan los pilotos preliminares y diagnósticos históricos en `reports/`:
explican correcciones y decisiones del piloto. Sus fuentes, copias anteriores y
huellas son evidencia de reproducción; no son entradas de producción. No se
eliminaron reportes previos por diferir del último dictamen.

## Documentación vigente

- `README.md`: entrada, arquitectura Qwen–CLIPS frente a GPT directo y estado experimental.
- `experiments/README.md`: comandos y comportamiento del instrumento actual.
- `docs/experiment/Guia_del_experimento.md`: estado vigente y antecedentes identificados como históricos.
- `docs/experiment/Cuaderno_desarrollo_60.md`: preparación y auditoría del conjunto de desarrollo.
- `reports/comparativo_escenario_20261024/INFORME.md`: consolidación del piloto de 900 primeros intentos.
- `docs/experiment/Protocolo_experimento_final_tesis.md`: propuesta independiente de 300 órdenes, cinco repeticiones y tres condiciones; pendiente de aprobación y congelación.

El soporte local de `at` se comprobó en `experiments/vendor/goal_adapter.py`;
no se certifica con ello la versión del workspace ROS externo. Las versiones
actuales de prompt y reglas no sustituyen las copias históricas de las campañas.

## Verificación realizada

- `python3 -m unittest discover -s tests -v`: 78 pruebas, resultado `OK`, con permiso para abrir sockets locales. La primera ejecución restringida produjo errores `PermissionError` en los servidores simulados.
- Enlaces Markdown locales de los siete documentos revisados: ninguno apunta a un archivo ausente.
- `git diff --check`: sin errores de espacios.
- La suite aún imprime avisos nativos CLIPS `ENVRNMNT8` al finalizar; pasar las pruebas no demuestra ausencia de crecimiento de memoria. No se modificó el motor durante esta limpieza.

No se ejecutaron inferencias reales ni campañas nuevas. No se certificaron las
capacidades físicas de Justina ni la disponibilidad de modelos o proveedores.

## Estabilización posterior de reportes

Con autorización posterior del usuario se archivaron 16 carpetas de reportes
superados y etapas editoriales, después de verificar sus 1,076 archivos mediante
SHA-256. La evidencia científica y los antecedentes requeridos por el consolidado
permanecen activos. El [índice de reportes](../reports/README.md) identifica las
fuentes vigentes y la restauración del archivo histórico. El
[estado estable](Estado_estable_20261104.md) registra los pendientes para retomar
el experimento final; esta limpieza no ejecuta ni congela esa evaluación.
