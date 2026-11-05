> Ejecutar los comandos desde la raíz del repositorio.

# Guía del experimento y del borrador del capítulo 6

Actualización — 4 de noviembre de 2026. El piloto consolidado comprende
60 órdenes, 28 intenciones, cinco repeticiones y tres condiciones: 900 primeros
intentos. La prueba final independiente sigue propuesta, sin ejecución acreditada.

## Estado vigente y fuentes

El [informe consolidado del 24 de octubre](../../reports/comparativo_escenario_20261024/INFORME.md)
es la fuente del piloto con cinco repeticiones y la decisión del escenario DEV-052.
Conserva la procedencia de los dictámenes: la revisión del asistente no equivale
a aprobación humana. Las excepciones DEV-050/051 no se convierten en cumplimiento
estricto ni se trasladan automáticamente al conjunto final.

El [protocolo final de tesis](Protocolo_experimento_final_tesis.md) es la descripción
vigente de la propuesta: 300 órdenes independientes de desarrollo, cinco
repeticiones y tres condiciones, 4,500 ejecuciones principales. Sus cuotas,
referencias y configuraciones requieren cierre antes de ejecutar.

Las secciones históricas siguientes documentan la primera pasada y las decisiones
de desarrollo. Sus cifras de 180 ejecuciones corresponden a R1, no al total actual.
Los procedimientos del piloto ya ejecutado se conservan para trazabilidad.

## Repeticiones adicionales — realizadas

R2–R5 añaden 720 ensayos a los 180 de R1. La
[preparación del 23 de octubre](../../reports/repeticiones_20261023/LEEME.md)
conserva los comandos y la correspondencia de repeticiones; su estado «preparadas»
es histórico. El informe consolidado citado arriba acredita su incorporación.

## Revisión del investigador — 22 de octubre de 2026

El [nuevo reporte](../../reports/comparativo_revision_investigador_20261022/index.html)
aplica los supuestos declarados de persona única para destinatarios nombrados y
la aceptación de protocolos de seguimiento/memoria. Conserva los errores independientes
de objeto y focus. DEV-050 y DEV-051 se registran como excepciones aceptadas,
separadas del cumplimiento estricto. Las referencias y campañas permanecen intactas.
El investigador decidió aplazar la implementación del conteo filtrado de DEV-050
y documentarlo como capacidad pendiente con aceptación excepcional en el reporte.
Ejecutor, CLIPS y prompt permanecen sin cambios: AnalyzePerson actual localiza
por atributo, no cuenta; `red_shirt` no es argumento admitido.

## Interpretación por bloques aprobados — 21 de octubre de 2026

El [reporte estratificado](../../reports/comparativo_bloques_20261021/index.html)
y su [informe](../../reports/comparativo_bloques_20261021/INFORME.md) aplican la
clasificación aprobada a los 180 primeros intentos existentes. La
[revisión por caso](../../reports/comparativo_bloques_20261021/REVISION_POR_CASO.md)
separa cumplimiento, incumplimiento, no verificable y no aplicable. Los dictámenes
siguen siendo propuestas del asistente; aprobar la clasificación no los aprueba.
DEV-050 y DEV-051 permanecen dentro del bloque G, con limitaciones de planificación.
El seguimiento tiene un consumidor en el código actual de Justina; aún falta
establecer su correspondencia histórica y cerrar identidad/memoria. No se han
repetido consultas ni modificado campañas.

## Primera pasada del piloto — histórica (R1)

Se completaron 180 primeros intentos: 60 con Qwen3B–CLIPS, 60 con Qwen7B–CLIPS
y 60 con GPT directo. Las tres campañas usan las mismas entradas, referencias
aprobadas e inventario de fuentes del cliente; ambos Qwen usan las mismas reglas.

- Qwen3B: 58 planes de contrato válido y dos HTTP 422; 38/54 coincidencias literales de objetivos.
- Qwen7B: 56 planes de contrato válido y cuatro HTTP 422; 38/54 coincidencias literales de objetivos.
- GPT: 53 planes de contrato válido, tres aclaraciones y cuatro rechazos; 52/54 coincidencias literales de objetivos.
- Estos valores no equivalen a cumplimiento semántico. GPT presenta un cierre anticipado de focus en DEV-024 y omite una instrucción de seguimiento en DEV-052. Persisten límites del repertorio y defectos del control.

