# Comparación de cinco ejecuciones — 24 de octubre de 2026

## Alcance y estado

Se consolidan 900 primeros intentos: 60 órdenes × cinco ejecuciones × tres sistemas.
Son 60 órdenes y 28 intenciones, no 300 observaciones lingüísticas independientes por modelo.
R1 procede de las campañas iniciales; R2–R5 corresponden a las repeticiones locales 1–4 de las campañas adicionales.
Se usa la campaña GPT con pausa; la campaña preparada anteriormente sin pausa queda excluida.
No se hicieron nuevas consultas ni se modificaron campañas, referencias o prompts. Esta versión incorpora la decisión explícita sobre DEV-052 y es fuente de los artículos actualizados.

El análisis técnico está completo. El cumplimiento conserva el alcance de la revisión histórica:
no convierte dictámenes propuestos por el asistente en aprobaciones humanas.
Se transfieren dictámenes solo cuando estado, tipo de respuesta, objetivos, plan, mensaje y tipo de error coinciden con R1.
Se revisaron **70 ejecuciones**, agrupadas en **42 variantes de 28 órdenes**, bajo los criterios acordados. La revisión original de variantes fue del asistente. La decisión posterior del autor confirma DEV-052 en las 14 ejecuciones con disparador de seguimiento; el resto conserva su procedencia.
Una variante pendiente no cuenta como fallo ni como acierto; las tablas muestran siempre el denominador completo.

## Decisión del escenario DEV-052

La primera persona encontrada representa a Simone. El ejecutor implementa el caso especial instruct_follow_to_* y sus pasos adicionales. Se acepta el cumplimiento simbólico de 14 ejecuciones, conservando el fallo de GPT R1 que omite ese disparador. Es una condición documentada del escenario, no una excepción que relaje la tarea ni una nueva ejecución física. La decisión y los identificadores figuran en decision_DEV052.json. No quedan dictámenes no verificables en esta versión.

## Resultados técnicos

| Sistema | Ensayos | Plan | Aclaración | Rechazo | Error |
|---|---:|---:|---:|---:|---:|
| Qwen3B | 300 | 290 | 0 | 0 | 10 |
| Qwen7B | 300 | 280 | 0 | 0 | 20 |
| GPT | 300 | 269 | 15 | 16 | 0 |

Generar un plan no implica cumplir la orden. Un error de ejecución tampoco equivale a un rechazo deliberado.

## Consistencia literal

| Sistema | Órdenes con objetivos distintos | Con planes distintos | Con tipo de respuesta distinto |
|---|---:|---:|---:|
| Qwen3B | 0/60 | 0/60 | 0/60 |
| Qwen7B | 0/60 | 0/60 | 0/60 |
| GPT | 4/60 | 24/60 | 1/60 |

Qwen usa generación sin muestreo según los manifiestos: la repetibilidad observada es coherente con esa configuración.
Los valores nulos de los ensayos fallidos también se repiten; no son planes válidos estables.
GPT cambia objetivos en DEV-028,030,049,050; cambia de rechazo a plan en DEV-049.
La variación literal puede ser inocua o funcional: requiere revisar las variantes. No se eliminan indiscriminadamente
acciones say porque varias activan protocolos. La igualdad literal no demuestra corrección ni ejecución física.

## Cumplimiento por bloque bajo criterios declarados

Criterio estricto bajo supuestos declarados. G es el ámbito aprobado del generador; L extensión léxica,
C composición adicional, M múltiples restricciones, A ambigüedad, F fuera de capacidad y X contradicción.
Los supuestos de identidad/protocolo y las excepciones DEV-050/051 siguen la revisión histórica.
Las excepciones solo se transfieren con evidencia idéntica; no se aplican automáticamente a nuevas variantes.

