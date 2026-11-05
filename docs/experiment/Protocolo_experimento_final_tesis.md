# Protocolo del experimento final de tesis

**Evaluación de Qwen2.5-3B–CLIPS, Qwen2.5-7B–CLIPS y GPT directo para planificación simbólica en robótica de servicio**

Versión: 0.1 · Fecha: 27 de octubre de 2026 · Estado: propuesta para revisión previa a la ejecución.

Este documento describe el diseño, la ejecución y la evaluación del experimento final. Es autónomo y puede exportarse para revisión, anexarse a la tesis o compartirse con otros evaluadores. No certifica que el conjunto final esté construido, que sus referencias estén aprobadas ni que las configuraciones estén congeladas. Las cifras propuestas de tamaño y repeticiones deben aprobarse antes de observar resultados finales.

## 1. Objetivo y alcance

La pregunta principal es: ¿qué tan bien transforman Qwen2.5-3B–CLIPS, Qwen2.5-7B–CLIPS y GPT directo las instrucciones del ámbito GPSR implementado en planes simbólicos correctos, y cómo responden a variaciones lingüísticas y solicitudes que exceden su cobertura?

GPSR significa General Purpose Service Robot, una prueba de RoboCup@Home que incluye órdenes de servicio. El ámbito de este experimento corresponde al generador de comandos, las extensiones locales y las capacidades implementadas. No se asume que esos componentes cubran todo GPSR ni toda instrucción robótica posible.

Se evalúan fidelidad a la orden, compatibilidad con el ejecutor, cumplimiento simbólico, robustez lingüística, consistencia entre ejecuciones, latencia y coste computacional observable. Se distinguen las diferencias entre las dos configuraciones Qwen de las diferencias entre arquitecturas completas.

La unidad evaluada es un sistema configurado: modelo, adaptación, prompt, validación y planificación. Una diferencia entre Qwen–CLIPS y GPT directo no puede atribuirse exclusivamente a CLIPS, al tamaño del modelo o al ajuste fino.

El núcleo del experimento es computacional, sin ejecutar físicamente los planes en Justina, el robot de servicio cuyo contrato de acciones se toma como referencia. Cumplimiento simbólico no equivale a éxito de percepción, navegación, manipulación ni interacción física.

## 2. Relación con el piloto

El piloto utilizó 60 órdenes, 28 intenciones, cinco repeticiones y tres sistemas: 900 ejecuciones. Sirvió para desarrollar el protocolo, identificar errores y precisar condiciones del escenario. Sus campañas, respuestas y dictámenes históricos deben conservarse intactos.

El conjunto final será independiente del conjunto de desarrollo. No se reutilizarán las 60 órdenes como prueba final ni se presentará el aumento de sus repeticiones como nueva evidencia de generalización.

Pueden corregirse modelos, prompts, adaptadores, validadores y reglas antes de congelar la versión final. Cada cambio debe quedar registrado. El piloto describe las versiones anteriores; no se recalificará como si hubiera utilizado las nuevas.

Las referencias finales se revisarán antes de observar las respuestas de los sistemas. Si el conjunto final se utiliza posteriormente para corregir el sistema, cualquier reevaluación se identificará como una versión posterior, sin sustituir silenciosamente la evaluación original.

## 3. Sistemas y control diagnóstico

| Condición | Entrada y procesamiento | Salida evaluada |
|---|---|---|
| Qwen2.5-3B–CLIPS | Orden en inglés → servidor Qwen con adaptación QLoRA → objetivos → normalización/validación → hechos → CLIPS | Objetivos, hechos disponibles y plan |
| Qwen2.5-7B–CLIPS | Mismo recorrido con el intérprete de 7B | Objetivos, hechos disponibles y plan |
| GPT directo | Orden en inglés → API con prompt y esquema estructurado → validación | Objetivos declarados, plan, aclaración o rechazo |
| Control CLIPS | Objetivos de referencia aprobados → mismo adaptador y reglas | Plan diagnóstico sin interpretación por Qwen |

El control no es una cuarta arquitectura competidora ni una referencia automáticamente correcta. Se evalúa contra los mismos requisitos de tarea. Permite detectar problemas de adaptación y expansión aun cuando la interpretación de referencia sea correcta.

