# Clasificación de las 60 órdenes — aprobada

Propuesta del 18 de octubre de 2026. **Clasificación aprobada por el investigador el 21 de octubre de 2026, sin cambios de bloque.**
El [registro de aprobación](../../reports/auditoria_cobertura_20261018/aprobacion_clasificacion_20261021.json) vincula las 60 decisiones a la huella de la propuesta.
La aprobación se refiere a cobertura; los dictámenes de las salidas siguen pendientes.
Los CSV/JSONL originales se conservan como propuesta histórica; el registro separado documenta la aprobación.

El campo `input` sigue siendo la instrucción original en inglés. El español es una ayuda
para revisar el significado: no se envía a los modelos y no sustituye las pruebas de ruido.
Las traducciones regularizan erratas, repeticiones y espacios del inglés. Se conservan nombres
propios, la etiqueta `Water` y la distinción entre `mug` y `cup`. “Punto de inspección” no es
el punto donde se recibió la instrucción.

La cobertura se refiere al **generador local ampliado y sus catálogos actuales**. No certifica
qué admite todo GPSR ni una edición oficial del Command Generator: su commit histórico sigue
sin identificarse. Una estructura admitida puede tener una redacción que el generador no emita
literalmente. La derivabilidad literal de cada frase no se ha certificado.

Se separan cuatro cuestiones: cobertura estructural y léxica, variante lingüística,
capacidad del planificador/ejecutor y coincidencia con el corpus. La categoría G no implica
plan correcto ni capacidad física demostrada. No se han usado los aciertos/fallos de los
modelos para decidir si una estructura pertenece al generador.

## Bloques propuestos
 
| Código | Criterio | Órdenes |
| --- | --- | ---: |
| G | Estructura y entidades contempladas por el generador local | 46 |
| L | Estructura contemplada con extensión léxica de ubicación | 3 |
| C | Composición fuera de las rutas del generador local | 4 |
| M | Conjunción de atributos fuera de las plantillas locales | 1 |
| A | Información necesaria ausente | 3 |
| F | Acciones fuera del repertorio actual | 2 |
| X | Instrucción contradictoria | 1 |

Los códigos son propios de esta propuesta; no reemplazan los bloques históricos ni usan A/B
como sinónimo de frase vista/no vista. `canonica`, paráfrasis y ruido se conservan como un eje
independiente, según la ficha original. Las 60 órdenes contienen 28 intenciones; las primeras
48 son 16 tríadas, no 48 tareas independientes.

## Cómo revisar

En cada ficha verifica la traducción, la familia/ruta, el bloque y la observación de capacidad.
En el CSV puedes completar `review_decision` con `aprobar`, `corregir` o `duda`, y explicar
la corrección en `review_notes`, con tu nombre en `reviewer`. No cambies `input`. También puedes
indicar las correcciones por ID. Mantén `review_status` pendiente hasta resolver las dudas.
Una observación de capacidad no es un dictamen final de ninguna salida del modelo.
Guarda una copia del CSV para tu revisión: regenerar los artefactos sobrescribe la propuesta.

Puntos prioritarios:

- DEV-001–003 y DEV-053: composiciones adicionales con acciones disponibles; medirlas aparte
  permite estudiar generalización, sin declararlas imposibles para el robot.
- DEV-016–018: decidir si `table` cuenta como alias contextual de `kitchen table` o extensión
  léxica. Esta propuesta conserva L; no inventa equivalencia entre lugares.
- DEV-049: gesto y vestimenta simultáneos; no confundirlo con color + prenda.
- DEV-050–051: estructuras presentes en el generador con brechas simbólicas. Mantenerlas dentro
  del ámbito del generador y señalar la limitación de extremo a extremo.
- DEV-054: `Water` sí es un objeto del catálogo; revisar el adaptador.
- DEV-055–060: medir aclaración, limitación o contradicción; no exigirles un plan ejecutable
  inventando lo que falta. En DEV-058 se solicita volar, no buscar una persona que vuele.

## Evidencia y límites

Fuentes: [familias locales](../../reports/auditoria_cobertura_20261018/FAMILIAS.md),
[procedencia](../../reports/auditoria_cobertura_20261018/PROCEDENCIA.md),
[plantillas y follow-ups](../../qwen_gpsr/domain/command_constants.py),
[expansión de objetivos](../../qwen_gpsr/generation/command_goals.py),
[resolución de plantillas](../../qwen_gpsr/generation/command_utils.py),
[catálogo de ubicaciones](../../data/CompetitionTemplate/maps/location_names.md),
[habitaciones](../../data/CompetitionTemplate/maps/room_names.md),
[objetos](../../data/CompetitionTemplate/objects/objects.md) y
[nombres](../../data/CompetitionTemplate/names/names.md).
Las observaciones simbólicas se apoyan en el
[adaptador independiente](../../experiments/vendor/goal_adapter.py) y las
[reglas CLIPS independientes](../../experiments/vendor/goals_planning.clp):
`qualifier` único, `count-query`, `size-filter` y heurística de nombre propio.
El [esquema canónico](../../qwen_gpsr/domain/goal_schema.py) define el repertorio de objetivos.

Las rutas de follow-up permiten buscar después de ir, tomar después de buscar un objeto y
colocar/entregar después de tomar. Las rutas de personas permiten conversar, seguir o guiar
tras encontrar. No incluyen un segundo go aislado ni reiniciar una tarea independiente de
recogida tras entregar. Esta lectura del código apoya C; la ausencia en el corpus por sí sola
no sería evidencia suficiente.

Las coincidencias vienen de la [auditoría v02](../../reports/evaluation/auditoria_desarrollo_v02.json),
cuya huella se comprueba contra las entradas y el corpus actuales. No hay coincidencias
literales; hay ocho órdenes coincidentes tras el normalizador (010, 012, 025, 027, 031, 033,
040, 042). Sus grupos de intención incluyen también 011, 026, 032 y 041. Ausencia de coincidencia
no demuestra novedad semántica. Ambos modelos usaron el mismo corpus según el investigador;
no se dispone de índices históricos que certifiquen qué filas estuvieron en train o validación.

Para el análisis principal, presentar desempeño dentro de G e indicar sus brechas de capacidad;
presentar L/C/M/A/F/X por separado. También se puede mostrar el subconjunto con capacidades
confirmadas, siempre con criterios explícitos y manteniendo visible el total G. Esta es una
estratificación exploratoria posterior al piloto: debe declararse así y fijarse antes del
experimento final independiente. No recalcular una puntuación global ocultando los casos difíciles.
Comparar variantes dentro de una misma intención y reportar tanto órdenes como intenciones;
los bloques pequeños de diagnóstico no permiten estimaciones precisas por sí solos.

## Fichas para revisar

### DEV-001 · INT-01 · C

**Inglés — entrada original:** Go to the corridor, then go to the inspection point.

**Español — ayuda de lectura:** Ve al pasillo y después al punto de inspección.

- **Bloque propuesto:** Composición fuera de las rutas del generador local.
- **Variante original:** `canonica`.
- **Familia/ruta:** `simpleGoToLoc / goToLoc`.
- **Justificación:** Dos go consecutivos. simpleGoToLoc produce uno; goToLoc continúa con buscar objeto/persona, no con otro desplazamiento aislado.
- **Capacidad a revisar:** Las acciones go existen. Evaluar generalización composicional; inspection point no es instruction_point.
- **Corpus:** Sin coincidencia normalizada detectada; pertenencia histórica a train no verificada. Grupo: `grupo_sin_coincidencias_detectadas_v02`.
- **Revisión:** aprobada por el investigador el 2026-10-21, sin correcciones de bloque.

### DEV-002 · INT-01 · C