El [reporte comparativo](../../reports/comparativo_piloto60_20261017/index.html)
contiene seis figuras PNG/SVG, matrices, comparación por caso y datos exportables.
El [informe](../../reports/comparativo_piloto60_20261017/INFORME.md) documenta
métricas, alcance y trazabilidad. Se expandieron localmente las 54 referencias
como diagnóstico; esto no sustituye una campaña oficial de control con sus
registros y mediciones. No se fabricaron tiempos ni recursos de ese diagnóstico.

En esta etapa quedaba pendiente revisar los dictámenes y los límites por
intención. La consolidación posterior se enlaza al inicio de esta guía. No modificar retrospectivamente estas campañas.

Para revisar el ámbito de cada caso, está disponible la
[clasificación de las 60 órdenes](Clasificacion_60_para_revision.md),
con traducciones auxiliares al español, evidencia del generador local y
observaciones de capacidad. El investigador aprobó la clasificación el 21 de
octubre de 2026. Conserva las entradas en inglés y no cambia las referencias ni
los resultados históricos. Esta aprobación no resuelve los dictámenes de cumplimiento
de las salidas ni constituye aprobación de un conjunto final independiente.

La [revisión de limpieza de CLIPS](../../reports/diagnostics/clips_cleanup_20261017/INFORME.md)
conserva evidencia de la corrección de ENVRNMNT8 y del crecimiento residual
observado. Los pilotos de diez órdenes y sus errores de autenticación permanecen
como evidencia histórica separada.

## Qué buscamos demostrar

La pregunta es con qué fidelidad y consistencia las configuraciones Qwen–CLIPS y GPT directo convierten una orden del dominio en un plan. Se evaluará el producto computacional y las etapas observables. No se medirán percepción, navegación física, manipulación real ni seguridad del robot.

La comparación no permite atribuir una diferencia exclusivamente a CLIPS: también cambian el modelo, su adaptación y el acceso al conocimiento del dominio. GPT recibe instrucciones detalladas de las convenciones de expansión. Las conclusiones describirán las tres condiciones concretas: Qwen2.5-3B–CLIPS, Qwen2.5-7B–CLIPS y GPT directo.

## Pruebas y evidencias

| Prueba | Qué hacemos | Qué buscamos | Qué no demuestra |
|---|---|---|---|
| Recorrido y registro | Enviar una orden y conservar todas las etapas disponibles | Saber de qué orden procede cada resultado, detectar tiempos agotados y respuestas tardías | Calidad semántica |
| Interpretación | Comparar objetivos originales con la ficha revisada | Subtareas, objeto, lugar, destinatario, atributos y dependencias correctos | Que exista un plan adecuado |
| Contrato | Analizar objetivos y acciones, argumentos y numeración | Formato y repertorio válidos | Cumplimiento de la orden |
| Cumplimiento del plan | Aplicar restricciones y efectos documentados de las acciones | Que todas las subtareas estén cubiertas, sin operaciones contradictorias | Éxito físico |
| Control de CLIPS | Pasar objetivos de referencia por el mismo adaptador y reglas | Examinar adaptación y expansión sin el error de interpretación de Qwen | Que el plan de control sea automáticamente correcto |
| Variación lingüística | Formular la misma intención de tres maneras | Conservar corrección ante paráfrasis y ruido | Independencia entre las tres observaciones |
| Composición | Aumentar subtareas y dependencias de manera identificada | Conservar objetos, destinatarios, orden y salida completa | Un efecto puro de longitud si cambian otras dificultades |
| Límites del dominio | Usar ambigüedad, contradicción o acciones no soportadas | Describir aclaración, rechazo, bloqueo o invención de tareas | Comparabilidad directa de contratos conversacionales distintos |
| Rendimiento | Medir tiempo completo, fallos, recursos locales y tokens | Caracterizar el coste observable del servicio | Memoria o energía internas del proveedor GPT |

## Ejemplo para entender la calificación

Orden de desarrollo: **Bring me a mug from the cabinet.**

Referencia aprobada para desarrollo:

```text
go(cabinet)
find(mug, kind=object)
take(mug)
deliver(mug, to=me)
```

El investigador aprobó esta referencia junto con las otras 59 después de las pruebas preliminares. Este conjunto sigue siendo de desarrollo; la evaluación final tendrá referencias nuevas revisadas antes de observar sus resultados. La ficha pedirá encontrar y adquirir la taza en cabinet y entregarla al operador. El plan podrá usar anuncios y referencias internas diferentes, siempre que conserve los efectos y las dependencias.