Solo se ejecutará con referencias aprobadas y aplicables. `ReferenceNotApproved` y `ReferenceNotApplicable` se contabilizarán como controles no realizados, separados de errores de CLIPS. Si una referencia válida llega al control y este falla, se registrará el fallo y su etapa.

## 4. Diseño del conjunto final

### 4.1 Tamaño propuesto

| Bloque | Cantidad propuesta | Propósito |
|---|---|---|
| Principal: cobertura implementada | 60 escenarios × 3 formulaciones = 180 órdenes | Cumplimiento y robustez lingüística |
| Composición | 40 órdenes | Combinaciones de acciones conocidas fuera de las rutas del generador local |
| Restricciones o capacidades no soportadas | 40 órdenes | Límites de representación, planificación o ejecución |
| Ambigüedad, información insuficiente o contradicción | 40 órdenes | Adecuación de aclaraciones y rechazos |
| Total | 300 órdenes | Evaluación principal y diagnósticos separados |

Se proponen cinco repeticiones por orden y sistema: 300 × 5 × 3 = 4,500 ejecuciones principales. Los controles y los reintentos se contabilizan aparte. Si no existen suficientes escenarios distintos, se ajustará la distribución antes de ejecutar; no se inflará la diversidad cambiando únicamente nombres u objetos.

Las cuotas por familia, los subtipos de cada bloque y la cantidad definitiva quedan pendientes de aprobación. Las etiquetas del conjunto final deberán tener un identificador propio; no se supondrá equivalencia automática con los bloques históricos G/L/C/M/A/F/X.

### 4.2 Escenarios y paráfrasis

Un escenario fija subtareas, entidades, restricciones y condiciones iniciales. Sus tres formulaciones serán: una cercana al generador, una paráfrasis léxica y una paráfrasis sintáctica. Las tres deben preservar exactamente la intención. Aumentar la longitud añadiendo acciones no constituye una paráfrasis.

Los escenarios se distribuirán entre las familias de acciones disponibles. Se registrarán por separado escenario, intención y familia: varias órdenes que solo cambian el objeto pueden compartir estructura y no constituyen familias independientes.

Las entradas de los modelos permanecerán en inglés. Una traducción al español podrá acompañar cada ficha para facilitar la revisión, sin enviarse al modelo ni introducir requisitos ausentes en el original.

### 4.3 Auditoría de cobertura y coincidencias

Para cada ficha se documentarán cinco ejes independientes:

1. Admisión por la versión concreta del Command Generator original.
2. Admisión por el generador local ampliado y la plantilla que la sustenta.
3. Relación con el corpus de entrenamiento: coincidencia literal, normalizada, estructural o ausencia de coincidencia bajo los criterios comprobados.
4. Representabilidad mediante objetivos canónicos y sus atributos.
5. Soporte en adaptador, CLIPS y contrato del ejecutor.

Se conservarán versiones y huellas de archivos. La ausencia de coincidencia literal no acredita una intención o familia inédita. Se registrarán las relaciones con el piloto y el corpus usado para ambos Qwen. No se conocen las posibles coincidencias con el entrenamiento del proveedor GPT.

La independencia final es respecto al desarrollo local y al uso de las fichas para ajustar el sistema. Si se reutilizan familias entrenadas, el resultado se describirá como generalización a instancias y formulaciones nuevas de esas familias, no a familias inéditas.

### 4.4 Contenido mínimo de una ficha

| Campo | Contenido requerido |
|---|---|
| Identificación | case_id, scenario_id, intent_id, family_id y versión |
| Entrada | Orden inglesa y traducción española informativa |
| Clasificación | Bloque y evidencia de los cinco ejes de cobertura |
| Tarea | Interpretación, subtareas obligatorias y restricciones |
| Dependencias | Precedencias y referencias que deben preservarse |
| Contexto | Condiciones iniciales y supuestos del escenario |
| Respuestas admisibles | Plan, aclaración o rechazo; condiciones para aceptarlos |
| Referencia | Objetivos aplicables, estado de aprobación y alternativas válidas |
| Dictamen | Criterios explícitos de cumplimiento y fallo |
| Revisión | Fecha, responsable, evidencia y resolución de discrepancias |

No se entregarán a los modelos objetivos de referencia ni dictámenes esperados. El conocimiento del contrato y de las convenciones del escenario que sí necesiten deberá suministrarse de forma coherente y quedar documentado para cada arquitectura.

