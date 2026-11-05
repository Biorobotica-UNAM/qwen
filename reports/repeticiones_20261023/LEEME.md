> Actualización GPT: usar `gpt_repeticiones_60_pausa_20261023`. Sustituye la campaña GPT preparada pero no ejecutada. Pausa de 2 s entre solicitudes, fuera de la latencia del ensayo; parada tras guardar HTTP 429, sin reintento automático. Los resultados Qwen ya obtenidos no se modifican. El ejecutor cambió de versión: las campañas antiguas se consultan como evidencia histórica, no se reanudan saltando comprobaciones de fuentes.

# Cuatro repeticiones adicionales — 23 de octubre de 2026

Estado: campañas preparadas, ninguna inferencia ejecutada en esta preparación.
Se conservan las tres campañas históricas; las nuevas tienen cuatro repeticiones locales.
La repetición local 1 corresponde a R2 global, 2 a R3, 3 a R4 y 4 a R5.
Cada sistema tendrá 60 × 5 = 300 registros, 900 entre los tres; quedan 720 nuevos,
de los cuales 240 son consultas GPT. No se agregan controles CLIPS como otro modelo.

Se verificaron las campañas históricas con load_campaign y se conservaron los mismos
config_id en las nuevas: código cliente, entorno, prompt, esquema, reglas, adaptador,
metadatos Qwen y parámetros explícitos. Los metadatos Qwen se toman de las copias
históricas para preparar sin conexión; el runner comprueba el servidor efectivo al ejecutar.
No basta que el servidor anuncie 3B/7B: los pesos, normalizador y configuración deben coincidir.

## Ejecución desde la raíz del repositorio

Primero Qwen3B. En una terminal, con el entorno habitual y las variables de autenticación:

```bash
python3 server.py --adapter-path models/nl2cd_qwen3b --port 8008
```

En otra terminal:

```bash
export QWEN_SERVER_URL=http://127.0.0.1:8008
python3 -m experiments.run_qwen_clips check --campaign reports/experiments/qwen3b_repeticiones_60_20261023
python3 -m experiments.run_qwen_clips run --campaign reports/experiments/qwen3b_repeticiones_60_20261023
```

Al terminar y con el servidor libre, detener 3B e iniciar 7B:

```bash
python3 server.py --adapter-path models/nl2cd_qwen7b --port 8008
```

Después:

```bash
python3 -m experiments.run_qwen_clips run --campaign reports/experiments/qwen7b_repeticiones_60_20261023
python3 -m experiments.run_gpt run --campaign reports/experiments/gpt_repeticiones_60_pausa_20261023
```

GPT requiere OPENAI_API_KEY del proyecto de facturación que se documentará; no escribirla
en informes ni comandos compartidos. Las claves Qwen se conservan en sus variables habituales.
No volver a ejecutar init: las campañas ya existen. run reanuda sin repetir resultados
terminados, incluidos fallos. No usar --retry-failed para reemplazar una repetición.
El resumen principal usa el primer intento de cada caso y repetición. Tras timeout Qwen,
respetar la comprobación de disponibilidad del servidor; no saltarse un bloqueo del runner.

## Análisis fijado antes de las nuevas respuestas

- Consistencia: por orden y modelo, comparar cinco ejecuciones; reportar estado de respuesta,
  acuerdo de objetivos, equivalencia de planes y estabilidad del cumplimiento. Separar
  igualdad literal de equivalencia semántica. Un error no desaparece del denominador.
- Reportar tareas cumplidas en las cinco repeticiones y fracción por orden; no llamar a
  las 300 ejecuciones de cada modelo 300 órdenes independientes.
- Robustez: usar las 16 tríadas existentes y comparar canónica/paráfrasis/ruido dentro
  de la misma intención y repetición. Son 14 tríadas G, una C y una L; no mezclar ámbitos.
  Los 12 casos restantes no forman tríadas. Repetir no aumenta la diversidad lingüística.
- Cumplimiento: mantener los criterios de la revisión del 22 de octubre. DEV-050/051
  son excepciones de escenario separadas del incumplimiento estricto. No transferir
  automáticamente un dictamen al nuevo resultado: una salida puede cambiar.
- Latencia: conservar fallos, reportar distribuciones por bloque y modelo, e informar
  fechas, calentamiento y carga. La ejecución por bloques no permite atribuir diferencias
  de latencia únicamente al tamaño del modelo.
- GPT: registrar identificador devuelto y parámetros, y analizar también las cuatro
  repeticiones nuevas sin R1. El identificador estable no certifica pesos idénticos
  del proveedor entre fechas.
- Costos: registrar el importe atribuido por Usage a cada campaña y moneda/unidad,
  separado del uso en tokens y de recursos internos no disponibles. El investigador confirmó US$0.42 (42 centavos) por las 60 solicitudes originales,
  equivalentes a US$0.007 por solicitud. Para 240 consultas adicionales, US$1.68 es
  una proyección al mismo costo medio, no un importe facturado ni garantizado.

Las órdenes y la clasificación no cambian. Las repeticiones nuevas no se presentan como
resultados hasta completarse y revisarse. protocolo.json conserva la vinculación entre campañas.

## Política GPT de envío

La pausa se fija al crear campaña con `--gpt-pause-seconds` (0–60 s; predeterminado 2 s),
y se registra en request_policy. No es garantía contra todos los límites de tokens/cuota.
Un 429 se conserva como error y detiene el lote. Revisar Usage/límites y esperar a que se
resuelva la condición antes de reanudar con el mismo comando. `run` omite el intento
fallido; cualquier recuperación explícita se reporta aparte. No se acumulan reintentos
automáticos. La pausa añade unos 478 segundos a 240 consultas si no hay interrupciones.
La política es distinta de R1 y debe constar al comparar tiempos y comportamiento de caché.
La transición y la vinculación R2–R5 están en pausa_gpt/transicion.json.