**Inglés — entrada original:** Visit the corridor first and the inspection point afterwards.

**Español — ayuda de lectura:** Visita primero el pasillo y después el punto de inspección.

- **Bloque propuesto:** Composición fuera de las rutas del generador local.
- **Variante original:** `parafrasis`.
- **Familia/ruta:** `simpleGoToLoc / goToLoc`.
- **Justificación:** Dos go consecutivos. simpleGoToLoc produce uno; goToLoc continúa con buscar objeto/persona, no con otro desplazamiento aislado.
- **Capacidad a revisar:** Las acciones go existen. Evaluar generalización composicional; inspection point no es instruction_point.
- **Corpus:** Sin coincidencia normalizada detectada; pertenencia histórica a train no verificada. Grupo: `grupo_sin_coincidencias_detectadas_v02`.
- **Revisión:** aprobada por el investigador el 2026-10-21, sin correcciones de bloque.

### DEV-003 · INT-01 · C

**Inglés — entrada original:** please go go to the corridor then go to the inspection point

**Español — ayuda de lectura:** Por favor, ve al pasillo y después al punto de inspección.

- **Bloque propuesto:** Composición fuera de las rutas del generador local.
- **Variante original:** `ruido_leve`.
- **Familia/ruta:** `simpleGoToLoc / goToLoc`.
- **Justificación:** Dos go consecutivos. simpleGoToLoc produce uno; goToLoc continúa con buscar objeto/persona, no con otro desplazamiento aislado.
- **Capacidad a revisar:** Las acciones go existen. Evaluar generalización composicional; inspection point no es instruction_point.
- **Corpus:** Sin coincidencia normalizada detectada; pertenencia histórica a train no verificada. Grupo: `grupo_sin_coincidencias_detectadas_v02`.
- **Revisión:** aprobada por el investigador el 2026-10-21, sin correcciones de bloque.

### DEV-004 · INT-02 · G

**Inglés — entrada original:** Find a peach in the bathroom.

**Español — ayuda de lectura:** Encuentra un durazno en el baño.

- **Bloque propuesto:** Estructura y entidades contempladas por el generador local.
- **Variante original:** `canonica`.
- **Familia/ruta:** `findObjectInRoomSimple`.
- **Justificación:** Ruta go(room) → find(objeto); peach y bathroom están en los catálogos.
- **Capacidad a revisar:** Conservar objeto y habitación.
- **Corpus:** Sin coincidencia normalizada detectada; pertenencia histórica a train no verificada. Grupo: `grupo_sin_coincidencias_detectadas_v02`.
- **Revisión:** aprobada por el investigador el 2026-10-21, sin correcciones de bloque.

### DEV-005 · INT-02 · G

**Inglés — entrada original:** Look for a peach inside the bathroom.

**Español — ayuda de lectura:** Busca un durazno dentro del baño.

- **Bloque propuesto:** Estructura y entidades contempladas por el generador local.
- **Variante original:** `parafrasis`.
- **Familia/ruta:** `findObjectInRoomSimple`.
- **Justificación:** Ruta go(room) → find(objeto); peach y bathroom están en los catálogos.
- **Capacidad a revisar:** Conservar objeto y habitación.
- **Corpus:** Sin coincidencia normalizada detectada; pertenencia histórica a train no verificada. Grupo: `grupo_sin_coincidencias_detectadas_v02`.
- **Revisión:** aprobada por el investigador el 2026-10-21, sin correcciones de bloque.

### DEV-006 · INT-02 · G

**Inglés — entrada original:** please find a peach in the bathrom

**Español — ayuda de lectura:** Por favor, encuentra un durazno en el baño.

- **Bloque propuesto:** Estructura y entidades contempladas por el generador local.
- **Variante original:** `ruido_leve`.
- **Familia/ruta:** `findObjectInRoomSimple`.
- **Justificación:** Ruta go(room) → find(objeto); peach y bathroom están en los catálogos.
- **Capacidad a revisar:** Conservar objeto y habitación.
- **Corpus:** Sin coincidencia normalizada detectada; pertenencia histórica a train no verificada. Grupo: `grupo_sin_coincidencias_detectadas_v02`.
- **Revisión:** aprobada por el investigador el 2026-10-21, sin correcciones de bloque.

### DEV-007 · INT-03 · G

**Inglés — entrada original:** Find a spoon at the bed and take it.

**Español — ayuda de lectura:** Encuentra una cuchara en la cama y tómala.

- **Bloque propuesto:** Estructura y entidades contempladas por el generador local.
- **Variante original:** `canonica`.
- **Familia/ruta:** `takeObjInRoom`.
- **Justificación:** Ruta go(loc_room) → find(objeto) → take; spoon y bed están en los catálogos.
- **Capacidad a revisar:** Conservar la dependencia encontrar antes de tomar.
- **Corpus:** Sin coincidencia normalizada detectada; pertenencia histórica a train no verificada. Grupo: `grupo_sin_coincidencias_detectadas_v02`.
- **Revisión:** aprobada por el investigador el 2026-10-21, sin correcciones de bloque.

### DEV-008 · INT-03 · G

**Inglés — entrada original:** Pick up the spoon you find at the bed.

**Español — ayuda de lectura:** Recoge la cuchara que encuentres en la cama.

- **Bloque propuesto:** Estructura y entidades contempladas por el generador local.
- **Variante original:** `parafrasis`.
- **Familia/ruta:** `takeObjInRoom`.
- **Justificación:** Ruta go(loc_room) → find(objeto) → take; spoon y bed están en los catálogos.
- **Capacidad a revisar:** Conservar la dependencia encontrar antes de tomar.
- **Corpus:** Sin coincidencia normalizada detectada; pertenencia histórica a train no verificada. Grupo: `grupo_sin_coincidencias_detectadas_v02`.
- **Revisión:** aprobada por el investigador el 2026-10-21, sin correcciones de bloque.

### DEV-009 · INT-03 · G

**Inglés — entrada original:** please find a spoon at the bed and and take it

**Español — ayuda de lectura:** Por favor, encuentra una cuchara en la cama y tómala.

- **Bloque propuesto:** Estructura y entidades contempladas por el generador local.
- **Variante original:** `ruido_leve`.
- **Familia/ruta:** `takeObjInRoom`.
- **Justificación:** Ruta go(loc_room) → find(objeto) → take; spoon y bed están en los catálogos.
- **Capacidad a revisar:** Conservar la dependencia encontrar antes de tomar.
- **Corpus:** Sin coincidencia normalizada detectada; pertenencia histórica a train no verificada. Grupo: `grupo_sin_coincidencias_detectadas_v02`.
- **Revisión:** aprobada por el investigador el 2026-10-21, sin correcciones de bloque.

### DEV-010 · INT-04 · G

**Inglés — entrada original:** Bring me a mug from the cabinet.

**Español — ayuda de lectura:** Tráeme una taza (mug) del gabinete.

- **Bloque propuesto:** Estructura y entidades contempladas por el generador local.
- **Variante original:** `canonica`.
- **Familia/ruta:** `bringMeObjFromPlcmt`.
- **Justificación:** Ruta go → find → take → deliver(to=me); mug y cabinet están en los catálogos.
- **Capacidad a revisar:** Entregar al solicitante; no basta con tomar el objeto.
- **Corpus:** Coincidencia normalizada, línea(s) 4671; pertenencia histórica a train no verificada. Grupo: `grupo_con_coincidencias_detectadas_v02`.
- **Revisión:** aprobada por el investigador el 2026-10-21, sin correcciones de bloque.

### DEV-011 · INT-04 · G

**Inglés — entrada original:** Fetch a mug at the cabinet and deliver it to me.