## 5. Condiciones especiales y límites del escenario

Estas condiciones explican cómo interpretar los planes; no son permisos generales para ignorar restricciones. Las aceptadas en desarrollo solo podrán trasladarse a fichas finales que las declaren previamente.

| Situación | Condición o criterio de evaluación |
|---|---|
| Destinatario nombrado | Si la ficha declara una única persona en la habitación y que representa al destinatario, encontrar esa persona puede satisfacer la identificación. No se extiende al conteo, a múltiples personas ni a todo GPSR. |
| Seguimiento y primera persona | El piloto aceptó para DEV-052 que la primera persona encontrada es la destinataria. En el conjunto final esto exige una condición explícita de la ficha; no se supone para cualquier orden. |
| Protocolo instruct_follow_to_* | Se interpreta como activación del caso especial del ejecutor que realiza seguimiento y pasos adicionales, conforme al contrato confirmado en desarrollo. Decir que se va a seguir a alguien sin activar ese protocolo ni una secuencia equivalente no basta. Registrar su soporte en la versión congelada. |
| Gestos y vestimenta | Deben conservarse los atributos solicitados. La equivalencia de identificadores como wavingperson se fija según el contrato; no se deduce solo de semejanza textual. Encontrar una persona cualquiera no satisface una restricción de vestimenta salvo condición explícita que la garantice. |
| Conteo por vestimenta | El piloto identificó una capacidad pendiente. Contar personas sin filtrar no cumple una petición de conteo por vestimenta. Localizar una persona mediante un argumento de color tampoco demuestra un conteo. |
| Peso frente a tamaño | biggest_fruit puede resolver selección por tamaño si el contrato lo admite; no demuestra selección por peso. La aproximación tamaño→peso del piloto se registra como excepción, no como cumplimiento del requisito original. |
| Focus durante el diálogo | La atención visual debe respetar el protocolo de interacción documentado. Puede mantenerse entre acciones consecutivas de hablar y escuchar dirigidas a la misma persona. Los anuncios generales, como task completed, no requieren atención a una persona. |
| Focus redundante | Desactivar y reactivar innecesariamente se registra como redundancia si conserva la tarea; constituye incumplimiento si rompe una dependencia o el protocolo obligatorio. La mera diferencia de secuencia no decide el dictamen. |
| Memoria de interacción | Claves como guest_name_last deben tener un origen válido en el protocolo. Informar el nombre exige una ruta coherente de adquisición y uso, no únicamente mencionar una clave. |
| Argumentos simbólicos | Los valores se comprueban en su acción. instruction_point e instruction point no se suponen equivalentes como ubicación. focus con argumento focus enable no equivale a enable bajo comparación exacta. |
| Texto hablado | Los espacios en una frase descriptiva de say no son por sí mismos un error. Algunas claves de say activan protocolos: deben distinguirse de anuncios de texto libre. |
| Terminación | task completed no demuestra que se hayan realizado las subtareas. Su presencia, posición y obligatoriedad se juzgan según el contrato congelado. |

DEV-050 y DEV-051 tuvieron aceptaciones excepcionales de escenario en el desarrollo, separadas de cumplimiento estricto. No se usarán para convertir automáticamente las mismas limitaciones en aciertos finales. Si se implementan las capacidades, se documentará la nueva versión; si no, se medirá el comportamiento ante el límite.

Para DEV-052, la aclaración de identidad y protocolo resolvió 14 dictámenes antes no verificables. No fue una excepción de cumplimiento. La respuesta GPT que omitía el disparador mantuvo su fallo. Este antecedente ilustra la importancia de fijar las condiciones antes de observar las salidas finales.

## 6. Congelación y ejecución

### 6.1 Registro previo obligatorio

Antes de iniciar, se fijarán:

- Versión y huella de dataset, fichas, criterios, generador y auditoría de coincidencias.
- Modelos base, adaptadores QLoRA, checkpoints, tokenizadores y parámetros de generación.
- Identificador del modelo GPT y versión disponible; prompt, JSON Schema y validadores con sus huellas.
- Adaptador, normalizador, reglas CLIPS, contrato del ejecutor y programas de campaña.
- Hardware, sistema operativo, dependencias, dispositivo, cuantización y límites de contexto/salida.
- Repeticiones, semillas, orden de ejecución, calentamiento, pausa entre solicitudes y timeouts por capa.
- Política de reintentos, detección de servidor libre y criterios de suspensión/reanudación.
- Métricas, denominadores, política de exclusiones y procedimiento de revisión.