| Bloque | Sistema | Órdenes | Ensayos | Cumple | Incumple | No verificable | No aplicable | Pendiente | Excepciones* |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| G | Qwen3B | 46 | 230 | 220 | 10 | 0 | 0 | 0 | 10 |
| G | Qwen7B | 46 | 230 | 215 | 15 | 0 | 0 | 0 | 10 |
| G | GPT | 46 | 230 | 216 | 14 | 0 | 0 | 0 | 8 |
| L | Qwen3B | 3 | 15 | 15 | 0 | 0 | 0 | 0 | 0 |
| L | Qwen7B | 3 | 15 | 15 | 0 | 0 | 0 | 0 | 0 |
| L | GPT | 3 | 15 | 15 | 0 | 0 | 0 | 0 | 0 |
| C | Qwen3B | 4 | 20 | 15 | 5 | 0 | 0 | 0 | 0 |
| C | Qwen7B | 4 | 20 | 5 | 15 | 0 | 0 | 0 | 0 |
| C | GPT | 4 | 20 | 20 | 0 | 0 | 0 | 0 | 0 |
| M | Qwen3B | 1 | 5 | 0 | 5 | 0 | 0 | 0 | 0 |
| M | Qwen7B | 1 | 5 | 0 | 5 | 0 | 0 | 0 | 0 |
| M | GPT | 1 | 5 | 0 | 5 | 0 | 0 | 0 | 0 |
| A | Qwen3B | 3 | 15 | 0 | 0 | 0 | 15 | 0 | 0 |
| A | Qwen7B | 3 | 15 | 0 | 0 | 0 | 15 | 0 | 0 |
| A | GPT | 3 | 15 | 0 | 0 | 0 | 15 | 0 | 0 |
| F | Qwen3B | 2 | 10 | 0 | 0 | 0 | 10 | 0 | 0 |
| F | Qwen7B | 2 | 10 | 0 | 0 | 0 | 10 | 0 | 0 |
| F | GPT | 2 | 10 | 0 | 0 | 0 | 10 | 0 | 0 |
| X | Qwen3B | 1 | 5 | 0 | 0 | 0 | 5 | 0 | 0 |
| X | Qwen7B | 1 | 5 | 0 | 0 | 0 | 5 | 0 | 0 |
| X | GPT | 1 | 5 | 0 | 0 | 0 | 5 | 0 | 0 |

* Las excepciones son una lectura adicional del escenario, no una categoría sumable a los dictámenes estrictos.
Consultar ANALISIS_CONSISTENCIA.md para argumentos, redundancias y cambios de redacción. Los dictámenes nuevos de GPT son revisión del asistente con evidencia; no atribuirlos a aprobación manual completa del investigador.
Para A/F/X se conserva además domain_response_correct: aclarar/rechazar adecuadamente se evalúa por separado.

## Robustez lingüística

`robustez_tripletas.csv` agrupa las 16 intenciones con tres formulaciones (14 de G, una de C y una de L),
por sistema y repetición. Las 12 órdenes diagnósticas restantes no se mezclan con estas tripletas.
Contiene cuántas formulaciones cumplen y si las tres cumplen; un grupo con pendientes no se declara robusto.
Cinco repeticiones miden consistencia; no amplían el repertorio lingüístico ni son cinco órdenes nuevas.
Reportar éxito por formulación y tripletas completas, conservando separación por bloque.

## Latencia y recursos

`latencias.csv` separa bloque, fase R1/R2–R5 y tipo de respuesta, con n, media, mediana y cuartiles.
La gráfica compara G e incluye los errores. No interpretar fallos rápidos como mayor eficiencia útil.
Las solicitudes adicionales GPT tienen pausa de dos segundos fuera de la latencia individual;
por eso se presentan también separadas de R1. No atribuir diferencias temporales únicamente al modelo.

| Sistema | Fase | n (G, todos los resultados) | Mediana (s) | Q25–Q75 (s) |
|---|---|---:|---:|---:|
| Qwen3B | R1 | 46 | 2.388 | 2.005–2.699 |
| Qwen3B | R2-R5 | 184 | 2.509 | 2.110–2.831 |
| Qwen7B | R1 | 46 | 1.905 | 1.643–2.140 |
| Qwen7B | R2-R5 | 184 | 2.041 | 1.714–2.272 |
| GPT | R1 | 46 | 3.986 | 3.244–5.100 |
| GPT | R2-R5 | 184 | 4.467 | 3.499–5.357 |