**Español — ayuda de lectura:** Recoge una taza (mug) en el gabinete y entrégamela.

- **Bloque propuesto:** Estructura y entidades contempladas por el generador local.
- **Variante original:** `parafrasis`.
- **Familia/ruta:** `bringMeObjFromPlcmt`.
- **Justificación:** Ruta go → find → take → deliver(to=me); mug y cabinet están en los catálogos.
- **Capacidad a revisar:** Entregar al solicitante; no basta con tomar el objeto.
- **Corpus:** Sin coincidencia normalizada detectada; pertenencia histórica a train no verificada. Grupo: `grupo_con_coincidencias_detectadas_v02`.
- **Revisión:** aprobada por el investigador el 2026-10-21, sin correcciones de bloque.

### DEV-012 · INT-04 · G

**Inglés — entrada original:** please bring me a mug from the cabnet

**Español — ayuda de lectura:** Por favor, tráeme una taza (mug) del gabinete.

- **Bloque propuesto:** Estructura y entidades contempladas por el generador local.
- **Variante original:** `ruido_leve`.
- **Familia/ruta:** `bringMeObjFromPlcmt`.
- **Justificación:** Ruta go → find → take → deliver(to=me); mug y cabinet están en los catálogos.
- **Capacidad a revisar:** Entregar al solicitante; no basta con tomar el objeto.
- **Corpus:** Coincidencia normalizada, línea(s) 4671; pertenencia histórica a train no verificada. Grupo: `grupo_con_coincidencias_detectadas_v02`.
- **Revisión:** aprobada por el investigador el 2026-10-21, sin correcciones de bloque.

### DEV-013 · INT-05 · G

**Inglés — entrada original:** Bring a bowl from the bed to the storage rack.

**Español — ayuda de lectura:** Lleva un tazón de la cama a la estantería de almacenamiento.

- **Bloque propuesto:** Estructura y entidades contempladas por el generador local.
- **Variante original:** `canonica`.
- **Familia/ruta:** `bringObjFromTo`.
- **Justificación:** Ruta go → find → take → place(at=destino); bowl, bed y storage rack están en los catálogos.
- **Capacidad a revisar:** Conservar origen y destino, sin confundir traslado con entrega a persona.
- **Corpus:** Sin coincidencia normalizada detectada; pertenencia histórica a train no verificada. Grupo: `grupo_sin_coincidencias_detectadas_v02`.
- **Revisión:** aprobada por el investigador el 2026-10-21, sin correcciones de bloque.

### DEV-014 · INT-05 · G

**Inglés — entrada original:** Collect a bowl at the bed and leave it at the storage rack.

**Español — ayuda de lectura:** Recoge un tazón en la cama y déjalo en la estantería de almacenamiento.

- **Bloque propuesto:** Estructura y entidades contempladas por el generador local.
- **Variante original:** `parafrasis`.
- **Familia/ruta:** `bringObjFromTo`.
- **Justificación:** Ruta go → find → take → place(at=destino); bowl, bed y storage rack están en los catálogos.
- **Capacidad a revisar:** Conservar origen y destino, sin confundir traslado con entrega a persona.
- **Corpus:** Sin coincidencia normalizada detectada; pertenencia histórica a train no verificada. Grupo: `grupo_sin_coincidencias_detectadas_v02`.
- **Revisión:** aprobada por el investigador el 2026-10-21, sin correcciones de bloque.

### DEV-015 · INT-05 · G

**Inglés — entrada original:** please bring a bowl from the bed to the storage  rack

**Español — ayuda de lectura:** Por favor, lleva un tazón de la cama a la estantería de almacenamiento.

- **Bloque propuesto:** Estructura y entidades contempladas por el generador local.
- **Variante original:** `ruido_leve`.
- **Familia/ruta:** `bringObjFromTo`.
- **Justificación:** Ruta go → find → take → place(at=destino); bowl, bed y storage rack están en los catálogos.
- **Capacidad a revisar:** Conservar origen y destino, sin confundir traslado con entrega a persona.
- **Corpus:** Sin coincidencia normalizada detectada; pertenencia histórica a train no verificada. Grupo: `grupo_sin_coincidencias_detectadas_v02`.
- **Revisión:** aprobada por el investigador el 2026-10-21, sin correcciones de bloque.

### DEV-016 · INT-06 · L

**Inglés — entrada original:** In the kitchen, find a cup, take it, and put it on the table.

**Español — ayuda de lectura:** En la cocina, encuentra una taza (cup), tómala y ponla sobre la mesa.

- **Bloque propuesto:** Estructura contemplada con extensión léxica de ubicación.
- **Variante original:** `canonica`.
- **Familia/ruta:** `findObjInRoom → takeObj → placeObjOnPlcmt`.
- **Justificación:** La estructura está contemplada. cup y kitchen existen, pero table no es una entrada literal del catálogo: sí existe kitchen table.
- **Capacidad a revisar:** Revisar si table se acepta como alias contextual. No sustituirlo automáticamente ni cambiar las órdenes históricas.
- **Corpus:** Sin coincidencia normalizada detectada; pertenencia histórica a train no verificada. Grupo: `grupo_sin_coincidencias_detectadas_v02`.
- **Revisión:** aprobada por el investigador el 2026-10-21, sin correcciones de bloque.

### DEV-017 · INT-06 · L

**Inglés — entrada original:** Locate a cup in the kitchen and pick it up, then place it on the table there.

**Español — ayuda de lectura:** Localiza una taza (cup) en la cocina y recógela; después colócala sobre la mesa de allí.

- **Bloque propuesto:** Estructura contemplada con extensión léxica de ubicación.
- **Variante original:** `parafrasis`.
- **Familia/ruta:** `findObjInRoom → takeObj → placeObjOnPlcmt`.
- **Justificación:** La estructura está contemplada. cup y kitchen existen, pero table no es una entrada literal del catálogo: sí existe kitchen table.
- **Capacidad a revisar:** Revisar si table se acepta como alias contextual. No sustituirlo automáticamente ni cambiar las órdenes históricas.
- **Corpus:** Sin coincidencia normalizada detectada; pertenencia histórica a train no verificada. Grupo: `grupo_sin_coincidencias_detectadas_v02`.
- **Revisión:** aprobada por el investigador el 2026-10-21, sin correcciones de bloque.

### DEV-018 · INT-06 · L

**Inglés — entrada original:** in the kichen find a cup take it and put it on the table please

**Español — ayuda de lectura:** En la cocina, encuentra una taza (cup), tómala y ponla sobre la mesa, por favor.

- **Bloque propuesto:** Estructura contemplada con extensión léxica de ubicación.
- **Variante original:** `ruido_leve`.
- **Familia/ruta:** `findObjInRoom → takeObj → placeObjOnPlcmt`.
- **Justificación:** La estructura está contemplada. cup y kitchen existen, pero table no es una entrada literal del catálogo: sí existe kitchen table.
- **Capacidad a revisar:** Revisar si table se acepta como alias contextual. No sustituirlo automáticamente ni cambiar las órdenes históricas.
- **Corpus:** Sin coincidencia normalizada detectada; pertenencia histórica a train no verificada. Grupo: `grupo_sin_coincidencias_detectadas_v02`.
- **Revisión:** aprobada por el investigador el 2026-10-21, sin correcciones de bloque.

### DEV-019 · INT-07 · G

**Inglés — entrada original:** Find Robin in the office.

**Español — ayuda de lectura:** Encuentra a Robin en la oficina.

