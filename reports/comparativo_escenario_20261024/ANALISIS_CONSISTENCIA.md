# Consistencia, argumentos y pasos adicionales

Este análisis complementa INFORME.md y registra la revisión del asistente bajo criterios aprobados por el investigador. La revisión mediante IA conserva su procedencia. El 24 de octubre se añadió la confirmación explícita del autor para DEV-052: sus 14 ejecuciones con disparador cumplen bajo condiciones del escenario. GPT R1 conserva el fallo por omisión. No quedan casos no verificables; no se midió ejecución física ni se aprobaron automáticamente otros dictámenes.

## Criterios aplicados

Los argumentos simbólicos se evalúan en su acción: una ubicación go_to requiere su identificador canónico; una frase descriptiva say puede contener espacios. En las 300 respuestas GPT no se observó go_to con instruction point ni otro argumento de navegación con espacios. Las diferencias observadas de esos nombres corresponden a anuncios. No se presentan como errores de ubicación.

La inspección de los argumentos operativos con espacios encontró cuatro pasos de DEV-043/R5, en una sola ejecución: focus enable/focus disable dentro del argumento de focus. El código actual compara enable de forma exacta; focus enable devuelve false y no activa la atención. Es un incumplimiento del contrato, no un fallo físico observado. En DEV-051/R4–R5, heaviest_fruit se interpreta como clase para conteo, no como selección por peso. Ambos casos pasaron el validador estructural registrado.

No se observaron nombres nuevos de acción en estas variantes. El término «instrucción inventada» se concreta aquí como argumento o consulta no admitida para la operación pretendida. No se infiere un error de ejecución solo a partir de la apariencia del texto.

DEV-056/058/059/060 conservan respuestas sin plan y explicaciones adecuadas pese a cambios de redacción. GPT mantiene 30/30 respuestas adecuadas en A/F/X; Qwen 0/30 con el contrato configurado. DEV-049 se distingue: pasa de rechazo prudente en R1 a planes que omiten vestimenta en R2–R5.

## Resultados consolidados

| Sistema | Cumple G / 230 | Incumple | No verificable | Órdenes G que cumplen 5/5 |
|---|---:|---:|---:|---:|
| Qwen3B | 220 | 10 | 0 | 44/46 |
| Qwen7B | 215 | 15 | 0 | 43/46 |
| GPT | 216 | 14 | 0 | 40/46 |

Las excepciones del escenario siguen separadas del cumplimiento estricto: 10, 10 y 8 ejecuciones respectivamente. GPT tiene dos ejecuciones con heaviest_fruit a las que no se extiende la excepción de usar tamaño como proxy de peso. No convertir la aceptación excepcional en equivalencia semántica.

La consistencia literal de planes cambia en 0/60, 0/60 y 24/60 órdenes. Una proyección operativa, que elimina únicamente anuncios say iniciados por I will/I have y la numeración, cambia en 0/60, 0/60 y 9/60. Se preservan instrucciones de diálogo y todas las demás acciones y argumentos. Esta proyección no demuestra equivalencia funcional: cuenta redundancias y cambios de mayúsculas, y no evalúa adecuación de respuestas sin plan. La estabilidad de cumplimiento se informa aparte. GPT alterna dictamen de cumplimiento en cuatro órdenes G (024,030,043,052); 052 pasa de incumple en R1 a cumple bajo las condiciones confirmadas en R2–R5. GPT sigue con 40/46 órdenes que cumplen cinco veces, porque R1 de DEV-052 mantiene el fallo.

Las redundancias de focus y la consulta duplicada del nombre conservan el cumplimiento de las subtareas, pero se etiquetan como desviaciones de protocolo/eficiencia; no se confunden con una secuencia operativa idéntica. DEV-028 omite un objetivo de búsqueda, aunque el plan lo conserva; DEV-030 pierde además la visita a kitchen y sí incumple. DEV-052 añade el disparador de seguimiento. La identidad y el caso especial del ejecutor quedaron confirmados por el autor como condiciones del escenario. Las diez ejecuciones Qwen y cuatro GPT que lo incluyen cumplen; la ejecución GPT R1 que lo omite no cumple.

## Frecuencias de cambios revisados

La tabla siguiente describe las 70 ejecuciones que difieren de R1; no es una taxonomía exhaustiva de todos los fallos en 900 ensayos. Cada fila cuenta ejecuciones y órdenes distintas. Algunas categorías son variaciones aceptables, no errores. Las diferencias observadas no se corrigen en los datos originales.

| Categoría | Ejecuciones | Órdenes |
|---|---:|---:|
| announcement_variation | 39 | 16 |
| constraint_omission | 4 | 1 |
| entity_case_variation | 1 | 1 |
| equivalent_nonplan_response | 7 | 4 |
| filtered_count_unsupported | 4 | 1 |
| goal_plan_discrepancy | 1 | 1 |
| interaction_redundancy | 1 | 1 |
| invalid_executor_argument | 1 | 1 |
| protocol_added_confirmed_scenario | 4 | 1 |
| protocol_correction | 3 | 1 |
| protocol_redundancy | 2 | 2 |
| required_subtask_omission | 1 | 1 |
| unsupported_executor_query | 2 | 1 |

## Coste y alcance

US$0.42 + US$1.65 = US$2.07 para 300 solicitudes, según declaración del investigador desde Usage; promedio US$0.0069. Recursos internos de GPT: no disponibles. No se usa el cliente como sustituto ni se asigna coste cero a Qwen. Las comparaciones son descriptivas sobre desarrollo; cinco repeticiones no son cinco órdenes independientes.