| Sistema | Fase | CPU mediana (s) | RAM RSS pico mediano (GiB) | GPU asignador pico mediano (GiB) |
|---|---|---:|---:|---:|
| Qwen3B | R1 | 2.385 (n=60) | 1.658 (n=60) | 2.154 (n=60) |
| Qwen3B | R2-R5 | 2.521 (n=240) | 1.654 (n=240) | 2.155 (n=240) |
| Qwen7B | R1 | 1.874 (n=60) | 1.671 (n=60) | 5.496 (n=60) |
| Qwen7B | R2-R5 | 2.019 (n=240) | 1.665 (n=240) | 5.501 (n=240) |
| GPT | R1 | no disponibles | no disponibles | no disponibles |
| GPT | R2-R5 | no disponibles | no disponibles | no disponibles |

Los recursos internos GPT figuran como **no disponibles**, nunca cero ni consumo del cliente.
`recursos.json` resume solo mediciones internas disponibles, con n observado; los faltantes no se imputan.
En Qwen, CPU y RAM son del proceso servidor durante inferencia; GPU es el pico muestreado del asignador PyTorch,
no memoria total de la tarjeta, energía, coste monetario ni recursos de toda la arquitectura CLIPS.
Las fases se mantienen separadas para no ocultar diferencias de carga o condiciones de ejecución.

## Coste GPT y tokens

Según los importes comunicados por el investigador desde OpenAI Usage:

| Fase | Solicitudes | Coste declarado | Promedio por solicitud |
|---|---:|---:|---:|
| R1 | 60 | US$0.42 | US$0.007000 |
| R2–R5 | 240 | US$1.65 | US$0.006875 |
| Total | 300 | **US$2.07** | **US$0.006900** |

Son importes declarados para estas campañas, no una estimación por tarifa ni una factura verificada independientemente.
No incluyen desarrollo previo ni representan el coste total de propiedad. No se asigna coste cero a Qwen.
`tokens.json` contiene el uso registrado por fase; cached_input_tokens es subconjunto de entrada y
reasoning_tokens de salida: no sumarlos de nuevo a total_tokens.

## Revisión y presentación en el artículo

Abrir `index.html`: cada variante tiene requisitos, texto español/inglés, diferencias respecto de R1 y evidencia completa.
En una **copia** de `variantes_para_revision.csv`, completar decision (pass, fail, not_verifiable o not_applicable) y comment
con justificación y referencia a requisitos. Para aclaraciones/rechazos, indicar también en comment
si la respuesta ante la limitación es adecuada y por qué; not_applicable no significa respuesta adecuada. Las excepciones deben declararse explícitamente, sin convertirlas en
cumplimiento estricto. Este generador no ingiere decisiones editadas: deben integrarse en una nueva versión del reporte,
conservando fuente, autor y fecha de revisión. No editar los registros originales.

La revisión de variantes se detalla en ANALISIS_CONSISTENCIA.md. Presentar: cumplimiento por bloque; mapa de éxito 0/5 por orden y sistema;
robustez de tripletas; consistencia literal frente a funcional; latencia y recursos; coste declarado.
Conservar los ejemplos de fallos persistentes y variaciones relevantes, sin escoger solo el mejor intento.
Si se calculan intervalos o contrastes, agrupar por intención/orden y mantener el emparejamiento entre sistemas;
no tratar los 900 ensayos como muestras independientes. Esta evaluación de desarrollo no demuestra generalización
sobre un conjunto independiente ni ejecución física en el robot.

## Trazabilidad y reproducción

`comprobaciones.json` registra huellas de manifiestos, activos referenciados y comparaciones de configuración.
`trazabilidad.json` inventaría las seis campañas antes y después y verifica que permanecen intactas.
Es lectura histórica: no certifica reproducibilidad del servicio remoto ni igualdad de pesos detrás de un alias.
No se usa el cargador estricto con el código actual para reejecutar campañas antiguas.

Desde la raíz del repositorio:

```bash
MPLCONFIGDIR=/tmp/matplotlib-comparativo python3 reports/comparativo_escenario_20261024/generar_reporte.py
MPLCONFIGDIR=/tmp/matplotlib-comparativo python3 reports/comparativo_escenario_20261024/completar_analisis.py
```

La regeneración sobrescribe los productos derivados; guardar la hoja de decisiones en un archivo distinto.
Este reporte sirve de fuente para la actualización de los artículos; se conserva la versión previa.