- **Bloque propuesto:** Estructura y entidades contempladas por el generador local.
- **Variante original:** `canonica`.
- **Familia/ruta:** `findNameInRoom`.
- **Justificación:** Ruta go → find(kind=person); Robin y office están en los catálogos.
- **Capacidad a revisar:** La corrección del plan requiere que la identidad solicitada se preserve; una búsqueda genérica no la demuestra.
- **Corpus:** Sin coincidencia normalizada detectada; pertenencia histórica a train no verificada. Grupo: `grupo_sin_coincidencias_detectadas_v02`.
- **Revisión:** aprobada por el investigador el 2026-10-21, sin correcciones de bloque.

### DEV-020 · INT-07 · G

**Inglés — entrada original:** Look for Robin inside the office.

**Español — ayuda de lectura:** Busca a Robin dentro de la oficina.

- **Bloque propuesto:** Estructura y entidades contempladas por el generador local.
- **Variante original:** `parafrasis`.
- **Familia/ruta:** `findNameInRoom`.
- **Justificación:** Ruta go → find(kind=person); Robin y office están en los catálogos.
- **Capacidad a revisar:** La corrección del plan requiere que la identidad solicitada se preserve; una búsqueda genérica no la demuestra.
- **Corpus:** Sin coincidencia normalizada detectada; pertenencia histórica a train no verificada. Grupo: `grupo_sin_coincidencias_detectadas_v02`.
- **Revisión:** aprobada por el investigador el 2026-10-21, sin correcciones de bloque.

### DEV-021 · INT-07 · G

**Inglés — entrada original:** please find Robin in the ofice

**Español — ayuda de lectura:** Por favor, encuentra a Robin en la oficina.

- **Bloque propuesto:** Estructura y entidades contempladas por el generador local.
- **Variante original:** `ruido_leve`.
- **Familia/ruta:** `findNameInRoom`.
- **Justificación:** Ruta go → find(kind=person); Robin y office están en los catálogos.
- **Capacidad a revisar:** La corrección del plan requiere que la identidad solicitada se preserve; una búsqueda genérica no la demuestra.
- **Corpus:** Sin coincidencia normalizada detectada; pertenencia histórica a train no verificada. Grupo: `grupo_sin_coincidencias_detectadas_v02`.
- **Revisión:** aprobada por el investigador el 2026-10-21, sin correcciones de bloque.

### DEV-022 · INT-08 · G

**Inglés — entrada original:** Find Morgan in the kitchen and guide them to the entrance.

**Español — ayuda de lectura:** Encuentra a Morgan en la cocina y guía a esa persona hasta la entrada.

- **Bloque propuesto:** Estructura y entidades contempladas por el generador local.
- **Variante original:** `canonica`.
- **Familia/ruta:** `meetPrsAtBeac → guidePrsToBeacon`.
- **Justificación:** Ruta go → find(nombre) → guide; Morgan, kitchen y entrance están en los catálogos.
- **Capacidad a revisar:** Verificar identidad y destino en el contrato del ejecutor.
- **Corpus:** Sin coincidencia normalizada detectada; pertenencia histórica a train no verificada. Grupo: `grupo_sin_coincidencias_detectadas_v02`.
- **Revisión:** aprobada por el investigador el 2026-10-21, sin correcciones de bloque.

### DEV-023 · INT-08 · G

**Inglés — entrada original:** Meet Morgan in the kitchen, then lead Morgan to the entrance.

**Español — ayuda de lectura:** Encuéntrate con Morgan en la cocina y después guía a Morgan hasta la entrada.

- **Bloque propuesto:** Estructura y entidades contempladas por el generador local.
- **Variante original:** `parafrasis`.
- **Familia/ruta:** `meetPrsAtBeac → guidePrsToBeacon`.
- **Justificación:** Ruta go → find(nombre) → guide; Morgan, kitchen y entrance están en los catálogos.
- **Capacidad a revisar:** Verificar identidad y destino en el contrato del ejecutor.
- **Corpus:** Sin coincidencia normalizada detectada; pertenencia histórica a train no verificada. Grupo: `grupo_sin_coincidencias_detectadas_v02`.
- **Revisión:** aprobada por el investigador el 2026-10-21, sin correcciones de bloque.

### DEV-024 · INT-08 · G

**Inglés — entrada original:** find Morgan in the kichen and guide them to the entrance please

**Español — ayuda de lectura:** Encuentra a Morgan en la cocina y guía a esa persona hasta la entrada, por favor.

- **Bloque propuesto:** Estructura y entidades contempladas por el generador local.
- **Variante original:** `ruido_leve`.
- **Familia/ruta:** `meetPrsAtBeac → guidePrsToBeacon`.
- **Justificación:** Ruta go → find(nombre) → guide; Morgan, kitchen y entrance están en los catálogos.
- **Capacidad a revisar:** Verificar identidad y destino en el contrato del ejecutor.
- **Corpus:** Sin coincidencia normalizada detectada; pertenencia histórica a train no verificada. Grupo: `grupo_sin_coincidencias_detectadas_v02`.
- **Revisión:** aprobada por el investigador el 2026-10-21, sin correcciones de bloque.

### DEV-025 · INT-09 · G

**Inglés — entrada original:** Find the waving person in the bedroom and follow them.

**Español — ayuda de lectura:** Encuentra en el dormitorio a la persona que saluda con la mano y síguela.

- **Bloque propuesto:** Estructura y entidades contempladas por el generador local.
- **Variante original:** `canonica`.
- **Familia/ruta:** `findPrsInRoom → followPrs / followPrsAtLoc`.
- **Justificación:** Ruta go → find(gesture=waving) → follow; bedroom está en el catálogo y waving es gesto admitido.
- **Capacidad a revisar:** Conservar el gesto y el referente de la persona seguida.
- **Corpus:** Coincidencia normalizada, línea(s) 35245; pertenencia histórica a train no verificada. Grupo: `grupo_con_coincidencias_detectadas_v02`.
- **Revisión:** aprobada por el investigador el 2026-10-21, sin correcciones de bloque.

### DEV-026 · INT-09 · G

**Inglés — entrada original:** In the bedroom, locate the person who is waving and follow that person.

**Español — ayuda de lectura:** En el dormitorio, localiza a la persona que saluda con la mano y sigue a esa persona.

- **Bloque propuesto:** Estructura y entidades contempladas por el generador local.
- **Variante original:** `parafrasis`.
- **Familia/ruta:** `findPrsInRoom → followPrs / followPrsAtLoc`.
- **Justificación:** Ruta go → find(gesture=waving) → follow; bedroom está en el catálogo y waving es gesto admitido.
- **Capacidad a revisar:** Conservar el gesto y el referente de la persona seguida.
- **Corpus:** Sin coincidencia normalizada detectada; pertenencia histórica a train no verificada. Grupo: `grupo_con_coincidencias_detectadas_v02`.
- **Revisión:** aprobada por el investigador el 2026-10-21, sin correcciones de bloque.

### DEV-027 · INT-09 · G

**Inglés — entrada original:** please find the waving person in the bedrom and follow them

**Español — ayuda de lectura:** Por favor, encuentra en el dormitorio a la persona que saluda con la mano y síguela.

- **Bloque propuesto:** Estructura y entidades contempladas por el generador local.
- **Variante original:** `ruido_leve`.
- **Familia/ruta:** `findPrsInRoom → followPrs / followPrsAtLoc`.
- **Justificación:** Ruta go → find(gesture=waving) → follow; bedroom está en el catálogo y waving es gesto admitido.
- **Capacidad a revisar:** Conservar el gesto y el referente de la persona seguida.
- **Corpus:** Coincidencia normalizada, línea(s) 35245; pertenencia histórica a train no verificada. Grupo: `grupo_con_coincidencias_detectadas_v02`.
- **Revisión:** aprobada por el investigador el 2026-10-21, sin correcciones de bloque.