| Resultado hipotético | Interpretación |
|---|---|
| Objetivos con refrigerator en vez de cabinet | Error semántico de ubicación |
| Objetivos correctos; adaptación altera el destinatario | Error de adaptación |
| Objetivos y hechos correctos; el plan entrega sin adquirir | Error de planificación |
| El plan dice «tarea completada» sin realizar las subtareas | Terminación formal sin cumplimiento |
| Objetivos y plan correctos con otros anuncios equivalentes | Resultado admisible |
| No llega respuesta antes del límite | Fallo de extremo a extremo; registrar origen técnico si se conoce |

Son ejemplos de calificación, no resultados observados. El plan producido al alimentar CLIPS con la referencia también debe pasar por esta evaluación.

## Cómo se realizará, en orden

1. **Revisar las fichas.** Confirmar intención, objetivos, restricciones y capacidades evaluables. No convertir una salida de CLIPS en referencia por el mero hecho de que CLIPS la produzca. Las 60 fichas fueron aprobadas sin cambios el 2026-10-17; véase [el registro de aprobación](Aprobacion_desarrollo_60.json).
2. **Cerrar el registro de coincidencias.** Conservar el informe y las huellas del conjunto usado. Marcar casos conocidos y casos sin coincidencias bajo los criterios comprobados.
3. **Preparar el instrumento común.** Asociar `case_id`, `intent_id`, versión, arquitectura, repetición y configuración con salida cruda, objetivos, hechos, plan, tiempo e incidencias. No enviar las referencias al modelo.
4. **Comprobar el evaluador.** Probar tanto planes correctos como versiones con errores deliberados. Verificar que acepte alternativas válidas y detecte omisiones.
5. **Ejecutar diez casos iniciales.** DEV-001, 004, 007, 010, 013, 016, 031, 037, 040 y 043. Usar Qwen–CLIPS, GPT y el control correspondiente. Revisar registros antes de ampliar. Son parte del conjunto de 60.
6. **Completar el piloto de 60.** Ajustar límites de salida, tiempos de espera, registros y rúbricas usando exclusivamente desarrollo. Los diagnósticos de capacidades no verificables no se convierten en éxitos.
7. **Fijar configuraciones y prueba final.** Congelar modelos, adaptador, prompt, reglas, normalizador, datos, evaluador, parámetros y política de reintentos. Preparar nuevas instancias de intención sin reutilizar las de desarrollo.
8. **Ejecutar la comparación final.** Mismas órdenes originales para ambas arquitecturas, sin historial y con estado reiniciado. Alternar el orden de condiciones por bloques; procesar una solicitud a la vez. Mantener los fallos y todas las repeticiones.
9. **Analizar por intención y presentar resultados.** Informar aciertos, fallos, incertidumbre, errores y costes. Conservar juntas las variantes de una intención. El capítulo 6 explicará el procedimiento; el 7 contendrá sus resultados.

## Auditoría v02 verificada

Se recibió `reports/evaluation/auditoria_desarrollo_v02.json` y se comprobó que sus huellas corresponden a las entradas actuales y al corpus registrado de 40 000 filas. El informe contiene cero coincidencias literales, cuatro por limpieza básica y ocho mediante el normalizador real de Qwen. Son ocho órdenes distintas en total.

Las coincidencias son DEV-010 y DEV-012 (entrega al operador), DEV-025 y DEV-027 (seguimiento), DEV-031 y DEV-033 (conteo), y DEV-040 y DEV-042 (respuesta a pregunta). Las paráfrasis DEV-011, DEV-026, DEV-032 y DEV-041 no coinciden directamente, pero comparten intención con ellas. Los cuatro grupos se conservan como diagnósticos conocidos de desarrollo.

Las 60 entradas y sus objetivos permanecen iguales. Se actualizaron las fichas con estado de coincidencia por orden y por grupo, filas del corpus y evidencia de ambas auditorías. Hay 52 órdenes sin coincidencia directa; cuatro son las paráfrasis indicadas. No debe presentarse ese número como 52 intenciones nuevas ni como prueba de independencia semántica.

