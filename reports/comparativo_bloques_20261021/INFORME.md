# Comparativo por bloques aprobados y revisión de cumplimiento

21 de octubre de 2026. **Clasificación aprobada; dictámenes del asistente pendientes de aprobación del investigador.**
180 primeros intentos guardados, 60 por sistema, una repetición. No se ejecutaron modelos,
no se cambió ninguna campaña ni se recalificó el formato como si fuera cumplimiento.
Este informe actualiza la interpretación del reporte del 17 de octubre; sus métricas históricas se conservan.

## Cómo leer los resultados

G es el ámbito del generador local ampliado, no una certificación del dominio oficial GPSR.
L, C, M, A, F y X se presentan separados, según la clasificación aprobada. DEV-050 y DEV-051
permanecen en G: sus objetivos son interpretables por el generador y los planes pierden
respectivamente el filtro de vestimenta y la distinción peso/tamaño. Esas limitaciones
no se eliminan del denominador principal. DEV-054 conserva Water como objeto y no se penaliza
por diferir del control CLIPS defectuoso.

Cumple significa que la revisión encuentra las subtareas y dependencias simbólicas;
incumple, una omisión/sustitución comprobada o falta de plan en una tarea aplicable.
No verificable señala evidencia insuficiente del contrato ejecutor; no es acierto ni fallo.
No aplicable corresponde a A/F/X, donde se puntúa por separado la respuesta de aclaración o rechazo.
Un incumplimiento comprobado prevalece aunque exista además una parte no verificable.
Los errores permanecen en su bloque y denominador; HTTP 422 no cuenta como rechazo deliberado.

La fracción cumple/n representa cumplimiento confirmado por esta revisión, no una tasa final
que presuponga fallidos los no verificables. Mostrar siempre sus cuatro conteos. No se publica
un ranking global ni se suman planes correctos y rechazos correctos como si fueran lo mismo.

## Resultado principal: G (46 órdenes, 18 intenciones por sistema)

| Sistema | Cumple | Incumple | No verificable | Confirmados / total | Objetivos semánticamente correctos |
|---|---:|---:|---:|---:|---:|
| Qwen3B | 22 | 2 | 22 | 22/46 (47.8 %) | 46/46 |
| Qwen7B | 22 | 3 | 21 | 22/46 (47.8 %) | 45/46 |
| GPT | 22 | 4 | 20 | 22/46 (47.8 %) | 46/46 |

La fidelidad de objetivos admite equivalencias semánticas revisadas (por ejemplo sintaxis de
entrega, singular/plural de vestimenta y capitalización); no sustituye la métrica histórica
de coincidencia literal. La exactitud del objetivo y el cumplimiento del plan son ejes distintos.

## Todos los bloques

| Bloque | Sistema | n | Intenciones | Cumple | Incumple | No verificable | No aplicable | Respuesta de límite adecuada |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| G | Qwen3B | 46 | 18 | 22 | 2 | 22 | 0 | — |
| G | Qwen7B | 46 | 18 | 22 | 3 | 21 | 0 | — |
| G | GPT | 46 | 18 | 22 | 4 | 20 | 0 | — |
| L | Qwen3B | 3 | 1 | 3 | 0 | 0 | 0 | — |
| L | Qwen7B | 3 | 1 | 3 | 0 | 0 | 0 | — |
| L | GPT | 3 | 1 | 3 | 0 | 0 | 0 | — |
| C | Qwen3B | 4 | 2 | 3 | 1 | 0 | 0 | — |
| C | Qwen7B | 4 | 2 | 1 | 3 | 0 | 0 | — |
| C | GPT | 4 | 2 | 4 | 0 | 0 | 0 | — |
| M | Qwen3B | 1 | 1 | 0 | 1 | 0 | 0 | 0/1 |
| M | Qwen7B | 1 | 1 | 0 | 1 | 0 | 0 | 0/1 |
| M | GPT | 1 | 1 | 0 | 1 | 0 | 0 | 1/1 |
| A | Qwen3B | 3 | 3 | 0 | 0 | 0 | 3 | 0/3 |
| A | Qwen7B | 3 | 3 | 0 | 0 | 0 | 3 | 0/3 |
| A | GPT | 3 | 3 | 0 | 0 | 0 | 3 | 3/3 |
| F | Qwen3B | 2 | 2 | 0 | 0 | 0 | 2 | 0/2 |
| F | Qwen7B | 2 | 2 | 0 | 0 | 0 | 2 | 0/2 |
| F | GPT | 2 | 2 | 0 | 0 | 0 | 2 | 2/2 |
| X | Qwen3B | 1 | 1 | 0 | 0 | 0 | 1 | 0/1 |
| X | Qwen7B | 1 | 1 | 0 | 0 | 0 | 1 | 0/1 |
| X | GPT | 1 | 1 | 0 | 0 | 0 | 1 | 1/1 |