### DEV-028 · INT-10 · G

**Inglés — entrada original:** Take an orange from the refrigerator and give it to Sarah in the kitchen.

**Español — ayuda de lectura:** Toma una naranja del refrigerador y dásela a Sarah en la cocina.

- **Bloque propuesto:** Estructura y entidades contempladas por el generador local.
- **Variante original:** `canonica`.
- **Familia/ruta:** `takeObjFromPlcmt → deliverObjToNameAtBeac`.
- **Justificación:** Ruta de recoger y entregar a una persona nombrada en otra habitación; orange, refrigerator, Sarah y kitchen están en los catálogos.
- **Capacidad a revisar:** orange es el objeto, no una prenda o atributo; verificar identidad de destinataria.
- **Corpus:** Sin coincidencia normalizada detectada; pertenencia histórica a train no verificada. Grupo: `grupo_sin_coincidencias_detectadas_v02`.
- **Revisión:** aprobada por el investigador el 2026-10-21, sin correcciones de bloque.

### DEV-029 · INT-10 · G

**Inglés — entrada original:** Fetch an orange at the refrigerator, then find Sarah in the kitchen and hand the orange to her.

**Español — ayuda de lectura:** Recoge una naranja en el refrigerador; después encuentra a Sarah en la cocina y entrégasela.

- **Bloque propuesto:** Estructura y entidades contempladas por el generador local.
- **Variante original:** `parafrasis`.
- **Familia/ruta:** `takeObjFromPlcmt → deliverObjToNameAtBeac`.
- **Justificación:** Ruta de recoger y entregar a una persona nombrada en otra habitación; orange, refrigerator, Sarah y kitchen están en los catálogos.
- **Capacidad a revisar:** orange es el objeto, no una prenda o atributo; verificar identidad de destinataria.
- **Corpus:** Sin coincidencia normalizada detectada; pertenencia histórica a train no verificada. Grupo: `grupo_sin_coincidencias_detectadas_v02`.
- **Revisión:** aprobada por el investigador el 2026-10-21, sin correcciones de bloque.

### DEV-030 · INT-10 · G

**Inglés — entrada original:** take an orange from the refridgerator and give it to Sarah in the kichen

**Español — ayuda de lectura:** Toma una naranja del refrigerador y dásela a Sarah en la cocina.

- **Bloque propuesto:** Estructura y entidades contempladas por el generador local.
- **Variante original:** `ruido_leve`.
- **Familia/ruta:** `takeObjFromPlcmt → deliverObjToNameAtBeac`.
- **Justificación:** Ruta de recoger y entregar a una persona nombrada en otra habitación; orange, refrigerator, Sarah y kitchen están en los catálogos.
- **Capacidad a revisar:** orange es el objeto, no una prenda o atributo; verificar identidad de destinataria.
- **Corpus:** Sin coincidencia normalizada detectada; pertenencia histórica a train no verificada. Grupo: `grupo_sin_coincidencias_detectadas_v02`.
- **Revisión:** aprobada por el investigador el 2026-10-21, sin correcciones de bloque.

### DEV-031 · INT-11 · G

**Inglés — entrada original:** Count the toys on the storage rack.

**Español — ayuda de lectura:** Cuenta los juguetes que están sobre la estantería de almacenamiento.

- **Bloque propuesto:** Estructura y entidades contempladas por el generador local.
- **Variante original:** `canonica`.
- **Familia/ruta:** `countObjOnPlcmt`.
- **Justificación:** Ruta go → count(categoría); toys y storage rack están en los catálogos.
- **Capacidad a revisar:** Verificar categoría contada; expresar el resultado según el contrato del plan.
- **Corpus:** Coincidencia normalizada, línea(s) 6467; pertenencia histórica a train no verificada. Grupo: `grupo_con_coincidencias_detectadas_v02`.
- **Revisión:** aprobada por el investigador el 2026-10-21, sin correcciones de bloque.

### DEV-032 · INT-11 · G

**Inglés — entrada original:** Tell me how many toys are on the storage rack.

**Español — ayuda de lectura:** Dime cuántos juguetes hay sobre la estantería de almacenamiento.

- **Bloque propuesto:** Estructura y entidades contempladas por el generador local.
- **Variante original:** `parafrasis`.
- **Familia/ruta:** `countObjOnPlcmt`.
- **Justificación:** Ruta go → count(categoría); toys y storage rack están en los catálogos.
- **Capacidad a revisar:** Verificar categoría contada; expresar el resultado según el contrato del plan.
- **Corpus:** Sin coincidencia normalizada detectada; pertenencia histórica a train no verificada. Grupo: `grupo_con_coincidencias_detectadas_v02`.
- **Revisión:** aprobada por el investigador el 2026-10-21, sin correcciones de bloque.

### DEV-033 · INT-11 · G

**Inglés — entrada original:** please count the the toys on the storage rack

**Español — ayuda de lectura:** Por favor, cuenta los juguetes que están sobre la estantería de almacenamiento.

- **Bloque propuesto:** Estructura y entidades contempladas por el generador local.
- **Variante original:** `ruido_leve`.
- **Familia/ruta:** `countObjOnPlcmt`.
- **Justificación:** Ruta go → count(categoría); toys y storage rack están en los catálogos.
- **Capacidad a revisar:** Verificar categoría contada; expresar el resultado según el contrato del plan.
- **Corpus:** Coincidencia normalizada, línea(s) 6467; pertenencia histórica a train no verificada. Grupo: `grupo_con_coincidencias_detectadas_v02`.
- **Revisión:** aprobada por el investigador el 2026-10-21, sin correcciones de bloque.

### DEV-034 · INT-12 · G

**Inglés — entrada original:** Find Charlie in the living room and tell Charlie the current time.

**Español — ayuda de lectura:** Encuentra a Charlie en la sala y dile la hora actual.

- **Bloque propuesto:** Estructura y entidades contempladas por el generador local.
- **Variante original:** `canonica`.
- **Familia/ruta:** `meetPrsAtBeac → talkInfo`.
- **Justificación:** Buscar persona nombrada y comunicar información; TALK_LIST incluye the time, equivalente semántico de current time en estas órdenes.
- **Capacidad a revisar:** Verificar identidad y comunicación de la hora; no inventar una hora constante.
- **Corpus:** Sin coincidencia normalizada detectada; pertenencia histórica a train no verificada. Grupo: `grupo_sin_coincidencias_detectadas_v02`.
- **Revisión:** aprobada por el investigador el 2026-10-21, sin correcciones de bloque.

### DEV-035 · INT-12 · G

**Inglés — entrada original:** Locate Charlie in the living room and say what time it is to Charlie.

**Español — ayuda de lectura:** Localiza a Charlie en la sala y dile qué hora es.

- **Bloque propuesto:** Estructura y entidades contempladas por el generador local.
- **Variante original:** `parafrasis`.
- **Familia/ruta:** `meetPrsAtBeac → talkInfo`.
- **Justificación:** Buscar persona nombrada y comunicar información; TALK_LIST incluye the time, equivalente semántico de current time en estas órdenes.
- **Capacidad a revisar:** Verificar identidad y comunicación de la hora; no inventar una hora constante.
- **Corpus:** Sin coincidencia normalizada detectada; pertenencia histórica a train no verificada. Grupo: `grupo_sin_coincidencias_detectadas_v02`.
- **Revisión:** aprobada por el investigador el 2026-10-21, sin correcciones de bloque.

### DEV-036 · INT-12 · G

**Inglés — entrada original:** please find Charlie in the living  room and tell Charlie the current time

**Español — ayuda de lectura:** Por favor, encuentra a Charlie en la sala y dile la hora actual.