No se presume que todas estas funciones estén implementadas por el código actual. Se realizará una comprobación técnica con entradas de desarrollo, separadas del conjunto final. El acta de congelación registrará los valores efectivos, no solo esta lista.

### 6.2 Secuencia de trabajo

1. Aprobar el protocolo y las cuotas por familia.
2. Cerrar las correcciones de desarrollo y documentar las capacidades pendientes.
3. Construir y auditar las nuevas fichas sin consultar las respuestas finales.
4. Aprobar referencias, condiciones y clases de respuesta admisibles.
5. Comprobar con datos de desarrollo el recorrido completo, registros, recursos y recuperación.
6. Congelar configuraciones y conjunto; guardar el manifiesto de huellas.
7. Ejecutar rondas aleatorizadas con semillas registradas. Alternar el orden de sistemas cuando sea viable y documentar el calendario real.
8. Ejecutar el control CLIPS donde corresponda, separando sus registros.
9. Revisar automáticamente y después semánticamente los resultados.
10. Resolver discrepancias, calcular métricas y elaborar el informe sin elegir los mejores intentos.

Las consultas serán secuenciales salvo que se defina otro régimen antes de empezar. No se mezclarán mediciones de concurrencia distinta. El calentamiento se registrará aparte. Los modelos recibirán solicitudes independientes, sin conversación acumulada que introduzca aprendizaje o contexto entre órdenes.

### 6.3 Fallos, timeouts y reintentos

La unidad principal es el primer intento de cada repetición. Todos sus errores y timeouts se conservan. Un reintento exitoso no reemplaza ese resultado; se muestra como recuperación adicional con su propio tiempo y coste.

Después de un timeout de Qwen, no se enviará la siguiente orden hasta verificar que el servidor está libre mediante un mecanismo documentado. Una respuesta tardía no se asociará a otra orden. Si el estado no puede comprobarse, se suspenderá la campaña y se reanudará cuando esté verificado, conservando el fallo original.

La espera entre peticiones GPT y la espera para liberar Qwen quedan fuera de la latencia individual definida, pero forman parte del tiempo total de campaña. Se registrarán pausas, respuestas tardías y cualquier reintento automático del cliente o SDK. Si el programa no permite identificarlos, esa limitación debe resolverse o declararse antes de comparar latencias y costes.

Una ejecución no iniciada no equivale a una respuesta incorrecta: se cuenta como pendiente y se informa la cobertura de ejecución. Una solicitud iniciada que falla sí pertenece al denominador correspondiente. No se presentará una campaña incompleta como la evaluación final completa.

## 7. Evaluación y dictámenes

### 7.1 Capas de evaluación

Cada registro tendrá resultados separados de formato, interpretación, contrato, cumplimiento y adecuación de respuesta. También tendrá un estado técnico. Un plan puede ser JSON válido y fallar semánticamente; una aclaración puede ser adecuada sin contener un plan.

La revisión seguirá este orden:

1. Comprobar integridad del registro, estado técnico y tipo de respuesta.
2. Validar esquema, acciones, argumentos, referencias y terminación según contrato.
3. Comparar objetivos con la intención y restricciones de la ficha.
4. Revisar el plan completo contra subtareas, dependencias y efectos documentados.
5. Aplicar exclusivamente las condiciones del escenario aprobadas.
6. Registrar dictamen, evidencia, etapa del error y observaciones de eficiencia.

No se exige coincidencia literal con una única secuencia. Se aceptan planes alternativos que satisfagan todos los requisitos. Los objetivos declarados y el plan se evalúan por separado: un objetivo omitido puede mantenerse en el plan, o un objetivo correcto puede expandirse incorrectamente.

### 7.2 Dictámenes y denominadores