En M/DEV-049, GPT no cumple la tarea executable de la referencia, pero reconoce explícitamente
la limitación. La adecuación de ese rechazo es una lectura diagnóstica retrospectiva,
separada del cumplimiento original. En A/F/X, la adecuación usa el criterio original y el
contenido de las respuestas. Los Qwen no tienen el mismo contrato conversacional que GPT:
la comparación describe las arquitecturas configuradas, no una capacidad intrínseca aislada.

## Revisión por caso: hallazgos

- C/DEV-001–003: 7B confunde el segundo destino o no devuelve JSON válido; 3B y GPT conservan las visitas.
- C/DEV-053: 3B coloca la taza en bed en vez de completar la primera entrega; 7B y GPT conservan ambas entregas.
- G/DEV-029: 7B sustituye orange por orange coat. Es error de interpretación dentro del ámbito previsto.
- G/DEV-024: GPT cierra focus antes de terminar la interacción de guía.
- G/DEV-050–051: los tres sistemas interpretan el atributo pero sus planes incumplen la restricción.
- G/DEV-052: GPT anuncia seguimiento pero omite instruct_follow_to_bedroom; en Qwen queda pendiente identidad/trazabilidad del consumidor.
- L/DEV-016–018: los planes conservan la colocación en table; ese cumplimiento no elimina la extensión léxica aprobada.
- A/DEV-055–057: GPT solicita la información faltante; Qwen genera referentes no resueltos o error.
- F/X/DEV-058–060: GPT explica limitación o contradicción; Qwen sustituye acciones o devuelve error.

Los detalles y planes completos de las 180 filas están en index.html y revision_por_caso.jsonl;
el CSV permite anotar decisiones sin tocar las campañas.

## Evidencia adicional del ejecutor actual

Se inspeccionaron FollowSequence, Say y Listen de Justina (huellas en trazabilidad.json).
El supervisor reconoce instruct_follow_only e instruct_follow_to_<destino>, activa/desactiva
seguimiento y para destinos comprueba llegada o timeout. Por tanto no es correcto afirmar
que esas claves sean solamente texto sin consumidor. DEV-025–027 son compatibles con el
protocolo actual, pero se conserva no_verificable histórico: ese código no estaba congelado
como evidencia del consumidor en las campañas. GPT/052 sigue omitiendo el disparador.

Listen almacena el dato extraído y Say consulta Knowledge. Esto aporta evidencia parcial
para DEV-037–039; falta verificar la resolución histórica completa de guest_name_last y
saved_name. En las búsquedas por nombre falta cerrar cómo se compara el nombre solicitado
con el observado: preguntar a cualquiera su nombre no demuestra encontrar a Robin/Morgan/etc.
No se ha probado ejecución ROS ni éxito físico. No se convirtió esta incertidumbre en un fallo automático.

## Latencia y recursos

resumen_por_bloque.csv/json incluye media y mediana por bloque, errores incluidos, y el número
de mediciones disponibles. Los recursos del servidor Qwen se mantienen separados del cliente;
los recursos internos de GPT son «no disponibles» y sus valores numéricos son null.
RAM/GPU son picos muestreados del proceso/allocator según la campaña, no consumo energético
ni memoria exclusiva de un comando. Los errores rápidos pueden reducir la media: consultar
siempre errors y valid_plan_contract junto con la latencia. El reporte histórico conserva
las figuras de coste y tokens; esta estratificación no inventa nuevas mediciones.

## Reproducción

Desde la raíz del repositorio:

```bash
MPLCONFIGDIR=/tmp/matplotlib-piloto python3 reports/comparativo_bloques_20261021/generar_reporte.py
```

El programa comprueba la aprobación y sus huellas, revalida las comprobaciones previas,
une por caso/modelo/run_id, exige primeros intentos, contrasta los 180 resultados originales
y comprueba que todas las huellas de campaña permanecen intactas. Las observaciones nuevas
sobre el consumidor se identifican como actuales, sin fabricar trazabilidad histórica.
El CSV de revisión es una salida generada: guardar una copia antes de anotar decisiones.

## Alcance y siguiente decisión

Esta separación fue aprobada después del piloto: es análisis exploratorio. Una repetición
no estima variabilidad estocástica; las paráfrasis de una intención no son independientes.
Las 60 órdenes representan 28 intenciones. No se extraen conclusiones generales de bloques
con uno o dos casos. Existen coincidencias con el corpus de desarrollo y ajuste previo del
prompt; no es el conjunto independiente final de tesis.

No cambió el conteo global de dictámenes respecto de la propuesta anterior; sí su distribución
por ámbito y la interpretación de las limitaciones. Los dictámenes no adquieren aprobación
humana por haberse aprobado la clasificación. El paso siguiente es resolver el contrato
histórico de identidad/memoria/seguimiento y aprobar o corregir estos dictámenes, antes de
preparar una versión posterior y el conjunto independiente.