- **Bloque propuesto:** Estructura y entidades contempladas por el generador local.
- **Variante original:** `ruido_leve`.
- **Familia/ruta:** `meetPrsAtBeac → talkInfo`.
- **Justificación:** Buscar persona nombrada y comunicar información; TALK_LIST incluye the time, equivalente semántico de current time en estas órdenes.
- **Capacidad a revisar:** Verificar identidad y comunicación de la hora; no inventar una hora constante.
- **Corpus:** Sin coincidencia normalizada detectada; pertenencia histórica a train no verificada. Grupo: `grupo_sin_coincidencias_detectadas_v02`.
- **Revisión:** aprobada por el investigador el 2026-10-21, sin correcciones de bloque.

### DEV-037 · INT-13 · G

**Inglés — entrada original:** Find a person in the bedroom, ask their name, and come back to tell me their name.

**Español — ayuda de lectura:** Encuentra a una persona en el dormitorio, pregúntale su nombre y regresa para decírmelo.

- **Bloque propuesto:** Estructura y entidades contempladas por el generador local.
- **Variante original:** `canonica`.
- **Familia/ruta:** `tellPrsInfoInLoc`.
- **Justificación:** persInfo=name produce go → find(person) → save(name) → go(instruction_point) → tell(name).
- **Capacidad a revisar:** Verificar consulta, memoria y reporte de la misma respuesta; el plan no demuestra que la persona responda físicamente.
- **Corpus:** Sin coincidencia normalizada detectada; pertenencia histórica a train no verificada. Grupo: `grupo_sin_coincidencias_detectadas_v02`.
- **Revisión:** aprobada por el investigador el 2026-10-21, sin correcciones de bloque.

### DEV-038 · INT-13 · G

**Inglés — entrada original:** Go to the bedroom, learn the name of a person there, then return and report it to me.

**Español — ayuda de lectura:** Ve al dormitorio, averigua el nombre de una persona que esté allí y después regresa para informármelo.

- **Bloque propuesto:** Estructura y entidades contempladas por el generador local.
- **Variante original:** `parafrasis`.
- **Familia/ruta:** `tellPrsInfoInLoc`.
- **Justificación:** persInfo=name produce go → find(person) → save(name) → go(instruction_point) → tell(name).
- **Capacidad a revisar:** Verificar consulta, memoria y reporte de la misma respuesta; el plan no demuestra que la persona responda físicamente.
- **Corpus:** Sin coincidencia normalizada detectada; pertenencia histórica a train no verificada. Grupo: `grupo_sin_coincidencias_detectadas_v02`.
- **Revisión:** aprobada por el investigador el 2026-10-21, sin correcciones de bloque.

### DEV-039 · INT-13 · G

**Inglés — entrada original:** please find a person in the bedroom ask their name and come back to tell me their name

**Español — ayuda de lectura:** Por favor, encuentra a una persona en el dormitorio, pregúntale su nombre y regresa para decírmelo.

- **Bloque propuesto:** Estructura y entidades contempladas por el generador local.
- **Variante original:** `ruido_leve`.
- **Familia/ruta:** `tellPrsInfoInLoc`.
- **Justificación:** persInfo=name produce go → find(person) → save(name) → go(instruction_point) → tell(name).
- **Capacidad a revisar:** Verificar consulta, memoria y reporte de la misma respuesta; el plan no demuestra que la persona responda físicamente.
- **Corpus:** Sin coincidencia normalizada detectada; pertenencia histórica a train no verificada. Grupo: `grupo_sin_coincidencias_detectadas_v02`.
- **Revisión:** aprobada por el investigador el 2026-10-21, sin correcciones de bloque.

### DEV-040 · INT-14 · G

**Inglés — entrada original:** Find the waving person in the corridor and answer their question.

**Español — ayuda de lectura:** Encuentra en el pasillo a la persona que saluda con la mano y responde a su pregunta.

- **Bloque propuesto:** Estructura y entidades contempladas por el generador local.
- **Variante original:** `canonica`.
- **Familia/ruta:** `answerQuestionOfPersInRoom`.
- **Justificación:** Ruta go → find(person,gesture) → answer_question; corridor y waving son admisibles.
- **Capacidad a revisar:** Revisar ciclo de interacción y conservación de la persona encontrada.
- **Corpus:** Coincidencia normalizada, línea(s) 18455; pertenencia histórica a train no verificada. Grupo: `grupo_con_coincidencias_detectadas_v02`.
- **Revisión:** aprobada por el investigador el 2026-10-21, sin correcciones de bloque.

### DEV-041 · INT-14 · G

**Inglés — entrada original:** In the corridor, locate the person who is waving and respond to that person's question.

**Español — ayuda de lectura:** En el pasillo, localiza a la persona que saluda con la mano y responde a la pregunta de esa persona.

- **Bloque propuesto:** Estructura y entidades contempladas por el generador local.
- **Variante original:** `parafrasis`.
- **Familia/ruta:** `answerQuestionOfPersInRoom`.
- **Justificación:** Ruta go → find(person,gesture) → answer_question; corridor y waving son admisibles.
- **Capacidad a revisar:** Revisar ciclo de interacción y conservación de la persona encontrada.
- **Corpus:** Sin coincidencia normalizada detectada; pertenencia histórica a train no verificada. Grupo: `grupo_con_coincidencias_detectadas_v02`.
- **Revisión:** aprobada por el investigador el 2026-10-21, sin correcciones de bloque.

### DEV-042 · INT-14 · G

**Inglés — entrada original:** find the waving person in the corridor and and answer their question please

**Español — ayuda de lectura:** Encuentra en el pasillo a la persona que saluda con la mano y responde a su pregunta, por favor.

- **Bloque propuesto:** Estructura y entidades contempladas por el generador local.
- **Variante original:** `ruido_leve`.
- **Familia/ruta:** `answerQuestionOfPersInRoom`.
- **Justificación:** Ruta go → find(person,gesture) → answer_question; corridor y waving son admisibles.
- **Capacidad a revisar:** Revisar ciclo de interacción y conservación de la persona encontrada.
- **Corpus:** Coincidencia normalizada, línea(s) 18455; pertenencia histórica a train no verificada. Grupo: `grupo_con_coincidencias_detectadas_v02`.
- **Revisión:** aprobada por el investigador el 2026-10-21, sin correcciones de bloque.

### DEV-043 · INT-15 · G

**Inglés — entrada original:** Find Jane in the kitchen and greet her.

**Español — ayuda de lectura:** Encuentra a Jane en la cocina y salúdala.

- **Bloque propuesto:** Estructura y entidades contempladas por el generador local.
- **Variante original:** `canonica`.
- **Familia/ruta:** `greetNameInRoomSimple`.
- **Justificación:** Ruta go → find(nombre) → greet; Jane y kitchen están en los catálogos.
- **Capacidad a revisar:** Verificar saludo a Jane y ciclo de interacción.
- **Corpus:** Sin coincidencia normalizada detectada; pertenencia histórica a train no verificada. Grupo: `grupo_sin_coincidencias_detectadas_v02`.
- **Revisión:** aprobada por el investigador el 2026-10-21, sin correcciones de bloque.

### DEV-044 · INT-15 · G

**Inglés — entrada original:** Look for Jane in the kitchen and say hello to Jane.

**Español — ayuda de lectura:** Busca a Jane en la cocina y dile hola.

