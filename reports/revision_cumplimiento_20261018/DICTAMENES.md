# Revisión de cumplimiento: propuestas para las 60 órdenes

Fecha: 18 de octubre de 2026. **180 propuestas del asistente, pendientes de revisión del investigador.**
No son dictámenes humanos aprobados ni sustituyen los registros de las campañas.
La revisión se apoya en las referencias aprobadas y en los planes, no en igualdad
con CLIPS ni únicamente en el formato. No se consultaron modelos ni se modificaron
prompts, reglas, datos de entrada, referencias o campañas.

## Criterios

- **Cumple (pass):** subtareas, argumentos y dependencias presentes en el plan simbólico. No demuestra ejecución física.
- **Incumple (fail):** omisión, sustitución o contradicción observable con una restricción, o falta de plan para una referencia aplicable. Un límite conocido explica el incumplimiento, sin convertirlo en éxito.
- **No verificable (not_verifiable):** el plan presenta el protocolo, pero falta precisar el efecto del ejecutor sobre identidad, memoria o seguimiento. No cuenta como fallo ni como acierto.
- **No aplicable (not_applicable):** DEV-055–060 no tienen tarea ejecutable de referencia. Se evalúa aparte si la aclaración/rechazo es adecuado en domain_response_correct.
- **semantic_correct:** fidelidad de los objetivos a la orden; null cuando no hay objetivos evaluables o el sistema rechaza. No inferir una interpretación semántica fallida del mero rechazo de GPT en DEV-049.
- Los fallos de JSON del modelo devueltos como HTTP 422 se distinguen de indisponibilidad de infraestructura. Cuando no hay objetivos parseables, semantic_correct queda null.
- Un incumplimiento observable tiene precedencia sobre otras partes no verificables. Las limitaciones coexistentes permanecen en las notas.

## Decisiones que requieren especial atención

1. **Identidad y memoria:** DEV-019–024, 028–030, 034–039 y 043–045 contienen protocolos de identificación o memoria, pero no acreditan sus efectos. Propuesta conservadora: no verificable, salvo errores observables como GPT/024 o 7B/029.
2. **Seguimiento:** DEV-025–027 y 052 no son éxitos por incluir instruct_follow. GPT/052 además omite esa instrucción: se propone incumple.
3. **DEV-049:** los tres sistemas no cumplen la tarea completa. GPT la rechaza explícitamente por capacidad; es una conducta prudente distinta de inventar un plan, pero no se modifica retrospectivamente la ficha executable. Su interpretación y adecuación del rechazo quedan sin puntuar aquí; registrar el motivo por separado.
4. **DEV-050:** objetivos correctos, expansión sin filtro rojo: incumplimiento de una restricción explícita.
5. **DEV-051:** objetivos correctos, plan de tamaño para peso: incumplimiento con etiqueta proxy_insuficiente, separado del bloque resoluble. No atribuirlo a interpretación ni exigir capacidad física que no existe.
6. **DEV-054:** los tres planes conservan el objeto y lo entregan. Propuesta: cumple simbólicamente, aunque difiera del control defectuoso.
7. **DEV-001–003:** conservar resultados y etiquetas originales. Su clasificación como composición fuera de la distribución es una nota posterior, no un motivo para borrar fallos de 7B.

## Cómo revisar

Leer cada ficha y marcar una decisión en el CSV o responder por ID/modelo.
Ejemplo: «Acepto las propuestas de DEV-001–018 para las tres condiciones» o
«GPT DEV-024: cambiar a ... porque ...». Todas las propuestas están pendientes;
la aprobación anterior de referencias no implica aprobación de estos dictámenes.
No importar dictamenes_propuestos.jsonl directamente al evaluador: contiene
propuestas anidadas, sin atribuir autoría ni aprobación al investigador.

Los conteos siguientes son provisionales; no publicar tasas finales a partir de
ellos. La tabla conserva todos los bloques y los cuatro estados separados.


| Condición | Cumple simbólico | Incumple | No verificable | No aplicable |
|---|---:|---:|---:|---:|
| Qwen3B | 28 | 4 | 22 | 6 |
| Qwen7B | 26 | 7 | 21 | 6 |
| GPT | 29 | 5 | 20 | 6 |

## Índice de propuestas

