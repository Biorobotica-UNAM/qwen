# Decisiones antes de preparar otra versión

18 de octubre de 2026. Propuestas, no cambios aprobados ni implementados.

## Primero: cerrar el criterio de cumplimiento

La rúbrica vigente distingue protocolo de identidad/seguimiento/memoria efectiva.
Las propuestas usan esa distinción. No es necesario probar físicamente el robot
para resolver toda esta incertidumbre: revisar el contrato y el código del
consumidor puede establecer qué hacen las claves. Si la implementación requiere
un dato que el plan no entrega, habrá un incumplimiento; si el mecanismo está
implementado y el plan aporta lo necesario, podrá revisarse el dictamen simbólico.
La existencia de un consumidor no demuestra éxito físico.

Prioridad de revisión con el investigador:

1. DEV-049–051: confirmar que límites de capacidad se reportan por separado.
   Distinguir un rechazo prudente de cumplir la tarea, y una interpretación
   correcta de una expansión insuficiente. La referencia aprobada no se cambia
   retrospectivamente para premiar una respuesta observada.
2. DEV-054: confirmar que Water es un objeto y que diferir del control defectuoso
   no implica error del modelo.
3. DEV-019–024, 025–030, 034–039, 043–045 y 052: revisar contratos de identidad,
   memoria y seguimiento; mantener no_verificable cuando la evidencia no basta.
4. GPT/DEV-024 y GPT/DEV-052: confirmar la infracción del protocolo de focus y la
   omisión de la clave de seguimiento; mantener las incertidumbres adicionales.
5. DEV-055–060: aprobar por separado adecuación de aclaración/rechazo. Su
   task_fulfillment es not_applicable, no fail ni pass de una tarea ejecutable.
6. Resto: revisar las propuestas positivas contrastando subtareas y referentes,
   sin inferir cumplimiento solo de la coincidencia con CLIPS.

## Después: posibles correcciones de desarrollo

| Área | Evidencia | Cambio a estudiar (no implementado) | Comprobación necesaria |
|---|---|---|---|
| Focus GPT | DEV-024 | Asegurar interacción continua en prompt/validación semántica | Probar combinaciones de say/listen y cambios de interlocutor |
| Seguimiento GPT | DEV-052 | Conservar instrucción de protocolo, no solo anuncio | Verificar contrato del ejecutor y retorno/destino |
| Adaptación de tipos | Control DEV-054 | Respetar kind=object ante mayúsculas | Objeto/persona con nombres ambiguos, prueba negativa y positiva |
| Atributos conjuntos | DEV-049 | Admitir conjunción o rechazar explícitamente | Dos atributos satisfechos a la vez, sin relajarlos a uno |
| Conteo filtrado | DEV-050 | Conservar wearing en expansión o declarar límite | Diferenciar conteo total y conteo filtrado |
| Peso | DEV-051 | Evitar sustituir peso por tamaño; delimitar/rechazar capacidad | No anunciar peso cuando solo se mide tamaño |
| Qwen y JSON | HTTP 422 | Investigar tokens de parada/decodificación y ejemplos | Conservar salida original; no ocultar acciones fuera del repertorio reparando solo JSON |
| Composición y entidades | DEV-001–003, 029, 053 | Auditar cobertura del entrenamiento, luego diseñar desarrollo controlado | Separar efecto de longitud, composición y léxico |

Cualquier ajuste genera una versión posterior y requiere nuevas campañas.
La selección del bloque principal y de diagnósticos debe declararse; no eliminar
retrospectivamente casos difíciles. Si cambian entradas, repetir auditoría.

## Conjunto independiente final

Todavía no se generan órdenes finales: primero cerrar familias admisibles,
contrato evaluable y configuración. Después diseñar nuevas instancias de
intención sin reutilizar desarrollo, con formulaciones agrupadas por intención,
auditoría contra los conjuntos realmente usados por ambos Qwen y aprobación
antes de observar respuestas. Congelar criterios, parámetros y política de
reintentos. Tres repeticiones no equivalen a tres intenciones independientes.

## Registro de aprobación

Las 180 filas conservan review_status=pending_investigator_review. El archivo
CSV permite anotar decisiones por caso/modelo. Tras recibirlas se puede crear
una evaluación versionada vinculada por run_id y huella, en una salida separada
para mantener intactas las campañas. No atribuir al investigador una aprobación
que todavía no ha dado ni trasladar automáticamente propuestas al evaluador.