- **Bloque propuesto:** Estructura y entidades contempladas por el generador local.
- **Variante original:** `parafrasis`.
- **Familia/ruta:** `greetNameInRoomSimple`.
- **Justificación:** Ruta go → find(nombre) → greet; Jane y kitchen están en los catálogos.
- **Capacidad a revisar:** Verificar saludo a Jane y ciclo de interacción.
- **Corpus:** Sin coincidencia normalizada detectada; pertenencia histórica a train no verificada. Grupo: `grupo_sin_coincidencias_detectadas_v02`.
- **Revisión:** aprobada por el investigador el 2026-10-21, sin correcciones de bloque.

### DEV-045 · INT-15 · G

**Inglés — entrada original:** please find Jane in the kichen and greet her

**Español — ayuda de lectura:** Por favor, encuentra a Jane en la cocina y salúdala.

- **Bloque propuesto:** Estructura y entidades contempladas por el generador local.
- **Variante original:** `ruido_leve`.
- **Familia/ruta:** `greetNameInRoomSimple`.
- **Justificación:** Ruta go → find(nombre) → greet; Jane y kitchen están en los catálogos.
- **Capacidad a revisar:** Verificar saludo a Jane y ciclo de interacción.
- **Corpus:** Sin coincidencia normalizada detectada; pertenencia histórica a train no verificada. Grupo: `grupo_sin_coincidencias_detectadas_v02`.
- **Revisión:** aprobada por el investigador el 2026-10-21, sin correcciones de bloque.

### DEV-046 · INT-16 · G

**Inglés — entrada original:** Tell me which is the largest fruit on the sofa.

**Español — ayuda de lectura:** Dime cuál es la fruta de mayor tamaño que está sobre el sofá.

- **Bloque propuesto:** Estructura y entidades contempladas por el generador local.
- **Variante original:** `canonica`.
- **Familia/ruta:** `tellCatPropOnPlcmt`.
- **Justificación:** Ruta go → find(categoría,property) → tell; fruit, sofa y largest/biggest son admisibles.
- **Capacidad a revisar:** Comparación de tamaño; distinguirla de peso. Verificar que el plan conserva la selección solicitada.
- **Corpus:** Sin coincidencia normalizada detectada; pertenencia histórica a train no verificada. Grupo: `grupo_sin_coincidencias_detectadas_v02`.
- **Revisión:** aprobada por el investigador el 2026-10-21, sin correcciones de bloque.

### DEV-047 · INT-16 · G

**Inglés — entrada original:** Identify the biggest fruit on the sofa and report which one it is.

**Español — ayuda de lectura:** Identifica la fruta más grande que está sobre el sofá e informa cuál es.

- **Bloque propuesto:** Estructura y entidades contempladas por el generador local.
- **Variante original:** `parafrasis`.
- **Familia/ruta:** `tellCatPropOnPlcmt`.
- **Justificación:** Ruta go → find(categoría,property) → tell; fruit, sofa y largest/biggest son admisibles.
- **Capacidad a revisar:** Comparación de tamaño; distinguirla de peso. Verificar que el plan conserva la selección solicitada.
- **Corpus:** Sin coincidencia normalizada detectada; pertenencia histórica a train no verificada. Grupo: `grupo_sin_coincidencias_detectadas_v02`.
- **Revisión:** aprobada por el investigador el 2026-10-21, sin correcciones de bloque.

### DEV-048 · INT-16 · G

**Inglés — entrada original:** please tell me which is the largest fruit on the sofa

**Español — ayuda de lectura:** Por favor, dime cuál es la fruta de mayor tamaño que está sobre el sofá.

- **Bloque propuesto:** Estructura y entidades contempladas por el generador local.
- **Variante original:** `ruido_leve`.
- **Familia/ruta:** `tellCatPropOnPlcmt`.
- **Justificación:** Ruta go → find(categoría,property) → tell; fruit, sofa y largest/biggest son admisibles.
- **Capacidad a revisar:** Comparación de tamaño; distinguirla de peso. Verificar que el plan conserva la selección solicitada.
- **Corpus:** Sin coincidencia normalizada detectada; pertenencia histórica a train no verificada. Grupo: `grupo_sin_coincidencias_detectadas_v02`.
- **Revisión:** aprobada por el investigador el 2026-10-21, sin correcciones de bloque.

### DEV-049 · INT-17 · M

**Inglés — entrada original:** Find the person waving and wearing a blue coat in the office, then guide them to the entrance.

**Español — ayuda de lectura:** Encuentra en la oficina a la persona que saluda con la mano y lleva un abrigo azul; después guíala hasta la entrada.

- **Bloque propuesto:** Conjunción de atributos fuera de las plantillas locales.
- **Variante original:** `diagnostico`.
- **Familia/ruta:** `guidePrsFromBeacToBeac / guideClothPrsFromBeacToBeac`.
- **Justificación:** Hay rutas para gesto y para vestimenta por separado, no para su conjunción en la misma búsqueda. Color + prenda sí constituye un atributo wearing admitido.
- **Capacidad a revisar:** El adaptador serializa un solo qualifier. No perder silenciosamente una de las dos condiciones; evaluar manejo de solicitud no soportada.
- **Corpus:** Sin coincidencia normalizada detectada; pertenencia histórica a train no verificada. Grupo: `grupo_sin_coincidencias_detectadas_v02`.
- **Revisión:** aprobada por el investigador el 2026-10-21, sin correcciones de bloque.

### DEV-050 · INT-18 · G

**Inglés — entrada original:** Count the people wearing red shirts in the living room.

**Español — ayuda de lectura:** Cuenta las personas que llevan camisas rojas en la sala.

- **Bloque propuesto:** Estructura y entidades contempladas por el generador local.
- **Variante original:** `diagnostico`.
- **Familia/ruta:** `countClothPrsInRoom`.
- **Justificación:** Plantilla explícita para contar personas con colorClothes; el corpus contiene 1163 filas count con wearing (ejemplo línea 13).
- **Capacidad a revisar:** Brecha simbólica: count-query devuelve count_person sin conservar el filtro de vestimenta. No excluir como fuera del generador.
- **Corpus:** Sin coincidencia normalizada detectada; pertenencia histórica a train no verificada. Grupo: `grupo_sin_coincidencias_detectadas_v02`.
- **Revisión:** aprobada por el investigador el 2026-10-21, sin correcciones de bloque.

### DEV-051 · INT-19 · G

**Inglés — entrada original:** Tell me which is the heaviest fruit on the sofa.

**Español — ayuda de lectura:** Dime cuál es la fruta más pesada que está sobre el sofá.

- **Bloque propuesto:** Estructura y entidades contempladas por el generador local.
- **Variante original:** `diagnostico`.
- **Familia/ruta:** `tellCatPropOnPlcmt`.
- **Justificación:** heaviest figura en OBJECT_COMP_LIST; hay 167 filas con property=heaviest (ejemplo línea 98). fruit y sofa son admisibles.
- **Capacidad a revisar:** Brecha simbólica: size-filter agrupa heaviest con mayor tamaño. El peso no se demuestra mediante biggest_fruit. No excluir del ámbito del generador.
- **Corpus:** Sin coincidencia normalizada detectada; pertenencia histórica a train no verificada. Grupo: `grupo_sin_coincidencias_detectadas_v02`.
- **Revisión:** aprobada por el investigador el 2026-10-21, sin correcciones de bloque.

### DEV-052 · INT-20 · G

**Inglés — entrada original:** Find Simone at the coatrack and follow Simone to the bedroom.

**Español — ayuda de lectura:** Encuentra a Simone junto al perchero y sigue a Simone hasta el dormitorio.