| Dictamen | Regla |
|---|---|
| Cumple | Satisface todas las subtareas y restricciones, respeta dependencias y utiliza acciones compatibles bajo las condiciones declaradas. |
| Incumple | Existe una omisión, contradicción, argumento incompatible o ausencia de respuesta válida para una tarea que exige plan. Registrar por separado si el origen es técnico o semántico. |
| No verificable | La tarea es evaluable, pero la evidencia o el contrato no permiten resolver una dependencia necesaria. No equivale a éxito; permanece en el denominador y se informa por separado. |
| No aplicable | La ficha no exige un plan ejecutable. Se evalúa la adecuación de aclaración/rechazo u otra respuesta admisible. No se asigna por el mero hecho de que el sistema falle. |

Un defecto observable determina incumplimiento aunque exista otra parte no verificable. Actualmente no quedan casos no verificables en el reporte final del piloto, pero el protocolo conserva una regla para tratarlos si aparecen en el conjunto nuevo.

Para cada bloque se publicarán tareas evaluables, no aplicables, ejecuciones realizadas y pendientes. El denominador no se reducirá después de ver errores. No se sumarán todos los bloques en una tasa global que confunda cumplimiento de planes y adecuación de rechazos.

En casos fuera de cobertura pueden admitirse un plan completo o una respuesta que reconoce correctamente el límite, si la ficha lo establece. Se informarán por separado resolución y reconocimiento del límite. Un plan parcial que omite una restricción no se acepta como ninguna de las dos cosas. Un fallo técnico tampoco cuenta como rechazo adecuado.

### 7.3 Procedimiento humano y apoyo automático

Los validadores deterministas sirven para comprobaciones de contrato, no sustituyen toda la revisión semántica. La IA puede proponer dictámenes y organizar evidencia; su procedencia se conserva y no se presenta como revisión humana.

Se propone aprobar humanamente todos los dictámenes principales, agrupando salidas idénticas cuando también coincidan orden, contexto y criterios. No se transferirán dictámenes únicamente por semejanza de redacción.

Se propone una segunda revisión independiente de una muestra estratificada del 20 % de las órdenes, incluyendo sus sistemas y repeticiones. Los casos dudosos se revisarán adicionalmente y se distinguirán de esa muestra para no sesgar la medida de acuerdo. La disponibilidad de la segunda persona está pendiente.

El acuerdo se calculará sobre decisiones anteriores a la conciliación, con porcentaje de acuerdo y una medida corregida por azar si procede. Se informará la unidad evaluada y la distribución de categorías. Cuando sea viable, se ocultará al revisor la etiqueta de sistema; las diferencias de formato pueden impedir un cegamiento completo.

## 8. Métricas y análisis comparativo

### 8.1 Resultado principal

Cumplimiento en el bloque principal = ejecuciones que cumplen / ejecuciones realizadas del primer intento en tareas evaluables del bloque principal.

Con 180 órdenes y cinco repeticiones completas, el denominador previsto es 900 por sistema. Incluye errores, timeouts y eventuales no verificables. Se publicarán numerador, denominador y categorías complementarias, además del porcentaje.

### 8.2 Medidas complementarias

| Dimensión | Medida y unidad |
|---|---|
| Cumplimiento sostenido | Órdenes que cumplen 5/5, sobre órdenes con cinco repeticiones realizadas |
| Robustez lingüística | Escenarios cuyas tres formulaciones cumplen en una misma ronda, sobre 60 × 5 combinaciones propuestas; también diferencias por formulación |
| Robustez sostenida | Escenarios que cumplen en las 15 ejecuciones de sus tres formulaciones |
| Consistencia de objetivos | Órdenes con alguna diferencia entre cinco ejecuciones, sobre órdenes completas |
| Consistencia de plan | Órdenes con cambios de plan literal y de proyección operativa, por separado |
| Consistencia de respuesta | Cambios de tipo de respuesta y de dictamen; permite distinguir ausencia estable de plan de estabilidad de un plan válido |
| Compatibilidad | Tasas de acciones, argumentos y referencias incompatibles, con denominador explícito de planes y pasos |
| Límites del dominio | Resolución correcta, aclaración adecuada, rechazo adecuado, plan incompleto y fallo técnico por bloque |
| Diagnóstico Qwen | Errores de interpretación, adaptación y expansión, contrastados con el control |

La proyección operativa usada en el piloto elimina numeración y solo anuncios de say iniciados por «I will » o «I have ». Conserva otras acciones, argumentos y claves de diálogo. Puede mantenerse para comparabilidad, pero debe congelarse su implementación. No prueba equivalencia funcional y puede conservar diferencias de mayúsculas o redundancias.