| Caso | Qwen3B | Qwen7B | GPT |
|---|---|---|---|
| [DEV-001](#dev-001) | Cumple simbólico | Incumple | Cumple simbólico |
| [DEV-002](#dev-002) | Cumple simbólico | Incumple | Cumple simbólico |
| [DEV-003](#dev-003) | Cumple simbólico | Incumple | Cumple simbólico |
| [DEV-004](#dev-004) | Cumple simbólico | Cumple simbólico | Cumple simbólico |
| [DEV-005](#dev-005) | Cumple simbólico | Cumple simbólico | Cumple simbólico |
| [DEV-006](#dev-006) | Cumple simbólico | Cumple simbólico | Cumple simbólico |
| [DEV-007](#dev-007) | Cumple simbólico | Cumple simbólico | Cumple simbólico |
| [DEV-008](#dev-008) | Cumple simbólico | Cumple simbólico | Cumple simbólico |
| [DEV-009](#dev-009) | Cumple simbólico | Cumple simbólico | Cumple simbólico |
| [DEV-010](#dev-010) | Cumple simbólico | Cumple simbólico | Cumple simbólico |
| [DEV-011](#dev-011) | Cumple simbólico | Cumple simbólico | Cumple simbólico |
| [DEV-012](#dev-012) | Cumple simbólico | Cumple simbólico | Cumple simbólico |
| [DEV-013](#dev-013) | Cumple simbólico | Cumple simbólico | Cumple simbólico |
| [DEV-014](#dev-014) | Cumple simbólico | Cumple simbólico | Cumple simbólico |
| [DEV-015](#dev-015) | Cumple simbólico | Cumple simbólico | Cumple simbólico |
| [DEV-016](#dev-016) | Cumple simbólico | Cumple simbólico | Cumple simbólico |
| [DEV-017](#dev-017) | Cumple simbólico | Cumple simbólico | Cumple simbólico |
| [DEV-018](#dev-018) | Cumple simbólico | Cumple simbólico | Cumple simbólico |
| [DEV-019](#dev-019) | No verificable | No verificable | No verificable |
| [DEV-020](#dev-020) | No verificable | No verificable | No verificable |
| [DEV-021](#dev-021) | No verificable | No verificable | No verificable |
| [DEV-022](#dev-022) | No verificable | No verificable | No verificable |
| [DEV-023](#dev-023) | No verificable | No verificable | No verificable |
| [DEV-024](#dev-024) | No verificable | No verificable | Incumple |
| [DEV-025](#dev-025) | No verificable | No verificable | No verificable |
| [DEV-026](#dev-026) | No verificable | No verificable | No verificable |
| [DEV-027](#dev-027) | No verificable | No verificable | No verificable |
| [DEV-028](#dev-028) | No verificable | No verificable | No verificable |
| [DEV-029](#dev-029) | No verificable | Incumple | No verificable |
| [DEV-030](#dev-030) | No verificable | No verificable | No verificable |
| [DEV-031](#dev-031) | Cumple simbólico | Cumple simbólico | Cumple simbólico |
| [DEV-032](#dev-032) | Cumple simbólico | Cumple simbólico | Cumple simbólico |
| [DEV-033](#dev-033) | Cumple simbólico | Cumple simbólico | Cumple simbólico |
| [DEV-034](#dev-034) | No verificable | No verificable | No verificable |
| [DEV-035](#dev-035) | No verificable | No verificable | No verificable |
| [DEV-036](#dev-036) | No verificable | No verificable | No verificable |
| [DEV-037](#dev-037) | No verificable | No verificable | No verificable |
| [DEV-038](#dev-038) | No verificable | No verificable | No verificable |
| [DEV-039](#dev-039) | No verificable | No verificable | No verificable |
| [DEV-040](#dev-040) | Cumple simbólico | Cumple simbólico | Cumple simbólico |
| [DEV-041](#dev-041) | Cumple simbólico | Cumple simbólico | Cumple simbólico |
| [DEV-042](#dev-042) | Cumple simbólico | Cumple simbólico | Cumple simbólico |
| [DEV-043](#dev-043) | No verificable | No verificable | No verificable |
| [DEV-044](#dev-044) | No verificable | No verificable | No verificable |
| [DEV-045](#dev-045) | No verificable | No verificable | No verificable |
| [DEV-046](#dev-046) | Cumple simbólico | Cumple simbólico | Cumple simbólico |
| [DEV-047](#dev-047) | Cumple simbólico | Cumple simbólico | Cumple simbólico |
| [DEV-048](#dev-048) | Cumple simbólico | Cumple simbólico | Cumple simbólico |
| [DEV-049](#dev-049) | Incumple | Incumple | Incumple |
| [DEV-050](#dev-050) | Incumple | Incumple | Incumple |
| [DEV-051](#dev-051) | Incumple | Incumple | Incumple |
| [DEV-052](#dev-052) | No verificable | No verificable | Incumple |
| [DEV-053](#dev-053) | Incumple | Cumple simbólico | Cumple simbólico |
| [DEV-054](#dev-054) | Cumple simbólico | Cumple simbólico | Cumple simbólico |
| [DEV-055](#dev-055) | No aplicable | No aplicable | No aplicable |
| [DEV-056](#dev-056) | No aplicable | No aplicable | No aplicable |
| [DEV-057](#dev-057) | No aplicable | No aplicable | No aplicable |
| [DEV-058](#dev-058) | No aplicable | No aplicable | No aplicable |
| [DEV-059](#dev-059) | No aplicable | No aplicable | No aplicable |
| [DEV-060](#dev-060) | No aplicable | No aplicable | No aplicable |

## DEV-001

**Orden:** Go to the corridor, then go to the inspection point.

**Intención:** INT-01. **Bloque:** funcional_y_linguistico.

**Subtareas:**

- Visitar corridor.
- Después visitar inspection point; distinguirlo de instruction_point.

**Restricciones:**

- La visita a corridor precede a la visita a inspection point.
- El retorno de cierre no sustituye ninguna de las visitas solicitadas.

**Límites de verificación de la ficha:**


### Qwen3B — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(corridor)",
  "go(inspection point)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to corridor
2: say I will navigate to inspection_point
1001: go_to corridor
1002: say I have arrived at corridor
1003: go_to inspection_point
1004: say I have arrived at inspection_point
1005: go_to instruction_point
1006: say task completed
```

run_id: `d44ae862-13d2-42e2-915a-4afeb7a9cfbc`

Decisión del investigador: **pendiente**. Observaciones: __________________

### Qwen7B — Incumple

Sustituye visitar inspection point por buscarlo como objeto.

Interpretación propuesta: `False`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(corridor)",
  "find(inspection point, kind=object)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to corridor
2: say I will search for inspection_point
1001: go_to corridor
1002: say I have arrived at corridor
1003: find_object inspection_point_1
1004: go_to instruction_point
1005: say task completed
```

run_id: `410cf9a7-45cc-4914-ae3b-ec0ad7c54857`

Decisión del investigador: **pendiente**. Observaciones: __________________

### GPT — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(corridor)",
  "go(inspection point)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to corridor
2: say I will navigate to inspection point
1001: go_to corridor
1002: say I have arrived at corridor
1003: go_to inspection_point
1004: say I have arrived at inspection point
1005: go_to instruction_point
1006: say task completed
```

run_id: `3f98299a-308b-468d-8471-9ed3e37b3486`

Decisión del investigador: **pendiente**. Observaciones: __________________

## DEV-002

**Orden:** Visit the corridor first and the inspection point afterwards.

**Intención:** INT-01. **Bloque:** funcional_y_linguistico.

**Subtareas:**

- Visitar corridor.
- Después visitar inspection point; distinguirlo de instruction_point.

**Restricciones:**

- La visita a corridor precede a la visita a inspection point.
- El retorno de cierre no sustituye ninguna de las visitas solicitadas.

**Límites de verificación de la ficha:**


### Qwen3B — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(corridor)",
  "go(inspection point)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to corridor
2: say I will navigate to inspection_point
1001: go_to corridor
1002: say I have arrived at corridor
1003: go_to inspection_point
1004: say I have arrived at inspection_point
1005: go_to instruction_point
1006: say task completed
```

run_id: `b2c5ab32-40f0-4c1b-8aae-1fc059b219df`

Decisión del investigador: **pendiente**. Observaciones: __________________

### Qwen7B — Incumple

No se obtuvo un plan. HTTP 422 conserva texto generado inválido; el servidor respondió, por lo que no se clasifica como caída de infraestructura.

Interpretación propuesta: `None`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
null
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
{"stage": "extraction", "type": "QwenHTTPError", "message": "Qwen devolvió HTTP 422; cuerpo conservado", "limit_ms": null}
```

run_id: `302d9047-e5e5-43df-9525-7af79f499299`

Decisión del investigador: **pendiente**. Observaciones: __________________

### GPT — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(corridor)",
  "go(inspection point)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to corridor
2: say I will navigate to inspection point
1001: go_to corridor
1002: say I have arrived at corridor
1003: go_to inspection_point
1004: say I have arrived at inspection point
1005: go_to instruction_point
1006: say task completed
```

run_id: `2f9d95fa-c3c0-4922-a07e-ccd42e95bfa7`

Decisión del investigador: **pendiente**. Observaciones: __________________

## DEV-003

**Orden:** please go go to the corridor then go to the inspection point

**Intención:** INT-01. **Bloque:** funcional_y_linguistico.

**Subtareas:**

- Visitar corridor.
- Después visitar inspection point; distinguirlo de instruction_point.

**Restricciones:**

- La visita a corridor precede a la visita a inspection point.
- El retorno de cierre no sustituye ninguna de las visitas solicitadas.

**Límites de verificación de la ficha:**


### Qwen3B — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(corridor)",
  "go(inspection point)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to corridor
2: say I will navigate to inspection_point
1001: go_to corridor
1002: say I have arrived at corridor
1003: go_to inspection_point
1004: say I have arrived at inspection_point
1005: go_to instruction_point
1006: say task completed
```

run_id: `913732aa-5aef-42f9-b55c-918f4fd3936d`

Decisión del investigador: **pendiente**. Observaciones: __________________

### Qwen7B — Incumple

Sustituye visitar inspection point por buscarlo como objeto.

Interpretación propuesta: `False`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(corridor)",
  "find(inspection point, kind=object)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to corridor
2: say I will search for inspection_point
1001: go_to corridor
1002: say I have arrived at corridor
1003: find_object inspection_point_1
1004: go_to instruction_point
1005: say task completed
```

run_id: `f78633d2-3bc0-4d67-9e6d-801ac63327cb`

Decisión del investigador: **pendiente**. Observaciones: __________________

### GPT — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(corridor)",
  "go(inspection point)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to corridor
2: say I will navigate to inspection point
1001: go_to corridor
1002: say I have arrived at corridor
1003: go_to inspection_point
1004: say I have arrived at inspection point
1005: go_to instruction_point
1006: say task completed
```

run_id: `c2afd8b6-da8f-4fa5-bd78-741e8d4a1e52`

Decisión del investigador: **pendiente**. Observaciones: __________________

## DEV-004

**Orden:** Find a peach in the bathroom.

**Intención:** INT-02. **Bloque:** funcional_y_linguistico.

**Subtareas:**

- Ir a bathroom.
- Buscar peach en bathroom.

**Restricciones:**

- No adquirir ni transportar el objeto: solo se solicita localizarlo.

**Límites de verificación de la ficha:**


### Qwen3B — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(bathroom)",
  "find(peach, kind=object)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to bathroom
2: say I will search for peach
1001: go_to bathroom
1002: say I have arrived at bathroom
1003: find_object peach_1
1004: go_to instruction_point
1005: say task completed
```

run_id: `5c6dc294-9dc0-4d08-af21-abf9455b9cd6`

Decisión del investigador: **pendiente**. Observaciones: __________________

### Qwen7B — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(bathroom)",
  "find(peach, kind=object)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to bathroom
2: say I will search for peach
1001: go_to bathroom
1002: say I have arrived at bathroom
1003: find_object peach_1
1004: go_to instruction_point
1005: say task completed
```

run_id: `a7c020c7-96ab-4df1-b0ad-12ce21702610`

Decisión del investigador: **pendiente**. Observaciones: __________________

### GPT — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(bathroom)",
  "find(peach, kind=object)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to bathroom
2: say I will search for peach
1001: go_to bathroom
1002: say I have arrived at bathroom
1003: find_object peach_1
1004: go_to instruction_point
1005: say task completed
```

run_id: `c29690f4-23f5-4c33-8554-9d2dd962782b`

Decisión del investigador: **pendiente**. Observaciones: __________________

## DEV-005

**Orden:** Look for a peach inside the bathroom.

**Intención:** INT-02. **Bloque:** funcional_y_linguistico.

**Subtareas:**

- Ir a bathroom.
- Buscar peach en bathroom.

**Restricciones:**

- No adquirir ni transportar el objeto: solo se solicita localizarlo.

**Límites de verificación de la ficha:**


### Qwen3B — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(bathroom)",
  "find(peach, kind=object)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to bathroom
2: say I will search for peach
1001: go_to bathroom
1002: say I have arrived at bathroom
1003: find_object peach_1
1004: go_to instruction_point
1005: say task completed
```

run_id: `11c76e2b-f743-482e-b647-9191c4ef7a26`

Decisión del investigador: **pendiente**. Observaciones: __________________

### Qwen7B — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(bathroom)",
  "find(peach, kind=object)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to bathroom
2: say I will search for peach
1001: go_to bathroom
1002: say I have arrived at bathroom
1003: find_object peach_1
1004: go_to instruction_point
1005: say task completed
```

run_id: `9d071a53-753a-4541-835e-4cb74279cd3f`

Decisión del investigador: **pendiente**. Observaciones: __________________

### GPT — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(bathroom)",
  "find(peach, kind=object)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to bathroom
2: say I will search for peach
1001: go_to bathroom
1002: say I have arrived at bathroom
1003: find_object peach_1
1004: go_to instruction_point
1005: say task completed
```

run_id: `eb6fae6c-646d-419b-828c-46f31c2eb6f8`

Decisión del investigador: **pendiente**. Observaciones: __________________

## DEV-006

**Orden:** please find a peach in the bathrom

**Intención:** INT-02. **Bloque:** funcional_y_linguistico.

**Subtareas:**

- Ir a bathroom.
- Buscar peach en bathroom.

**Restricciones:**

- No adquirir ni transportar el objeto: solo se solicita localizarlo.

**Límites de verificación de la ficha:**


### Qwen3B — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(bathroom)",
  "find(peach, kind=object)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to bathroom
2: say I will search for peach
1001: go_to bathroom
1002: say I have arrived at bathroom
1003: find_object peach_1
1004: go_to instruction_point
1005: say task completed
```

run_id: `e384c246-7696-47b4-9398-7a509369c13f`

Decisión del investigador: **pendiente**. Observaciones: __________________

### Qwen7B — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(bathroom)",
  "find(peach, kind=object)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to bathroom
2: say I will search for peach
1001: go_to bathroom
1002: say I have arrived at bathroom
1003: find_object peach_1
1004: go_to instruction_point
1005: say task completed
```

run_id: `4a466f42-a698-4535-ad7a-8e91c1bd9efd`

Decisión del investigador: **pendiente**. Observaciones: __________________

### GPT — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(bathroom)",
  "find(peach, kind=object)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to bathroom
2: say I will search for peach
1001: go_to bathroom
1002: say I have arrived at bathroom
1003: find_object peach_1
1004: go_to instruction_point
1005: say task completed
```

run_id: `eca1fc19-1898-4df1-9771-628a096f221c`

Decisión del investigador: **pendiente**. Observaciones: __________________

## DEV-007

**Orden:** Find a spoon at the bed and take it.

**Intención:** INT-03. **Bloque:** funcional_y_linguistico.

**Subtareas:**

- Ir a bed.
- Localizar spoon.
- Adquirir ese mismo spoon.

**Restricciones:**

- La búsqueda precede a la adquisición; it refiere a spoon.

**Límites de verificación de la ficha:**


### Qwen3B — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(bed)",
  "find(spoon, kind=object)",
  "take(spoon)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to bed
2: say I will search for spoon
3: say I will pick up spoon
1001: go_to bed
1002: say I have arrived at bed
1003: find_object spoon_1
1004: take spoon_1
1005: say I have picked up spoon
1006: go_to instruction_point
1007: say task completed
```

run_id: `cb08fdf6-e77c-4730-9133-99a24b04e3a4`

Decisión del investigador: **pendiente**. Observaciones: __________________

### Qwen7B — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(bed)",
  "find(spoon, kind=object)",
  "take(spoon)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to bed
2: say I will search for spoon
3: say I will pick up spoon
1001: go_to bed
1002: say I have arrived at bed
1003: find_object spoon_1
1004: take spoon_1
1005: say I have picked up spoon
1006: go_to instruction_point
1007: say task completed
```

run_id: `44a3626a-dac6-4bc5-bd64-766b6f12d0b7`

Decisión del investigador: **pendiente**. Observaciones: __________________

### GPT — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(bed)",
  "find(spoon, kind=object)",
  "take(spoon)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to bed
2: say I will search for spoon
3: say I will pick up spoon
1001: go_to bed
1002: say I have arrived at bed
1003: find_object spoon_1
1004: take spoon_1
1005: say I have picked up spoon
1006: go_to instruction_point
1007: say task completed
```

run_id: `90336056-8572-46bd-89f1-119642beef5e`

Decisión del investigador: **pendiente**. Observaciones: __________________

## DEV-008

**Orden:** Pick up the spoon you find at the bed.

**Intención:** INT-03. **Bloque:** funcional_y_linguistico.

**Subtareas:**

- Ir a bed.
- Localizar spoon.
- Adquirir ese mismo spoon.

**Restricciones:**

- La búsqueda precede a la adquisición; it refiere a spoon.

**Límites de verificación de la ficha:**


### Qwen3B — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(bed)",
  "find(spoon, kind=object)",
  "take(spoon)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to bed
2: say I will search for spoon
3: say I will pick up spoon
1001: go_to bed
1002: say I have arrived at bed
1003: find_object spoon_1
1004: take spoon_1
1005: say I have picked up spoon
1006: go_to instruction_point
1007: say task completed
```

run_id: `3289892f-12df-4ca5-bc74-bb2a2c9dc3be`

Decisión del investigador: **pendiente**. Observaciones: __________________

### Qwen7B — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(bed)",
  "find(spoon, kind=object)",
  "take(spoon)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to bed
2: say I will search for spoon
3: say I will pick up spoon
1001: go_to bed
1002: say I have arrived at bed
1003: find_object spoon_1
1004: take spoon_1
1005: say I have picked up spoon
1006: go_to instruction_point
1007: say task completed
```

run_id: `ff7d665c-0267-4575-900f-e12ed24238ff`

Decisión del investigador: **pendiente**. Observaciones: __________________

### GPT — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(bed)",
  "find(spoon, kind=object)",
  "take(spoon)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to bed
2: say I will search for spoon
3: say I will pick up spoon
1001: go_to bed
1002: say I have arrived at bed
1003: find_object spoon_1
1004: take spoon_1
1005: say I have picked up spoon
1006: go_to instruction_point
1007: say task completed
```

run_id: `624a691f-a4d3-4c45-8f11-a3f9026a930b`

Decisión del investigador: **pendiente**. Observaciones: __________________

## DEV-009

**Orden:** please find a spoon at the bed and and take it

**Intención:** INT-03. **Bloque:** funcional_y_linguistico.

**Subtareas:**

- Ir a bed.
- Localizar spoon.
- Adquirir ese mismo spoon.

**Restricciones:**

- La búsqueda precede a la adquisición; it refiere a spoon.

**Límites de verificación de la ficha:**


### Qwen3B — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(bed)",
  "find(spoon, kind=object)",
  "take(spoon)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to bed
2: say I will search for spoon
3: say I will pick up spoon
1001: go_to bed
1002: say I have arrived at bed
1003: find_object spoon_1
1004: take spoon_1
1005: say I have picked up spoon
1006: go_to instruction_point
1007: say task completed
```

run_id: `99003758-08de-4321-9708-83dac3004d05`

Decisión del investigador: **pendiente**. Observaciones: __________________

### Qwen7B — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(bed)",
  "find(spoon, kind=object)",
  "take(spoon)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to bed
2: say I will search for spoon
3: say I will pick up spoon
1001: go_to bed
1002: say I have arrived at bed
1003: find_object spoon_1
1004: take spoon_1
1005: say I have picked up spoon
1006: go_to instruction_point
1007: say task completed
```

run_id: `71d4df12-6ebe-443a-9f8f-f88d756ba025`

Decisión del investigador: **pendiente**. Observaciones: __________________

### GPT — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(bed)",
  "find(spoon, kind=object)",
  "take(spoon)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to bed
2: say I will search for spoon
3: say I will pick up spoon
1001: go_to bed
1002: say I have arrived at bed
1003: find_object spoon_1
1004: take spoon_1
1005: say I have picked up spoon
1006: go_to instruction_point
1007: say task completed
```

run_id: `d39bc672-9a9b-44fe-8ac2-3e1f011b0b0c`

Decisión del investigador: **pendiente**. Observaciones: __________________

## DEV-010

**Orden:** Bring me a mug from the cabinet.

**Intención:** INT-04. **Bloque:** funcional_y_linguistico.

**Subtareas:**

- Buscar y adquirir mug en cabinet.
- Regresar al punto del operador y entregarle mug.

**Restricciones:**

- No confundir el origen cabinet con el destinatario.
- La entrega requiere adquisición previa y una acción de entrega, no solo un anuncio.

**Límites de verificación de la ficha:**


### Qwen3B — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(cabinet)",
  "find(mug, kind=object)",
  "take(mug)",
  "deliver(mug, to=me)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to cabinet
2: say I will search for mug
3: say I will pick up mug
4: say I will return to the instruction point
5: say I will deliver mug to you
1001: go_to cabinet
1002: say I have arrived at cabinet
1003: find_object mug_1
1004: take mug_1
1005: say I have picked up mug
1006: go_to instruction_point
1007: approach host_1
1008: give mug_1
1009: say I have delivered mug
1010: say task completed
```

run_id: `e120bd41-bb84-40e0-8457-44dc8f1720b9`

Decisión del investigador: **pendiente**. Observaciones: __________________

### Qwen7B — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(cabinet)",
  "find(mug, kind=object)",
  "take(mug)",
  "deliver(mug, to=me)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to cabinet
2: say I will search for mug
3: say I will pick up mug
4: say I will return to the instruction point
5: say I will deliver mug to you
1001: go_to cabinet
1002: say I have arrived at cabinet
1003: find_object mug_1
1004: take mug_1
1005: say I have picked up mug
1006: go_to instruction_point
1007: approach host_1
1008: give mug_1
1009: say I have delivered mug
1010: say task completed
```

run_id: `1e7219f0-135e-4f1e-bf36-c7b12cdef8b8`

Decisión del investigador: **pendiente**. Observaciones: __________________

### GPT — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(cabinet)",
  "find(mug, kind=object)",
  "take(mug)",
  "deliver(mug, to=me)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to cabinet
2: say I will search for mug
3: say I will pick up mug
4: say I will return to the instruction point
5: say I will deliver mug to you
1001: go_to cabinet
1002: say I have arrived at cabinet
1003: find_object mug_1
1004: take mug_1
1005: say I have picked up mug
1006: go_to instruction_point
1007: approach host_1
1008: give mug_1
1009: say I have delivered mug
1010: say task completed
```

run_id: `5226af9e-ad4d-4a49-984d-0453fc5ed96c`

Decisión del investigador: **pendiente**. Observaciones: __________________

## DEV-011

**Orden:** Fetch a mug at the cabinet and deliver it to me.

**Intención:** INT-04. **Bloque:** funcional_y_linguistico.

**Subtareas:**

- Buscar y adquirir mug en cabinet.
- Regresar al punto del operador y entregarle mug.

**Restricciones:**

- No confundir el origen cabinet con el destinatario.
- La entrega requiere adquisición previa y una acción de entrega, no solo un anuncio.

**Límites de verificación de la ficha:**


### Qwen3B — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(cabinet)",
  "find(mug, kind=object)",
  "take(mug)",
  "deliver(mug, to=me)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to cabinet
2: say I will search for mug
3: say I will pick up mug
4: say I will return to the instruction point
5: say I will deliver mug to you
1001: go_to cabinet
1002: say I have arrived at cabinet
1003: find_object mug_1
1004: take mug_1
1005: say I have picked up mug
1006: go_to instruction_point
1007: approach host_1
1008: give mug_1
1009: say I have delivered mug
1010: say task completed
```

run_id: `1f644be8-fcb0-4749-8b58-02c9932b9aec`

Decisión del investigador: **pendiente**. Observaciones: __________________

### Qwen7B — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(cabinet)",
  "find(mug, kind=object)",
  "take(mug)",
  "deliver(mug, to=me)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to cabinet
2: say I will search for mug
3: say I will pick up mug
4: say I will return to the instruction point
5: say I will deliver mug to you
1001: go_to cabinet
1002: say I have arrived at cabinet
1003: find_object mug_1
1004: take mug_1
1005: say I have picked up mug
1006: go_to instruction_point
1007: approach host_1
1008: give mug_1
1009: say I have delivered mug
1010: say task completed
```

run_id: `64ab4fae-b5d5-4db5-b24c-746fbd382ee9`

Decisión del investigador: **pendiente**. Observaciones: __________________

### GPT — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(cabinet)",
  "find(mug, kind=object)",
  "take(mug)",
  "deliver(mug, to=me)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to cabinet
2: say I will search for mug
3: say I will pick up mug
4: say I will return to the instruction point
5: say I will deliver mug to you
1001: go_to cabinet
1002: say I have arrived at cabinet
1003: find_object mug_1
1004: take mug_1
1005: say I have picked up mug
1006: go_to instruction_point
1007: approach host_1
1008: give mug_1
1009: say I have delivered mug
1010: say task completed
```

run_id: `f2239204-1423-4d64-8e2f-1b89212a68e3`

Decisión del investigador: **pendiente**. Observaciones: __________________

## DEV-012

**Orden:** please bring me a mug from the cabnet

**Intención:** INT-04. **Bloque:** funcional_y_linguistico.

**Subtareas:**

- Buscar y adquirir mug en cabinet.
- Regresar al punto del operador y entregarle mug.

**Restricciones:**

- No confundir el origen cabinet con el destinatario.
- La entrega requiere adquisición previa y una acción de entrega, no solo un anuncio.

**Límites de verificación de la ficha:**


### Qwen3B — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(cabinet)",
  "find(mug, kind=object)",
  "take(mug)",
  "deliver(mug, to=me)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to cabinet
2: say I will search for mug
3: say I will pick up mug
4: say I will return to the instruction point
5: say I will deliver mug to you
1001: go_to cabinet
1002: say I have arrived at cabinet
1003: find_object mug_1
1004: take mug_1
1005: say I have picked up mug
1006: go_to instruction_point
1007: approach host_1
1008: give mug_1
1009: say I have delivered mug
1010: say task completed
```

run_id: `c21747a0-1ff8-4db4-8057-51b22aed3ccd`

Decisión del investigador: **pendiente**. Observaciones: __________________

### Qwen7B — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(cabinet)",
  "find(mug, kind=object)",
  "take(mug)",
  "deliver(mug, to=me)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to cabinet
2: say I will search for mug
3: say I will pick up mug
4: say I will return to the instruction point
5: say I will deliver mug to you
1001: go_to cabinet
1002: say I have arrived at cabinet
1003: find_object mug_1
1004: take mug_1
1005: say I have picked up mug
1006: go_to instruction_point
1007: approach host_1
1008: give mug_1
1009: say I have delivered mug
1010: say task completed
```

run_id: `33557b4d-179d-4ed5-8f75-4e553d4763cb`

Decisión del investigador: **pendiente**. Observaciones: __________________

### GPT — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(cabinet)",
  "find(mug, kind=object)",
  "take(mug)",
  "deliver(mug, to=me)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to cabinet
2: say I will search for mug
3: say I will pick up mug
4: say I will return to the instruction point
5: say I will deliver mug to you
1001: go_to cabinet
1002: say I have arrived at cabinet
1003: find_object mug_1
1004: take mug_1
1005: say I have picked up mug
1006: go_to instruction_point
1007: approach host_1
1008: give mug_1
1009: say I have delivered mug
1010: say task completed
```

run_id: `0dfb81ab-8df6-45a6-8754-8cb6bc9f182c`

Decisión del investigador: **pendiente**. Observaciones: __________________

## DEV-013

**Orden:** Bring a bowl from the bed to the storage rack.

**Intención:** INT-05. **Bloque:** funcional_y_linguistico.

**Subtareas:**

- Buscar y adquirir bowl en bed.
- Trasladarlo a storage rack y colocarlo allí.

**Restricciones:**

- bed es el origen y storage rack es el destino; no invertirlos.
- Llegar al destino antes de colocar el objeto.

**Límites de verificación de la ficha:**


### Qwen3B — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(bed)",
  "find(bowl, kind=object)",
  "take(bowl)",
  "place(bowl, at=storage rack)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to bed
2: say I will search for bowl
3: say I will pick up bowl
4: say I will navigate to storage_rack
5: say I will place bowl at storage_rack
1001: go_to bed
1002: say I have arrived at bed
1003: find_object bowl_1
1004: take bowl_1
1005: say I have picked up bowl
1006: go_to storage_rack
1007: find_space shelf
1008: drop bowl_1
1009: say I have placed bowl
1010: go_to instruction_point
1011: say task completed
```

run_id: `8b50acef-401f-4ba9-9129-6ed687268b57`

Decisión del investigador: **pendiente**. Observaciones: __________________

### Qwen7B — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(bed)",
  "find(bowl, kind=object)",
  "take(bowl)",
  "place(bowl, at=storage rack)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to bed
2: say I will search for bowl
3: say I will pick up bowl
4: say I will navigate to storage_rack
5: say I will place bowl at storage_rack
1001: go_to bed
1002: say I have arrived at bed
1003: find_object bowl_1
1004: take bowl_1
1005: say I have picked up bowl
1006: go_to storage_rack
1007: find_space shelf
1008: drop bowl_1
1009: say I have placed bowl
1010: go_to instruction_point
1011: say task completed
```

run_id: `d22f4c30-fb52-41a7-bafd-c1536090ce0d`

Decisión del investigador: **pendiente**. Observaciones: __________________

### GPT — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(bed)",
  "find(bowl, kind=object)",
  "take(bowl)",
  "place(bowl, at=storage rack)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to bed
2: say I will search for bowl
3: say I will pick up bowl
4: say I will navigate to storage rack
5: say I will place bowl at storage rack
1001: go_to bed
1002: say I have arrived at bed
1003: find_object bowl_1
1004: take bowl_1
1005: say I have picked up bowl
1006: go_to storage_rack
1007: find_space shelf
1008: drop bowl_1
1009: say I have placed bowl
1010: go_to instruction_point
1011: say task completed
```

run_id: `69f72f3d-4d30-4e80-a978-ed1b83e01e41`

Decisión del investigador: **pendiente**. Observaciones: __________________

## DEV-014

**Orden:** Collect a bowl at the bed and leave it at the storage rack.

**Intención:** INT-05. **Bloque:** funcional_y_linguistico.

**Subtareas:**

- Buscar y adquirir bowl en bed.
- Trasladarlo a storage rack y colocarlo allí.

**Restricciones:**

- bed es el origen y storage rack es el destino; no invertirlos.
- Llegar al destino antes de colocar el objeto.

**Límites de verificación de la ficha:**


### Qwen3B — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(bed)",
  "find(bowl, kind=object)",
  "take(bowl)",
  "place(bowl, at=storage rack)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to bed
2: say I will search for bowl
3: say I will pick up bowl
4: say I will navigate to storage_rack
5: say I will place bowl at storage_rack
1001: go_to bed
1002: say I have arrived at bed
1003: find_object bowl_1
1004: take bowl_1
1005: say I have picked up bowl
1006: go_to storage_rack
1007: find_space shelf
1008: drop bowl_1
1009: say I have placed bowl
1010: go_to instruction_point
1011: say task completed
```

run_id: `638a26d0-1c7f-4c44-a978-0805802b9b10`

Decisión del investigador: **pendiente**. Observaciones: __________________

### Qwen7B — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(bed)",
  "find(bowl, kind=object)",
  "take(bowl)",
  "place(bowl, at=storage rack)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to bed
2: say I will search for bowl
3: say I will pick up bowl
4: say I will navigate to storage_rack
5: say I will place bowl at storage_rack
1001: go_to bed
1002: say I have arrived at bed
1003: find_object bowl_1
1004: take bowl_1
1005: say I have picked up bowl
1006: go_to storage_rack
1007: find_space shelf
1008: drop bowl_1
1009: say I have placed bowl
1010: go_to instruction_point
1011: say task completed
```

run_id: `8acfeb1e-e12a-4448-831b-86a3d2937431`

Decisión del investigador: **pendiente**. Observaciones: __________________

### GPT — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(bed)",
  "find(bowl, kind=object)",
  "take(bowl)",
  "place(bowl, at=storage rack)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to bed
2: say I will search for bowl
3: say I will pick up bowl
4: say I will navigate to storage_rack
5: say I will place bowl at storage_rack
1001: go_to bed
1002: say I have arrived at bed
1003: find_object bowl_1
1004: take bowl_1
1005: say I have picked up bowl
1006: go_to storage_rack
1007: find_space shelf
1008: drop bowl_1
1009: say I have placed bowl
1010: go_to instruction_point
1011: say task completed
```

run_id: `39f03f44-615e-4604-8387-7cb695400f0a`

Decisión del investigador: **pendiente**. Observaciones: __________________

## DEV-015

**Orden:** please bring a bowl from the bed to the storage  rack

**Intención:** INT-05. **Bloque:** funcional_y_linguistico.

**Subtareas:**

- Buscar y adquirir bowl en bed.
- Trasladarlo a storage rack y colocarlo allí.

**Restricciones:**

- bed es el origen y storage rack es el destino; no invertirlos.
- Llegar al destino antes de colocar el objeto.

**Límites de verificación de la ficha:**


### Qwen3B — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(bed)",
  "find(bowl, kind=object)",
  "take(bowl)",
  "place(bowl, at=storage rack)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to bed
2: say I will search for bowl
3: say I will pick up bowl
4: say I will navigate to storage_rack
5: say I will place bowl at storage_rack
1001: go_to bed
1002: say I have arrived at bed
1003: find_object bowl_1
1004: take bowl_1
1005: say I have picked up bowl
1006: go_to storage_rack
1007: find_space shelf
1008: drop bowl_1
1009: say I have placed bowl
1010: go_to instruction_point
1011: say task completed
```

run_id: `77e6de41-e04a-48ec-8f3c-2d6a8ba2537f`

Decisión del investigador: **pendiente**. Observaciones: __________________

### Qwen7B — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(bed)",
  "find(bowl, kind=object)",
  "take(bowl)",
  "place(bowl, at=storage rack)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to bed
2: say I will search for bowl
3: say I will pick up bowl
4: say I will navigate to storage_rack
5: say I will place bowl at storage_rack
1001: go_to bed
1002: say I have arrived at bed
1003: find_object bowl_1
1004: take bowl_1
1005: say I have picked up bowl
1006: go_to storage_rack
1007: find_space shelf
1008: drop bowl_1
1009: say I have placed bowl
1010: go_to instruction_point
1011: say task completed
```

run_id: `ce7a49aa-7fa1-4088-a7e7-210dec8e462a`

Decisión del investigador: **pendiente**. Observaciones: __________________

### GPT — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(bed)",
  "find(bowl, kind=object)",
  "take(bowl)",
  "place(bowl, at=storage rack)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to bed
2: say I will search for bowl
3: say I will pick up bowl
4: say I will navigate to storage rack
5: say I will place bowl on storage rack
1001: go_to bed
1002: say I have arrived at bed
1003: find_object bowl_1
1004: take bowl_1
1005: say I have picked up bowl
1006: go_to storage_rack
1007: find_space shelf
1008: drop bowl_1
1009: say I have placed bowl
1010: go_to instruction_point
1011: say task completed
```

run_id: `88f174f5-d2d2-479c-95de-8c3fa446e394`

Decisión del investigador: **pendiente**. Observaciones: __________________

## DEV-016

**Orden:** In the kitchen, find a cup, take it, and put it on the table.

**Intención:** INT-06. **Bloque:** funcional_y_linguistico.

**Subtareas:**

- Buscar y adquirir cup en kitchen.
- Colocar cup sobre la mesa local de kitchen.

**Restricciones:**

- table es un soporte local, no una habitación ni un punto de navegación adicional.
- No confundir colocación con entrega a una persona.

**Límites de verificación de la ficha:**

- La regla place puede asignar el soporte a location; revisar la representación del estado sin inferir desplazamiento físico.

### Qwen3B — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(kitchen)",
  "find(cup, kind=object)",
  "take(cup)",
  "place(cup, on=table)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to kitchen
2: say I will search for cup
3: say I will pick up cup
4: say I will place cup on table
1001: go_to kitchen
1002: say I have arrived at kitchen
1003: find_object cup_1
1004: take cup_1
1005: say I have picked up cup
1006: find_space table
1007: drop cup_1
1008: say I have placed cup
1009: go_to instruction_point
1010: say task completed
```

run_id: `40273b70-550f-45aa-b382-f974e0575416`

Decisión del investigador: **pendiente**. Observaciones: __________________

### Qwen7B — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(kitchen)",
  "find(cup, kind=object)",
  "take(cup)",
  "place(cup, on=table)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to kitchen
2: say I will search for cup
3: say I will pick up cup
4: say I will place cup on table
1001: go_to kitchen
1002: say I have arrived at kitchen
1003: find_object cup_1
1004: take cup_1
1005: say I have picked up cup
1006: find_space table
1007: drop cup_1
1008: say I have placed cup
1009: go_to instruction_point
1010: say task completed
```

run_id: `9d4c7ff6-9949-4e0e-88a1-f2c102579701`

Decisión del investigador: **pendiente**. Observaciones: __________________

### GPT — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(kitchen)",
  "find(cup, kind=object)",
  "take(cup)",
  "place(cup, on=table)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to kitchen
2: say I will search for cup
3: say I will pick up cup
4: say I will place cup on table
1001: go_to kitchen
1002: say I have arrived at kitchen
1003: find_object cup_1
1004: take cup_1
1005: say I have picked up cup
1006: find_space table
1007: drop cup_1
1008: say I have placed cup
1009: go_to instruction_point
1010: say task completed
```

run_id: `9f5be139-a571-40b8-be2f-2107d0542afb`

Decisión del investigador: **pendiente**. Observaciones: __________________

## DEV-017

**Orden:** Locate a cup in the kitchen and pick it up, then place it on the table there.

**Intención:** INT-06. **Bloque:** funcional_y_linguistico.

**Subtareas:**

- Buscar y adquirir cup en kitchen.
- Colocar cup sobre la mesa local de kitchen.

**Restricciones:**

- table es un soporte local, no una habitación ni un punto de navegación adicional.
- No confundir colocación con entrega a una persona.

**Límites de verificación de la ficha:**

- La regla place puede asignar el soporte a location; revisar la representación del estado sin inferir desplazamiento físico.

### Qwen3B — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(kitchen)",
  "find(cup, kind=object)",
  "take(cup)",
  "place(cup, on=table)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to kitchen
2: say I will search for cup
3: say I will pick up cup
4: say I will place cup on table
1001: go_to kitchen
1002: say I have arrived at kitchen
1003: find_object cup_1
1004: take cup_1
1005: say I have picked up cup
1006: find_space table
1007: drop cup_1
1008: say I have placed cup
1009: go_to instruction_point
1010: say task completed
```

run_id: `2f806c91-bcb0-48d5-b823-f726fa3fe70d`

Decisión del investigador: **pendiente**. Observaciones: __________________

### Qwen7B — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(kitchen)",
  "find(cup, kind=object)",
  "take(cup)",
  "place(cup, on=table)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to kitchen
2: say I will search for cup
3: say I will pick up cup
4: say I will place cup on table
1001: go_to kitchen
1002: say I have arrived at kitchen
1003: find_object cup_1
1004: take cup_1
1005: say I have picked up cup
1006: find_space table
1007: drop cup_1
1008: say I have placed cup
1009: go_to instruction_point
1010: say task completed
```

run_id: `de79cd1c-618a-4da8-8926-43f6cbb1f495`

Decisión del investigador: **pendiente**. Observaciones: __________________

### GPT — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(kitchen)",
  "find(cup, kind=object)",
  "take(cup)",
  "place(cup, on=table)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to kitchen
2: say I will search for cup
3: say I will pick up cup
4: say I will place cup on table
1001: go_to kitchen
1002: say I have arrived at kitchen
1003: find_object cup_1
1004: take cup_1
1005: say I have picked up cup
1006: find_space table
1007: drop cup_1
1008: say I have placed cup
1009: go_to instruction_point
1010: say task completed
```

run_id: `2b8e3388-a99e-44fb-bb0b-03dabb728549`

Decisión del investigador: **pendiente**. Observaciones: __________________

## DEV-018

**Orden:** in the kichen find a cup take it and put it on the table please

**Intención:** INT-06. **Bloque:** funcional_y_linguistico.

**Subtareas:**

- Buscar y adquirir cup en kitchen.
- Colocar cup sobre la mesa local de kitchen.

**Restricciones:**

- table es un soporte local, no una habitación ni un punto de navegación adicional.
- No confundir colocación con entrega a una persona.

**Límites de verificación de la ficha:**

- La regla place puede asignar el soporte a location; revisar la representación del estado sin inferir desplazamiento físico.

### Qwen3B — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(kitchen)",
  "find(cup, kind=object)",
  "take(cup)",
  "place(cup, on=table)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to kitchen
2: say I will search for cup
3: say I will pick up cup
4: say I will place cup on table
1001: go_to kitchen
1002: say I have arrived at kitchen
1003: find_object cup_1
1004: take cup_1
1005: say I have picked up cup
1006: find_space table
1007: drop cup_1
1008: say I have placed cup
1009: go_to instruction_point
1010: say task completed
```

run_id: `f5acd885-0f60-4d03-af67-7dca32d5a54b`

Decisión del investigador: **pendiente**. Observaciones: __________________

### Qwen7B — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(kitchen)",
  "find(cup, kind=object)",
  "take(cup)",
  "place(cup, on=table)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to kitchen
2: say I will search for cup
3: say I will pick up cup
4: say I will place cup on table
1001: go_to kitchen
1002: say I have arrived at kitchen
1003: find_object cup_1
1004: take cup_1
1005: say I have picked up cup
1006: find_space table
1007: drop cup_1
1008: say I have placed cup
1009: go_to instruction_point
1010: say task completed
```

run_id: `ec7c5e2d-8035-43ad-b5a2-e4b6e6942ff2`

Decisión del investigador: **pendiente**. Observaciones: __________________

### GPT — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(kitchen)",
  "find(cup, kind=object)",
  "take(cup)",
  "place(cup, on=table)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to kitchen
2: say I will search for cup
3: say I will pick up cup
4: say I will place cup on table
1001: go_to kitchen
1002: say I have arrived at kitchen
1003: find_object cup_1
1004: take cup_1
1005: say I have picked up cup
1006: find_space table
1007: drop cup_1
1008: say I have placed cup
1009: go_to instruction_point
1010: say task completed
```

run_id: `45377023-e3b7-4d22-ac94-b1566b72e22c`

Decisión del investigador: **pendiente**. Observaciones: __________________

## DEV-019

**Orden:** Find Robin in the office.

**Intención:** INT-07. **Bloque:** funcional_y_linguistico.

**Subtareas:**

- Ir a office y localizar a la persona llamada Robin.

**Restricciones:**

- No tratar Robin como objeto o ubicación.
- Buscar a anybody sin un mecanismo de identificación no acredita encontrar a Robin.

**Límites de verificación de la ficha:**

- Separar conformidad con el protocolo ask_name/listen de la verificación efectiva del nombre: la coincidencia de identidad requiere revisión del contrato del ejecutor.

### Qwen3B — No verificable

El plan pregunta y escucha el nombre, pero no contiene evidencia de comparación con Robin. Falta precisar el contrato de identificación.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(office)",
  "find(Robin, kind=person)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to office
2: say I will look for Robin
1001: go_to office
1002: say I have arrived at office
1003: find_person anybody
1004: focus enable
1005: say ask_name
1006: listen guest_name_last
1007: say acknowledge_name_last
1008: focus disable
1009: go_to instruction_point
1010: say task completed
```

run_id: `5652ac01-558d-4aba-8c31-849ce26acfa4`

Decisión del investigador: **pendiente**. Observaciones: __________________

### Qwen7B — No verificable

El plan pregunta y escucha el nombre, pero no contiene evidencia de comparación con Robin. Falta precisar el contrato de identificación.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(office)",
  "find(Robin, kind=person)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to office
2: say I will look for Robin
1001: go_to office
1002: say I have arrived at office
1003: find_person anybody
1004: focus enable
1005: say ask_name
1006: listen guest_name_last
1007: say acknowledge_name_last
1008: focus disable
1009: go_to instruction_point
1010: say task completed
```

run_id: `321beedc-c1a0-4904-8b16-c63f47c18fdc`

Decisión del investigador: **pendiente**. Observaciones: __________________

### GPT — No verificable

El plan pregunta y escucha el nombre, pero no contiene evidencia de comparación con Robin. Falta precisar el contrato de identificación.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(office)",
  "find(Robin, kind=person)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to office
2: say I will look for Robin
1001: go_to office
1002: say I have arrived at office
1003: find_person anybody
1004: focus enable
1005: say ask_name
1006: listen guest_name_last
1007: say acknowledge_name_last
1008: focus disable
1009: go_to instruction_point
1010: say task completed
```

run_id: `bad66a7e-074e-4039-875d-cd69cc316977`

Decisión del investigador: **pendiente**. Observaciones: __________________

## DEV-020

**Orden:** Look for Robin inside the office.

**Intención:** INT-07. **Bloque:** funcional_y_linguistico.

**Subtareas:**

- Ir a office y localizar a la persona llamada Robin.

**Restricciones:**

- No tratar Robin como objeto o ubicación.
- Buscar a anybody sin un mecanismo de identificación no acredita encontrar a Robin.

**Límites de verificación de la ficha:**

- Separar conformidad con el protocolo ask_name/listen de la verificación efectiva del nombre: la coincidencia de identidad requiere revisión del contrato del ejecutor.

### Qwen3B — No verificable

El plan pregunta y escucha el nombre, pero no contiene evidencia de comparación con Robin. Falta precisar el contrato de identificación.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(office)",
  "find(Robin, kind=person)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to office
2: say I will look for Robin
1001: go_to office
1002: say I have arrived at office
1003: find_person anybody
1004: focus enable
1005: say ask_name
1006: listen guest_name_last
1007: say acknowledge_name_last
1008: focus disable
1009: go_to instruction_point
1010: say task completed
```

run_id: `026bf9b3-fa0a-4004-92e5-c1f51a8ab579`

Decisión del investigador: **pendiente**. Observaciones: __________________

### Qwen7B — No verificable

El plan pregunta y escucha el nombre, pero no contiene evidencia de comparación con Robin. Falta precisar el contrato de identificación.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(office)",
  "find(Robin, kind=person)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to office
2: say I will look for Robin
1001: go_to office
1002: say I have arrived at office
1003: find_person anybody
1004: focus enable
1005: say ask_name
1006: listen guest_name_last
1007: say acknowledge_name_last
1008: focus disable
1009: go_to instruction_point
1010: say task completed
```

run_id: `83b2965d-ce56-43ad-9d1e-575ee411bb4f`

Decisión del investigador: **pendiente**. Observaciones: __________________

### GPT — No verificable

El plan pregunta y escucha el nombre, pero no contiene evidencia de comparación con Robin. Falta precisar el contrato de identificación.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(office)",
  "find(Robin, kind=person)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to office
2: say I will look for Robin
1001: go_to office
1002: say I have arrived at office
1003: find_person anybody
1004: focus enable
1005: say ask_name
1006: listen guest_name_last
1007: say acknowledge_name_last
1008: focus disable
1009: go_to instruction_point
1010: say task completed
```

run_id: `affe64b7-af04-47ef-ba80-7c09971b0d16`

Decisión del investigador: **pendiente**. Observaciones: __________________

## DEV-021

**Orden:** please find Robin in the ofice

**Intención:** INT-07. **Bloque:** funcional_y_linguistico.

**Subtareas:**

- Ir a office y localizar a la persona llamada Robin.

**Restricciones:**

- No tratar Robin como objeto o ubicación.
- Buscar a anybody sin un mecanismo de identificación no acredita encontrar a Robin.

**Límites de verificación de la ficha:**

- Separar conformidad con el protocolo ask_name/listen de la verificación efectiva del nombre: la coincidencia de identidad requiere revisión del contrato del ejecutor.

### Qwen3B — No verificable

El plan pregunta y escucha el nombre, pero no contiene evidencia de comparación con Robin. Falta precisar el contrato de identificación.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(office)",
  "find(Robin, kind=person)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to office
2: say I will look for Robin
1001: go_to office
1002: say I have arrived at office
1003: find_person anybody
1004: focus enable
1005: say ask_name
1006: listen guest_name_last
1007: say acknowledge_name_last
1008: focus disable
1009: go_to instruction_point
1010: say task completed
```

run_id: `aba2904d-2acd-4ce5-b126-1f27f2dab7f6`

Decisión del investigador: **pendiente**. Observaciones: __________________

### Qwen7B — No verificable

El plan pregunta y escucha el nombre, pero no contiene evidencia de comparación con Robin. Falta precisar el contrato de identificación.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(office)",
  "find(Robin, kind=person)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to office
2: say I will look for Robin
1001: go_to office
1002: say I have arrived at office
1003: find_person anybody
1004: focus enable
1005: say ask_name
1006: listen guest_name_last
1007: say acknowledge_name_last
1008: focus disable
1009: go_to instruction_point
1010: say task completed
```

run_id: `7851e165-39a1-4b69-b1bf-6c50b4d17d11`

Decisión del investigador: **pendiente**. Observaciones: __________________

### GPT — No verificable

El plan pregunta y escucha el nombre, pero no contiene evidencia de comparación con Robin. Falta precisar el contrato de identificación.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(office)",
  "find(Robin, kind=person)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to office
2: say I will look for Robin
1001: go_to office
1002: say I have arrived at office
1003: find_person anybody
1004: focus enable
1005: say ask_name
1006: listen guest_name_last
1007: say acknowledge_name_last
1008: focus disable
1009: go_to instruction_point
1010: say task completed
```

run_id: `8fddb33d-4c1f-4aea-9668-64f7b3841b54`

Decisión del investigador: **pendiente**. Observaciones: __________________

## DEV-022

**Orden:** Find Morgan in the kitchen and guide them to the entrance.

**Intención:** INT-08. **Bloque:** funcional_y_linguistico.

**Subtareas:**

- Localizar a Morgan en kitchen.
- Indicar a Morgan que siga al robot y guiarle a entrance.

**Restricciones:**

- Resolver them como Morgan; conservar entrance como destino.
- Un desplazamiento sin vincular a la persona no cubre por sí solo la subtarea de guía.

**Límites de verificación de la ficha:**

- Identidad de la persona sujeta al contrato de identificación; presencia física durante la guía fuera del alcance.

### Qwen3B — No verificable

La guía y su destino se expresan, pero no se acredita que la persona identificada sea Morgan; falta el contrato de identificación.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(kitchen)",
  "find(Morgan, kind=person)",
  "guide(Morgan, to=entrance)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to kitchen
2: say I will look for Morgan
3: say I will guide Morgan to entrance
1001: go_to kitchen
1002: say I have arrived at kitchen
1003: find_person anybody
1004: focus enable
1005: say ask_name
1006: listen guest_name_last
1007: say acknowledge_name_last
1008: say Please follow me to entrance
1009: focus disable
1010: go_to entrance
1011: say I have guided Morgan to entrance
1012: go_to instruction_point
1013: say task completed
```

run_id: `305c8491-9beb-43a1-b234-0843214aed61`

Decisión del investigador: **pendiente**. Observaciones: __________________

### Qwen7B — No verificable

La guía y su destino se expresan, pero no se acredita que la persona identificada sea Morgan; falta el contrato de identificación.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(kitchen)",
  "find(Morgan, kind=person)",
  "guide(Morgan, to=entrance)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to kitchen
2: say I will look for Morgan
3: say I will guide Morgan to entrance
1001: go_to kitchen
1002: say I have arrived at kitchen
1003: find_person anybody
1004: focus enable
1005: say ask_name
1006: listen guest_name_last
1007: say acknowledge_name_last
1008: say Please follow me to entrance
1009: focus disable
1010: go_to entrance
1011: say I have guided Morgan to entrance
1012: go_to instruction_point
1013: say task completed
```

run_id: `b22dc792-08df-421e-be17-6c6cc26376d9`

Decisión del investigador: **pendiente**. Observaciones: __________________

### GPT — No verificable

La guía y su destino se expresan, pero no se acredita que la persona identificada sea Morgan; falta el contrato de identificación.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(kitchen)",
  "find(Morgan, kind=person)",
  "guide(Morgan, to=entrance)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to kitchen
2: say I will look for Morgan
3: say I will guide Morgan to entrance
1001: go_to kitchen
1002: say I have arrived at kitchen
1003: find_person anybody
1004: focus enable
1005: say ask_name
1006: listen guest_name_last
1007: say acknowledge_name_last
1008: say Please follow me to entrance
1009: focus disable
1010: go_to entrance
1011: say I have guided Morgan to entrance
1012: go_to instruction_point
1013: say task completed
```

run_id: `85f6ed1b-b42d-4b1a-bfbd-519701b34675`

Decisión del investigador: **pendiente**. Observaciones: __________________

## DEV-023

**Orden:** Meet Morgan in the kitchen, then lead Morgan to the entrance.

**Intención:** INT-08. **Bloque:** funcional_y_linguistico.

**Subtareas:**

- Localizar a Morgan en kitchen.
- Indicar a Morgan que siga al robot y guiarle a entrance.

**Restricciones:**

- Resolver them como Morgan; conservar entrance como destino.
- Un desplazamiento sin vincular a la persona no cubre por sí solo la subtarea de guía.

**Límites de verificación de la ficha:**

- Identidad de la persona sujeta al contrato de identificación; presencia física durante la guía fuera del alcance.

### Qwen3B — No verificable

La guía y su destino se expresan, pero no se acredita que la persona identificada sea Morgan; falta el contrato de identificación.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(kitchen)",
  "find(Morgan, kind=person)",
  "guide(Morgan, to=entrance)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to kitchen
2: say I will look for Morgan
3: say I will guide Morgan to entrance
1001: go_to kitchen
1002: say I have arrived at kitchen
1003: find_person anybody
1004: focus enable
1005: say ask_name
1006: listen guest_name_last
1007: say acknowledge_name_last
1008: say Please follow me to entrance
1009: focus disable
1010: go_to entrance
1011: say I have guided Morgan to entrance
1012: go_to instruction_point
1013: say task completed
```

run_id: `45ccfe5c-1d03-41f1-a6e4-d33ac466946e`

Decisión del investigador: **pendiente**. Observaciones: __________________

### Qwen7B — No verificable

La guía y su destino se expresan, pero no se acredita que la persona identificada sea Morgan; falta el contrato de identificación.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(kitchen)",
  "find(Morgan, kind=person)",
  "guide(Morgan, to=entrance)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to kitchen
2: say I will look for Morgan
3: say I will guide Morgan to entrance
1001: go_to kitchen
1002: say I have arrived at kitchen
1003: find_person anybody
1004: focus enable
1005: say ask_name
1006: listen guest_name_last
1007: say acknowledge_name_last
1008: say Please follow me to entrance
1009: focus disable
1010: go_to entrance
1011: say I have guided Morgan to entrance
1012: go_to instruction_point
1013: say task completed
```

run_id: `e43f38ed-d4db-4b6c-b33f-d7532f285eaf`

Decisión del investigador: **pendiente**. Observaciones: __________________

### GPT — No verificable

La guía y su destino se expresan, pero no se acredita que la persona identificada sea Morgan; falta el contrato de identificación.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(kitchen)",
  "find(Morgan, kind=person)",
  "guide(Morgan, to=entrance)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to kitchen
2: say I will look for Morgan
3: say I will guide Morgan to entrance
1001: go_to kitchen
1002: say I have arrived at kitchen
1003: find_person anybody
1004: focus enable
1005: say ask_name
1006: listen guest_name_last
1007: say acknowledge_name_last
1008: say Please follow me to entrance
1009: focus disable
1010: go_to entrance
1011: say I have guided Morgan to entrance
1012: go_to instruction_point
1013: say task completed
```

run_id: `bb5bbef9-fd82-477e-b679-47691ac6bf11`

Decisión del investigador: **pendiente**. Observaciones: __________________

## DEV-024

**Orden:** find Morgan in the kichen and guide them to the entrance please

**Intención:** INT-08. **Bloque:** funcional_y_linguistico.

**Subtareas:**

- Localizar a Morgan en kitchen.
- Indicar a Morgan que siga al robot y guiarle a entrance.

**Restricciones:**

- Resolver them como Morgan; conservar entrance como destino.
- Un desplazamiento sin vincular a la persona no cubre por sí solo la subtarea de guía.

**Límites de verificación de la ficha:**

- Identidad de la persona sujeta al contrato de identificación; presencia física durante la guía fuera del alcance.

### Qwen3B — No verificable

La guía y su destino se expresan, pero no se acredita que la persona identificada sea Morgan; falta el contrato de identificación.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(kitchen)",
  "find(Morgan, kind=person)",
  "guide(Morgan, to=entrance)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to kitchen
2: say I will look for Morgan
3: say I will guide Morgan to entrance
1001: go_to kitchen
1002: say I have arrived at kitchen
1003: find_person anybody
1004: focus enable
1005: say ask_name
1006: listen guest_name_last
1007: say acknowledge_name_last
1008: say Please follow me to entrance
1009: focus disable
1010: go_to entrance
1011: say I have guided Morgan to entrance
1012: go_to instruction_point
1013: say task completed
```

run_id: `a9681656-5b42-4de2-b21a-90aa2b8f9b4a`

Decisión del investigador: **pendiente**. Observaciones: __________________

### Qwen7B — No verificable

La guía y su destino se expresan, pero no se acredita que la persona identificada sea Morgan; falta el contrato de identificación.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(kitchen)",
  "find(Morgan, kind=person)",
  "guide(Morgan, to=entrance)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to kitchen
2: say I will look for Morgan
3: say I will guide Morgan to entrance
1001: go_to kitchen
1002: say I have arrived at kitchen
1003: find_person anybody
1004: focus enable
1005: say ask_name
1006: listen guest_name_last
1007: say acknowledge_name_last
1008: say Please follow me to entrance
1009: focus disable
1010: go_to entrance
1011: say I have guided Morgan to entrance
1012: go_to instruction_point
1013: say task completed
```

run_id: `6dc31b93-230c-4702-bed3-dbbc3d395747`

Decisión del investigador: **pendiente**. Observaciones: __________________

### GPT — Incumple

Desactiva focus antes de Please follow me to entrance, aunque la interacción continúa. Además persiste la limitación de identificación de Morgan.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(kitchen)",
  "find(Morgan, kind=person)",
  "guide(Morgan, to=entrance)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to kitchen
2: say I will look for Morgan
3: say I will guide Morgan to entrance
1001: go_to kitchen
1002: say I have arrived at kitchen
1003: find_person anybody
1004: focus enable
1005: say ask_name
1006: listen guest_name_last
1007: say acknowledge_name_last
1008: focus disable
1009: say Please follow me to entrance
1010: go_to entrance
1011: say I have guided Morgan to entrance
1012: go_to instruction_point
1013: say task completed
```

run_id: `e8e868bc-303a-4b6b-b8ea-7cc33069af08`

Decisión del investigador: **pendiente**. Observaciones: __________________

## DEV-025

**Orden:** Find the waving person in the bedroom and follow them.

**Intención:** INT-09. **Bloque:** funcional_y_linguistico.

**Subtareas:**

- Localizar una persona que saluda con la mano en bedroom.
- Iniciar seguimiento de esa misma persona sin inventar un destino.

**Restricciones:**

- El gesto debe conservarse en la búsqueda.
- El seguimiento debe corresponder al referente encontrado.

**Límites de verificación de la ficha:**

- instruct_follow_only es una clave de protocolo. Su presencia no demuestra seguimiento; cumplimiento operativo no verificable hasta precisar el contrato del ejecutor.

### Qwen3B — No verificable

Se emite instruct_follow_only, pero no están establecidos sus efectos ejecutables de seguimiento.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(bedroom)",
  "find(person, kind=person, gesture='waving person')",
  "follow(person)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to bedroom
2: say I will look for person waving_person
3: say I will follow person
1001: go_to bedroom
1002: say I have arrived at bedroom
1003: find_pose waving_1
1004: approach customer_1
1005: focus enable
1006: say instruct_follow_only
1007: focus disable
1008: go_to instruction_point
1009: say task completed
```

run_id: `b732b10b-0a3e-44aa-b2ed-6001d3111035`

Decisión del investigador: **pendiente**. Observaciones: __________________

### Qwen7B — No verificable

Se emite instruct_follow_only, pero no están establecidos sus efectos ejecutables de seguimiento.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(bedroom)",
  "find(person, kind=person, gesture='waving person')",
  "follow(person)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to bedroom
2: say I will look for person waving_person
3: say I will follow person
1001: go_to bedroom
1002: say I have arrived at bedroom
1003: find_pose waving_1
1004: approach customer_1
1005: focus enable
1006: say instruct_follow_only
1007: focus disable
1008: go_to instruction_point
1009: say task completed
```

run_id: `8e8f9dfd-5691-41db-90b9-1abaf4150330`

Decisión del investigador: **pendiente**. Observaciones: __________________

### GPT — No verificable

Se emite instruct_follow_only, pero no están establecidos sus efectos ejecutables de seguimiento.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(bedroom)",
  "find(person, kind=person, gesture='waving person')",
  "follow(person)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to bedroom
2: say I will look for person waving person
3: say I will follow person
1001: go_to bedroom
1002: say I have arrived at bedroom
1003: find_pose waving_1
1004: approach customer_1
1005: focus enable
1006: say instruct_follow_only
1007: focus disable
1008: go_to instruction_point
1009: say task completed
```

run_id: `1ae4eb01-4112-4e15-a9c7-afb32d9cafb9`

Decisión del investigador: **pendiente**. Observaciones: __________________

## DEV-026

**Orden:** In the bedroom, locate the person who is waving and follow that person.

**Intención:** INT-09. **Bloque:** funcional_y_linguistico.

**Subtareas:**

- Localizar una persona que saluda con la mano en bedroom.
- Iniciar seguimiento de esa misma persona sin inventar un destino.

**Restricciones:**

- El gesto debe conservarse en la búsqueda.
- El seguimiento debe corresponder al referente encontrado.

**Límites de verificación de la ficha:**

- instruct_follow_only es una clave de protocolo. Su presencia no demuestra seguimiento; cumplimiento operativo no verificable hasta precisar el contrato del ejecutor.

### Qwen3B — No verificable

Se emite instruct_follow_only, pero no están establecidos sus efectos ejecutables de seguimiento.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(bedroom)",
  "find(person, kind=person, gesture='person who is waving')",
  "follow(person)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to bedroom
2: say I will look for person person_who_is_waving
3: say I will follow person
1001: go_to bedroom
1002: say I have arrived at bedroom
1003: find_pose waving_1
1004: approach customer_1
1005: focus enable
1006: say instruct_follow_only
1007: focus disable
1008: go_to instruction_point
1009: say task completed
```

run_id: `964067c1-292e-4b16-ba67-5bb559cd839d`

Decisión del investigador: **pendiente**. Observaciones: __________________

### Qwen7B — No verificable

Se emite instruct_follow_only, pero no están establecidos sus efectos ejecutables de seguimiento.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(bedroom)",
  "find(person, kind=person, gesture='waving person')",
  "follow(person)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to bedroom
2: say I will look for person waving_person
3: say I will follow person
1001: go_to bedroom
1002: say I have arrived at bedroom
1003: find_pose waving_1
1004: approach customer_1
1005: focus enable
1006: say instruct_follow_only
1007: focus disable
1008: go_to instruction_point
1009: say task completed
```

run_id: `36cc7223-e4e0-4a45-bc68-12ca5af07671`

Decisión del investigador: **pendiente**. Observaciones: __________________

### GPT — No verificable

Se emite instruct_follow_only, pero no están establecidos sus efectos ejecutables de seguimiento.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(bedroom)",
  "find(person, kind=person, gesture='waving person')",
  "follow(person)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to bedroom
2: say I will look for person waving person
3: say I will follow person
1001: go_to bedroom
1002: say I have arrived at bedroom
1003: find_pose waving_1
1004: approach customer_1
1005: focus enable
1006: say instruct_follow_only
1007: focus disable
1008: go_to instruction_point
1009: say task completed
```

run_id: `096fc9eb-04b2-488c-bf4a-4d07f3886588`

Decisión del investigador: **pendiente**. Observaciones: __________________

## DEV-027

**Orden:** please find the waving person in the bedrom and follow them

**Intención:** INT-09. **Bloque:** funcional_y_linguistico.

**Subtareas:**

- Localizar una persona que saluda con la mano en bedroom.
- Iniciar seguimiento de esa misma persona sin inventar un destino.

**Restricciones:**

- El gesto debe conservarse en la búsqueda.
- El seguimiento debe corresponder al referente encontrado.

**Límites de verificación de la ficha:**

- instruct_follow_only es una clave de protocolo. Su presencia no demuestra seguimiento; cumplimiento operativo no verificable hasta precisar el contrato del ejecutor.

### Qwen3B — No verificable

Se emite instruct_follow_only, pero no están establecidos sus efectos ejecutables de seguimiento.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(bedroom)",
  "find(person, kind=person, gesture='waving person')",
  "follow(person)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to bedroom
2: say I will look for person waving_person
3: say I will follow person
1001: go_to bedroom
1002: say I have arrived at bedroom
1003: find_pose waving_1
1004: approach customer_1
1005: focus enable
1006: say instruct_follow_only
1007: focus disable
1008: go_to instruction_point
1009: say task completed
```

run_id: `cd735468-7df7-49f1-bd48-2918cb74f971`

Decisión del investigador: **pendiente**. Observaciones: __________________

### Qwen7B — No verificable

Se emite instruct_follow_only, pero no están establecidos sus efectos ejecutables de seguimiento.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(bedroom)",
  "find(person, kind=person, gesture='waving person')",
  "follow(person)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to bedroom
2: say I will look for person waving_person
3: say I will follow person
1001: go_to bedroom
1002: say I have arrived at bedroom
1003: find_pose waving_1
1004: approach customer_1
1005: focus enable
1006: say instruct_follow_only
1007: focus disable
1008: go_to instruction_point
1009: say task completed
```

run_id: `669e5fc8-cf57-4021-9cdf-9fc8f5ff36cb`

Decisión del investigador: **pendiente**. Observaciones: __________________

### GPT — No verificable

Se emite instruct_follow_only, pero no están establecidos sus efectos ejecutables de seguimiento.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(bedroom)",
  "find(person, kind=person, gesture='waving person')",
  "follow(person)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to bedroom
2: say I will look for person waving person
3: say I will follow person
1001: go_to bedroom
1002: say I have arrived at bedroom
1003: find_pose waving_1
1004: approach customer_1
1005: focus enable
1006: say instruct_follow_only
1007: focus disable
1008: go_to instruction_point
1009: say task completed
```

run_id: `78df8d0a-fb0b-4c2c-af8a-0a4c2e8196c4`

Decisión del investigador: **pendiente**. Observaciones: __________________

## DEV-028

**Orden:** Take an orange from the refrigerator and give it to Sarah in the kitchen.

**Intención:** INT-10. **Bloque:** funcional_y_linguistico.

**Subtareas:**

- Adquirir orange en refrigerator.
- Localizar a Sarah en kitchen.
- Entregar a Sarah la misma orange.

**Restricciones:**

- Conservar el objeto al cambiar de ubicación y buscar a Sarah.
- No entregar al operador ni confundir orange con un atributo de ropa.

**Límites de verificación de la ficha:**

- Verificar el enlace entre el nombre Sarah y la referencia interna del destinatario.

### Qwen3B — No verificable

Se conserva el objeto y se entrega a guest_last, pero el vínculo verificado entre guest_last y Sarah depende del contrato de identificación.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(refrigerator)",
  "find(orange, kind=object)",
  "take(orange)",
  "go(kitchen)",
  "find(Sarah, kind=person)",
  "deliver(orange, Sarah)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to refrigerator
2: say I will search for orange
3: say I will pick up orange
4: say I will navigate to kitchen
5: say I will look for Sarah
6: say I will deliver orange to Sarah
1001: go_to refrigerator
1002: say I have arrived at refrigerator
1003: find_object orange_1
1004: take orange_1
1005: say I have picked up orange
1006: go_to kitchen
1007: say I have arrived at kitchen
1008: find_person anybody
1009: focus enable
1010: say ask_name
1011: listen guest_name_last
1012: say acknowledge_name_last
1013: focus disable
1014: approach guest_last
1015: give orange_1
1016: say I have delivered orange
1017: go_to instruction_point
1018: say task completed
```

run_id: `5e76c32a-ad58-44ff-a635-43e8c4ba2ffb`

Decisión del investigador: **pendiente**. Observaciones: __________________

### Qwen7B — No verificable

Se conserva el objeto y se entrega a guest_last, pero el vínculo verificado entre guest_last y Sarah depende del contrato de identificación.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(refrigerator)",
  "find(orange, kind=object)",
  "take(orange)",
  "go(kitchen)",
  "find(Sarah, kind=person)",
  "deliver(orange, Sarah)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to refrigerator
2: say I will search for orange
3: say I will pick up orange
4: say I will navigate to kitchen
5: say I will look for Sarah
6: say I will deliver orange to Sarah
1001: go_to refrigerator
1002: say I have arrived at refrigerator
1003: find_object orange_1
1004: take orange_1
1005: say I have picked up orange
1006: go_to kitchen
1007: say I have arrived at kitchen
1008: find_person anybody
1009: focus enable
1010: say ask_name
1011: listen guest_name_last
1012: say acknowledge_name_last
1013: focus disable
1014: approach guest_last
1015: give orange_1
1016: say I have delivered orange
1017: go_to instruction_point
1018: say task completed
```

run_id: `2269607b-8e9d-46a7-a702-e1881e2cc52f`

Decisión del investigador: **pendiente**. Observaciones: __________________

### GPT — No verificable

Se conserva el objeto y se entrega a guest_last, pero el vínculo verificado entre guest_last y Sarah depende del contrato de identificación.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(refrigerator)",
  "find(orange, kind=object)",
  "take(orange)",
  "go(kitchen)",
  "find(Sarah, kind=person)",
  "deliver(orange, to=Sarah)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to refrigerator
2: say I will search for orange
3: say I will pick up orange
4: say I will navigate to kitchen
5: say I will look for Sarah
6: say I will deliver orange to Sarah
1001: go_to refrigerator
1002: say I have arrived at refrigerator
1003: find_object orange_1
1004: take orange_1
1005: say I have picked up orange
1006: go_to kitchen
1007: say I have arrived at kitchen
1008: find_person anybody
1009: focus enable
1010: say ask_name
1011: listen guest_name_last
1012: say acknowledge_name_last
1013: focus disable
1014: approach guest_last
1015: give orange_1
1016: say I have delivered orange
1017: go_to instruction_point
1018: say task completed
```

run_id: `6da9fcd2-ae0f-4414-933c-0e49f1fdcc97`

Decisión del investigador: **pendiente**. Observaciones: __________________

## DEV-029

**Orden:** Fetch an orange at the refrigerator, then find Sarah in the kitchen and hand the orange to her.

**Intención:** INT-10. **Bloque:** funcional_y_linguistico.

**Subtareas:**

- Adquirir orange en refrigerator.
- Localizar a Sarah en kitchen.
- Entregar a Sarah la misma orange.

**Restricciones:**

- Conservar el objeto al cambiar de ubicación y buscar a Sarah.
- No entregar al operador ni confundir orange con un atributo de ropa.

**Límites de verificación de la ficha:**

- Verificar el enlace entre el nombre Sarah y la referencia interna del destinatario.

### Qwen3B — No verificable

Se conserva el objeto y se entrega a guest_last, pero el vínculo verificado entre guest_last y Sarah depende del contrato de identificación.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(refrigerator)",
  "find(orange, kind=object)",
  "take(orange)",
  "go(kitchen)",
  "find(Sarah, kind=person)",
  "deliver(orange, Sarah)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to refrigerator
2: say I will search for orange
3: say I will pick up orange
4: say I will navigate to kitchen
5: say I will look for Sarah
6: say I will deliver orange to Sarah
1001: go_to refrigerator
1002: say I have arrived at refrigerator
1003: find_object orange_1
1004: take orange_1
1005: say I have picked up orange
1006: go_to kitchen
1007: say I have arrived at kitchen
1008: find_person anybody
1009: focus enable
1010: say ask_name
1011: listen guest_name_last
1012: say acknowledge_name_last
1013: focus disable
1014: approach guest_last
1015: give orange_1
1016: say I have delivered orange
1017: go_to instruction_point
1018: say task completed
```

run_id: `8df1a785-4400-45bf-9c9f-81efba7311dd`

Decisión del investigador: **pendiente**. Observaciones: __________________

### Qwen7B — Incumple

Busca, toma y entrega orange coat en lugar de orange; la referencia prohíbe confundir objeto y ropa.

Interpretación propuesta: `False`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(refrigerator)",
  "find(orange coat, kind=object)",
  "take(orange coat)",
  "go(kitchen)",
  "find(Sarah, kind=person)",
  "deliver(orange coat, Sarah)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to refrigerator
2: say I will search for orange_coat
3: say I will pick up orange_coat
4: say I will navigate to kitchen
5: say I will look for Sarah
6: say I will deliver orange_coat to Sarah
1001: go_to refrigerator
1002: say I have arrived at refrigerator
1003: find_object orange_coat_1
1004: take orange_coat_1
1005: say I have picked up orange_coat
1006: go_to kitchen
1007: say I have arrived at kitchen
1008: find_person anybody
1009: focus enable
1010: say ask_name
1011: listen guest_name_last
1012: say acknowledge_name_last
1013: focus disable
1014: approach guest_last
1015: give orange_coat_1
1016: say I have delivered orange_coat
1017: go_to instruction_point
1018: say task completed
```

run_id: `08c6dcec-22db-4e5e-848c-7534e2942fbb`

Decisión del investigador: **pendiente**. Observaciones: __________________

### GPT — No verificable

Se conserva el objeto y se entrega a guest_last, pero el vínculo verificado entre guest_last y Sarah depende del contrato de identificación.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(refrigerator)",
  "find(orange, kind=object)",
  "take(orange)",
  "go(kitchen)",
  "find(Sarah, kind=person)",
  "deliver(orange, to=Sarah)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to refrigerator
2: say I will search for orange
3: say I will pick up orange
4: say I will navigate to kitchen
5: say I will look for Sarah
6: say I will deliver orange to Sarah
1001: go_to refrigerator
1002: say I have arrived at refrigerator
1003: find_object orange_1
1004: take orange_1
1005: say I have picked up orange
1006: go_to kitchen
1007: say I have arrived at kitchen
1008: find_person anybody
1009: focus enable
1010: say ask_name
1011: listen guest_name_last
1012: say acknowledge_name_last
1013: focus disable
1014: approach guest_last
1015: give orange_1
1016: say I have delivered orange
1017: go_to instruction_point
1018: say task completed
```

run_id: `2e7e813d-98b5-4263-8458-69920db04327`

Decisión del investigador: **pendiente**. Observaciones: __________________

## DEV-030

**Orden:** take an orange from the refridgerator and give it to Sarah in the kichen

**Intención:** INT-10. **Bloque:** funcional_y_linguistico.

**Subtareas:**

- Adquirir orange en refrigerator.
- Localizar a Sarah en kitchen.
- Entregar a Sarah la misma orange.

**Restricciones:**

- Conservar el objeto al cambiar de ubicación y buscar a Sarah.
- No entregar al operador ni confundir orange con un atributo de ropa.

**Límites de verificación de la ficha:**

- Verificar el enlace entre el nombre Sarah y la referencia interna del destinatario.

### Qwen3B — No verificable

Se conserva el objeto y se entrega a guest_last, pero el vínculo verificado entre guest_last y Sarah depende del contrato de identificación.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(refrigerator)",
  "find(orange, kind=object)",
  "take(orange)",
  "go(kitchen)",
  "find(Sarah, kind=person)",
  "deliver(orange, Sarah)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to refrigerator
2: say I will search for orange
3: say I will pick up orange
4: say I will navigate to kitchen
5: say I will look for Sarah
6: say I will deliver orange to Sarah
1001: go_to refrigerator
1002: say I have arrived at refrigerator
1003: find_object orange_1
1004: take orange_1
1005: say I have picked up orange
1006: go_to kitchen
1007: say I have arrived at kitchen
1008: find_person anybody
1009: focus enable
1010: say ask_name
1011: listen guest_name_last
1012: say acknowledge_name_last
1013: focus disable
1014: approach guest_last
1015: give orange_1
1016: say I have delivered orange
1017: go_to instruction_point
1018: say task completed
```

run_id: `f494ff7e-12ef-47b3-9904-ae18de29d425`

Decisión del investigador: **pendiente**. Observaciones: __________________

### Qwen7B — No verificable

Se conserva el objeto y se entrega a guest_last, pero el vínculo verificado entre guest_last y Sarah depende del contrato de identificación.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(refrigerator)",
  "find(orange, kind=object)",
  "take(orange)",
  "go(kitchen)",
  "find(Sarah, kind=person)",
  "deliver(orange, Sarah)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to refrigerator
2: say I will search for orange
3: say I will pick up orange
4: say I will navigate to kitchen
5: say I will look for Sarah
6: say I will deliver orange to Sarah
1001: go_to refrigerator
1002: say I have arrived at refrigerator
1003: find_object orange_1
1004: take orange_1
1005: say I have picked up orange
1006: go_to kitchen
1007: say I have arrived at kitchen
1008: find_person anybody
1009: focus enable
1010: say ask_name
1011: listen guest_name_last
1012: say acknowledge_name_last
1013: focus disable
1014: approach guest_last
1015: give orange_1
1016: say I have delivered orange
1017: go_to instruction_point
1018: say task completed
```

run_id: `1c4a24e9-d68c-4376-bf97-342f5f5f3a29`

Decisión del investigador: **pendiente**. Observaciones: __________________

### GPT — No verificable

Se conserva el objeto y se entrega a guest_last, pero el vínculo verificado entre guest_last y Sarah depende del contrato de identificación.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(refrigerator)",
  "find(orange, kind=object)",
  "take(orange)",
  "go(kitchen)",
  "find(Sarah, kind=person)",
  "deliver(orange, to=Sarah)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to refrigerator
2: say I will search for orange
3: say I will pick up orange
4: say I will navigate to kitchen
5: say I will look for Sarah
6: say I will deliver orange to Sarah
1001: go_to refrigerator
1002: say I have arrived at refrigerator
1003: find_object orange_1
1004: take orange_1
1005: say I have picked up orange
1006: go_to kitchen
1007: say I have arrived at kitchen
1008: find_person anybody
1009: focus enable
1010: say ask_name
1011: listen guest_name_last
1012: say acknowledge_name_last
1013: focus disable
1014: approach guest_last
1015: give orange_1
1016: say I have delivered orange
1017: go_to instruction_point
1018: say task completed
```

run_id: `b583216d-cc2c-4afb-8388-c55056e1d514`

Decisión del investigador: **pendiente**. Observaciones: __________________

## DEV-031

**Orden:** Count the toys on the storage rack.

**Intención:** INT-11. **Bloque:** funcional_y_linguistico.

**Subtareas:**

- Contar toys en storage rack y comunicar el conteo al operador.

**Restricciones:**

- No inventar una cantidad: el plan debe solicitar el análisis y la comunicación del resultado.
- La categoría completa toys debe preservarse.

**Límites de verificación de la ficha:**


### Qwen3B — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(storage rack)",
  "count(toys, kind=object)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to storage_rack
2: say I will count toys
3: say I will return to the instruction point to report the count
1001: go_to storage_rack
1002: say I have arrived at storage_rack
1003: analyze_objects count_toys
1004: go_to instruction_point
1005: focus enable
1006: say count_category
1007: focus disable
1008: say task completed
```

run_id: `cd6ee87b-e1f9-458d-879b-dc381b0891fe`

Decisión del investigador: **pendiente**. Observaciones: __________________

### Qwen7B — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(storage rack)",
  "count(toys, kind=object)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to storage_rack
2: say I will count toys
3: say I will return to the instruction point to report the count
1001: go_to storage_rack
1002: say I have arrived at storage_rack
1003: analyze_objects count_toys
1004: go_to instruction_point
1005: focus enable
1006: say count_category
1007: focus disable
1008: say task completed
```

run_id: `b31e5245-031f-4051-8390-46f8ee3e4363`

Decisión del investigador: **pendiente**. Observaciones: __________________

### GPT — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(storage rack)",
  "count(toys, kind=object)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to storage rack
2: say I will count toys
3: say I will return to the instruction point to report the count
1001: go_to storage_rack
1002: say I have arrived at storage rack
1003: analyze_objects count_toys
1004: go_to instruction_point
1005: focus enable
1006: say count_category
1007: focus disable
1008: say task completed
```

run_id: `81143f68-4bc4-445f-bee5-71dd0c247f21`

Decisión del investigador: **pendiente**. Observaciones: __________________

## DEV-032

**Orden:** Tell me how many toys are on the storage rack.

**Intención:** INT-11. **Bloque:** funcional_y_linguistico.

**Subtareas:**

- Contar toys en storage rack y comunicar el conteo al operador.

**Restricciones:**

- No inventar una cantidad: el plan debe solicitar el análisis y la comunicación del resultado.
- La categoría completa toys debe preservarse.

**Límites de verificación de la ficha:**


### Qwen3B — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(storage rack)",
  "count(toys, kind=object)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to storage_rack
2: say I will count toys
3: say I will return to the instruction point to report the count
1001: go_to storage_rack
1002: say I have arrived at storage_rack
1003: analyze_objects count_toys
1004: go_to instruction_point
1005: focus enable
1006: say count_category
1007: focus disable
1008: say task completed
```

run_id: `c63ed1d3-08f2-4369-9dbb-235ebe8285bb`

Decisión del investigador: **pendiente**. Observaciones: __________________

### Qwen7B — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(storage rack)",
  "count(toys, kind=object)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to storage_rack
2: say I will count toys
3: say I will return to the instruction point to report the count
1001: go_to storage_rack
1002: say I have arrived at storage_rack
1003: analyze_objects count_toys
1004: go_to instruction_point
1005: focus enable
1006: say count_category
1007: focus disable
1008: say task completed
```

run_id: `f91bc2e6-b17c-4349-9b95-8f4d94b2b89a`

Decisión del investigador: **pendiente**. Observaciones: __________________

### GPT — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(storage rack)",
  "count(toys, kind=object)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to storage_rack
2: say I will count toys
3: say I will return to the instruction point to report the count
1001: go_to storage_rack
1002: say I have arrived at storage_rack
1003: analyze_objects count_toys
1004: go_to instruction_point
1005: focus enable
1006: say count_category
1007: focus disable
1008: say task completed
```

run_id: `c8625a10-e712-481c-9155-b7c0adf0838c`

Decisión del investigador: **pendiente**. Observaciones: __________________

## DEV-033

**Orden:** please count the the toys on the storage rack

**Intención:** INT-11. **Bloque:** funcional_y_linguistico.

**Subtareas:**

- Contar toys en storage rack y comunicar el conteo al operador.

**Restricciones:**

- No inventar una cantidad: el plan debe solicitar el análisis y la comunicación del resultado.
- La categoría completa toys debe preservarse.

**Límites de verificación de la ficha:**


### Qwen3B — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(storage rack)",
  "count(toys, kind=object)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to storage_rack
2: say I will count toys
3: say I will return to the instruction point to report the count
1001: go_to storage_rack
1002: say I have arrived at storage_rack
1003: analyze_objects count_toys
1004: go_to instruction_point
1005: focus enable
1006: say count_category
1007: focus disable
1008: say task completed
```

run_id: `b67802b0-bc70-48ef-8d6e-4ab1094ddda9`

Decisión del investigador: **pendiente**. Observaciones: __________________

### Qwen7B — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(storage rack)",
  "count(toys, kind=object)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to storage_rack
2: say I will count toys
3: say I will return to the instruction point to report the count
1001: go_to storage_rack
1002: say I have arrived at storage_rack
1003: analyze_objects count_toys
1004: go_to instruction_point
1005: focus enable
1006: say count_category
1007: focus disable
1008: say task completed
```

run_id: `02214167-6500-4245-bd89-9a50d36e1786`

Decisión del investigador: **pendiente**. Observaciones: __________________

### GPT — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(storage rack)",
  "count(toys, kind=object)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to storage_rack
2: say I will count toys
3: say I will return to the instruction point to report the count
1001: go_to storage_rack
1002: say I have arrived at storage_rack
1003: analyze_objects count_toys
1004: go_to instruction_point
1005: focus enable
1006: say count_category
1007: focus disable
1008: say task completed
```

run_id: `2d02c78d-255c-49b0-81d5-8efbcdaae29d`

Decisión del investigador: **pendiente**. Observaciones: __________________

## DEV-034

**Orden:** Find Charlie in the living room and tell Charlie the current time.

**Intención:** INT-12. **Bloque:** funcional_y_linguistico.

**Subtareas:**

- Localizar a Charlie en living room.
- Comunicarle la hora actual.

**Restricciones:**

- Normalizar la información a current_time y conservar el contexto de Charlie.
- No reemplazar la hora por fecha o nombre del equipo.

**Límites de verificación de la ficha:**

- Comprobar que el diálogo se dirige a la persona identificada; no inferir identidad correcta de un simple acuse hablado.

### Qwen3B — No verificable

Se comunica current_time tras ask_name/listen, pero no se verifica que el interlocutor sea Charlie.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(living room)",
  "find(Charlie, kind=person)",
  "tell('the current time')"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to living_room
2: say I will look for Charlie
3: say I will say the current time
1001: go_to living_room
1002: say I have arrived at living_room
1003: find_person anybody
1004: focus enable
1005: say ask_name
1006: listen guest_name_last
1007: say acknowledge_name_last
1008: say current_time
1009: focus disable
1010: go_to instruction_point
1011: say task completed
```

run_id: `d8dd0b27-b8a0-44fb-a3c8-adcf236cfef0`

Decisión del investigador: **pendiente**. Observaciones: __________________

### Qwen7B — No verificable

Se comunica current_time tras ask_name/listen, pero no se verifica que el interlocutor sea Charlie.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(living room)",
  "find(Charlie, kind=person)",
  "tell('the current time')"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to living_room
2: say I will look for Charlie
3: say I will say the current time
1001: go_to living_room
1002: say I have arrived at living_room
1003: find_person anybody
1004: focus enable
1005: say ask_name
1006: listen guest_name_last
1007: say acknowledge_name_last
1008: say current_time
1009: focus disable
1010: go_to instruction_point
1011: say task completed
```

run_id: `e2bed523-5741-45c0-9630-71f4286cf02e`

Decisión del investigador: **pendiente**. Observaciones: __________________

### GPT — No verificable

Se comunica current_time tras ask_name/listen, pero no se verifica que el interlocutor sea Charlie.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(living room)",
  "find(Charlie, kind=person)",
  "tell(current_time)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to living_room
2: say I will look for Charlie
3: say I will say the current time
1001: go_to living_room
1002: say I have arrived at living_room
1003: find_person anybody
1004: focus enable
1005: say ask_name
1006: listen guest_name_last
1007: say acknowledge_name_last
1008: say current_time
1009: focus disable
1010: go_to instruction_point
1011: say task completed
```

run_id: `d8009ab2-b301-470b-936b-3c57b1536f51`

Decisión del investigador: **pendiente**. Observaciones: __________________

## DEV-035

**Orden:** Locate Charlie in the living room and say what time it is to Charlie.

**Intención:** INT-12. **Bloque:** funcional_y_linguistico.

**Subtareas:**

- Localizar a Charlie en living room.
- Comunicarle la hora actual.

**Restricciones:**

- Normalizar la información a current_time y conservar el contexto de Charlie.
- No reemplazar la hora por fecha o nombre del equipo.

**Límites de verificación de la ficha:**

- Comprobar que el diálogo se dirige a la persona identificada; no inferir identidad correcta de un simple acuse hablado.

### Qwen3B — No verificable

Se comunica current_time tras ask_name/listen, pero no se verifica que el interlocutor sea Charlie.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(living room)",
  "find(Charlie, kind=person)",
  "tell('what time it is')"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to living_room
2: say I will look for Charlie
3: say I will say the current time
1001: go_to living_room
1002: say I have arrived at living_room
1003: find_person anybody
1004: focus enable
1005: say ask_name
1006: listen guest_name_last
1007: say acknowledge_name_last
1008: say current_time
1009: focus disable
1010: go_to instruction_point
1011: say task completed
```

run_id: `a2641599-ef1a-4c04-a7d3-9bf32e1188a3`

Decisión del investigador: **pendiente**. Observaciones: __________________

### Qwen7B — No verificable

Se comunica current_time tras ask_name/listen, pero no se verifica que el interlocutor sea Charlie.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(living room)",
  "find(Charlie, kind=person)",
  "tell('what time it is')"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to living_room
2: say I will look for Charlie
3: say I will say the current time
1001: go_to living_room
1002: say I have arrived at living_room
1003: find_person anybody
1004: focus enable
1005: say ask_name
1006: listen guest_name_last
1007: say acknowledge_name_last
1008: say current_time
1009: focus disable
1010: go_to instruction_point
1011: say task completed
```

run_id: `eb9f72e6-f4de-41ea-b6f2-cc02cdca69c1`

Decisión del investigador: **pendiente**. Observaciones: __________________

### GPT — No verificable

Se comunica current_time tras ask_name/listen, pero no se verifica que el interlocutor sea Charlie.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(living room)",
  "find(Charlie, kind=person)",
  "tell(current_time)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to living_room
2: say I will look for Charlie
3: say I will say the current time
1001: go_to living_room
1002: say I have arrived at living_room
1003: find_person anybody
1004: focus enable
1005: say ask_name
1006: listen guest_name_last
1007: say acknowledge_name_last
1008: say current_time
1009: focus disable
1010: go_to instruction_point
1011: say task completed
```

run_id: `52fca670-e337-4b0d-bf16-d239185241ab`

Decisión del investigador: **pendiente**. Observaciones: __________________

## DEV-036

**Orden:** please find Charlie in the living  room and tell Charlie the current time

**Intención:** INT-12. **Bloque:** funcional_y_linguistico.

**Subtareas:**

- Localizar a Charlie en living room.
- Comunicarle la hora actual.

**Restricciones:**

- Normalizar la información a current_time y conservar el contexto de Charlie.
- No reemplazar la hora por fecha o nombre del equipo.

**Límites de verificación de la ficha:**

- Comprobar que el diálogo se dirige a la persona identificada; no inferir identidad correcta de un simple acuse hablado.

### Qwen3B — No verificable

Se comunica current_time tras ask_name/listen, pero no se verifica que el interlocutor sea Charlie.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(living room)",
  "find(Charlie, kind=person)",
  "tell('the current time')"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to living_room
2: say I will look for Charlie
3: say I will say the current time
1001: go_to living_room
1002: say I have arrived at living_room
1003: find_person anybody
1004: focus enable
1005: say ask_name
1006: listen guest_name_last
1007: say acknowledge_name_last
1008: say current_time
1009: focus disable
1010: go_to instruction_point
1011: say task completed
```

run_id: `ee7b7138-31c2-48da-8adf-07f98a436c9c`

Decisión del investigador: **pendiente**. Observaciones: __________________

### Qwen7B — No verificable

Se comunica current_time tras ask_name/listen, pero no se verifica que el interlocutor sea Charlie.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(living room)",
  "find(Charlie, kind=person)",
  "tell('the current time')"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to living_room
2: say I will look for Charlie
3: say I will say the current time
1001: go_to living_room
1002: say I have arrived at living_room
1003: find_person anybody
1004: focus enable
1005: say ask_name
1006: listen guest_name_last
1007: say acknowledge_name_last
1008: say current_time
1009: focus disable
1010: go_to instruction_point
1011: say task completed
```

run_id: `fc5ad1c3-96f4-4595-b37a-972f4cde8928`

Decisión del investigador: **pendiente**. Observaciones: __________________

### GPT — No verificable

Se comunica current_time tras ask_name/listen, pero no se verifica que el interlocutor sea Charlie.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(living room)",
  "find(Charlie, kind=person)",
  "tell(current_time)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to living room
2: say I will look for Charlie
3: say I will say the current time
1001: go_to living_room
1002: say I have arrived at living_room
1003: find_person anybody
1004: focus enable
1005: say ask_name
1006: listen guest_name_last
1007: say acknowledge_name_last
1008: say current_time
1009: focus disable
1010: go_to instruction_point
1011: say task completed
```

run_id: `6d01559e-f783-466c-b24c-b42425cbfe2f`

Decisión del investigador: **pendiente**. Observaciones: __________________

## DEV-037

**Orden:** Find a person in the bedroom, ask their name, and come back to tell me their name.

**Intención:** INT-13. **Bloque:** funcional_y_linguistico.

**Subtareas:**

- Encontrar una persona en bedroom y adquirir su nombre.
- Regresar al operador y comunicar el nombre adquirido.

**Restricciones:**

- No inventar el nombre ni confundirlo con un nombre fijo del catálogo.
- La comunicación al operador debe referirse a la información adquirida.

**Límites de verificación de la ficha:**

- La persistencia y recuperación de saved_name deben verificarse respecto del contrato del ejecutor.

### Qwen3B — No verificable

Se solicita el nombre y se emite saved_name al regresar; falta establecer la persistencia y recuperación del dato entre esas acciones.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(bedroom)",
  "find(person, kind=person)",
  "save(name)",
  "go(instruction_point)",
  "tell(name)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to bedroom
2: say I will look for person
3: say I will save name
4: say I will navigate to instruction_point
5: say I will tell name
1001: go_to bedroom
1002: say I have arrived at bedroom
1003: find_person anybody
1004: focus enable
1005: say ask_name
1006: listen guest_name_last
1007: say acknowledge_name_last
1008: focus disable
1009: go_to instruction_point
1010: say I have arrived at instruction_point
1011: focus enable
1012: say saved_name
1013: focus disable
1014: say task completed
```

run_id: `b7a96a95-a39e-4635-a339-66428917525b`

Decisión del investigador: **pendiente**. Observaciones: __________________

### Qwen7B — No verificable

Se solicita el nombre y se emite saved_name al regresar; falta establecer la persistencia y recuperación del dato entre esas acciones.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(bedroom)",
  "find(person, kind=person)",
  "save(name)",
  "go(instruction_point)",
  "tell(name)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to bedroom
2: say I will look for person
3: say I will save name
4: say I will navigate to instruction_point
5: say I will tell name
1001: go_to bedroom
1002: say I have arrived at bedroom
1003: find_person anybody
1004: focus enable
1005: say ask_name
1006: listen guest_name_last
1007: say acknowledge_name_last
1008: focus disable
1009: go_to instruction_point
1010: say I have arrived at instruction_point
1011: focus enable
1012: say saved_name
1013: focus disable
1014: say task completed
```

run_id: `f2bc978d-adc9-40e3-9ba7-5be068b4e6b8`

Decisión del investigador: **pendiente**. Observaciones: __________________

### GPT — No verificable

Se solicita el nombre y se emite saved_name al regresar; falta establecer la persistencia y recuperación del dato entre esas acciones.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(bedroom)",
  "find(person, kind=person)",
  "save(name)",
  "go(instruction_point)",
  "tell(name)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to bedroom
2: say I will look for person
3: say I will save the name
4: say I will navigate to instruction point
5: say I will tell name
1001: go_to bedroom
1002: say I have arrived at bedroom
1003: find_person anybody
1004: focus enable
1005: say ask_name
1006: listen guest_name_last
1007: say acknowledge_name_last
1008: focus disable
1009: go_to instruction_point
1010: say I have arrived at instruction point
1011: focus enable
1012: say saved_name
1013: focus disable
1014: say task completed
```

run_id: `26386b60-b69b-4055-9142-fb22ad257c20`

Decisión del investigador: **pendiente**. Observaciones: __________________

## DEV-038

**Orden:** Go to the bedroom, learn the name of a person there, then return and report it to me.

**Intención:** INT-13. **Bloque:** funcional_y_linguistico.

**Subtareas:**

- Encontrar una persona en bedroom y adquirir su nombre.
- Regresar al operador y comunicar el nombre adquirido.

**Restricciones:**

- No inventar el nombre ni confundirlo con un nombre fijo del catálogo.
- La comunicación al operador debe referirse a la información adquirida.

**Límites de verificación de la ficha:**

- La persistencia y recuperación de saved_name deben verificarse respecto del contrato del ejecutor.

### Qwen3B — No verificable

Se solicita el nombre y se emite saved_name al regresar; falta establecer la persistencia y recuperación del dato entre esas acciones.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(bedroom)",
  "find(person, kind=person)",
  "save(name)",
  "go(instruction_point)",
  "tell(name)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to bedroom
2: say I will look for person
3: say I will save name
4: say I will navigate to instruction_point
5: say I will tell name
1001: go_to bedroom
1002: say I have arrived at bedroom
1003: find_person anybody
1004: focus enable
1005: say ask_name
1006: listen guest_name_last
1007: say acknowledge_name_last
1008: focus disable
1009: go_to instruction_point
1010: say I have arrived at instruction_point
1011: focus enable
1012: say saved_name
1013: focus disable
1014: say task completed
```

run_id: `da41604b-717c-4efc-b882-c29a29559d75`

Decisión del investigador: **pendiente**. Observaciones: __________________

### Qwen7B — No verificable

Se solicita el nombre y se emite saved_name al regresar; falta establecer la persistencia y recuperación del dato entre esas acciones.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(bedroom)",
  "find(person, kind=person)",
  "save(name)",
  "go(instruction_point)",
  "tell(name)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to bedroom
2: say I will look for person
3: say I will save name
4: say I will navigate to instruction_point
5: say I will tell name
1001: go_to bedroom
1002: say I have arrived at bedroom
1003: find_person anybody
1004: focus enable
1005: say ask_name
1006: listen guest_name_last
1007: say acknowledge_name_last
1008: focus disable
1009: go_to instruction_point
1010: say I have arrived at instruction_point
1011: focus enable
1012: say saved_name
1013: focus disable
1014: say task completed
```

run_id: `25e1e51f-6544-4926-8cc7-c6a540eaf1a5`

Decisión del investigador: **pendiente**. Observaciones: __________________

### GPT — No verificable

Se solicita el nombre y se emite saved_name al regresar; falta establecer la persistencia y recuperación del dato entre esas acciones.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(bedroom)",
  "find(person, kind=person)",
  "save(name)",
  "go(instruction_point)",
  "tell(name)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to bedroom
2: say I will look for person
3: say I will save name
4: say I will navigate to instruction point
5: say I will tell name
1001: go_to bedroom
1002: say I have arrived at bedroom
1003: find_person anybody
1004: focus enable
1005: say ask_name
1006: listen guest_name_last
1007: say acknowledge_name_last
1008: focus disable
1009: go_to instruction_point
1010: say I have arrived at instruction point
1011: focus enable
1012: say saved_name
1013: focus disable
1014: say task completed
```

run_id: `378a4dfd-21e2-43c3-b553-dd97cc5e3d3b`

Decisión del investigador: **pendiente**. Observaciones: __________________

## DEV-039

**Orden:** please find a person in the bedroom ask their name and come back to tell me their name

**Intención:** INT-13. **Bloque:** funcional_y_linguistico.

**Subtareas:**

- Encontrar una persona en bedroom y adquirir su nombre.
- Regresar al operador y comunicar el nombre adquirido.

**Restricciones:**

- No inventar el nombre ni confundirlo con un nombre fijo del catálogo.
- La comunicación al operador debe referirse a la información adquirida.

**Límites de verificación de la ficha:**

- La persistencia y recuperación de saved_name deben verificarse respecto del contrato del ejecutor.

### Qwen3B — No verificable

Se solicita el nombre y se emite saved_name al regresar; falta establecer la persistencia y recuperación del dato entre esas acciones.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(bedroom)",
  "find(person, kind=person)",
  "save(name)",
  "go(instruction_point)",
  "tell(name)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to bedroom
2: say I will look for person
3: say I will save name
4: say I will navigate to instruction_point
5: say I will tell name
1001: go_to bedroom
1002: say I have arrived at bedroom
1003: find_person anybody
1004: focus enable
1005: say ask_name
1006: listen guest_name_last
1007: say acknowledge_name_last
1008: focus disable
1009: go_to instruction_point
1010: say I have arrived at instruction_point
1011: focus enable
1012: say saved_name
1013: focus disable
1014: say task completed
```

run_id: `70854928-d3e1-4020-aecc-f0a5e93e6074`

Decisión del investigador: **pendiente**. Observaciones: __________________

### Qwen7B — No verificable

Se solicita el nombre y se emite saved_name al regresar; falta establecer la persistencia y recuperación del dato entre esas acciones.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(bedroom)",
  "find(person, kind=person)",
  "save(name)",
  "go(instruction_point)",
  "tell(name)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to bedroom
2: say I will look for person
3: say I will save name
4: say I will navigate to instruction_point
5: say I will tell name
1001: go_to bedroom
1002: say I have arrived at bedroom
1003: find_person anybody
1004: focus enable
1005: say ask_name
1006: listen guest_name_last
1007: say acknowledge_name_last
1008: focus disable
1009: go_to instruction_point
1010: say I have arrived at instruction_point
1011: focus enable
1012: say saved_name
1013: focus disable
1014: say task completed
```

run_id: `49af957b-ed82-419c-8de7-537dd465d713`

Decisión del investigador: **pendiente**. Observaciones: __________________

### GPT — No verificable

Se solicita el nombre y se emite saved_name al regresar; falta establecer la persistencia y recuperación del dato entre esas acciones.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(bedroom)",
  "find(person, kind=person)",
  "save(name)",
  "go(instruction_point)",
  "tell(name)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to bedroom
2: say I will look for person
3: say I will save name
4: say I will navigate to instruction_point
5: say I will tell name
1001: go_to bedroom
1002: say I have arrived at bedroom
1003: find_person anybody
1004: focus enable
1005: say ask_name
1006: listen guest_name_last
1007: say acknowledge_name_last
1008: focus disable
1009: go_to instruction_point
1010: say I have arrived at instruction_point
1011: focus enable
1012: say saved_name
1013: focus disable
1014: say task completed
```

run_id: `a4af5ade-2688-45ea-8bdc-99dff6dddc60`

Decisión del investigador: **pendiente**. Observaciones: __________________

## DEV-040

**Orden:** Find the waving person in the corridor and answer their question.

**Intención:** INT-14. **Bloque:** funcional_y_linguistico.

**Subtareas:**

- Localizar en corridor a la persona que saluda con la mano.
- Escuchar su pregunta y solicitar la respuesta.

**Restricciones:**

- Conservar el contexto de esa persona.
- No inventar la pregunta ni una respuesta concreta en el plan.

**Límites de verificación de la ficha:**


### Qwen3B — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(corridor)",
  "find(person, kind=person, gesture='waving person')",
  "answer_question()"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to corridor
2: say I will look for person waving_person
3: say I will answer the question
1001: go_to corridor
1002: say I have arrived at corridor
1003: find_pose waving_1
1004: approach customer_1
1005: focus enable
1006: listen answer_question
1007: say answer_question
1008: focus disable
1009: go_to instruction_point
1010: say task completed
```

run_id: `b32e5823-737e-46ee-b6be-279ca4befd1f`

Decisión del investigador: **pendiente**. Observaciones: __________________

### Qwen7B — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(corridor)",
  "find(person, kind=person, gesture='waving person')",
  "answer_question()"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to corridor
2: say I will look for person waving_person
3: say I will answer the question
1001: go_to corridor
1002: say I have arrived at corridor
1003: find_pose waving_1
1004: approach customer_1
1005: focus enable
1006: listen answer_question
1007: say answer_question
1008: focus disable
1009: go_to instruction_point
1010: say task completed
```

run_id: `f86446ba-2d9b-4a58-a32c-36ebc402aed7`

Decisión del investigador: **pendiente**. Observaciones: __________________

### GPT — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(corridor)",
  "find(person, kind=person, gesture='waving person')",
  "answer_question()"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to corridor
2: say I will look for person waving person
3: say I will answer the question
1001: go_to corridor
1002: say I have arrived at corridor
1003: find_pose waving_1
1004: approach customer_1
1005: focus enable
1006: listen answer_question
1007: say answer_question
1008: focus disable
1009: go_to instruction_point
1010: say task completed
```

run_id: `3a0af930-104a-4066-bb2c-5e7d93698c05`

Decisión del investigador: **pendiente**. Observaciones: __________________

## DEV-041

**Orden:** In the corridor, locate the person who is waving and respond to that person's question.

**Intención:** INT-14. **Bloque:** funcional_y_linguistico.

**Subtareas:**

- Localizar en corridor a la persona que saluda con la mano.
- Escuchar su pregunta y solicitar la respuesta.

**Restricciones:**

- Conservar el contexto de esa persona.
- No inventar la pregunta ni una respuesta concreta en el plan.

**Límites de verificación de la ficha:**


### Qwen3B — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(corridor)",
  "find(person, kind=person, gesture='person who is waving')",
  "answer_question()"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to corridor
2: say I will look for person person_who_is_waving
3: say I will answer the question
1001: go_to corridor
1002: say I have arrived at corridor
1003: find_pose waving_1
1004: approach customer_1
1005: focus enable
1006: listen answer_question
1007: say answer_question
1008: focus disable
1009: go_to instruction_point
1010: say task completed
```

run_id: `bf731e00-2d6b-4a9a-bffc-0229167d8818`

Decisión del investigador: **pendiente**. Observaciones: __________________

### Qwen7B — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(corridor)",
  "find(person, kind=person, gesture='waving person')",
  "answer_question()"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to corridor
2: say I will look for person waving_person
3: say I will answer the question
1001: go_to corridor
1002: say I have arrived at corridor
1003: find_pose waving_1
1004: approach customer_1
1005: focus enable
1006: listen answer_question
1007: say answer_question
1008: focus disable
1009: go_to instruction_point
1010: say task completed
```

run_id: `2cd9c0bc-54cf-410f-8632-c067fe4a9925`

Decisión del investigador: **pendiente**. Observaciones: __________________

### GPT — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(corridor)",
  "find(person, kind=person, gesture='waving person')",
  "answer_question()"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to corridor
2: say I will look for person waving person
3: say I will answer the question
1001: go_to corridor
1002: say I have arrived at corridor
1003: find_pose waving_1
1004: approach customer_1
1005: focus enable
1006: listen answer_question
1007: say answer_question
1008: focus disable
1009: go_to instruction_point
1010: say task completed
```

run_id: `4ea32bdb-fd0e-4d23-9873-1ac24efd126a`

Decisión del investigador: **pendiente**. Observaciones: __________________

## DEV-042

**Orden:** find the waving person in the corridor and and answer their question please

**Intención:** INT-14. **Bloque:** funcional_y_linguistico.

**Subtareas:**

- Localizar en corridor a la persona que saluda con la mano.
- Escuchar su pregunta y solicitar la respuesta.

**Restricciones:**

- Conservar el contexto de esa persona.
- No inventar la pregunta ni una respuesta concreta en el plan.

**Límites de verificación de la ficha:**


### Qwen3B — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(corridor)",
  "find(person, kind=person, gesture='waving person')",
  "answer_question()"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to corridor
2: say I will look for person waving_person
3: say I will answer the question
1001: go_to corridor
1002: say I have arrived at corridor
1003: find_pose waving_1
1004: approach customer_1
1005: focus enable
1006: listen answer_question
1007: say answer_question
1008: focus disable
1009: go_to instruction_point
1010: say task completed
```

run_id: `b3e07a37-591f-47b9-9efb-4b74ee195948`

Decisión del investigador: **pendiente**. Observaciones: __________________

### Qwen7B — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(corridor)",
  "find(person, kind=person, gesture='waving person')",
  "answer_question()"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to corridor
2: say I will look for person waving_person
3: say I will answer the question
1001: go_to corridor
1002: say I have arrived at corridor
1003: find_pose waving_1
1004: approach customer_1
1005: focus enable
1006: listen answer_question
1007: say answer_question
1008: focus disable
1009: go_to instruction_point
1010: say task completed
```

run_id: `840ce262-e6bd-4b5a-b735-ba037603b934`

Decisión del investigador: **pendiente**. Observaciones: __________________

### GPT — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(corridor)",
  "find(person, kind=person, gesture='waving person')",
  "answer_question()"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to corridor
2: say I will look for person waving person
3: say I will answer the question
1001: go_to corridor
1002: say I have arrived at corridor
1003: find_pose waving_1
1004: approach customer_1
1005: focus enable
1006: listen answer_question
1007: say answer_question
1008: focus disable
1009: go_to instruction_point
1010: say task completed
```

run_id: `120ba494-5038-473c-9fbc-472ddf2facc9`

Decisión del investigador: **pendiente**. Observaciones: __________________

## DEV-043

**Orden:** Find Jane in the kitchen and greet her.

**Intención:** INT-15. **Bloque:** funcional_y_linguistico.

**Subtareas:**

- Localizar a Jane en kitchen y saludarla.

**Restricciones:**

- Resolver her como Jane; no saludar al operador ni a una persona distinta.

**Límites de verificación de la ficha:**

- La identificación por nombre debe distinguirse de la búsqueda de una persona cualquiera.

### Qwen3B — No verificable

Se localiza una persona y se saluda a guest_last; la identificación efectiva como Jane no está acreditada por el plan.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(kitchen)",
  "find(Jane, kind=person)",
  "greet(Jane)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to kitchen
2: say I will look for Jane
3: say I will greet Jane
1001: go_to kitchen
1002: say I have arrived at kitchen
1003: find_person anybody
1004: focus enable
1005: say ask_name
1006: listen guest_name_last
1007: say acknowledge_name_last
1008: focus disable
1009: approach guest_last
1010: focus enable
1011: say greet
1012: focus disable
1013: go_to instruction_point
1014: say task completed
```

run_id: `ea8f69b5-f726-42af-bc5d-6db42ac03ef1`

Decisión del investigador: **pendiente**. Observaciones: __________________

### Qwen7B — No verificable

Se localiza una persona y se saluda a guest_last; la identificación efectiva como Jane no está acreditada por el plan.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(kitchen)",
  "find(Jane, kind=person)",
  "greet(Jane)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to kitchen
2: say I will look for Jane
3: say I will greet Jane
1001: go_to kitchen
1002: say I have arrived at kitchen
1003: find_person anybody
1004: focus enable
1005: say ask_name
1006: listen guest_name_last
1007: say acknowledge_name_last
1008: focus disable
1009: approach guest_last
1010: focus enable
1011: say greet
1012: focus disable
1013: go_to instruction_point
1014: say task completed
```

run_id: `ee134944-dcc5-498e-adc1-9cf38be4a944`

Decisión del investigador: **pendiente**. Observaciones: __________________

### GPT — No verificable

Se localiza una persona y se saluda a guest_last; la identificación efectiva como Jane no está acreditada por el plan.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(kitchen)",
  "find(Jane, kind=person)",
  "greet(Jane)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to kitchen
2: say I will look for Jane
3: say I will greet Jane
1001: go_to kitchen
1002: say I have arrived at kitchen
1003: find_person anybody
1004: focus enable
1005: say ask_name
1006: listen guest_name_last
1007: say acknowledge_name_last
1008: focus disable
1009: approach guest_last
1010: focus enable
1011: say greet
1012: focus disable
1013: go_to instruction_point
1014: say task completed
```

run_id: `42eefc95-7880-4544-a0c9-02734ad27b1a`

Decisión del investigador: **pendiente**. Observaciones: __________________

## DEV-044

**Orden:** Look for Jane in the kitchen and say hello to Jane.

**Intención:** INT-15. **Bloque:** funcional_y_linguistico.

**Subtareas:**

- Localizar a Jane en kitchen y saludarla.

**Restricciones:**

- Resolver her como Jane; no saludar al operador ni a una persona distinta.

**Límites de verificación de la ficha:**

- La identificación por nombre debe distinguirse de la búsqueda de una persona cualquiera.

### Qwen3B — No verificable

Se localiza una persona y se saluda a guest_last; la identificación efectiva como Jane no está acreditada por el plan.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(kitchen)",
  "find(Jane, kind=person)",
  "greet(Jane)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to kitchen
2: say I will look for Jane
3: say I will greet Jane
1001: go_to kitchen
1002: say I have arrived at kitchen
1003: find_person anybody
1004: focus enable
1005: say ask_name
1006: listen guest_name_last
1007: say acknowledge_name_last
1008: focus disable
1009: approach guest_last
1010: focus enable
1011: say greet
1012: focus disable
1013: go_to instruction_point
1014: say task completed
```

run_id: `c9db8fe1-c739-4356-b491-22e0b5724a3b`

Decisión del investigador: **pendiente**. Observaciones: __________________

### Qwen7B — No verificable

Se localiza una persona y se saluda a guest_last; la identificación efectiva como Jane no está acreditada por el plan.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(kitchen)",
  "find(Jane, kind=person)",
  "greet(Jane)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to kitchen
2: say I will look for Jane
3: say I will greet Jane
1001: go_to kitchen
1002: say I have arrived at kitchen
1003: find_person anybody
1004: focus enable
1005: say ask_name
1006: listen guest_name_last
1007: say acknowledge_name_last
1008: focus disable
1009: approach guest_last
1010: focus enable
1011: say greet
1012: focus disable
1013: go_to instruction_point
1014: say task completed
```

run_id: `a2c3b72c-5aa0-4535-abdf-339216db28b3`

Decisión del investigador: **pendiente**. Observaciones: __________________

### GPT — No verificable

Se localiza una persona y se saluda a guest_last; la identificación efectiva como Jane no está acreditada por el plan.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(kitchen)",
  "find(Jane, kind=person)",
  "greet(Jane)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to kitchen
2: say I will look for Jane
3: say I will greet Jane
1001: go_to kitchen
1002: say I have arrived at kitchen
1003: find_person anybody
1004: focus enable
1005: say ask_name
1006: listen guest_name_last
1007: say acknowledge_name_last
1008: focus disable
1009: approach guest_last
1010: focus enable
1011: say greet
1012: focus disable
1013: go_to instruction_point
1014: say task completed
```

run_id: `6554baaa-2487-41a6-aa3f-c43afd2e86c2`

Decisión del investigador: **pendiente**. Observaciones: __________________

## DEV-045

**Orden:** please find Jane in the kichen and greet her

**Intención:** INT-15. **Bloque:** funcional_y_linguistico.

**Subtareas:**

- Localizar a Jane en kitchen y saludarla.

**Restricciones:**

- Resolver her como Jane; no saludar al operador ni a una persona distinta.

**Límites de verificación de la ficha:**

- La identificación por nombre debe distinguirse de la búsqueda de una persona cualquiera.

### Qwen3B — No verificable

Se localiza una persona y se saluda a guest_last; la identificación efectiva como Jane no está acreditada por el plan.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(kitchen)",
  "find(Jane, kind=person)",
  "greet(Jane)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to kitchen
2: say I will look for Jane
3: say I will greet Jane
1001: go_to kitchen
1002: say I have arrived at kitchen
1003: find_person anybody
1004: focus enable
1005: say ask_name
1006: listen guest_name_last
1007: say acknowledge_name_last
1008: focus disable
1009: approach guest_last
1010: focus enable
1011: say greet
1012: focus disable
1013: go_to instruction_point
1014: say task completed
```

run_id: `cb1d3bde-0010-4d3f-95c5-937fc67a3381`

Decisión del investigador: **pendiente**. Observaciones: __________________

### Qwen7B — No verificable

Se localiza una persona y se saluda a guest_last; la identificación efectiva como Jane no está acreditada por el plan.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(kitchen)",
  "find(Jane, kind=person)",
  "greet(Jane)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to kitchen
2: say I will look for Jane
3: say I will greet Jane
1001: go_to kitchen
1002: say I have arrived at kitchen
1003: find_person anybody
1004: focus enable
1005: say ask_name
1006: listen guest_name_last
1007: say acknowledge_name_last
1008: focus disable
1009: approach guest_last
1010: focus enable
1011: say greet
1012: focus disable
1013: go_to instruction_point
1014: say task completed
```

run_id: `7ed3d7c6-3728-4291-91e0-e583ef4d1435`

Decisión del investigador: **pendiente**. Observaciones: __________________

### GPT — No verificable

Se localiza una persona y se saluda a guest_last; la identificación efectiva como Jane no está acreditada por el plan.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(kitchen)",
  "find(Jane, kind=person)",
  "greet(Jane)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to kitchen
2: say I will look for Jane
3: say I will greet Jane
1001: go_to kitchen
1002: say I have arrived at kitchen
1003: find_person anybody
1004: focus enable
1005: say ask_name
1006: listen guest_name_last
1007: say acknowledge_name_last
1008: focus disable
1009: approach guest_last
1010: focus enable
1011: say greet
1012: focus disable
1013: go_to instruction_point
1014: say task completed
```

run_id: `db74418a-0c74-4ce2-bebb-037ac43581a0`

Decisión del investigador: **pendiente**. Observaciones: __________________

## DEV-046

**Orden:** Tell me which is the largest fruit on the sofa.

**Intención:** INT-16. **Bloque:** funcional_y_linguistico.

**Subtareas:**

- Analizar el tamaño de las frutas en sofa y comunicar cuál es la mayor.

**Restricciones:**

- No sustituir tamaño por peso ni buscar un objeto arbitrario.
- biggest y largest son equivalentes semánticos aquí; registrar diferencia literal sin penalizar semántica.

**Límites de verificación de la ficha:**


### Qwen3B — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(sofa)",
  "find(fruit, kind=object, property=largest)",
  "tell(fruit,property=largest)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to sofa
2: say I will search for the largest fruit
3: say I will report the largest fruit
1001: go_to sofa
1002: say I have arrived at sofa
1003: analyze_objects biggest_fruit
1004: say biggest_category
1005: go_to instruction_point
1006: say task completed
```

run_id: `d07751a0-8153-4c5f-9a65-75c2967da325`

Decisión del investigador: **pendiente**. Observaciones: __________________

### Qwen7B — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(sofa)",
  "find(fruit, kind=object, property=largest)",
  "tell(fruit,property=largest)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to sofa
2: say I will search for the largest fruit
3: say I will report the largest fruit
1001: go_to sofa
1002: say I have arrived at sofa
1003: analyze_objects biggest_fruit
1004: say biggest_category
1005: go_to instruction_point
1006: say task completed
```

run_id: `bb908935-1289-465d-942e-c3f6ff11a67d`

Decisión del investigador: **pendiente**. Observaciones: __________________

### GPT — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(sofa)",
  "find(fruit, kind=object, property=largest)",
  "tell(fruit, property=largest)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to sofa
2: say I will search for the largest fruit
3: say I will report the largest fruit
1001: go_to sofa
1002: say I have arrived at sofa
1003: analyze_objects biggest_fruit
1004: say biggest_category
1005: go_to instruction_point
1006: say task completed
```

run_id: `829b25cc-6af1-43ab-9d5f-cf43fc59daa7`

Decisión del investigador: **pendiente**. Observaciones: __________________

## DEV-047

**Orden:** Identify the biggest fruit on the sofa and report which one it is.

**Intención:** INT-16. **Bloque:** funcional_y_linguistico.

**Subtareas:**

- Analizar el tamaño de las frutas en sofa y comunicar cuál es la mayor.

**Restricciones:**

- No sustituir tamaño por peso ni buscar un objeto arbitrario.
- biggest y largest son equivalentes semánticos aquí; registrar diferencia literal sin penalizar semántica.

**Límites de verificación de la ficha:**


### Qwen3B — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(sofa)",
  "find(fruit, kind=object, property=biggest)",
  "tell(fruit,property=biggest)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to sofa
2: say I will search for the biggest fruit
3: say I will report the biggest fruit
1001: go_to sofa
1002: say I have arrived at sofa
1003: analyze_objects biggest_fruit
1004: say biggest_category
1005: go_to instruction_point
1006: say task completed
```

run_id: `fca6b26b-e999-47cc-b55a-d6de82f4dfa8`

Decisión del investigador: **pendiente**. Observaciones: __________________

### Qwen7B — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(sofa)",
  "find(fruit, kind=object, property=biggest)",
  "tell(fruit,property=biggest)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to sofa
2: say I will search for the biggest fruit
3: say I will report the biggest fruit
1001: go_to sofa
1002: say I have arrived at sofa
1003: analyze_objects biggest_fruit
1004: say biggest_category
1005: go_to instruction_point
1006: say task completed
```

run_id: `d319d446-3b39-44ae-a1b3-4e783d5b7885`

Decisión del investigador: **pendiente**. Observaciones: __________________

### GPT — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(sofa)",
  "find(fruit, kind=object, property=biggest)",
  "tell(fruit, property=biggest)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to sofa
2: say I will search for the biggest fruit
3: say I will report the biggest fruit
1001: go_to sofa
1002: say I have arrived at sofa
1003: analyze_objects biggest_fruit
1004: say biggest_category
1005: go_to instruction_point
1006: say task completed
```

run_id: `beec9d89-d077-41bd-89ca-77ba2af5fee1`

Decisión del investigador: **pendiente**. Observaciones: __________________

## DEV-048

**Orden:** please tell me which is the largest fruit on the sofa

**Intención:** INT-16. **Bloque:** funcional_y_linguistico.

**Subtareas:**

- Analizar el tamaño de las frutas en sofa y comunicar cuál es la mayor.

**Restricciones:**

- No sustituir tamaño por peso ni buscar un objeto arbitrario.
- biggest y largest son equivalentes semánticos aquí; registrar diferencia literal sin penalizar semántica.

**Límites de verificación de la ficha:**


### Qwen3B — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(sofa)",
  "find(fruit, kind=object, property=largest)",
  "tell(fruit,property=largest)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to sofa
2: say I will search for the largest fruit
3: say I will report the largest fruit
1001: go_to sofa
1002: say I have arrived at sofa
1003: analyze_objects biggest_fruit
1004: say biggest_category
1005: go_to instruction_point
1006: say task completed
```

run_id: `06e542c5-592b-479e-9979-09692d4ce614`

Decisión del investigador: **pendiente**. Observaciones: __________________

### Qwen7B — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(sofa)",
  "find(fruit, kind=object, property=largest)",
  "tell(fruit,property=largest)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to sofa
2: say I will search for the largest fruit
3: say I will report the largest fruit
1001: go_to sofa
1002: say I have arrived at sofa
1003: analyze_objects biggest_fruit
1004: say biggest_category
1005: go_to instruction_point
1006: say task completed
```

run_id: `166686ae-ac89-42cc-b5a8-b2b586b4d400`

Decisión del investigador: **pendiente**. Observaciones: __________________

### GPT — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(sofa)",
  "find(fruit, kind=object, property=largest)",
  "tell(fruit, property=largest)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to sofa
2: say I will search for the largest fruit
3: say I will report the largest fruit
1001: go_to sofa
1002: say I have arrived at sofa
1003: analyze_objects biggest_fruit
1004: say biggest_category
1005: go_to instruction_point
1006: say task completed
```

run_id: `6f7ae271-15d9-4527-a00e-155339515530`

Decisión del investigador: **pendiente**. Observaciones: __________________

## DEV-049

**Orden:** Find the person waving and wearing a blue coat in the office, then guide them to the entrance.

**Intención:** INT-17. **Bloque:** limites_y_composicion.

**Subtareas:**

- Buscar en office una única persona que cumpla ambos atributos.
- Guiar a esa persona a entrance.

**Restricciones:**

- La conjunción gesto y vestimenta debe mantenerse; no basta con cualquiera de ellos.

**Límites de verificación de la ficha:**

- El adaptador conserva un único qualifier y puede perder un atributo; registrar la pérdida.

### Qwen3B — Incumple

No se representa la conjunción con ambos campos de búsqueda utilizables; el plan solo verifica el gesto y no el abrigo azul.

Interpretación propuesta: `False`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(office)",
  "find(person, kind=person, gesture='person waving, wearing a blue coat')",
  "guide(person, to=entrance)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to office
2: say I will look for person person_waving,_wearing_a_blue_coat
3: say I will guide person to entrance
1001: go_to office
1002: say I have arrived at office
1003: find_pose waving_1
1004: approach customer_1
1005: focus enable
1006: say Please follow me to entrance
1007: focus disable
1008: go_to entrance
1009: say I have guided person to entrance
1010: go_to instruction_point
1011: say task completed
```

run_id: `a1f7f368-e2e2-4a74-8bc0-ad84cea4d006`

Decisión del investigador: **pendiente**. Observaciones: __________________

### Qwen7B — Incumple

No se representa la conjunción con ambos campos de búsqueda utilizables; el plan solo verifica el gesto y no el abrigo azul.

Interpretación propuesta: `False`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(office)",
  "find(person, kind=person, gesture='waving person')",
  "guide(person, to=entrance)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to office
2: say I will look for person waving_person
3: say I will guide person to entrance
1001: go_to office
1002: say I have arrived at office
1003: find_pose waving_1
1004: approach customer_1
1005: focus enable
1006: say Please follow me to entrance
1007: focus disable
1008: go_to entrance
1009: say I have guided person to entrance
1010: go_to instruction_point
1011: say task completed
```

run_id: `8628e5cf-0806-415c-8fbc-6a90a1d82777`

Decisión del investigador: **pendiente**. Observaciones: __________________

### GPT — Incumple

Rechazo explícito por límite de capacidad. No realiza la tarea que la ficha aprobada describe como executable; no se atribuye fallo lingüístico ni plan incorrecto.

Interpretación propuesta: `None`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
Combined gesture and clothing person searches are unsupported by the executor.
```

run_id: `d4d8dd5d-45c3-45d7-8f3b-06f83b4d5a0b`

Decisión del investigador: **pendiente**. Observaciones: __________________

## DEV-050

**Orden:** Count the people wearing red shirts in the living room.

**Intención:** INT-18. **Bloque:** limites_y_composicion.

**Subtareas:**

- Contar exclusivamente las personas con camisa roja en living room.
- Comunicar el resultado al operador.

**Restricciones:**

- El plan debe conservar el filtro de vestimenta; un conteo de todas las personas no cumple.

**Límites de verificación de la ficha:**

- La expansión actual de count puede omitir el filtro; comprobarlo sin equiparar planificabilidad con cumplimiento.

### Qwen3B — Incumple

La interpretación conserva el filtro rojo, pero el plan solo ejecuta count_person y no expresa un conteo filtrado. La ficha prohíbe contar todas las personas como sustituto.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(living room)",
  "count(person, kind=person, wearing='red shirt')"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to living_room
2: say I will count person_wearing:red_shirt
3: say I will return to the instruction point to report the count
1001: go_to living_room
1002: say I have arrived at living_room
1003: analyze_objects count_person
1004: go_to instruction_point
1005: focus enable
1006: say count_category
1007: focus disable
1008: say task completed
```

run_id: `0b08e302-5ddb-491e-8f38-573987ff36af`

Decisión del investigador: **pendiente**. Observaciones: __________________

### Qwen7B — Incumple

La interpretación conserva el filtro rojo, pero el plan solo ejecuta count_person y no expresa un conteo filtrado. La ficha prohíbe contar todas las personas como sustituto.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(living room)",
  "count(person, kind=person, wearing='red shirt')"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to living_room
2: say I will count person_wearing:red_shirt
3: say I will return to the instruction point to report the count
1001: go_to living_room
1002: say I have arrived at living_room
1003: analyze_objects count_person
1004: go_to instruction_point
1005: focus enable
1006: say count_category
1007: focus disable
1008: say task completed
```

run_id: `be0f9eeb-3abb-4662-8b9f-5452ed42865e`

Decisión del investigador: **pendiente**. Observaciones: __________________

### GPT — Incumple

La interpretación conserva el filtro rojo, pero el plan solo ejecuta count_person y no expresa un conteo filtrado. La ficha prohíbe contar todas las personas como sustituto.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(living room)",
  "count(person, kind=person, wearing='red shirts')"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to living room
2: say I will count person wearing red shirts
3: say I will return to the instruction point to report the count
1001: go_to living_room
1002: say I have arrived at living room
1003: analyze_objects count_person
1004: go_to instruction_point
1005: focus enable
1006: say count_category
1007: focus disable
1008: say task completed
```

run_id: `1a7a523c-a1c8-41f7-a268-bfc1595582f3`

Decisión del investigador: **pendiente**. Observaciones: __________________

## DEV-051

**Orden:** Tell me which is the heaviest fruit on the sofa.

**Intención:** INT-19. **Bloque:** limites_y_composicion.

**Subtareas:**

- Determinar qué fruta tiene mayor peso en sofa y comunicarlo.

**Restricciones:**

- No sustituir peso por tamaño.

**Límites de verificación de la ficha:**

- heaviest pertenece al vocabulario pero la expansión usa tamaño como aproximación; clasificar proxy_insuficiente si no existe evidencia del peso. No exigir un plan exitoso cuando el repertorio no permite satisfacerlo.

### Qwen3B — Incumple

Interpreta heaviest, pero sustituye la medición de peso por biggest_fruit. Es una incompatibilidad explícita con la restricción «No sustituir peso por tamaño», no mera ausencia de prueba física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(sofa)",
  "find(fruit, kind=object, property=heaviest)",
  "tell(fruit,property=heaviest)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to sofa
2: say I will search for the heaviest fruit
3: say I will report the heaviest fruit
1001: go_to sofa
1002: say I have arrived at sofa
1003: analyze_objects biggest_fruit
1004: say heaviest_category
1005: go_to instruction_point
1006: say task completed
```

run_id: `c9258a8c-45f8-48c6-ab7f-58f9306d30c8`

Decisión del investigador: **pendiente**. Observaciones: __________________

### Qwen7B — Incumple

Interpreta heaviest, pero sustituye la medición de peso por biggest_fruit. Es una incompatibilidad explícita con la restricción «No sustituir peso por tamaño», no mera ausencia de prueba física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(sofa)",
  "find(fruit, kind=object, property=heaviest)",
  "tell(fruit,property=heaviest)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to sofa
2: say I will search for the heaviest fruit
3: say I will report the heaviest fruit
1001: go_to sofa
1002: say I have arrived at sofa
1003: analyze_objects biggest_fruit
1004: say heaviest_category
1005: go_to instruction_point
1006: say task completed
```

run_id: `ef578cb6-0a05-4d14-a1b5-a0bffc70af11`

Decisión del investigador: **pendiente**. Observaciones: __________________

### GPT — Incumple

Interpreta heaviest, pero sustituye la medición de peso por biggest_fruit. Es una incompatibilidad explícita con la restricción «No sustituir peso por tamaño», no mera ausencia de prueba física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(sofa)",
  "find(fruit, kind=object, property=heaviest)",
  "tell(fruit, property=heaviest)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to sofa
2: say I will search for the heaviest fruit
3: say I will report the heaviest fruit
1001: go_to sofa
1002: say I have arrived at sofa
1003: analyze_objects biggest_fruit
1004: say heaviest_category
1005: go_to instruction_point
1006: say task completed
```

run_id: `d7e90095-3dc2-44ac-831c-eb5b2719be62`

Decisión del investigador: **pendiente**. Observaciones: __________________

## DEV-052

**Orden:** Find Simone at the coatrack and follow Simone to the bedroom.

**Intención:** INT-20. **Bloque:** limites_y_composicion.

**Subtareas:**

- Localizar a Simone en coatrack.
- Seguir a Simone hasta bedroom.

**Restricciones:**

- No convertir seguimiento en guía.
- No ir solo a bedroom antes de localizar a Simone.

**Límites de verificación de la ficha:**

- El protocolo instruct_follow_to requiere precisar los efectos del ejecutor; un anuncio no acredita llegar siguiendo a Simone.

### Qwen3B — No verificable

Se emite instruct_follow_to_bedroom, pero sus efectos de seguimiento y la identidad Simone dependen de un contrato aún no precisado.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(coatrack)",
  "find(Simone, kind=person)",
  "follow(Simone, to=bedroom)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to coatrack
2: say I will look for Simone
3: say I will follow Simone to bedroom
1001: go_to coatrack
1002: say I have arrived at coatrack
1003: find_person anybody
1004: focus enable
1005: say ask_name
1006: listen guest_name_last
1007: say acknowledge_name_last
1008: focus disable
1009: approach guest_last
1010: focus enable
1011: say I will follow Simone to bedroom
1012: say instruct_follow_to_bedroom
1013: focus disable
1014: go_to instruction_point
1015: say task completed
```

run_id: `d0e03872-a2bd-4745-b8f3-ba11b0e942b2`

Decisión del investigador: **pendiente**. Observaciones: __________________

### Qwen7B — No verificable

Se emite instruct_follow_to_bedroom, pero sus efectos de seguimiento y la identidad Simone dependen de un contrato aún no precisado.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(coatrack)",
  "find(Simone, kind=person)",
  "follow(Simone, to=bedroom)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to coatrack
2: say I will look for Simone
3: say I will follow Simone to bedroom
1001: go_to coatrack
1002: say I have arrived at coatrack
1003: find_person anybody
1004: focus enable
1005: say ask_name
1006: listen guest_name_last
1007: say acknowledge_name_last
1008: focus disable
1009: approach guest_last
1010: focus enable
1011: say I will follow Simone to bedroom
1012: say instruct_follow_to_bedroom
1013: focus disable
1014: go_to instruction_point
1015: say task completed
```

run_id: `0cd8bffd-066d-4312-99cc-ce618c2593b8`

Decisión del investigador: **pendiente**. Observaciones: __________________

### GPT — Incumple

Solo anuncia I will follow Simone to bedroom; omite instruct_follow_to_bedroom y regresa al operador. Falta el elemento de protocolo, aun antes de verificar sus efectos.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(coatrack)",
  "find(Simone, kind=person)",
  "follow(Simone, to=bedroom)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to coatrack
2: say I will look for Simone
3: say I will follow Simone to bedroom
1001: go_to coatrack
1002: say I have arrived at coatrack
1003: find_person anybody
1004: focus enable
1005: say ask_name
1006: listen guest_name_last
1007: say acknowledge_name_last
1008: focus disable
1009: approach guest_last
1010: focus enable
1011: say I will follow Simone to bedroom
1012: focus disable
1013: go_to instruction_point
1014: say task completed
```

run_id: `3a8abcf9-f51f-40bb-b844-bad304f0bba9`

Decisión del investigador: **pendiente**. Observaciones: __________________

## DEV-053

**Orden:** Bring me a mug from the refrigerator, then bring me a spoon from the bed.

**Intención:** INT-21. **Bloque:** limites_y_composicion.

**Subtareas:**

- Entregar al operador mug desde refrigerator.
- Después entregar al operador spoon desde bed.

**Restricciones:**

- Completar la primera entrega antes de buscar el segundo objeto.
- Reiniciar la posesión tras cada entrega; no reutilizar el identificador de mug para spoon.

**Límites de verificación de la ficha:**

- Caso para comprobar truncamiento por límite de tokens, conservación de orden y reinicio del estado de posesión.

### Qwen3B — Incumple

Coloca mug en bed en vez de entregarla al operador; la segunda entrega no compensa la primera omitida.

Interpretación propuesta: `False`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(refrigerator)",
  "find(mug, kind=object)",
  "take(mug)",
  "place(mug, at=bed)",
  "go(bed)",
  "find(spoon, kind=object)",
  "take(spoon)",
  "deliver(spoon, to=me)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to refrigerator
2: say I will search for mug
3: say I will pick up mug
4: say I will navigate to bed
5: say I will place mug at bed
6: say I will search for spoon
7: say I will pick up spoon
8: say I will return to the instruction point
9: say I will deliver spoon to you
1001: go_to refrigerator
1002: say I have arrived at refrigerator
1003: find_object mug_1
1004: take mug_1
1005: say I have picked up mug
1006: go_to bed
1007: find_space table
1008: drop mug_1
1009: say I have placed mug
1010: find_object spoon_1
1011: take spoon_1
1012: say I have picked up spoon
1013: go_to instruction_point
1014: approach host_1
1015: give spoon_1
1016: say I have delivered spoon
1017: say task completed
```

run_id: `67e05529-becb-4e08-8849-fb894b11e160`

Decisión del investigador: **pendiente**. Observaciones: __________________

### Qwen7B — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(refrigerator)",
  "find(mug, kind=object)",
  "take(mug)",
  "deliver(mug, to=me)",
  "go(bed)",
  "find(spoon, kind=object)",
  "take(spoon)",
  "deliver(spoon, to=me)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to refrigerator
2: say I will search for mug
3: say I will pick up mug
4: say I will return to the instruction point
5: say I will deliver mug to you
6: say I will navigate to bed
7: say I will search for spoon
8: say I will pick up spoon
9: say I will return to the instruction point
10: say I will deliver spoon to you
1001: go_to refrigerator
1002: say I have arrived at refrigerator
1003: find_object mug_1
1004: take mug_1
1005: say I have picked up mug
1006: go_to instruction_point
1007: approach host_1
1008: give mug_1
1009: say I have delivered mug
1010: go_to bed
1011: say I have arrived at bed
1012: find_object spoon_1
1013: take spoon_1
1014: say I have picked up spoon
1015: go_to instruction_point
1016: approach host_1
1017: give spoon_1
1018: say I have delivered spoon
1019: say task completed
```

run_id: `58064304-5794-4a6d-960d-a2117decffc9`

Decisión del investigador: **pendiente**. Observaciones: __________________

### GPT — Cumple simbólico

La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(refrigerator)",
  "find(mug, kind=object)",
  "take(mug)",
  "deliver(mug, to=me)",
  "go(bed)",
  "find(spoon, kind=object)",
  "take(spoon)",
  "deliver(spoon, to=me)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to refrigerator
2: say I will search for mug
3: say I will pick up mug
4: say I will return to the instruction point
5: say I will deliver mug to you
6: say I will navigate to bed
7: say I will search for spoon
8: say I will pick up spoon
9: say I will return to the instruction point
10: say I will deliver spoon to you
1001: go_to refrigerator
1002: say I have arrived at refrigerator
1003: find_object mug_1
1004: take mug_1
1005: say I have picked up mug
1006: go_to instruction_point
1007: approach host_1
1008: give mug_1
1009: say I have delivered mug
1010: go_to bed
1011: say I have arrived at bed
1012: find_object spoon_1
1013: take spoon_1
1014: say I have picked up spoon
1015: go_to instruction_point
1016: approach host_1
1017: give spoon_1
1018: say I have delivered spoon
1019: say task completed
```

run_id: `f825fc63-128a-4c1f-b858-7dff892b820c`

Decisión del investigador: **pendiente**. Observaciones: __________________

## DEV-054

**Orden:** Find Water in the kitchen, take it, and bring it to me.

**Intención:** INT-22. **Bloque:** limites_y_composicion.

**Subtareas:**

- Buscar y adquirir el objeto Water en kitchen.
- Entregarlo al operador.

**Restricciones:**

- La mayúscula de Water no debe convertir el objeto en una persona.

**Límites de verificación de la ficha:**

- Examinar la predicción original y el kind calculado por el adaptador por separado.

### Qwen3B — Cumple simbólico

Conserva Water como objeto y lo entrega al operador; la diferencia de capitalización no cambia el referente. No reproduce el defecto del control que lo trata como persona.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(kitchen)",
  "find(water, kind=object)",
  "take(water)",
  "deliver(water, to=me)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to kitchen
2: say I will search for water
3: say I will pick up water
4: say I will return to the instruction point
5: say I will deliver water to you
1001: go_to kitchen
1002: say I have arrived at kitchen
1003: find_object water_1
1004: take water_1
1005: say I have picked up water
1006: go_to instruction_point
1007: approach host_1
1008: give water_1
1009: say I have delivered water
1010: say task completed
```

run_id: `0c0f0bc2-848f-43b2-b7a8-f40a02a7a81b`

Decisión del investigador: **pendiente**. Observaciones: __________________

### Qwen7B — Cumple simbólico

Conserva Water como objeto y lo entrega al operador; la diferencia de capitalización no cambia el referente. No reproduce el defecto del control que lo trata como persona.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(kitchen)",
  "find(water, kind=object)",
  "take(water)",
  "deliver(water, to=me)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to kitchen
2: say I will search for water
3: say I will pick up water
4: say I will return to the instruction point
5: say I will deliver water to you
1001: go_to kitchen
1002: say I have arrived at kitchen
1003: find_object water_1
1004: take water_1
1005: say I have picked up water
1006: go_to instruction_point
1007: approach host_1
1008: give water_1
1009: say I have delivered water
1010: say task completed
```

run_id: `332f6a71-0798-4c98-8bd7-121bc93e508b`

Decisión del investigador: **pendiente**. Observaciones: __________________

### GPT — Cumple simbólico

Conserva Water como objeto y lo entrega al operador; la diferencia de capitalización no cambia el referente. No reproduce el defecto del control que lo trata como persona.

Interpretación propuesta: `True`. Respuesta de dominio: `None`.

**Objetivos originales:**

```json
[
  "go(kitchen)",
  "find(Water, kind=object)",
  "take(Water)",
  "deliver(Water, to=me)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to kitchen
2: say I will search for Water
3: say I will pick up Water
4: say I will return to the instruction point
5: say I will deliver Water to you
1001: go_to kitchen
1002: say I have arrived at kitchen
1003: find_object Water_1
1004: take Water_1
1005: say I have picked up Water
1006: go_to instruction_point
1007: say I have arrived at instruction_point
1008: approach host_1
1009: give Water_1
1010: say I have delivered Water
1011: say task completed
```

run_id: `cf70787d-bac9-48ea-b4b4-485ff7e1eb89`

Decisión del investigador: **pendiente**. Observaciones: __________________

## DEV-055

**Orden:** Go to the kitchen and bring it to me.

**Intención:** INT-23. **Bloque:** ambiguedad_y_fuera_dominio.

**Subtareas:**


**Restricciones:**

- No completar datos faltantes ni generar un plan completo apoyado en suposiciones no autorizadas.

**Límites de verificación de la ficha:**

- Qwen no implementa el mismo contrato conversacional: registrar su respuesta observada sin equiparar error de esquema y aclaración.

### Qwen3B — No aplicable

Produce un plan pese a información faltante o acciones fuera del dominio; no cumple la respuesta de dominio prevista.

Interpretación propuesta: `None`. Respuesta de dominio: `False`.

**Objetivos originales:**

```json
[
  "go(kitchen)",
  "find(it, kind=object)",
  "take(it)",
  "deliver(it, to=me)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to kitchen
2: say I will search for it
3: say I will pick up it
4: say I will return to the instruction point
5: say I will deliver it to you
1001: go_to kitchen
1002: say I have arrived at kitchen
1003: find_object it_1
1004: take it_1
1005: say I have picked up it
1006: go_to instruction_point
1007: approach host_1
1008: give it_1
1009: say I have delivered it
1010: say task completed
```

run_id: `5fe62e52-0a42-45ed-a60f-cc38a7ea59e4`

Decisión del investigador: **pendiente**. Observaciones: __________________

### Qwen7B — No aplicable

Produce un plan pese a información faltante o acciones fuera del dominio; no cumple la respuesta de dominio prevista.

Interpretación propuesta: `None`. Respuesta de dominio: `False`.

**Objetivos originales:**

```json
[
  "go(kitchen)",
  "find(item, kind=object)",
  "take(item)",
  "deliver(item, to=me)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to kitchen
2: say I will search for item
3: say I will pick up item
4: say I will return to the instruction point
5: say I will deliver item to you
1001: go_to kitchen
1002: say I have arrived at kitchen
1003: find_object item_1
1004: take item_1
1005: say I have picked up item
1006: go_to instruction_point
1007: approach host_1
1008: give item_1
1009: say I have delivered item
1010: say task completed
```

run_id: `2413fef1-e834-4b02-9717-c7cd0bbe4ab3`

Decisión del investigador: **pendiente**. Observaciones: __________________

### GPT — No aplicable

La respuesta pide la información faltante o explica el rechazo previsto; no inventa objetivos ni plan.

Interpretación propuesta: `None`. Respuesta de dominio: `True`.

**Objetivos originales:**

```json
[]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
What object should I bring from the kitchen?
```

run_id: `726dde02-448f-48b7-b387-8476a23cb50e`

Decisión del investigador: **pendiente**. Observaciones: __________________

## DEV-056

**Orden:** Find Robin in the office and guide Robin to the destination.

**Intención:** INT-24. **Bloque:** ambiguedad_y_fuera_dominio.

**Subtareas:**


**Restricciones:**

- No completar datos faltantes ni generar un plan completo apoyado en suposiciones no autorizadas.

**Límites de verificación de la ficha:**

- Qwen no implementa el mismo contrato conversacional: registrar su respuesta observada sin equiparar error de esquema y aclaración.

### Qwen3B — No aplicable

Produce un plan pese a información faltante o acciones fuera del dominio; no cumple la respuesta de dominio prevista.

Interpretación propuesta: `None`. Respuesta de dominio: `False`.

**Objetivos originales:**

```json
[
  "go(office)",
  "find(Robin, kind=person)",
  "guide(Robin, to=destination)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to office
2: say I will look for Robin
3: say I will guide Robin to destination
1001: go_to office
1002: say I have arrived at office
1003: find_person anybody
1004: focus enable
1005: say ask_name
1006: listen guest_name_last
1007: say acknowledge_name_last
1008: say Please follow me to destination
1009: focus disable
1010: go_to destination
1011: say I have guided Robin to destination
1012: go_to instruction_point
1013: say task completed
```

run_id: `8801fd0f-4673-48c4-ac16-959f12f016d7`

Decisión del investigador: **pendiente**. Observaciones: __________________

### Qwen7B — No aplicable

Produce un plan pese a información faltante o acciones fuera del dominio; no cumple la respuesta de dominio prevista.

Interpretación propuesta: `None`. Respuesta de dominio: `False`.

**Objetivos originales:**

```json
[
  "go(office)",
  "find(Robin, kind=person)",
  "guide(Robin, to=destination)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to office
2: say I will look for Robin
3: say I will guide Robin to destination
1001: go_to office
1002: say I have arrived at office
1003: find_person anybody
1004: focus enable
1005: say ask_name
1006: listen guest_name_last
1007: say acknowledge_name_last
1008: say Please follow me to destination
1009: focus disable
1010: go_to destination
1011: say I have guided Robin to destination
1012: go_to instruction_point
1013: say task completed
```

run_id: `161a0f30-c991-466d-834c-30ddd94feaff`

Decisión del investigador: **pendiente**. Observaciones: __________________

### GPT — No aplicable

La respuesta pide la información faltante o explica el rechazo previsto; no inventa objetivos ni plan.

Interpretación propuesta: `None`. Respuesta de dominio: `True`.

**Objetivos originales:**

```json
[]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
Where should I guide Robin?
```

run_id: `ad38cafe-5a0d-4f50-9acb-5eb9c8be3e4b`

Decisión del investigador: **pendiente**. Observaciones: __________________

## DEV-057

**Orden:** Take a fork from the shelf and give it to her.

**Intención:** INT-25. **Bloque:** ambiguedad_y_fuera_dominio.

**Subtareas:**


**Restricciones:**

- No completar datos faltantes ni generar un plan completo apoyado en suposiciones no autorizadas.

**Límites de verificación de la ficha:**

- Qwen no implementa el mismo contrato conversacional: registrar su respuesta observada sin equiparar error de esquema y aclaración.

### Qwen3B — No aplicable

Produce un plan pese a información faltante o acciones fuera del dominio; no cumple la respuesta de dominio prevista.

Interpretación propuesta: `None`. Respuesta de dominio: `False`.

**Objetivos originales:**

```json
[
  "go(shelf)",
  "find(fork, kind=object)",
  "take(fork)",
  "deliver(fork, to=her)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to shelf
2: say I will search for fork
3: say I will pick up fork
4: say I will deliver fork to her
1001: go_to shelf
1002: say I have arrived at shelf
1003: find_object fork_1
1004: take fork_1
1005: say I have picked up fork
1006: find_person her_1
1007: approach her_1
1008: give fork_1
1009: say I have delivered fork
1010: go_to instruction_point
1011: say task completed
```

run_id: `0a090391-77da-4acd-9e30-252a08e35de8`

Decisión del investigador: **pendiente**. Observaciones: __________________

### Qwen7B — No aplicable

No se obtuvo aclaración ni rechazo deliberado. HTTP 422 por salida de modelo inválida; no confundir el error con una respuesta correcta de dominio.

Interpretación propuesta: `None`. Respuesta de dominio: `False`.

**Objetivos originales:**

```json
null
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
{"stage": "extraction", "type": "QwenHTTPError", "message": "Qwen devolvió HTTP 422; cuerpo conservado", "limit_ms": null}
```

run_id: `c095c49b-500a-4f7c-8b65-e5e492a0092a`

Decisión del investigador: **pendiente**. Observaciones: __________________

### GPT — No aplicable

La respuesta pide la información faltante o explica el rechazo previsto; no inventa objetivos ni plan.

Interpretación propuesta: `None`. Respuesta de dominio: `True`.

**Objetivos originales:**

```json
[]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
Who does "her" refer to?
```

run_id: `4f5ad2c3-4669-4f6f-b734-65430464f237`

Decisión del investigador: **pendiente**. Observaciones: __________________

## DEV-058

**Orden:** Fly to the ceiling and inspect the lamp.

**Intención:** INT-26. **Bloque:** ambiguedad_y_fuera_dominio.

**Subtareas:**


**Restricciones:**

- No completar datos faltantes ni generar un plan completo apoyado en suposiciones no autorizadas.

**Límites de verificación de la ficha:**

- Qwen no implementa el mismo contrato conversacional: registrar su respuesta observada sin equiparar error de esquema y aclaración.

### Qwen3B — No aplicable

Produce un plan pese a información faltante o acciones fuera del dominio; no cumple la respuesta de dominio prevista.

Interpretación propuesta: `None`. Respuesta de dominio: `False`.

**Objetivos originales:**

```json
[
  "go(ceiling)",
  "find(lamp, kind=object)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to ceiling
2: say I will search for lamp
1001: go_to ceiling
1002: say I have arrived at ceiling
1003: find_object lamp_1
1004: go_to instruction_point
1005: say task completed
```

run_id: `2dba0856-7f7e-42a4-b8f8-c6c12abd8d41`

Decisión del investigador: **pendiente**. Observaciones: __________________

### Qwen7B — No aplicable

Produce un plan pese a información faltante o acciones fuera del dominio; no cumple la respuesta de dominio prevista.

Interpretación propuesta: `None`. Respuesta de dominio: `False`.

**Objetivos originales:**

```json
[
  "go(ceiling)",
  "find(lamp, kind=object)"
]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
1: say I will navigate to ceiling
2: say I will search for lamp
1001: go_to ceiling
1002: say I have arrived at ceiling
1003: find_object lamp_1
1004: go_to instruction_point
1005: say task completed
```

run_id: `5a4f4e67-b58c-4a56-b835-a1b8cc92455f`

Decisión del investigador: **pendiente**. Observaciones: __________________

### GPT — No aplicable

La respuesta pide la información faltante o explica el rechazo previsto; no inventa objetivos ni plan.

Interpretación propuesta: `None`. Respuesta de dominio: `True`.

**Objetivos originales:**

```json
[]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
Flying and lamp inspection are unsupported GPSR actions.
```

run_id: `2f35c77c-9e4d-4cdd-8c3b-0027079427d7`

Decisión del investigador: **pendiente**. Observaciones: __________________

## DEV-059

**Orden:** Set the thermostat to twenty degrees.

**Intención:** INT-27. **Bloque:** ambiguedad_y_fuera_dominio.

**Subtareas:**


**Restricciones:**

- No completar datos faltantes ni generar un plan completo apoyado en suposiciones no autorizadas.

**Límites de verificación de la ficha:**

- Qwen no implementa el mismo contrato conversacional: registrar su respuesta observada sin equiparar error de esquema y aclaración.

### Qwen3B — No aplicable

No se obtuvo aclaración ni rechazo deliberado. HTTP 422 por salida de modelo inválida; no confundir el error con una respuesta correcta de dominio.

Interpretación propuesta: `None`. Respuesta de dominio: `False`.

**Objetivos originales:**

```json
null
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
{"stage": "extraction", "type": "QwenHTTPError", "message": "Qwen devolvió HTTP 422; cuerpo conservado", "limit_ms": null}
```

run_id: `739b9454-8b83-48ad-b43a-3920d4eb8b18`

Decisión del investigador: **pendiente**. Observaciones: __________________

### Qwen7B — No aplicable

No se obtuvo aclaración ni rechazo deliberado. HTTP 422 por salida de modelo inválida; no confundir el error con una respuesta correcta de dominio.

Interpretación propuesta: `None`. Respuesta de dominio: `False`.

**Objetivos originales:**

```json
null
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
{"stage": "extraction", "type": "QwenHTTPError", "message": "Qwen devolvió HTTP 422; cuerpo conservado", "limit_ms": null}
```

run_id: `b2ce555e-f1d3-4198-a224-fb618cb8d664`

Decisión del investigador: **pendiente**. Observaciones: __________________

### GPT — No aplicable

La respuesta pide la información faltante o explica el rechazo previsto; no inventa objetivos ni plan.

Interpretación propuesta: `None`. Respuesta de dominio: `True`.

**Objetivos originales:**

```json
[]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
Setting a thermostat is not a supported GPSR action.
```

run_id: `4ce490f7-4b76-4e82-95ad-f91e28f5594e`

Decisión del investigador: **pendiente**. Observaciones: __________________

## DEV-060

**Orden:** Pick up the apple on the shelf, but do not pick up the apple.

**Intención:** INT-28. **Bloque:** ambiguedad_y_fuera_dominio.

**Subtareas:**


**Restricciones:**

- No completar datos faltantes ni generar un plan completo apoyado en suposiciones no autorizadas.

**Límites de verificación de la ficha:**

- Qwen no implementa el mismo contrato conversacional: registrar su respuesta observada sin equiparar error de esquema y aclaración.

### Qwen3B — No aplicable

No se obtuvo aclaración ni rechazo deliberado. HTTP 422 por salida de modelo inválida; no confundir el error con una respuesta correcta de dominio.

Interpretación propuesta: `None`. Respuesta de dominio: `False`.

**Objetivos originales:**

```json
null
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
{"stage": "extraction", "type": "QwenHTTPError", "message": "Qwen devolvió HTTP 422; cuerpo conservado", "limit_ms": null}
```

run_id: `5332d2af-b6bc-43ba-a971-abe02fe15d68`

Decisión del investigador: **pendiente**. Observaciones: __________________

### Qwen7B — No aplicable

No se obtuvo aclaración ni rechazo deliberado. HTTP 422 por salida de modelo inválida; no confundir el error con una respuesta correcta de dominio.

Interpretación propuesta: `None`. Respuesta de dominio: `False`.

**Objetivos originales:**

```json
null
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
{"stage": "extraction", "type": "QwenHTTPError", "message": "Qwen devolvió HTTP 422; cuerpo conservado", "limit_ms": null}
```

run_id: `93a2b0c2-2b34-4250-b034-dd617cac2d73`

Decisión del investigador: **pendiente**. Observaciones: __________________

### GPT — No aplicable

La respuesta pide la información faltante o explica el rechazo previsto; no inventa objetivos ni plan.

Interpretación propuesta: `None`. Respuesta de dominio: `True`.

**Objetivos originales:**

```json
[]
```

**Evidencia del plan (incluye anuncios y operaciones):**

```text
The command is contradictory: it both requires and forbids picking up the apple.
```

run_id: `7d12a9ab-013f-4db0-b2e0-3d9c97c28fcb`

Decisión del investigador: **pendiente**. Observaciones: __________________