- **Bloque propuesto:** Estructura y entidades contempladas por el generador local.
- **Variante original:** `diagnostico`.
- **Familia/ruta:** `followNameFromBeacToRoom`.
- **Justificación:** Ruta go → find(nombre) → follow(to=room); Simone, coatrack y bedroom están en los catálogos.
- **Capacidad a revisar:** Verificar identidad y destino del seguimiento, incluida la instrucción asociada al destino si la exige el ejecutor.
- **Corpus:** Sin coincidencia normalizada detectada; pertenencia histórica a train no verificada. Grupo: `grupo_sin_coincidencias_detectadas_v02`.
- **Revisión:** aprobada por el investigador el 2026-10-21, sin correcciones de bloque.

### DEV-053 · INT-21 · C

**Inglés — entrada original:** Bring me a mug from the refrigerator, then bring me a spoon from the bed.

**Español — ayuda de lectura:** Tráeme una taza (mug) del refrigerador y después tráeme una cuchara de la cama.

- **Bloque propuesto:** Composición fuera de las rutas del generador local.
- **Variante original:** `diagnostico`.
- **Familia/ruta:** `Dos instancias de bringMeObjFromPlcmt`.
- **Justificación:** Cada entrega es admisible aisladamente; las rutas actuales no concatenan dos tareas completas de recogida/entrega con objetos distintos.
- **Capacidad a revisar:** Las acciones individuales existen. Evaluar orden de las dos entregas y separación de referentes, no solo longitud textual.
- **Corpus:** Sin coincidencia normalizada detectada; pertenencia histórica a train no verificada. Grupo: `grupo_sin_coincidencias_detectadas_v02`.
- **Revisión:** aprobada por el investigador el 2026-10-21, sin correcciones de bloque.

### DEV-054 · INT-22 · G

**Inglés — entrada original:** Find Water in the kitchen, take it, and bring it to me.

**Español — ayuda de lectura:** Encuentra Water (agua, etiqueta del objeto) en la cocina, tómalo y tráemelo.

- **Bloque propuesto:** Estructura y entidades contempladas por el generador local.
- **Variante original:** `diagnostico`.
- **Familia/ruta:** `findObjInRoom → takeObj → deliverObjToMe`.
- **Justificación:** Water aparece con mayúscula en objects.md; la ruta buscar → tomar → entregar al solicitante está contemplada.
- **Capacidad a revisar:** Comprobar kind=object. La heurística de mayúsculas del adaptador puede tratar Water como persona; no atribuirlo automáticamente al modelo.
- **Corpus:** Sin coincidencia normalizada detectada; pertenencia histórica a train no verificada. Grupo: `grupo_sin_coincidencias_detectadas_v02`.
- **Revisión:** aprobada por el investigador el 2026-10-21, sin correcciones de bloque.

### DEV-055 · INT-23 · A

**Inglés — entrada original:** Go to the kitchen and bring it to me.

**Español — ayuda de lectura:** Ve a la cocina y tráemelo.

- **Bloque propuesto:** Información necesaria ausente.
- **Variante original:** `limite_dominio`.
- **Familia/ruta:** `Objeto ausente en entrega`.
- **Justificación:** it no tiene antecedente en esta orden independiente; kitchen identifica lugar, no objeto.
- **Capacidad a revisar:** Pedir aclaración del objeto; no inventarlo.
- **Corpus:** Sin coincidencia normalizada detectada; pertenencia histórica a train no verificada. Grupo: `grupo_sin_coincidencias_detectadas_v02`.
- **Revisión:** aprobada por el investigador el 2026-10-21, sin correcciones de bloque.

### DEV-056 · INT-24 · A

**Inglés — entrada original:** Find Robin in the office and guide Robin to the destination.

**Español — ayuda de lectura:** Encuentra a Robin en la oficina y guía a Robin hasta el destino.

- **Bloque propuesto:** Información necesaria ausente.
- **Variante original:** `limite_dominio`.
- **Familia/ruta:** `Destino ausente en guía`.
- **Justificación:** the destination no identifica un destino concreto y no hay conversación previa que lo determine.
- **Capacidad a revisar:** Pedir aclaración del destino; no asumir entrance u otra ubicación.
- **Corpus:** Sin coincidencia normalizada detectada; pertenencia histórica a train no verificada. Grupo: `grupo_sin_coincidencias_detectadas_v02`.
- **Revisión:** aprobada por el investigador el 2026-10-21, sin correcciones de bloque.

### DEV-057 · INT-25 · A

**Inglés — entrada original:** Take a fork from the shelf and give it to her.

**Español — ayuda de lectura:** Toma un tenedor de la repisa y dáselo a ella.

- **Bloque propuesto:** Información necesaria ausente.
- **Variante original:** `limite_dominio`.
- **Familia/ruta:** `Destinataria ausente en entrega`.
- **Justificación:** her no tiene antecedente en esta orden independiente; fork y shelf no identifican a la destinataria.
- **Capacidad a revisar:** Pedir aclaración de la destinataria; no inventar persona.
- **Corpus:** Sin coincidencia normalizada detectada; pertenencia histórica a train no verificada. Grupo: `grupo_sin_coincidencias_detectadas_v02`.
- **Revisión:** aprobada por el investigador el 2026-10-21, sin correcciones de bloque.

### DEV-058 · INT-26 · F

**Inglés — entrada original:** Fly to the ceiling and inspect the lamp.

**Español — ayuda de lectura:** Vuela hasta el techo e inspecciona la lámpara.

- **Bloque propuesto:** Acciones fuera del repertorio actual.
- **Variante original:** `limite_dominio`.
- **Familia/ruta:** `Vuelo e inspección no disponibles`.
- **Justificación:** No hay objetivos canónicos para volar e inspeccionar la lámpara; volar es una acción solicitada, no un atributo de búsqueda.
- **Capacidad a revisar:** Reconocer limitación sin convertir silenciosamente la orden en navegación/búsqueda terrestre.
- **Corpus:** Sin coincidencia normalizada detectada; pertenencia histórica a train no verificada. Grupo: `grupo_sin_coincidencias_detectadas_v02`.
- **Revisión:** aprobada por el investigador el 2026-10-21, sin correcciones de bloque.

### DEV-059 · INT-27 · F

**Inglés — entrada original:** Set the thermostat to twenty degrees.

**Español — ayuda de lectura:** Ajusta el termostato a veinte grados.

- **Bloque propuesto:** Acciones fuera del repertorio actual.
- **Variante original:** `limite_dominio`.
- **Familia/ruta:** `Control de termostato no disponible`.
- **Justificación:** No hay objetivo canónico ni acción del repertorio evaluado para ajustar un termostato.
- **Capacidad a revisar:** Reconocer limitación; no generar una acción inexistente.
- **Corpus:** Sin coincidencia normalizada detectada; pertenencia histórica a train no verificada. Grupo: `grupo_sin_coincidencias_detectadas_v02`.
- **Revisión:** aprobada por el investigador el 2026-10-21, sin correcciones de bloque.

### DEV-060 · INT-28 · X

**Inglés — entrada original:** Pick up the apple on the shelf, but do not pick up the apple.

**Español — ayuda de lectura:** Recoge la manzana que está sobre la repisa, pero no recojas la manzana.

- **Bloque propuesto:** Instrucción contradictoria.
- **Variante original:** `limite_dominio`.
- **Familia/ruta:** `Tomar y no tomar el mismo objeto`.
- **Justificación:** La misma orden exige y prohíbe recoger la misma manzana; los referentes sí están especificados.
- **Capacidad a revisar:** Reconocer contradicción y solicitar resolución o rechazar justificadamente, según el criterio aprobado; no ejecutar solo una mitad.
- **Corpus:** Sin coincidencia normalizada detectada; pertenencia histórica a train no verificada. Grupo: `grupo_sin_coincidencias_detectadas_v02`.
- **Revisión:** aprobada por el investigador el 2026-10-21, sin correcciones de bloque.