La ausencia de cambio no implica corrección. Se informará si la salida estable es un plan, un rechazo o un error. Los cambios en respuestas sin plan se analizarán mediante tipo y adecuación, sin exigir coincidencia literal de su redacción.

La comparación principal será emparejada: los sistemas reciben las mismas órdenes. Se proponen intervalos de confianza del 95 % y diferencias entre sistemas mediante remuestreo agrupado por escenario, conservando juntas formulaciones y repeticiones. Deben fijarse número de remuestreos y semilla antes del análisis. Si varias instancias comparten una intención estrecha, se evaluará también la sensibilidad al agrupamiento por intención o familia.

Las 4,500 ejecuciones no son observaciones independientes. Tampoco lo son las 300 combinaciones escenario–ronda de robustez. Se mostrarán resultados por familia y no se afirmará un efecto aislado de longitud si también cambia la composición de la tarea.

No se propone una puntuación única que mezcle cumplimiento, coste y latencia con pesos arbitrarios. El veredicto describirá qué configuración ofrece mejores resultados en cada dimensión y bajo qué condiciones. La ausencia de una diferencia concluyente también es un resultado válido.

### 8.3 Latencia, recursos y coste

La latencia de extremo a extremo se medirá desde el envío del intento hasta la recepción y procesamiento de la respuesta por el programa, con límites temporales definidos. Se registrarán etapas por separado cuando sean observables. Se reportarán mediana, media, cuartiles y percentiles altos, separando respuestas completadas de tiempos agotados. Los timeouts no se tratarán como si su duración límite fuera el tiempo de finalización real.

Para Qwen se distinguirán memoria del asignador GPU, memoria total observada de GPU, RAM del proceso y utilización si están disponibles. Se documentarán herramienta, unidad, frecuencia de muestreo y si CLIPS o el servidor están incluidos. No se llamará «consumo energético» a la memoria ni se inferirá energía sin medición.

Los recursos internos GPT se indicarán como «no disponibles», nunca cero ni consumo del cliente. Los recursos del cliente podrán registrarse por separado. La ejecución local no tiene coste total cero: equipo, electricidad y mantenimiento son componentes distintos del gasto por petición API.

Se registrarán tokens de entrada y salida, detalles de caché y razonamiento cuando existan, identificador de respuesta, modelo y gasto atribuido a la campaña. Las subcategorías de tokens no se sumarán nuevamente a sus totales. Se diferenciará coste facturado o consultado en Usage de una estimación por tarifas.

El piloto registró US$2.07 para 300 solicitudes GPT, según la consulta del usuario al panel Usage. Es un antecedente histórico, no un presupuesto garantizado del conjunto final. El gasto final distinguirá intentos principales, reintentos y desarrollo; no se atribuirá todo el consumo de una cuenta a la campaña sin comprobarlo.

## 9. Presentación de resultados

El informe incluirá:

- Tabla de configuración y versiones de los tres sistemas.
- Tabla de cobertura, familias y coincidencias con entrenamiento/desarrollo.
- Flujo de registros: previstos, ejecutados, errores, timeouts, controles omitidos y reintentos.
- Cumplimiento principal por sistema, familia y formulación, con intervalos y diferencias emparejadas.
- Tabla de consistencia y mapa por orden y repetición.
- Resultados separados de composición, límites y respuestas sin plan.
- Distribuciones de latencia, recursos locales y coste API.
- Taxonomía de errores con ejemplos trazables y planes legibles, no únicamente JSON.

Una matriz de confusión es apropiada si las fichas fijan una clase esperada de respuesta —por ejemplo plan, aclaración o rechazo— y una regla inequívoca para compararla. Si hay varias clases admisibles, debe declararse cómo se representan; no se inventará una clase única después de ver las salidas. Los objetivos con múltiples acciones requieren métricas por acción o estructura, no una matriz convencional de clase única. La matriz no sustituye la evaluación de cumplimiento del plan.

Se conservarán resultados negativos y casos difíciles. Las exclusiones solo seguirán reglas previas o incidencias justificadas con trazabilidad; se informará su efecto en los denominadores.

## 10. Artefactos y trazabilidad