No se necesita otra auditoría por esta actualización de metadatos. Sí deberá repetirse si se cambian las entradas, el dataset o el normalizador. La comparación con todo el corpus no permite asignar las coincidencias a entrenamiento o validación ni demostrar memorización.

La revisión semántica de las 60 referencias fue aprobada por el investigador el 2026-10-17. Todo el conjunto de desarrollo se mantendrá separado de la prueba final. En tareas simples con pocas combinaciones disponibles, las coincidencias pueden conservarse como controles conocidos; no se ocultarán cambiando únicamente palabras superfluas o puntuación.

## Tamaño y repeticiones del final propuesto

El [protocolo final](Protocolo_experimento_final_tesis.md) sustituye el
predimensionamiento anterior de 870 órdenes. Propone 180 órdenes de cobertura
(60 escenarios × tres formulaciones), 40 de composición, 40 de capacidades no
soportadas y 40 de ambigüedad o contradicción: 300 en total. Con cinco
repeticiones por cada una de las tres condiciones serían 4,500 ejecuciones
principales, más controles y reintentos por separado.

Estas cantidades no están aprobadas ni ejecutadas. Deben cerrarse junto con las
cuotas por familia, referencias, condiciones del escenario y configuraciones antes
de consultar el conjunto final. Las 60 órdenes del piloto y sus variantes siguen
siendo desarrollo. Repetirlas no sustituye construir el conjunto independiente.

## Pendientes para la versión final

- **Verificación operativa antes de congelar:** usar los programas de `experiments/`, que registran identificadores, intentos, artefactos y tiempos. Verificar las URLs y `/metadata` de ambos servidores Qwen, el modelo/adaptador cargado, medición de recursos y comprobación de servidor libre tras timeout. La aprobación de las fichas no certifica que los servidores estén disponibles.
- **Evaluación del contenido:** los validadores actuales de sintaxis y contrato son útiles, pero no comprueban todas las subtareas, precondiciones y referencias de una orden.
- **Control real:** ejecutar la referencia a través del adaptador usado en ROS y las mismas reglas, con registro de hechos. No sustituirlo por otro conversor sin demostrar equivalencia.
- **Contrato de acciones:** precisar seguimiento, verificación de nombres, atributos conjuntos y conservación de información. Distinguir efectos definidos, errores identificables y propiedades que no pueden verificarse.
- **Configuración final:** límites de tokens, tiempos de espera de cada capa, modalidad local o remota de Qwen, repeticiones y reintentos. Un tiempo externo mayor no resuelve un tiempo interno menor sin ajustar ambas capas.
- **Referencias y tamaño final:** las referencias de desarrollo ya están aprobadas. Preparar el conjunto final independiente, revisar sus fichas y fijar la composición por familia antes de observar sus respuestas.

No hace falta otro entrenamiento para avanzar en estos puntos. Si el piloto motivara cambiar el modelo o entrenar nuevamente, esa decisión debe producirse antes de fijar la configuración final y quedar documentada.

## Archivos del borrador y cómo integrarlos

- `Ch06_Validation.tex`: capítulo redactado en LaTeX como protocolo propuesto, con secciones 6.1 a 6.7.
- `Ch06_Validation_lectura.md`: copia del mismo capítulo para lectura, no una segunda versión con contenido distinto.
- `referencias_capitulo6.bib`: dos antecedentes metodológicos consultados. Añadir sus entradas al archivo bibliográfico principal y evitar duplicarlas si ya existen con otras claves.
- Este archivo: explicación operativa y pendientes, separada del texto académico.

El `.tex` se integra con `\include` o `\input` desde el documento principal. Usa `amsmath`, `amssymb` y `booktabs`. No contiene un preámbulo ni activa por sí mismo la bibliografía.

Se propone sustituir la antigua sección 6.6 «Evaluación física con Justina» por «Robustez, límites del dominio y alcance físico». Si no se realizan pruebas físicas, también deberá ajustarse el apartado correspondiente del capítulo 7. La cifra de ocho coincidencias se conserva en esta guía de trabajo; no se presenta en el capítulo como una auditoría final ya cerrada.

El borrador no está listo para convertirse íntegramente a tiempo pasado: el piloto se ejecutó, pero falta la campaña final y cerrar la evaluación de contenido. Al completarlos, deberán incorporarse los tamaños, configuraciones y procedimientos realmente utilizados, sin transformar decisiones propuestas en hechos retrospectivos.
