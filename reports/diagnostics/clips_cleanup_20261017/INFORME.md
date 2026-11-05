# Revisión de memoria de CLIPS — 17 de octubre de 2026

Se reprodujo el aviso ENVRNMNT8 de DEV-010 sin Qwen, HTTP ni ejecución física.
La lectura mediante objetos Fact de clipspy reproducía el problema: 480 bytes y
15 asignaciones no liberadas por ciclo; tras 3 000 ciclos, 1 440 000 bytes y
45 000 asignaciones reportadas al destruir el entorno. Reset, clear y recolección
Python no resolvían esa retención en la implementación anterior.

## Corrección aplicada

`experiments/symbolic.py` mantiene las direcciones de hechos dentro de CLIPS y
extrae índices, nombres, textos y slots como valores simples. No se modifican
reglas, objetivos, planes ni el esquema de resultados. close libera el router y
la referencia al entorno y admite llamadas repetidas.

## Verificación y límites

- Planes y toda la evidencia extraída idénticos antes/después para las 54 fichas
  con objetivos. La comparación incluyó también los casos de límites.
- Regresión de 300 planes en tres entornos: resultados idénticos, sin diagnósticos
  nativos al cerrar. La prueba captura stdout y stderr desde un subproceso.
- 75 tests pasaron. La primera ejecución restringida no pudo abrir los sockets
  locales simulados; se repitió con permiso para esos sockets. No hubo consultas
  a modelos. Algunos verificadores antiguos de la suite todavía usan objetos
  Fact y emiten ENVRNMNT8; no son la extracción experimental corregida.
- Estrés, 3 000 planificaciones en el mismo entorno: antes, RSS de 25 305 088 a
  45 740 032 bytes; después, de 25 280 512 a 28 971 008 bytes. La versión corregida
  cerró sin ENVRNMNT8.
- Sigue existiendo crecimiento residual: no se afirma ausencia de acumulación.
  También se observó crecimiento de mem-used al ejecutar reglas sin extraer
  hechos. Su causa interna no quedó determinada. La devolución completa al
  sistema operativo se obtiene al terminar el proceso trabajador de la campaña;
  no se presupone que reset libere toda su memoria.

## Siguiente paso

Crear una campaña nueva para las diez órdenes iniciales con Qwen7B y el control,
con una repetición. Revisar planes, focus, errores y recursos antes de ampliar a
60. Vigilar la evolución del consumo del cliente; si sigue creciendo de forma
relevante, estudiar el ciclo de vida del motor o reciclar trabajadores con la
inicialización registrada separadamente. Las mediciones de esta prueba local
no incluyen recursos del servidor Qwen.

El código de extracción cambió: no reanudar una campaña histórica con sus huellas
anteriores. Conservar sus resultados; crear un nuevo manifiesto. No hace falta
reiniciar Qwen por este cambio del cliente.

## Evidencia reproducible

Desde la raíz del repositorio:

```bash
PYTHONPATH=. python3 reports/diagnostics/clips_cleanup_20261017/measure_memory.py before
PYTHONPATH=. python3 reports/diagnostics/clips_cleanup_20261017/measure_memory.py after
python3 -m unittest discover -s tests -p test_clips_cleanup.py -v
```

`symbolic_before.py` es una copia histórica para reproducir el diagnóstico;
no se utiliza en las campañas. Logs y mediciones numéricas acompañan este informe.