Cada ejecución registrará campaña, case_id, escenario, sistema, repetición, intento, run_id, fecha, configuración y versiones; entrada, respuesta cruda, objetivos, hechos disponibles, plan, validaciones, tiempos, recursos, errores y coste cuando sea observable.

Cada dictamen registrará criterio aplicado, evidencia, responsable o herramienta, fecha, versión, excepción y cualquier dictamen anterior. Las correcciones de evaluación no borrarán la evidencia ni el historial.

El paquete exportable final contendrá protocolo aprobado, manifiesto de versiones y huellas, fichas y traducciones, auditoría de coincidencias, registros crudos, revisión por ejecución, scripts de análisis, resultados tabulares, informe y figuras. No se incluirán claves API ni credenciales.

Este documento dispone de una fuente Markdown editable y versiones de lectura exportadas. Las exportaciones deben regenerarse cuando cambie la fuente; la versión y fecha visibles deben coincidir.

## 11. Limitaciones y alcance de las conclusiones

Los resultados caracterizarán las configuraciones y el ámbito implementado. No demostrarán planificación robótica universal, éxito físico ni generalización a familias nuevas que no se hayan evaluado expresamente.

Los contrastes fuera de cobertura diagnostican límites; no deben diluirse en el resultado principal. La diferencia de contratos de aclaración entre sistemas forma parte de la arquitectura evaluada y no prueba por sí sola una capacidad intrínseca del modelo.

El diseño está informado por el piloto. El conjunto final independiente reduce el ajuste a esos ejemplos, pero no elimina toda dependencia de las familias de entrenamiento. La posible presencia de tareas similares en el entrenamiento GPT es desconocida.

La revisión humana puede contener desacuerdos. La disponibilidad de una segunda revisión, las condiciones de hardware, los cambios externos del proveedor y la falta de medición física se documentarán según lo ocurrido, sin declarar controles que no se hayan realizado.

Una evaluación adicional de integración o ejecución física con Justina puede incorporarse como estudio separado, con métricas y protocolo propios. No se considerará ejecutada ni obligatoria por este documento.

## 12. Decisiones pendientes y autorización de inicio

Antes de ejecutar deben quedar cerrados: tamaño y cuotas finales; fichas y supuestos; versiones de sistemas y contrato; capacidades pendientes; configuración de generación; repeticiones y semillas; calentamiento, pausas y timeouts; política de recuperación; herramientas de recursos; revisión humana; análisis estadístico; presupuesto y calendario.

El acta de aprobación deberá indicar versión del protocolo, fecha, responsable, huellas de datos y configuraciones, y desviaciones aceptadas. La creación de este documento no constituye esa aprobación ni inicia campañas.

## 13. Fuentes internas y antecedentes

Las rutas siguientes son relativas a la raíz del repositorio Qwen2.5-7B. Sirven para recuperar la evidencia de desarrollo; el documento puede leerse sin acceder a ellas.

| Recurso | Utilidad |
|---|---|
| README.md | Arquitectura y procedencia del proyecto |
| docs/experiment/Guia_del_experimento.md | Guía histórica del desarrollo; sus cifras de etapas previas no sustituyen el reporte consolidado |
| docs/experiment/Clasificacion_60_para_revision.md | Clasificación revisada de las órdenes de desarrollo |
| data/datasets/dataset_gpsr.jsonl | Corpus indicado por el usuario como común a ambos ajustes Qwen |
| qwen_gpsr/generation/ | Generador local y conversión a objetivos |
| reports/comparativo_escenario_20261024/ | Reporte consolidado del piloto, revisión y consistencia |
| reports/comparativo_escenario_20261024/decision_DEV052.json | Confirmación de identidad y protocolo de seguimiento |
| reports/comparativo_escenario_20261024/ANALISIS_CONSISTENCIA.md | Argumentos incompatibles, redundancias y criterios de consistencia |
| experiments/README.md | Funcionamiento de los programas de campaña |

El generador original identificado por el usuario es RoboCupAtHome/CommandGenerator. Su URL es https://github.com/RoboCupAtHome/CommandGenerator. La revisión final debe registrar el commit o la huella de la copia efectivamente utilizada; la URL por sí sola no fija una versión.

## 14. Historial

Versión 0.1, 27 de octubre de 2026: propuesta inicial del protocolo final, basada en el piloto consolidado y en la discusión de diseño. No modifica campañas, dictámenes ni artículos existentes.
