# Las 60 fichas de desarrollo aprobadas por el investigador

Estas fichas reproducen las órdenes y referencias actuales del archivo de datos. La aprobación se refiere a la referencia y a sus criterios, no al resultado de un modelo. Las 60 fueron aprobadas sin cambios por el investigador el 17 de octubre de 2026.

**Fuente:** `data/development/desarrollo_60_referencias.jsonl`.

**SHA-256 de la fuente:** `833c7fc26e4d8dd0dda185707c9ae4df581f7e0268a8c898188867b7f24758e4`.

## Cómo revisar

En cada ficha comprueba la interpretación de la orden, los objetivos, el orden de las subtareas, las restricciones y lo que realmente permite verificar el contrato del robot. La decisión registrada es aprobación sin cambios; cualquier revisión posterior deberá conservar trazabilidad. Puedes responder por IDs, por ejemplo: «DEV-001: aprobada» o «DEV-055: corregir la pregunta esperada a …».

Las fichas de aclaración o rechazo no necesitan una lista de objetivos ejecutables. Los límites de capacidad deben mantenerse como diagnósticos separados. Aprobar una ficha no demuestra ejecución física ni convierte una capacidad no verificable en éxito.

La aprobación está registrada como `reference_status: approved` en las 60 referencias. Las huellas antes y después constan en [Aprobacion_desarrollo_60.json](Aprobacion_desarrollo_60.json). Se reconciliaron los metadatos de coincidencias con la auditoría v02 existente, sin cambiar órdenes, objetivos ni criterios. Los campos históricos `planned_assessment` no describen el estado actual de las pruebas; los resultados están en `reports/experiments/`.

## Índice de las 60 órdenes

| Ficha | Intención | Orden original | Respuesta prevista |
|---|---|---|---|
| [DEV-001](#dev-001) | INT-01 | Go to the corridor, then go to the inspection point. | `executable` |
| [DEV-002](#dev-002) | INT-01 | Visit the corridor first and the inspection point afterwards. | `executable` |
| [DEV-003](#dev-003) | INT-01 | please go go to the corridor then go to the inspection point | `executable` |
| [DEV-004](#dev-004) | INT-02 | Find a peach in the bathroom. | `executable` |
| [DEV-005](#dev-005) | INT-02 | Look for a peach inside the bathroom. | `executable` |
| [DEV-006](#dev-006) | INT-02 | please find a peach in the bathrom | `executable` |
| [DEV-007](#dev-007) | INT-03 | Find a spoon at the bed and take it. | `executable` |
| [DEV-008](#dev-008) | INT-03 | Pick up the spoon you find at the bed. | `executable` |
| [DEV-009](#dev-009) | INT-03 | please find a spoon at the bed and and take it | `executable` |
| [DEV-010](#dev-010) | INT-04 | Bring me a mug from the cabinet. | `executable` |
| [DEV-011](#dev-011) | INT-04 | Fetch a mug at the cabinet and deliver it to me. | `executable` |
| [DEV-012](#dev-012) | INT-04 | please bring me a mug from the cabnet | `executable` |
| [DEV-013](#dev-013) | INT-05 | Bring a bowl from the bed to the storage rack. | `executable` |
| [DEV-014](#dev-014) | INT-05 | Collect a bowl at the bed and leave it at the storage rack. | `executable` |
| [DEV-015](#dev-015) | INT-05 | please bring a bowl from the bed to the storage  rack | `executable` |
| [DEV-016](#dev-016) | INT-06 | In the kitchen, find a cup, take it, and put it on the table. | `executable` |
| [DEV-017](#dev-017) | INT-06 | Locate a cup in the kitchen and pick it up, then place it on the table there. | `executable` |
| [DEV-018](#dev-018) | INT-06 | in the kichen find a cup take it and put it on the table please | `executable` |
| [DEV-019](#dev-019) | INT-07 | Find Robin in the office. | `executable` |
| [DEV-020](#dev-020) | INT-07 | Look for Robin inside the office. | `executable` |
| [DEV-021](#dev-021) | INT-07 | please find Robin in the ofice | `executable` |
| [DEV-022](#dev-022) | INT-08 | Find Morgan in the kitchen and guide them to the entrance. | `executable` |
| [DEV-023](#dev-023) | INT-08 | Meet Morgan in the kitchen, then lead Morgan to the entrance. | `executable` |
| [DEV-024](#dev-024) | INT-08 | find Morgan in the kichen and guide them to the entrance please | `executable` |
| [DEV-025](#dev-025) | INT-09 | Find the waving person in the bedroom and follow them. | `executable` |
| [DEV-026](#dev-026) | INT-09 | In the bedroom, locate the person who is waving and follow that person. | `executable` |
| [DEV-027](#dev-027) | INT-09 | please find the waving person in the bedrom and follow them | `executable` |
| [DEV-028](#dev-028) | INT-10 | Take an orange from the refrigerator and give it to Sarah in the kitchen. | `executable` |
| [DEV-029](#dev-029) | INT-10 | Fetch an orange at the refrigerator, then find Sarah in the kitchen and hand the orange to her. | `executable` |
| [DEV-030](#dev-030) | INT-10 | take an orange from the refridgerator and give it to Sarah in the kichen | `executable` |
| [DEV-031](#dev-031) | INT-11 | Count the toys on the storage rack. | `executable` |
| [DEV-032](#dev-032) | INT-11 | Tell me how many toys are on the storage rack. | `executable` |
| [DEV-033](#dev-033) | INT-11 | please count the the toys on the storage rack | `executable` |
| [DEV-034](#dev-034) | INT-12 | Find Charlie in the living room and tell Charlie the current time. | `executable` |
| [DEV-035](#dev-035) | INT-12 | Locate Charlie in the living room and say what time it is to Charlie. | `executable` |
| [DEV-036](#dev-036) | INT-12 | please find Charlie in the living  room and tell Charlie the current time | `executable` |
| [DEV-037](#dev-037) | INT-13 | Find a person in the bedroom, ask their name, and come back to tell me their name. | `executable` |
| [DEV-038](#dev-038) | INT-13 | Go to the bedroom, learn the name of a person there, then return and report it to me. | `executable` |
| [DEV-039](#dev-039) | INT-13 | please find a person in the bedroom ask their name and come back to tell me their name | `executable` |
| [DEV-040](#dev-040) | INT-14 | Find the waving person in the corridor and answer their question. | `executable` |
| [DEV-041](#dev-041) | INT-14 | In the corridor, locate the person who is waving and respond to that person's question. | `executable` |
| [DEV-042](#dev-042) | INT-14 | find the waving person in the corridor and and answer their question please | `executable` |
| [DEV-043](#dev-043) | INT-15 | Find Jane in the kitchen and greet her. | `executable` |
| [DEV-044](#dev-044) | INT-15 | Look for Jane in the kitchen and say hello to Jane. | `executable` |
| [DEV-045](#dev-045) | INT-15 | please find Jane in the kichen and greet her | `executable` |
| [DEV-046](#dev-046) | INT-16 | Tell me which is the largest fruit on the sofa. | `executable` |
| [DEV-047](#dev-047) | INT-16 | Identify the biggest fruit on the sofa and report which one it is. | `executable` |
| [DEV-048](#dev-048) | INT-16 | please tell me which is the largest fruit on the sofa | `executable` |
| [DEV-049](#dev-049) | INT-17 | Find the person waving and wearing a blue coat in the office, then guide them to the entrance. | `executable` |
| [DEV-050](#dev-050) | INT-18 | Count the people wearing red shirts in the living room. | `executable` |
| [DEV-051](#dev-051) | INT-19 | Tell me which is the heaviest fruit on the sofa. | `domain_capability_review` |
| [DEV-052](#dev-052) | INT-20 | Find Simone at the coatrack and follow Simone to the bedroom. | `executable` |
| [DEV-053](#dev-053) | INT-21 | Bring me a mug from the refrigerator, then bring me a spoon from the bed. | `executable` |
| [DEV-054](#dev-054) | INT-22 | Find Water in the kitchen, take it, and bring it to me. | `executable` |
| [DEV-055](#dev-055) | INT-23 | Go to the kitchen and bring it to me. | `clarification` |
| [DEV-056](#dev-056) | INT-24 | Find Robin in the office and guide Robin to the destination. | `clarification` |
| [DEV-057](#dev-057) | INT-25 | Take a fork from the shelf and give it to her. | `clarification` |
| [DEV-058](#dev-058) | INT-26 | Fly to the ceiling and inspect the lamp. | `rejected` |
| [DEV-059](#dev-059) | INT-27 | Set the thermostat to twenty degrees. | `rejected` |
| [DEV-060](#dev-060) | INT-28 | Pick up the apple on the shelf, but do not pick up the apple. | `rejected` |

## DEV-001

**Intención:** INT-01 · **Grupo:** navegacion · **Variante:** canonica · **Bloque:** funcional_y_linguistico

**Orden original:**

> Go to the corridor, then go to the inspection point.

**Propósito:** Orden de dos visitas y distinción entre inspection point e instruction_point

**Respuesta prevista:** `executable`.

**Objetivos propuestos:**

```text
go(corridor)
go(inspection point)
```

**Subtareas requeridas:**

- Visitar corridor.
- Después visitar inspection point; distinguirlo de instruction_point.

**Restricciones:**

- La visita a corridor precede a la visita a inspection point.
- El retorno de cierre no sustituye ninguna de las visitas solicitadas.

**Conductas prohibidas:**

- Inventar entidades, destinos o subtareas no solicitados.

**Variaciones aceptables:**

- Variar el texto de anuncios conservando su sentido.
- Usar identificadores internos consistentes sin cambiar el referente.

**Límites de verificación:**

Sin elementos especificados en la ficha.

**Condiciones iniciales:**

```json
{
  "location": "unknown",
  "holding": "nothing",
  "focus": false,
  "manipulation_enabled": true,
  "independent_request": true
}
```

**Supuestos del escenario:**

- Las entidades mencionadas son referencias del dominio; su detección y disponibilidad física no se evalúan.
- Cada orden se procesa sin conversación previa.

**Comprobaciones comunes del plan:**

- Acciones y parámetros dentro del contrato compartido.
- No añadir tareas ajenas; se admiten los cierres convencionales de retorno y comunicación.
- Referentes consistentes y dependencias de adquisición/entrega respetadas.
- Distinguir protocolo generado de operación física no observada.

**Notas existentes de revisión:**

- 2026-10-17: el investigador confirmó en la conversación haber revisado las 60 fichas y encontrarlas en orden; aprobación sin cambios de órdenes, objetivos ni criterios. Aprobación para desarrollo, no dictamen sobre salidas de modelos.

**Decisión del investigador:**

- [x] Aprobada sin cambios.
- [ ] Requiere correcciones.
- [ ] No aprobada.

**Correcciones u observaciones:**

Sin correcciones solicitadas.

**Revisor y fecha:** Investigador (usuario), 2026-10-17.

<details>
<summary>Metadatos y trazabilidad de la ficha original</summary>

```json
{
  "reference_status": "approved",
  "split": "development",
  "development_version": "0.2",
  "overlap_status": "sin_coincidencia_detectada_v02",
  "overlap_audit_history": [
    {
      "development_version": "0.1",
      "input_audited": "Go to the inspection point.",
      "development_sha256": "02103490f89367add79ae9b6aea90e01ecd7f9def7cb32c24d9fb51e6b0b5c7b",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [
          10731
        ],
        "normalizador_real": [
          10731,
          11912,
          22687
        ]
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    },
    {
      "development_version": "0.2",
      "input_audited": "Go to the corridor, then go to the inspection point.",
      "development_sha256": "4c1a356fa50ac317ad6b428c101a48183968a41e2771e2ad2bd7c622f61d4480",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "audit_path": "reports/evaluation/auditoria_desarrollo_v02.json",
      "audit_sha256": "f4d5c3c3088dc5bd9f61d6ebef4b33716401dd4014491585317a184e647e0346",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    }
  ],
  "revision_history": [
    {
      "version": "0.2",
      "previous_input": "Go to the inspection point.",
      "previous_goals_ref": [
        "go(inspection point)"
      ],
      "reason": "Sustitución de las tres variantes de un grupo con coincidencias; nueva auditoría pendiente."
    }
  ],
  "planned_assessment": {
    "semantic": "no_ejecutado",
    "plan_contract": "no_ejecutado",
    "task_fulfillment": "no_ejecutado",
    "latency_ms": null
  }
}
```

</details>

## DEV-002

**Intención:** INT-01 · **Grupo:** navegacion · **Variante:** parafrasis · **Bloque:** funcional_y_linguistico

**Orden original:**

> Visit the corridor first and the inspection point afterwards.

**Propósito:** Orden de dos visitas y distinción entre inspection point e instruction_point

**Respuesta prevista:** `executable`.

**Objetivos propuestos:**

```text
go(corridor)
go(inspection point)
```

**Subtareas requeridas:**

- Visitar corridor.
- Después visitar inspection point; distinguirlo de instruction_point.

**Restricciones:**

- La visita a corridor precede a la visita a inspection point.
- El retorno de cierre no sustituye ninguna de las visitas solicitadas.

**Conductas prohibidas:**

- Inventar entidades, destinos o subtareas no solicitados.

**Variaciones aceptables:**

- Variar el texto de anuncios conservando su sentido.
- Usar identificadores internos consistentes sin cambiar el referente.

**Límites de verificación:**

Sin elementos especificados en la ficha.

**Condiciones iniciales:**

```json
{
  "location": "unknown",
  "holding": "nothing",
  "focus": false,
  "manipulation_enabled": true,
  "independent_request": true
}
```

**Supuestos del escenario:**

- Las entidades mencionadas son referencias del dominio; su detección y disponibilidad física no se evalúan.
- Cada orden se procesa sin conversación previa.

**Comprobaciones comunes del plan:**

- Acciones y parámetros dentro del contrato compartido.
- No añadir tareas ajenas; se admiten los cierres convencionales de retorno y comunicación.
- Referentes consistentes y dependencias de adquisición/entrega respetadas.
- Distinguir protocolo generado de operación física no observada.

**Notas existentes de revisión:**

- 2026-10-17: el investigador confirmó en la conversación haber revisado las 60 fichas y encontrarlas en orden; aprobación sin cambios de órdenes, objetivos ni criterios. Aprobación para desarrollo, no dictamen sobre salidas de modelos.

**Decisión del investigador:**

- [x] Aprobada sin cambios.
- [ ] Requiere correcciones.
- [ ] No aprobada.

**Correcciones u observaciones:**

Sin correcciones solicitadas.

**Revisor y fecha:** Investigador (usuario), 2026-10-17.

<details>
<summary>Metadatos y trazabilidad de la ficha original</summary>

```json
{
  "reference_status": "approved",
  "split": "development",
  "development_version": "0.2",
  "overlap_status": "sin_coincidencia_detectada_v02",
  "overlap_audit_history": [
    {
      "development_version": "0.1",
      "input_audited": "Navigate to the location called inspection point.",
      "development_sha256": "02103490f89367add79ae9b6aea90e01ecd7f9def7cb32c24d9fb51e6b0b5c7b",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    },
    {
      "development_version": "0.2",
      "input_audited": "Visit the corridor first and the inspection point afterwards.",
      "development_sha256": "4c1a356fa50ac317ad6b428c101a48183968a41e2771e2ad2bd7c622f61d4480",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "audit_path": "reports/evaluation/auditoria_desarrollo_v02.json",
      "audit_sha256": "f4d5c3c3088dc5bd9f61d6ebef4b33716401dd4014491585317a184e647e0346",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    }
  ],
  "revision_history": [
    {
      "version": "0.2",
      "previous_input": "Navigate to the location called inspection point.",
      "previous_goals_ref": [
        "go(inspection point)"
      ],
      "reason": "Sustitución de las tres variantes de un grupo con coincidencias; nueva auditoría pendiente."
    }
  ],
  "planned_assessment": {
    "semantic": "no_ejecutado",
    "plan_contract": "no_ejecutado",
    "task_fulfillment": "no_ejecutado",
    "latency_ms": null
  }
}
```

</details>

## DEV-003

**Intención:** INT-01 · **Grupo:** navegacion · **Variante:** ruido_leve · **Bloque:** funcional_y_linguistico

**Orden original:**

> please go go to the corridor then go to the inspection point

**Propósito:** Orden de dos visitas y distinción entre inspection point e instruction_point

**Respuesta prevista:** `executable`.

**Objetivos propuestos:**

```text
go(corridor)
go(inspection point)
```

**Subtareas requeridas:**

- Visitar corridor.
- Después visitar inspection point; distinguirlo de instruction_point.

**Restricciones:**

- La visita a corridor precede a la visita a inspection point.
- El retorno de cierre no sustituye ninguna de las visitas solicitadas.

**Conductas prohibidas:**

- Inventar entidades, destinos o subtareas no solicitados.

**Variaciones aceptables:**

- Variar el texto de anuncios conservando su sentido.
- Usar identificadores internos consistentes sin cambiar el referente.

**Límites de verificación:**

Sin elementos especificados en la ficha.

**Condiciones iniciales:**

```json
{
  "location": "unknown",
  "holding": "nothing",
  "focus": false,
  "manipulation_enabled": true,
  "independent_request": true
}
```

**Supuestos del escenario:**

- Las entidades mencionadas son referencias del dominio; su detección y disponibilidad física no se evalúan.
- Cada orden se procesa sin conversación previa.

**Comprobaciones comunes del plan:**

- Acciones y parámetros dentro del contrato compartido.
- No añadir tareas ajenas; se admiten los cierres convencionales de retorno y comunicación.
- Referentes consistentes y dependencias de adquisición/entrega respetadas.
- Distinguir protocolo generado de operación física no observada.

**Notas existentes de revisión:**

- 2026-10-17: el investigador confirmó en la conversación haber revisado las 60 fichas y encontrarlas en orden; aprobación sin cambios de órdenes, objetivos ni criterios. Aprobación para desarrollo, no dictamen sobre salidas de modelos.

**Decisión del investigador:**

- [x] Aprobada sin cambios.
- [ ] Requiere correcciones.
- [ ] No aprobada.

**Correcciones u observaciones:**

Sin correcciones solicitadas.

**Revisor y fecha:** Investigador (usuario), 2026-10-17.

<details>
<summary>Metadatos y trazabilidad de la ficha original</summary>

```json
{
  "reference_status": "approved",
  "split": "development",
  "development_version": "0.2",
  "overlap_status": "sin_coincidencia_detectada_v02",
  "overlap_audit_history": [
    {
      "development_version": "0.1",
      "input_audited": "please go go to the inspection point",
      "development_sha256": "02103490f89367add79ae9b6aea90e01ecd7f9def7cb32c24d9fb51e6b0b5c7b",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": [
          10731,
          11912,
          22687
        ]
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    },
    {
      "development_version": "0.2",
      "input_audited": "please go go to the corridor then go to the inspection point",
      "development_sha256": "4c1a356fa50ac317ad6b428c101a48183968a41e2771e2ad2bd7c622f61d4480",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "audit_path": "reports/evaluation/auditoria_desarrollo_v02.json",
      "audit_sha256": "f4d5c3c3088dc5bd9f61d6ebef4b33716401dd4014491585317a184e647e0346",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    }
  ],
  "revision_history": [
    {
      "version": "0.2",
      "previous_input": "please go go to the inspection point",
      "previous_goals_ref": [
        "go(inspection point)"
      ],
      "reason": "Sustitución de las tres variantes de un grupo con coincidencias; nueva auditoría pendiente."
    }
  ],
  "planned_assessment": {
    "semantic": "no_ejecutado",
    "plan_contract": "no_ejecutado",
    "task_fulfillment": "no_ejecutado",
    "latency_ms": null
  }
}
```

</details>

## DEV-004

**Intención:** INT-02 · **Grupo:** busqueda_objeto · **Variante:** canonica · **Bloque:** funcional_y_linguistico

**Orden original:**

> Find a peach in the bathroom.

**Propósito:** Objeto y habitación

**Respuesta prevista:** `executable`.

**Objetivos propuestos:**

```text
go(bathroom)
find(peach, kind=object)
```

**Subtareas requeridas:**

- Ir a bathroom.
- Buscar peach en bathroom.

**Restricciones:**

- No adquirir ni transportar el objeto: solo se solicita localizarlo.

**Conductas prohibidas:**

- Inventar entidades, destinos o subtareas no solicitados.

**Variaciones aceptables:**

- Variar el texto de anuncios conservando su sentido.
- Usar identificadores internos consistentes sin cambiar el referente.

**Límites de verificación:**

Sin elementos especificados en la ficha.

**Condiciones iniciales:**

```json
{
  "location": "unknown",
  "holding": "nothing",
  "focus": false,
  "manipulation_enabled": true,
  "independent_request": true
}
```

**Supuestos del escenario:**

- Las entidades mencionadas son referencias del dominio; su detección y disponibilidad física no se evalúan.
- Cada orden se procesa sin conversación previa.

**Comprobaciones comunes del plan:**

- Acciones y parámetros dentro del contrato compartido.
- No añadir tareas ajenas; se admiten los cierres convencionales de retorno y comunicación.
- Referentes consistentes y dependencias de adquisición/entrega respetadas.
- Distinguir protocolo generado de operación física no observada.

**Notas existentes de revisión:**

- 2026-10-17: el investigador confirmó en la conversación haber revisado las 60 fichas y encontrarlas en orden; aprobación sin cambios de órdenes, objetivos ni criterios. Aprobación para desarrollo, no dictamen sobre salidas de modelos.

**Decisión del investigador:**

- [x] Aprobada sin cambios.
- [ ] Requiere correcciones.
- [ ] No aprobada.

**Correcciones u observaciones:**

Sin correcciones solicitadas.

**Revisor y fecha:** Investigador (usuario), 2026-10-17.

<details>
<summary>Metadatos y trazabilidad de la ficha original</summary>

```json
{
  "reference_status": "approved",
  "split": "development",
  "development_version": "0.2",
  "overlap_status": "sin_coincidencia_detectada_v02",
  "overlap_audit_history": [
    {
      "development_version": "0.1",
      "input_audited": "Find a pear in the kitchen.",
      "development_sha256": "02103490f89367add79ae9b6aea90e01ecd7f9def7cb32c24d9fb51e6b0b5c7b",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [
          4879
        ],
        "normalizador_real": [
          4879
        ]
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    },
    {
      "development_version": "0.2",
      "input_audited": "Find a peach in the bathroom.",
      "development_sha256": "4c1a356fa50ac317ad6b428c101a48183968a41e2771e2ad2bd7c622f61d4480",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "audit_path": "reports/evaluation/auditoria_desarrollo_v02.json",
      "audit_sha256": "f4d5c3c3088dc5bd9f61d6ebef4b33716401dd4014491585317a184e647e0346",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    }
  ],
  "revision_history": [
    {
      "version": "0.2",
      "previous_input": "Find a pear in the kitchen.",
      "previous_goals_ref": [
        "go(kitchen)",
        "find(pear, kind=object)"
      ],
      "reason": "Sustitución de las tres variantes de un grupo con coincidencias; nueva auditoría pendiente."
    }
  ],
  "planned_assessment": {
    "semantic": "no_ejecutado",
    "plan_contract": "no_ejecutado",
    "task_fulfillment": "no_ejecutado",
    "latency_ms": null
  }
}
```

</details>

## DEV-005

**Intención:** INT-02 · **Grupo:** busqueda_objeto · **Variante:** parafrasis · **Bloque:** funcional_y_linguistico

**Orden original:**

> Look for a peach inside the bathroom.

**Propósito:** Objeto y habitación

**Respuesta prevista:** `executable`.

**Objetivos propuestos:**

```text
go(bathroom)
find(peach, kind=object)
```

**Subtareas requeridas:**

- Ir a bathroom.
- Buscar peach en bathroom.

**Restricciones:**

- No adquirir ni transportar el objeto: solo se solicita localizarlo.

**Conductas prohibidas:**

- Inventar entidades, destinos o subtareas no solicitados.

**Variaciones aceptables:**

- Variar el texto de anuncios conservando su sentido.
- Usar identificadores internos consistentes sin cambiar el referente.

**Límites de verificación:**

Sin elementos especificados en la ficha.

**Condiciones iniciales:**

```json
{
  "location": "unknown",
  "holding": "nothing",
  "focus": false,
  "manipulation_enabled": true,
  "independent_request": true
}
```

**Supuestos del escenario:**

- Las entidades mencionadas son referencias del dominio; su detección y disponibilidad física no se evalúan.
- Cada orden se procesa sin conversación previa.

**Comprobaciones comunes del plan:**

- Acciones y parámetros dentro del contrato compartido.
- No añadir tareas ajenas; se admiten los cierres convencionales de retorno y comunicación.
- Referentes consistentes y dependencias de adquisición/entrega respetadas.
- Distinguir protocolo generado de operación física no observada.

**Notas existentes de revisión:**

- 2026-10-17: el investigador confirmó en la conversación haber revisado las 60 fichas y encontrarlas en orden; aprobación sin cambios de órdenes, objetivos ni criterios. Aprobación para desarrollo, no dictamen sobre salidas de modelos.

**Decisión del investigador:**

- [x] Aprobada sin cambios.
- [ ] Requiere correcciones.
- [ ] No aprobada.

**Correcciones u observaciones:**

Sin correcciones solicitadas.

**Revisor y fecha:** Investigador (usuario), 2026-10-17.

<details>
<summary>Metadatos y trazabilidad de la ficha original</summary>

```json
{
  "reference_status": "approved",
  "split": "development",
  "development_version": "0.2",
  "overlap_status": "sin_coincidencia_detectada_v02",
  "overlap_audit_history": [
    {
      "development_version": "0.1",
      "input_audited": "Look for a pear inside the kitchen.",
      "development_sha256": "02103490f89367add79ae9b6aea90e01ecd7f9def7cb32c24d9fb51e6b0b5c7b",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    },
    {
      "development_version": "0.2",
      "input_audited": "Look for a peach inside the bathroom.",
      "development_sha256": "4c1a356fa50ac317ad6b428c101a48183968a41e2771e2ad2bd7c622f61d4480",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "audit_path": "reports/evaluation/auditoria_desarrollo_v02.json",
      "audit_sha256": "f4d5c3c3088dc5bd9f61d6ebef4b33716401dd4014491585317a184e647e0346",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    }
  ],
  "revision_history": [
    {
      "version": "0.2",
      "previous_input": "Look for a pear inside the kitchen.",
      "previous_goals_ref": [
        "go(kitchen)",
        "find(pear, kind=object)"
      ],
      "reason": "Sustitución de las tres variantes de un grupo con coincidencias; nueva auditoría pendiente."
    }
  ],
  "planned_assessment": {
    "semantic": "no_ejecutado",
    "plan_contract": "no_ejecutado",
    "task_fulfillment": "no_ejecutado",
    "latency_ms": null
  }
}
```

</details>

## DEV-006

**Intención:** INT-02 · **Grupo:** busqueda_objeto · **Variante:** ruido_leve · **Bloque:** funcional_y_linguistico

**Orden original:**

> please find a peach in the bathrom

**Propósito:** Objeto y habitación

**Respuesta prevista:** `executable`.

**Objetivos propuestos:**

```text
go(bathroom)
find(peach, kind=object)
```

**Subtareas requeridas:**

- Ir a bathroom.
- Buscar peach en bathroom.

**Restricciones:**

- No adquirir ni transportar el objeto: solo se solicita localizarlo.

**Conductas prohibidas:**

- Inventar entidades, destinos o subtareas no solicitados.

**Variaciones aceptables:**

- Variar el texto de anuncios conservando su sentido.
- Usar identificadores internos consistentes sin cambiar el referente.

**Límites de verificación:**

Sin elementos especificados en la ficha.

**Condiciones iniciales:**

```json
{
  "location": "unknown",
  "holding": "nothing",
  "focus": false,
  "manipulation_enabled": true,
  "independent_request": true
}
```

**Supuestos del escenario:**

- Las entidades mencionadas son referencias del dominio; su detección y disponibilidad física no se evalúan.
- Cada orden se procesa sin conversación previa.

**Comprobaciones comunes del plan:**

- Acciones y parámetros dentro del contrato compartido.
- No añadir tareas ajenas; se admiten los cierres convencionales de retorno y comunicación.
- Referentes consistentes y dependencias de adquisición/entrega respetadas.
- Distinguir protocolo generado de operación física no observada.

**Notas existentes de revisión:**

- 2026-10-17: el investigador confirmó en la conversación haber revisado las 60 fichas y encontrarlas en orden; aprobación sin cambios de órdenes, objetivos ni criterios. Aprobación para desarrollo, no dictamen sobre salidas de modelos.

**Decisión del investigador:**

- [x] Aprobada sin cambios.
- [ ] Requiere correcciones.
- [ ] No aprobada.

**Correcciones u observaciones:**

Sin correcciones solicitadas.

**Revisor y fecha:** Investigador (usuario), 2026-10-17.

<details>
<summary>Metadatos y trazabilidad de la ficha original</summary>

```json
{
  "reference_status": "approved",
  "split": "development",
  "development_version": "0.2",
  "overlap_status": "sin_coincidencia_detectada_v02",
  "overlap_audit_history": [
    {
      "development_version": "0.1",
      "input_audited": "please find a pear in the kichen",
      "development_sha256": "02103490f89367add79ae9b6aea90e01ecd7f9def7cb32c24d9fb51e6b0b5c7b",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": [
          4879
        ]
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    },
    {
      "development_version": "0.2",
      "input_audited": "please find a peach in the bathrom",
      "development_sha256": "4c1a356fa50ac317ad6b428c101a48183968a41e2771e2ad2bd7c622f61d4480",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "audit_path": "reports/evaluation/auditoria_desarrollo_v02.json",
      "audit_sha256": "f4d5c3c3088dc5bd9f61d6ebef4b33716401dd4014491585317a184e647e0346",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    }
  ],
  "revision_history": [
    {
      "version": "0.2",
      "previous_input": "please find a pear in the kichen",
      "previous_goals_ref": [
        "go(kitchen)",
        "find(pear, kind=object)"
      ],
      "reason": "Sustitución de las tres variantes de un grupo con coincidencias; nueva auditoría pendiente."
    }
  ],
  "planned_assessment": {
    "semantic": "no_ejecutado",
    "plan_contract": "no_ejecutado",
    "task_fulfillment": "no_ejecutado",
    "latency_ms": null
  }
}
```

</details>

## DEV-007

**Intención:** INT-03 · **Grupo:** adquisicion · **Variante:** canonica · **Bloque:** funcional_y_linguistico

**Orden original:**

> Find a spoon at the bed and take it.

**Propósito:** Referencia pronominal y adquisición

**Respuesta prevista:** `executable`.

**Objetivos propuestos:**

```text
go(bed)
find(spoon, kind=object)
take(spoon)
```

**Subtareas requeridas:**

- Ir a bed.
- Localizar spoon.
- Adquirir ese mismo spoon.

**Restricciones:**

- La búsqueda precede a la adquisición; it refiere a spoon.

**Conductas prohibidas:**

- Inventar entidades, destinos o subtareas no solicitados.

**Variaciones aceptables:**

- Variar el texto de anuncios conservando su sentido.
- Usar identificadores internos consistentes sin cambiar el referente.

**Límites de verificación:**

Sin elementos especificados en la ficha.

**Condiciones iniciales:**

```json
{
  "location": "unknown",
  "holding": "nothing",
  "focus": false,
  "manipulation_enabled": true,
  "independent_request": true
}
```

**Supuestos del escenario:**

- Las entidades mencionadas son referencias del dominio; su detección y disponibilidad física no se evalúan.
- Cada orden se procesa sin conversación previa.

**Comprobaciones comunes del plan:**

- Acciones y parámetros dentro del contrato compartido.
- No añadir tareas ajenas; se admiten los cierres convencionales de retorno y comunicación.
- Referentes consistentes y dependencias de adquisición/entrega respetadas.
- Distinguir protocolo generado de operación física no observada.

**Notas existentes de revisión:**

- 2026-10-17: el investigador confirmó en la conversación haber revisado las 60 fichas y encontrarlas en orden; aprobación sin cambios de órdenes, objetivos ni criterios. Aprobación para desarrollo, no dictamen sobre salidas de modelos.

**Decisión del investigador:**

- [x] Aprobada sin cambios.
- [ ] Requiere correcciones.
- [ ] No aprobada.

**Correcciones u observaciones:**

Sin correcciones solicitadas.

**Revisor y fecha:** Investigador (usuario), 2026-10-17.

<details>
<summary>Metadatos y trazabilidad de la ficha original</summary>

```json
{
  "reference_status": "approved",
  "split": "development",
  "development_version": "0.2",
  "overlap_status": "sin_coincidencia_detectada_v02",
  "overlap_audit_history": [
    {
      "development_version": "0.1",
      "input_audited": "Find a spoon at the bed and take it.",
      "development_sha256": "02103490f89367add79ae9b6aea90e01ecd7f9def7cb32c24d9fb51e6b0b5c7b",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    },
    {
      "development_version": "0.2",
      "input_audited": "Find a spoon at the bed and take it.",
      "development_sha256": "4c1a356fa50ac317ad6b428c101a48183968a41e2771e2ad2bd7c622f61d4480",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "audit_path": "reports/evaluation/auditoria_desarrollo_v02.json",
      "audit_sha256": "f4d5c3c3088dc5bd9f61d6ebef4b33716401dd4014491585317a184e647e0346",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    }
  ],
  "planned_assessment": {
    "semantic": "no_ejecutado",
    "plan_contract": "no_ejecutado",
    "task_fulfillment": "no_ejecutado",
    "latency_ms": null
  }
}
```

</details>

## DEV-008

**Intención:** INT-03 · **Grupo:** adquisicion · **Variante:** parafrasis · **Bloque:** funcional_y_linguistico

**Orden original:**

> Pick up the spoon you find at the bed.

**Propósito:** Referencia pronominal y adquisición

**Respuesta prevista:** `executable`.

**Objetivos propuestos:**

```text
go(bed)
find(spoon, kind=object)
take(spoon)
```

**Subtareas requeridas:**

- Ir a bed.
- Localizar spoon.
- Adquirir ese mismo spoon.

**Restricciones:**

- La búsqueda precede a la adquisición; it refiere a spoon.

**Conductas prohibidas:**

- Inventar entidades, destinos o subtareas no solicitados.

**Variaciones aceptables:**

- Variar el texto de anuncios conservando su sentido.
- Usar identificadores internos consistentes sin cambiar el referente.

**Límites de verificación:**

Sin elementos especificados en la ficha.

**Condiciones iniciales:**

```json
{
  "location": "unknown",
  "holding": "nothing",
  "focus": false,
  "manipulation_enabled": true,
  "independent_request": true
}
```

**Supuestos del escenario:**

- Las entidades mencionadas son referencias del dominio; su detección y disponibilidad física no se evalúan.
- Cada orden se procesa sin conversación previa.

**Comprobaciones comunes del plan:**

- Acciones y parámetros dentro del contrato compartido.
- No añadir tareas ajenas; se admiten los cierres convencionales de retorno y comunicación.
- Referentes consistentes y dependencias de adquisición/entrega respetadas.
- Distinguir protocolo generado de operación física no observada.

**Notas existentes de revisión:**

- 2026-10-17: el investigador confirmó en la conversación haber revisado las 60 fichas y encontrarlas en orden; aprobación sin cambios de órdenes, objetivos ni criterios. Aprobación para desarrollo, no dictamen sobre salidas de modelos.

**Decisión del investigador:**

- [x] Aprobada sin cambios.
- [ ] Requiere correcciones.
- [ ] No aprobada.

**Correcciones u observaciones:**

Sin correcciones solicitadas.

**Revisor y fecha:** Investigador (usuario), 2026-10-17.

<details>
<summary>Metadatos y trazabilidad de la ficha original</summary>

```json
{
  "reference_status": "approved",
  "split": "development",
  "development_version": "0.2",
  "overlap_status": "sin_coincidencia_detectada_v02",
  "overlap_audit_history": [
    {
      "development_version": "0.1",
      "input_audited": "Pick up the spoon you find at the bed.",
      "development_sha256": "02103490f89367add79ae9b6aea90e01ecd7f9def7cb32c24d9fb51e6b0b5c7b",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    },
    {
      "development_version": "0.2",
      "input_audited": "Pick up the spoon you find at the bed.",
      "development_sha256": "4c1a356fa50ac317ad6b428c101a48183968a41e2771e2ad2bd7c622f61d4480",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "audit_path": "reports/evaluation/auditoria_desarrollo_v02.json",
      "audit_sha256": "f4d5c3c3088dc5bd9f61d6ebef4b33716401dd4014491585317a184e647e0346",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    }
  ],
  "planned_assessment": {
    "semantic": "no_ejecutado",
    "plan_contract": "no_ejecutado",
    "task_fulfillment": "no_ejecutado",
    "latency_ms": null
  }
}
```

</details>

## DEV-009

**Intención:** INT-03 · **Grupo:** adquisicion · **Variante:** ruido_leve · **Bloque:** funcional_y_linguistico

**Orden original:**

> please find a spoon at the bed and and take it

**Propósito:** Referencia pronominal y adquisición

**Respuesta prevista:** `executable`.

**Objetivos propuestos:**

```text
go(bed)
find(spoon, kind=object)
take(spoon)
```

**Subtareas requeridas:**

- Ir a bed.
- Localizar spoon.
- Adquirir ese mismo spoon.

**Restricciones:**

- La búsqueda precede a la adquisición; it refiere a spoon.

**Conductas prohibidas:**

- Inventar entidades, destinos o subtareas no solicitados.

**Variaciones aceptables:**

- Variar el texto de anuncios conservando su sentido.
- Usar identificadores internos consistentes sin cambiar el referente.

**Límites de verificación:**

Sin elementos especificados en la ficha.

**Condiciones iniciales:**

```json
{
  "location": "unknown",
  "holding": "nothing",
  "focus": false,
  "manipulation_enabled": true,
  "independent_request": true
}
```

**Supuestos del escenario:**

- Las entidades mencionadas son referencias del dominio; su detección y disponibilidad física no se evalúan.
- Cada orden se procesa sin conversación previa.

**Comprobaciones comunes del plan:**

- Acciones y parámetros dentro del contrato compartido.
- No añadir tareas ajenas; se admiten los cierres convencionales de retorno y comunicación.
- Referentes consistentes y dependencias de adquisición/entrega respetadas.
- Distinguir protocolo generado de operación física no observada.

**Notas existentes de revisión:**

- 2026-10-17: el investigador confirmó en la conversación haber revisado las 60 fichas y encontrarlas en orden; aprobación sin cambios de órdenes, objetivos ni criterios. Aprobación para desarrollo, no dictamen sobre salidas de modelos.

**Decisión del investigador:**

- [x] Aprobada sin cambios.
- [ ] Requiere correcciones.
- [ ] No aprobada.

**Correcciones u observaciones:**

Sin correcciones solicitadas.

**Revisor y fecha:** Investigador (usuario), 2026-10-17.

<details>
<summary>Metadatos y trazabilidad de la ficha original</summary>

```json
{
  "reference_status": "approved",
  "split": "development",
  "development_version": "0.2",
  "overlap_status": "sin_coincidencia_detectada_v02",
  "overlap_audit_history": [
    {
      "development_version": "0.1",
      "input_audited": "please find a spoon at the bed and and take it",
      "development_sha256": "02103490f89367add79ae9b6aea90e01ecd7f9def7cb32c24d9fb51e6b0b5c7b",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    },
    {
      "development_version": "0.2",
      "input_audited": "please find a spoon at the bed and and take it",
      "development_sha256": "4c1a356fa50ac317ad6b428c101a48183968a41e2771e2ad2bd7c622f61d4480",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "audit_path": "reports/evaluation/auditoria_desarrollo_v02.json",
      "audit_sha256": "f4d5c3c3088dc5bd9f61d6ebef4b33716401dd4014491585317a184e647e0346",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    }
  ],
  "planned_assessment": {
    "semantic": "no_ejecutado",
    "plan_contract": "no_ejecutado",
    "task_fulfillment": "no_ejecutado",
    "latency_ms": null
  }
}
```

</details>

## DEV-010

**Intención:** INT-04 · **Grupo:** entrega_operador · **Variante:** canonica · **Bloque:** funcional_y_linguistico

**Orden original:**

> Bring me a mug from the cabinet.

**Propósito:** Origen y destinatario me

**Respuesta prevista:** `executable`.

**Objetivos propuestos:**

```text
go(cabinet)
find(mug, kind=object)
take(mug)
deliver(mug, to=me)
```

**Subtareas requeridas:**

- Buscar y adquirir mug en cabinet.
- Regresar al punto del operador y entregarle mug.

**Restricciones:**

- No confundir el origen cabinet con el destinatario.
- La entrega requiere adquisición previa y una acción de entrega, no solo un anuncio.

**Conductas prohibidas:**

- Inventar entidades, destinos o subtareas no solicitados.

**Variaciones aceptables:**

- Variar el texto de anuncios conservando su sentido.
- Usar identificadores internos consistentes sin cambiar el referente.

**Límites de verificación:**

Sin elementos especificados en la ficha.

**Condiciones iniciales:**

```json
{
  "location": "unknown",
  "holding": "nothing",
  "focus": false,
  "manipulation_enabled": true,
  "independent_request": true
}
```

**Supuestos del escenario:**

- Las entidades mencionadas son referencias del dominio; su detección y disponibilidad física no se evalúan.
- Cada orden se procesa sin conversación previa.

**Comprobaciones comunes del plan:**

- Acciones y parámetros dentro del contrato compartido.
- No añadir tareas ajenas; se admiten los cierres convencionales de retorno y comunicación.
- Referentes consistentes y dependencias de adquisición/entrega respetadas.
- Distinguir protocolo generado de operación física no observada.

**Notas existentes de revisión:**

- 2026-10-17: el investigador confirmó en la conversación haber revisado las 60 fichas y encontrarlas en orden; aprobación sin cambios de órdenes, objetivos ni criterios. Aprobación para desarrollo, no dictamen sobre salidas de modelos.

**Decisión del investigador:**

- [x] Aprobada sin cambios.
- [ ] Requiere correcciones.
- [ ] No aprobada.

**Correcciones u observaciones:**

Sin correcciones solicitadas.

**Revisor y fecha:** Investigador (usuario), 2026-10-17.

<details>
<summary>Metadatos y trazabilidad de la ficha original</summary>

```json
{
  "reference_status": "approved",
  "split": "development",
  "development_version": "0.2",
  "overlap_status": "coincidencia_detectada_v02",
  "overlap_audit_history": [
    {
      "development_version": "0.1",
      "input_audited": "Bring me a mug from the refrigerator.",
      "development_sha256": "02103490f89367add79ae9b6aea90e01ecd7f9def7cb32c24d9fb51e6b0b5c7b",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [
          10047
        ],
        "normalizador_real": [
          10047
        ]
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    },
    {
      "development_version": "0.2",
      "input_audited": "Bring me a mug from the cabinet.",
      "development_sha256": "4c1a356fa50ac317ad6b428c101a48183968a41e2771e2ad2bd7c622f61d4480",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "audit_path": "reports/evaluation/auditoria_desarrollo_v02.json",
      "audit_sha256": "f4d5c3c3088dc5bd9f61d6ebef4b33716401dd4014491585317a184e647e0346",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [
          4671
        ],
        "normalizador_real": [
          4671
        ]
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    }
  ],
  "revision_history": [
    {
      "version": "0.2",
      "previous_input": "Bring me a mug from the refrigerator.",
      "previous_goals_ref": [
        "go(refrigerator)",
        "find(mug, kind=object)",
        "take(mug)",
        "deliver(mug, to=me)"
      ],
      "reason": "Sustitución de las tres variantes de un grupo con coincidencias; nueva auditoría pendiente."
    }
  ],
  "planned_assessment": {
    "semantic": "no_ejecutado",
    "plan_contract": "no_ejecutado",
    "task_fulfillment": "no_ejecutado",
    "latency_ms": null
  }
}
```

</details>

## DEV-011

**Intención:** INT-04 · **Grupo:** entrega_operador · **Variante:** parafrasis · **Bloque:** funcional_y_linguistico

**Orden original:**

> Fetch a mug at the cabinet and deliver it to me.

**Propósito:** Origen y destinatario me

**Respuesta prevista:** `executable`.

**Objetivos propuestos:**

```text
go(cabinet)
find(mug, kind=object)
take(mug)
deliver(mug, to=me)
```

**Subtareas requeridas:**

- Buscar y adquirir mug en cabinet.
- Regresar al punto del operador y entregarle mug.

**Restricciones:**

- No confundir el origen cabinet con el destinatario.
- La entrega requiere adquisición previa y una acción de entrega, no solo un anuncio.

**Conductas prohibidas:**

- Inventar entidades, destinos o subtareas no solicitados.

**Variaciones aceptables:**

- Variar el texto de anuncios conservando su sentido.
- Usar identificadores internos consistentes sin cambiar el referente.

**Límites de verificación:**

Sin elementos especificados en la ficha.

**Condiciones iniciales:**

```json
{
  "location": "unknown",
  "holding": "nothing",
  "focus": false,
  "manipulation_enabled": true,
  "independent_request": true
}
```

**Supuestos del escenario:**

- Las entidades mencionadas son referencias del dominio; su detección y disponibilidad física no se evalúan.
- Cada orden se procesa sin conversación previa.

**Comprobaciones comunes del plan:**

- Acciones y parámetros dentro del contrato compartido.
- No añadir tareas ajenas; se admiten los cierres convencionales de retorno y comunicación.
- Referentes consistentes y dependencias de adquisición/entrega respetadas.
- Distinguir protocolo generado de operación física no observada.

**Notas existentes de revisión:**

- 2026-10-17: el investigador confirmó en la conversación haber revisado las 60 fichas y encontrarlas en orden; aprobación sin cambios de órdenes, objetivos ni criterios. Aprobación para desarrollo, no dictamen sobre salidas de modelos.

**Decisión del investigador:**

- [x] Aprobada sin cambios.
- [ ] Requiere correcciones.
- [ ] No aprobada.

**Correcciones u observaciones:**

Sin correcciones solicitadas.

**Revisor y fecha:** Investigador (usuario), 2026-10-17.

<details>
<summary>Metadatos y trazabilidad de la ficha original</summary>

```json
{
  "reference_status": "approved",
  "split": "development",
  "development_version": "0.2",
  "overlap_status": "sin_coincidencia_detectada_v02",
  "overlap_audit_history": [
    {
      "development_version": "0.1",
      "input_audited": "Fetch a mug at the refrigerator and deliver it to me.",
      "development_sha256": "02103490f89367add79ae9b6aea90e01ecd7f9def7cb32c24d9fb51e6b0b5c7b",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    },
    {
      "development_version": "0.2",
      "input_audited": "Fetch a mug at the cabinet and deliver it to me.",
      "development_sha256": "4c1a356fa50ac317ad6b428c101a48183968a41e2771e2ad2bd7c622f61d4480",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "audit_path": "reports/evaluation/auditoria_desarrollo_v02.json",
      "audit_sha256": "f4d5c3c3088dc5bd9f61d6ebef4b33716401dd4014491585317a184e647e0346",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    }
  ],
  "revision_history": [
    {
      "version": "0.2",
      "previous_input": "Fetch a mug at the refrigerator and deliver it to me.",
      "previous_goals_ref": [
        "go(refrigerator)",
        "find(mug, kind=object)",
        "take(mug)",
        "deliver(mug, to=me)"
      ],
      "reason": "Sustitución de las tres variantes de un grupo con coincidencias; nueva auditoría pendiente."
    }
  ],
  "planned_assessment": {
    "semantic": "no_ejecutado",
    "plan_contract": "no_ejecutado",
    "task_fulfillment": "no_ejecutado",
    "latency_ms": null
  }
}
```

</details>

## DEV-012

**Intención:** INT-04 · **Grupo:** entrega_operador · **Variante:** ruido_leve · **Bloque:** funcional_y_linguistico

**Orden original:**

> please bring me a mug from the cabnet

**Propósito:** Origen y destinatario me

**Respuesta prevista:** `executable`.

**Objetivos propuestos:**

```text
go(cabinet)
find(mug, kind=object)
take(mug)
deliver(mug, to=me)
```

**Subtareas requeridas:**

- Buscar y adquirir mug en cabinet.
- Regresar al punto del operador y entregarle mug.

**Restricciones:**

- No confundir el origen cabinet con el destinatario.
- La entrega requiere adquisición previa y una acción de entrega, no solo un anuncio.

**Conductas prohibidas:**

- Inventar entidades, destinos o subtareas no solicitados.

**Variaciones aceptables:**

- Variar el texto de anuncios conservando su sentido.
- Usar identificadores internos consistentes sin cambiar el referente.

**Límites de verificación:**

Sin elementos especificados en la ficha.

**Condiciones iniciales:**

```json
{
  "location": "unknown",
  "holding": "nothing",
  "focus": false,
  "manipulation_enabled": true,
  "independent_request": true
}
```

**Supuestos del escenario:**

- Las entidades mencionadas son referencias del dominio; su detección y disponibilidad física no se evalúan.
- Cada orden se procesa sin conversación previa.

**Comprobaciones comunes del plan:**

- Acciones y parámetros dentro del contrato compartido.
- No añadir tareas ajenas; se admiten los cierres convencionales de retorno y comunicación.
- Referentes consistentes y dependencias de adquisición/entrega respetadas.
- Distinguir protocolo generado de operación física no observada.

**Notas existentes de revisión:**

- 2026-10-17: el investigador confirmó en la conversación haber revisado las 60 fichas y encontrarlas en orden; aprobación sin cambios de órdenes, objetivos ni criterios. Aprobación para desarrollo, no dictamen sobre salidas de modelos.

**Decisión del investigador:**

- [x] Aprobada sin cambios.
- [ ] Requiere correcciones.
- [ ] No aprobada.

**Correcciones u observaciones:**

Sin correcciones solicitadas.

**Revisor y fecha:** Investigador (usuario), 2026-10-17.

<details>
<summary>Metadatos y trazabilidad de la ficha original</summary>

```json
{
  "reference_status": "approved",
  "split": "development",
  "development_version": "0.2",
  "overlap_status": "coincidencia_detectada_v02",
  "overlap_audit_history": [
    {
      "development_version": "0.1",
      "input_audited": "please bring me a mug from the refridgerator",
      "development_sha256": "02103490f89367add79ae9b6aea90e01ecd7f9def7cb32c24d9fb51e6b0b5c7b",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": [
          10047
        ]
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    },
    {
      "development_version": "0.2",
      "input_audited": "please bring me a mug from the cabnet",
      "development_sha256": "4c1a356fa50ac317ad6b428c101a48183968a41e2771e2ad2bd7c622f61d4480",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "audit_path": "reports/evaluation/auditoria_desarrollo_v02.json",
      "audit_sha256": "f4d5c3c3088dc5bd9f61d6ebef4b33716401dd4014491585317a184e647e0346",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": [
          4671
        ]
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    }
  ],
  "revision_history": [
    {
      "version": "0.2",
      "previous_input": "please bring me a mug from the refridgerator",
      "previous_goals_ref": [
        "go(refrigerator)",
        "find(mug, kind=object)",
        "take(mug)",
        "deliver(mug, to=me)"
      ],
      "reason": "Sustitución de las tres variantes de un grupo con coincidencias; nueva auditoría pendiente."
    }
  ],
  "planned_assessment": {
    "semantic": "no_ejecutado",
    "plan_contract": "no_ejecutado",
    "task_fulfillment": "no_ejecutado",
    "latency_ms": null
  }
}
```

</details>

## DEV-013

**Intención:** INT-05 · **Grupo:** transporte_ubicaciones · **Variante:** canonica · **Bloque:** funcional_y_linguistico

**Orden original:**

> Bring a bowl from the bed to the storage rack.

**Propósito:** Destino navegable de colocación

**Respuesta prevista:** `executable`.

**Objetivos propuestos:**

```text
go(bed)
find(bowl, kind=object)
take(bowl)
place(bowl, at=storage rack)
```

**Subtareas requeridas:**

- Buscar y adquirir bowl en bed.
- Trasladarlo a storage rack y colocarlo allí.

**Restricciones:**

- bed es el origen y storage rack es el destino; no invertirlos.
- Llegar al destino antes de colocar el objeto.

**Conductas prohibidas:**

- Inventar entidades, destinos o subtareas no solicitados.

**Variaciones aceptables:**

- Variar el texto de anuncios conservando su sentido.
- Usar identificadores internos consistentes sin cambiar el referente.

**Límites de verificación:**

Sin elementos especificados en la ficha.

**Condiciones iniciales:**

```json
{
  "location": "unknown",
  "holding": "nothing",
  "focus": false,
  "manipulation_enabled": true,
  "independent_request": true
}
```

**Supuestos del escenario:**

- Las entidades mencionadas son referencias del dominio; su detección y disponibilidad física no se evalúan.
- Cada orden se procesa sin conversación previa.

**Comprobaciones comunes del plan:**

- Acciones y parámetros dentro del contrato compartido.
- No añadir tareas ajenas; se admiten los cierres convencionales de retorno y comunicación.
- Referentes consistentes y dependencias de adquisición/entrega respetadas.
- Distinguir protocolo generado de operación física no observada.

**Notas existentes de revisión:**

- 2026-10-17: el investigador confirmó en la conversación haber revisado las 60 fichas y encontrarlas en orden; aprobación sin cambios de órdenes, objetivos ni criterios. Aprobación para desarrollo, no dictamen sobre salidas de modelos.

**Decisión del investigador:**

- [x] Aprobada sin cambios.
- [ ] Requiere correcciones.
- [ ] No aprobada.

**Correcciones u observaciones:**

Sin correcciones solicitadas.

**Revisor y fecha:** Investigador (usuario), 2026-10-17.

<details>
<summary>Metadatos y trazabilidad de la ficha original</summary>

```json
{
  "reference_status": "approved",
  "split": "development",
  "development_version": "0.2",
  "overlap_status": "sin_coincidencia_detectada_v02",
  "overlap_audit_history": [
    {
      "development_version": "0.1",
      "input_audited": "Bring a bowl from the bed to the storage rack.",
      "development_sha256": "02103490f89367add79ae9b6aea90e01ecd7f9def7cb32c24d9fb51e6b0b5c7b",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    },
    {
      "development_version": "0.2",
      "input_audited": "Bring a bowl from the bed to the storage rack.",
      "development_sha256": "4c1a356fa50ac317ad6b428c101a48183968a41e2771e2ad2bd7c622f61d4480",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "audit_path": "reports/evaluation/auditoria_desarrollo_v02.json",
      "audit_sha256": "f4d5c3c3088dc5bd9f61d6ebef4b33716401dd4014491585317a184e647e0346",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    }
  ],
  "planned_assessment": {
    "semantic": "no_ejecutado",
    "plan_contract": "no_ejecutado",
    "task_fulfillment": "no_ejecutado",
    "latency_ms": null
  }
}
```

</details>

## DEV-014

**Intención:** INT-05 · **Grupo:** transporte_ubicaciones · **Variante:** parafrasis · **Bloque:** funcional_y_linguistico

**Orden original:**

> Collect a bowl at the bed and leave it at the storage rack.

**Propósito:** Destino navegable de colocación

**Respuesta prevista:** `executable`.

**Objetivos propuestos:**

```text
go(bed)
find(bowl, kind=object)
take(bowl)
place(bowl, at=storage rack)
```

**Subtareas requeridas:**

- Buscar y adquirir bowl en bed.
- Trasladarlo a storage rack y colocarlo allí.

**Restricciones:**

- bed es el origen y storage rack es el destino; no invertirlos.
- Llegar al destino antes de colocar el objeto.

**Conductas prohibidas:**

- Inventar entidades, destinos o subtareas no solicitados.

**Variaciones aceptables:**

- Variar el texto de anuncios conservando su sentido.
- Usar identificadores internos consistentes sin cambiar el referente.

**Límites de verificación:**

Sin elementos especificados en la ficha.

**Condiciones iniciales:**

```json
{
  "location": "unknown",
  "holding": "nothing",
  "focus": false,
  "manipulation_enabled": true,
  "independent_request": true
}
```

**Supuestos del escenario:**

- Las entidades mencionadas son referencias del dominio; su detección y disponibilidad física no se evalúan.
- Cada orden se procesa sin conversación previa.

**Comprobaciones comunes del plan:**

- Acciones y parámetros dentro del contrato compartido.
- No añadir tareas ajenas; se admiten los cierres convencionales de retorno y comunicación.
- Referentes consistentes y dependencias de adquisición/entrega respetadas.
- Distinguir protocolo generado de operación física no observada.

**Notas existentes de revisión:**

- 2026-10-17: el investigador confirmó en la conversación haber revisado las 60 fichas y encontrarlas en orden; aprobación sin cambios de órdenes, objetivos ni criterios. Aprobación para desarrollo, no dictamen sobre salidas de modelos.

**Decisión del investigador:**

- [x] Aprobada sin cambios.
- [ ] Requiere correcciones.
- [ ] No aprobada.

**Correcciones u observaciones:**

Sin correcciones solicitadas.

**Revisor y fecha:** Investigador (usuario), 2026-10-17.

<details>
<summary>Metadatos y trazabilidad de la ficha original</summary>

```json
{
  "reference_status": "approved",
  "split": "development",
  "development_version": "0.2",
  "overlap_status": "sin_coincidencia_detectada_v02",
  "overlap_audit_history": [
    {
      "development_version": "0.1",
      "input_audited": "Collect a bowl at the bed and leave it at the storage rack.",
      "development_sha256": "02103490f89367add79ae9b6aea90e01ecd7f9def7cb32c24d9fb51e6b0b5c7b",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    },
    {
      "development_version": "0.2",
      "input_audited": "Collect a bowl at the bed and leave it at the storage rack.",
      "development_sha256": "4c1a356fa50ac317ad6b428c101a48183968a41e2771e2ad2bd7c622f61d4480",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "audit_path": "reports/evaluation/auditoria_desarrollo_v02.json",
      "audit_sha256": "f4d5c3c3088dc5bd9f61d6ebef4b33716401dd4014491585317a184e647e0346",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    }
  ],
  "planned_assessment": {
    "semantic": "no_ejecutado",
    "plan_contract": "no_ejecutado",
    "task_fulfillment": "no_ejecutado",
    "latency_ms": null
  }
}
```

</details>

## DEV-015

**Intención:** INT-05 · **Grupo:** transporte_ubicaciones · **Variante:** ruido_leve · **Bloque:** funcional_y_linguistico

**Orden original:**

> please bring a bowl from the bed to the storage  rack

**Propósito:** Destino navegable de colocación

**Respuesta prevista:** `executable`.

**Objetivos propuestos:**

```text
go(bed)
find(bowl, kind=object)
take(bowl)
place(bowl, at=storage rack)
```

**Subtareas requeridas:**

- Buscar y adquirir bowl en bed.
- Trasladarlo a storage rack y colocarlo allí.

**Restricciones:**

- bed es el origen y storage rack es el destino; no invertirlos.
- Llegar al destino antes de colocar el objeto.

**Conductas prohibidas:**

- Inventar entidades, destinos o subtareas no solicitados.

**Variaciones aceptables:**

- Variar el texto de anuncios conservando su sentido.
- Usar identificadores internos consistentes sin cambiar el referente.

**Límites de verificación:**

Sin elementos especificados en la ficha.

**Condiciones iniciales:**

```json
{
  "location": "unknown",
  "holding": "nothing",
  "focus": false,
  "manipulation_enabled": true,
  "independent_request": true
}
```

**Supuestos del escenario:**

- Las entidades mencionadas son referencias del dominio; su detección y disponibilidad física no se evalúan.
- Cada orden se procesa sin conversación previa.

**Comprobaciones comunes del plan:**

- Acciones y parámetros dentro del contrato compartido.
- No añadir tareas ajenas; se admiten los cierres convencionales de retorno y comunicación.
- Referentes consistentes y dependencias de adquisición/entrega respetadas.
- Distinguir protocolo generado de operación física no observada.

**Notas existentes de revisión:**

- 2026-10-17: el investigador confirmó en la conversación haber revisado las 60 fichas y encontrarlas en orden; aprobación sin cambios de órdenes, objetivos ni criterios. Aprobación para desarrollo, no dictamen sobre salidas de modelos.

**Decisión del investigador:**

- [x] Aprobada sin cambios.
- [ ] Requiere correcciones.
- [ ] No aprobada.

**Correcciones u observaciones:**

Sin correcciones solicitadas.

**Revisor y fecha:** Investigador (usuario), 2026-10-17.

<details>
<summary>Metadatos y trazabilidad de la ficha original</summary>

```json
{
  "reference_status": "approved",
  "split": "development",
  "development_version": "0.2",
  "overlap_status": "sin_coincidencia_detectada_v02",
  "overlap_audit_history": [
    {
      "development_version": "0.1",
      "input_audited": "please bring a bowl from the bed to the storage  rack",
      "development_sha256": "02103490f89367add79ae9b6aea90e01ecd7f9def7cb32c24d9fb51e6b0b5c7b",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    },
    {
      "development_version": "0.2",
      "input_audited": "please bring a bowl from the bed to the storage  rack",
      "development_sha256": "4c1a356fa50ac317ad6b428c101a48183968a41e2771e2ad2bd7c622f61d4480",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "audit_path": "reports/evaluation/auditoria_desarrollo_v02.json",
      "audit_sha256": "f4d5c3c3088dc5bd9f61d6ebef4b33716401dd4014491585317a184e647e0346",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    }
  ],
  "planned_assessment": {
    "semantic": "no_ejecutado",
    "plan_contract": "no_ejecutado",
    "task_fulfillment": "no_ejecutado",
    "latency_ms": null
  }
}
```

</details>

## DEV-016

**Intención:** INT-06 · **Grupo:** colocacion_local · **Variante:** canonica · **Bloque:** funcional_y_linguistico

**Orden original:**

> In the kitchen, find a cup, take it, and put it on the table.

**Propósito:** Soporte local y relación on

**Respuesta prevista:** `executable`.

**Objetivos propuestos:**

```text
go(kitchen)
find(cup, kind=object)
take(cup)
place(cup, on=table)
```

**Subtareas requeridas:**

- Buscar y adquirir cup en kitchen.
- Colocar cup sobre la mesa local de kitchen.

**Restricciones:**

- table es un soporte local, no una habitación ni un punto de navegación adicional.
- No confundir colocación con entrega a una persona.

**Conductas prohibidas:**

- Inventar entidades, destinos o subtareas no solicitados.

**Variaciones aceptables:**

- Variar el texto de anuncios conservando su sentido.
- Usar identificadores internos consistentes sin cambiar el referente.

**Límites de verificación:**

- La regla place puede asignar el soporte a location; revisar la representación del estado sin inferir desplazamiento físico.

**Condiciones iniciales:**

```json
{
  "location": "unknown",
  "holding": "nothing",
  "focus": false,
  "manipulation_enabled": true,
  "independent_request": true
}
```

**Supuestos del escenario:**

- Las entidades mencionadas son referencias del dominio; su detección y disponibilidad física no se evalúan.
- Cada orden se procesa sin conversación previa.

**Comprobaciones comunes del plan:**

- Acciones y parámetros dentro del contrato compartido.
- No añadir tareas ajenas; se admiten los cierres convencionales de retorno y comunicación.
- Referentes consistentes y dependencias de adquisición/entrega respetadas.
- Distinguir protocolo generado de operación física no observada.

**Notas existentes de revisión:**

- 2026-10-17: el investigador confirmó en la conversación haber revisado las 60 fichas y encontrarlas en orden; aprobación sin cambios de órdenes, objetivos ni criterios. Aprobación para desarrollo, no dictamen sobre salidas de modelos.

**Decisión del investigador:**

- [x] Aprobada sin cambios.
- [ ] Requiere correcciones.
- [ ] No aprobada.

**Correcciones u observaciones:**

Sin correcciones solicitadas.

**Revisor y fecha:** Investigador (usuario), 2026-10-17.

<details>
<summary>Metadatos y trazabilidad de la ficha original</summary>

```json
{
  "reference_status": "approved",
  "split": "development",
  "development_version": "0.2",
  "overlap_status": "sin_coincidencia_detectada_v02",
  "overlap_audit_history": [
    {
      "development_version": "0.1",
      "input_audited": "In the kitchen, find a cup, take it, and put it on the table.",
      "development_sha256": "02103490f89367add79ae9b6aea90e01ecd7f9def7cb32c24d9fb51e6b0b5c7b",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    },
    {
      "development_version": "0.2",
      "input_audited": "In the kitchen, find a cup, take it, and put it on the table.",
      "development_sha256": "4c1a356fa50ac317ad6b428c101a48183968a41e2771e2ad2bd7c622f61d4480",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "audit_path": "reports/evaluation/auditoria_desarrollo_v02.json",
      "audit_sha256": "f4d5c3c3088dc5bd9f61d6ebef4b33716401dd4014491585317a184e647e0346",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    }
  ],
  "planned_assessment": {
    "semantic": "no_ejecutado",
    "plan_contract": "no_ejecutado",
    "task_fulfillment": "no_ejecutado",
    "latency_ms": null
  }
}
```

</details>

## DEV-017

**Intención:** INT-06 · **Grupo:** colocacion_local · **Variante:** parafrasis · **Bloque:** funcional_y_linguistico

**Orden original:**

> Locate a cup in the kitchen and pick it up, then place it on the table there.

**Propósito:** Soporte local y relación on

**Respuesta prevista:** `executable`.

**Objetivos propuestos:**

```text
go(kitchen)
find(cup, kind=object)
take(cup)
place(cup, on=table)
```

**Subtareas requeridas:**

- Buscar y adquirir cup en kitchen.
- Colocar cup sobre la mesa local de kitchen.

**Restricciones:**

- table es un soporte local, no una habitación ni un punto de navegación adicional.
- No confundir colocación con entrega a una persona.

**Conductas prohibidas:**

- Inventar entidades, destinos o subtareas no solicitados.

**Variaciones aceptables:**

- Variar el texto de anuncios conservando su sentido.
- Usar identificadores internos consistentes sin cambiar el referente.

**Límites de verificación:**

- La regla place puede asignar el soporte a location; revisar la representación del estado sin inferir desplazamiento físico.

**Condiciones iniciales:**

```json
{
  "location": "unknown",
  "holding": "nothing",
  "focus": false,
  "manipulation_enabled": true,
  "independent_request": true
}
```

**Supuestos del escenario:**

- Las entidades mencionadas son referencias del dominio; su detección y disponibilidad física no se evalúan.
- Cada orden se procesa sin conversación previa.

**Comprobaciones comunes del plan:**

- Acciones y parámetros dentro del contrato compartido.
- No añadir tareas ajenas; se admiten los cierres convencionales de retorno y comunicación.
- Referentes consistentes y dependencias de adquisición/entrega respetadas.
- Distinguir protocolo generado de operación física no observada.

**Notas existentes de revisión:**

- 2026-10-17: el investigador confirmó en la conversación haber revisado las 60 fichas y encontrarlas en orden; aprobación sin cambios de órdenes, objetivos ni criterios. Aprobación para desarrollo, no dictamen sobre salidas de modelos.

**Decisión del investigador:**

- [x] Aprobada sin cambios.
- [ ] Requiere correcciones.
- [ ] No aprobada.

**Correcciones u observaciones:**

Sin correcciones solicitadas.

**Revisor y fecha:** Investigador (usuario), 2026-10-17.

<details>
<summary>Metadatos y trazabilidad de la ficha original</summary>

```json
{
  "reference_status": "approved",
  "split": "development",
  "development_version": "0.2",
  "overlap_status": "sin_coincidencia_detectada_v02",
  "overlap_audit_history": [
    {
      "development_version": "0.1",
      "input_audited": "Locate a cup in the kitchen and pick it up, then place it on the table there.",
      "development_sha256": "02103490f89367add79ae9b6aea90e01ecd7f9def7cb32c24d9fb51e6b0b5c7b",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    },
    {
      "development_version": "0.2",
      "input_audited": "Locate a cup in the kitchen and pick it up, then place it on the table there.",
      "development_sha256": "4c1a356fa50ac317ad6b428c101a48183968a41e2771e2ad2bd7c622f61d4480",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "audit_path": "reports/evaluation/auditoria_desarrollo_v02.json",
      "audit_sha256": "f4d5c3c3088dc5bd9f61d6ebef4b33716401dd4014491585317a184e647e0346",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    }
  ],
  "planned_assessment": {
    "semantic": "no_ejecutado",
    "plan_contract": "no_ejecutado",
    "task_fulfillment": "no_ejecutado",
    "latency_ms": null
  }
}
```

</details>

## DEV-018

**Intención:** INT-06 · **Grupo:** colocacion_local · **Variante:** ruido_leve · **Bloque:** funcional_y_linguistico

**Orden original:**

> in the kichen find a cup take it and put it on the table please

**Propósito:** Soporte local y relación on

**Respuesta prevista:** `executable`.

**Objetivos propuestos:**

```text
go(kitchen)
find(cup, kind=object)
take(cup)
place(cup, on=table)
```

**Subtareas requeridas:**

- Buscar y adquirir cup en kitchen.
- Colocar cup sobre la mesa local de kitchen.

**Restricciones:**

- table es un soporte local, no una habitación ni un punto de navegación adicional.
- No confundir colocación con entrega a una persona.

**Conductas prohibidas:**

- Inventar entidades, destinos o subtareas no solicitados.

**Variaciones aceptables:**

- Variar el texto de anuncios conservando su sentido.
- Usar identificadores internos consistentes sin cambiar el referente.

**Límites de verificación:**

- La regla place puede asignar el soporte a location; revisar la representación del estado sin inferir desplazamiento físico.

**Condiciones iniciales:**

```json
{
  "location": "unknown",
  "holding": "nothing",
  "focus": false,
  "manipulation_enabled": true,
  "independent_request": true
}
```

**Supuestos del escenario:**

- Las entidades mencionadas son referencias del dominio; su detección y disponibilidad física no se evalúan.
- Cada orden se procesa sin conversación previa.

**Comprobaciones comunes del plan:**

- Acciones y parámetros dentro del contrato compartido.
- No añadir tareas ajenas; se admiten los cierres convencionales de retorno y comunicación.
- Referentes consistentes y dependencias de adquisición/entrega respetadas.
- Distinguir protocolo generado de operación física no observada.

**Notas existentes de revisión:**

- 2026-10-17: el investigador confirmó en la conversación haber revisado las 60 fichas y encontrarlas en orden; aprobación sin cambios de órdenes, objetivos ni criterios. Aprobación para desarrollo, no dictamen sobre salidas de modelos.

**Decisión del investigador:**

- [x] Aprobada sin cambios.
- [ ] Requiere correcciones.
- [ ] No aprobada.

**Correcciones u observaciones:**

Sin correcciones solicitadas.

**Revisor y fecha:** Investigador (usuario), 2026-10-17.

<details>
<summary>Metadatos y trazabilidad de la ficha original</summary>

```json
{
  "reference_status": "approved",
  "split": "development",
  "development_version": "0.2",
  "overlap_status": "sin_coincidencia_detectada_v02",
  "overlap_audit_history": [
    {
      "development_version": "0.1",
      "input_audited": "in the kichen find a cup take it and put it on the table please",
      "development_sha256": "02103490f89367add79ae9b6aea90e01ecd7f9def7cb32c24d9fb51e6b0b5c7b",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    },
    {
      "development_version": "0.2",
      "input_audited": "in the kichen find a cup take it and put it on the table please",
      "development_sha256": "4c1a356fa50ac317ad6b428c101a48183968a41e2771e2ad2bd7c622f61d4480",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "audit_path": "reports/evaluation/auditoria_desarrollo_v02.json",
      "audit_sha256": "f4d5c3c3088dc5bd9f61d6ebef4b33716401dd4014491585317a184e647e0346",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    }
  ],
  "planned_assessment": {
    "semantic": "no_ejecutado",
    "plan_contract": "no_ejecutado",
    "task_fulfillment": "no_ejecutado",
    "latency_ms": null
  }
}
```

</details>

## DEV-019

**Intención:** INT-07 · **Grupo:** busqueda_persona_nombre · **Variante:** canonica · **Bloque:** funcional_y_linguistico

**Orden original:**

> Find Robin in the office.

**Propósito:** Nombre propio y tipo person

**Respuesta prevista:** `executable`.

**Objetivos propuestos:**

```text
go(office)
find(Robin, kind=person)
```

**Subtareas requeridas:**

- Ir a office y localizar a la persona llamada Robin.

**Restricciones:**

- No tratar Robin como objeto o ubicación.
- Buscar a anybody sin un mecanismo de identificación no acredita encontrar a Robin.

**Conductas prohibidas:**

- Inventar entidades, destinos o subtareas no solicitados.

**Variaciones aceptables:**

- Variar el texto de anuncios conservando su sentido.
- Usar identificadores internos consistentes sin cambiar el referente.

**Límites de verificación:**

- Separar conformidad con el protocolo ask_name/listen de la verificación efectiva del nombre: la coincidencia de identidad requiere revisión del contrato del ejecutor.

**Condiciones iniciales:**

```json
{
  "location": "unknown",
  "holding": "nothing",
  "focus": false,
  "manipulation_enabled": true,
  "independent_request": true
}
```

**Supuestos del escenario:**

- Las entidades mencionadas son referencias del dominio; su detección y disponibilidad física no se evalúan.
- Cada orden se procesa sin conversación previa.

**Comprobaciones comunes del plan:**

- Acciones y parámetros dentro del contrato compartido.
- No añadir tareas ajenas; se admiten los cierres convencionales de retorno y comunicación.
- Referentes consistentes y dependencias de adquisición/entrega respetadas.
- Distinguir protocolo generado de operación física no observada.

**Notas existentes de revisión:**

- 2026-10-17: el investigador confirmó en la conversación haber revisado las 60 fichas y encontrarlas en orden; aprobación sin cambios de órdenes, objetivos ni criterios. Aprobación para desarrollo, no dictamen sobre salidas de modelos.

**Decisión del investigador:**

- [x] Aprobada sin cambios.
- [ ] Requiere correcciones.
- [ ] No aprobada.

**Correcciones u observaciones:**

Sin correcciones solicitadas.

**Revisor y fecha:** Investigador (usuario), 2026-10-17.

<details>
<summary>Metadatos y trazabilidad de la ficha original</summary>

```json
{
  "reference_status": "approved",
  "split": "development",
  "development_version": "0.2",
  "overlap_status": "sin_coincidencia_detectada_v02",
  "overlap_audit_history": [
    {
      "development_version": "0.1",
      "input_audited": "Find Robin in the office.",
      "development_sha256": "02103490f89367add79ae9b6aea90e01ecd7f9def7cb32c24d9fb51e6b0b5c7b",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    },
    {
      "development_version": "0.2",
      "input_audited": "Find Robin in the office.",
      "development_sha256": "4c1a356fa50ac317ad6b428c101a48183968a41e2771e2ad2bd7c622f61d4480",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "audit_path": "reports/evaluation/auditoria_desarrollo_v02.json",
      "audit_sha256": "f4d5c3c3088dc5bd9f61d6ebef4b33716401dd4014491585317a184e647e0346",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    }
  ],
  "planned_assessment": {
    "semantic": "no_ejecutado",
    "plan_contract": "no_ejecutado",
    "task_fulfillment": "no_ejecutado",
    "latency_ms": null
  }
}
```

</details>

## DEV-020

**Intención:** INT-07 · **Grupo:** busqueda_persona_nombre · **Variante:** parafrasis · **Bloque:** funcional_y_linguistico

**Orden original:**

> Look for Robin inside the office.

**Propósito:** Nombre propio y tipo person

**Respuesta prevista:** `executable`.

**Objetivos propuestos:**

```text
go(office)
find(Robin, kind=person)
```

**Subtareas requeridas:**

- Ir a office y localizar a la persona llamada Robin.

**Restricciones:**

- No tratar Robin como objeto o ubicación.
- Buscar a anybody sin un mecanismo de identificación no acredita encontrar a Robin.

**Conductas prohibidas:**

- Inventar entidades, destinos o subtareas no solicitados.

**Variaciones aceptables:**

- Variar el texto de anuncios conservando su sentido.
- Usar identificadores internos consistentes sin cambiar el referente.

**Límites de verificación:**

- Separar conformidad con el protocolo ask_name/listen de la verificación efectiva del nombre: la coincidencia de identidad requiere revisión del contrato del ejecutor.

**Condiciones iniciales:**

```json
{
  "location": "unknown",
  "holding": "nothing",
  "focus": false,
  "manipulation_enabled": true,
  "independent_request": true
}
```

**Supuestos del escenario:**

- Las entidades mencionadas son referencias del dominio; su detección y disponibilidad física no se evalúan.
- Cada orden se procesa sin conversación previa.

**Comprobaciones comunes del plan:**

- Acciones y parámetros dentro del contrato compartido.
- No añadir tareas ajenas; se admiten los cierres convencionales de retorno y comunicación.
- Referentes consistentes y dependencias de adquisición/entrega respetadas.
- Distinguir protocolo generado de operación física no observada.

**Notas existentes de revisión:**

- 2026-10-17: el investigador confirmó en la conversación haber revisado las 60 fichas y encontrarlas en orden; aprobación sin cambios de órdenes, objetivos ni criterios. Aprobación para desarrollo, no dictamen sobre salidas de modelos.

**Decisión del investigador:**

- [x] Aprobada sin cambios.
- [ ] Requiere correcciones.
- [ ] No aprobada.

**Correcciones u observaciones:**

Sin correcciones solicitadas.

**Revisor y fecha:** Investigador (usuario), 2026-10-17.

<details>
<summary>Metadatos y trazabilidad de la ficha original</summary>

```json
{
  "reference_status": "approved",
  "split": "development",
  "development_version": "0.2",
  "overlap_status": "sin_coincidencia_detectada_v02",
  "overlap_audit_history": [
    {
      "development_version": "0.1",
      "input_audited": "Look for Robin inside the office.",
      "development_sha256": "02103490f89367add79ae9b6aea90e01ecd7f9def7cb32c24d9fb51e6b0b5c7b",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    },
    {
      "development_version": "0.2",
      "input_audited": "Look for Robin inside the office.",
      "development_sha256": "4c1a356fa50ac317ad6b428c101a48183968a41e2771e2ad2bd7c622f61d4480",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "audit_path": "reports/evaluation/auditoria_desarrollo_v02.json",
      "audit_sha256": "f4d5c3c3088dc5bd9f61d6ebef4b33716401dd4014491585317a184e647e0346",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    }
  ],
  "planned_assessment": {
    "semantic": "no_ejecutado",
    "plan_contract": "no_ejecutado",
    "task_fulfillment": "no_ejecutado",
    "latency_ms": null
  }
}
```

</details>

## DEV-021

**Intención:** INT-07 · **Grupo:** busqueda_persona_nombre · **Variante:** ruido_leve · **Bloque:** funcional_y_linguistico

**Orden original:**

> please find Robin in the ofice

**Propósito:** Nombre propio y tipo person

**Respuesta prevista:** `executable`.

**Objetivos propuestos:**

```text
go(office)
find(Robin, kind=person)
```

**Subtareas requeridas:**

- Ir a office y localizar a la persona llamada Robin.

**Restricciones:**

- No tratar Robin como objeto o ubicación.
- Buscar a anybody sin un mecanismo de identificación no acredita encontrar a Robin.

**Conductas prohibidas:**

- Inventar entidades, destinos o subtareas no solicitados.

**Variaciones aceptables:**

- Variar el texto de anuncios conservando su sentido.
- Usar identificadores internos consistentes sin cambiar el referente.

**Límites de verificación:**

- Separar conformidad con el protocolo ask_name/listen de la verificación efectiva del nombre: la coincidencia de identidad requiere revisión del contrato del ejecutor.

**Condiciones iniciales:**

```json
{
  "location": "unknown",
  "holding": "nothing",
  "focus": false,
  "manipulation_enabled": true,
  "independent_request": true
}
```

**Supuestos del escenario:**

- Las entidades mencionadas son referencias del dominio; su detección y disponibilidad física no se evalúan.
- Cada orden se procesa sin conversación previa.

**Comprobaciones comunes del plan:**

- Acciones y parámetros dentro del contrato compartido.
- No añadir tareas ajenas; se admiten los cierres convencionales de retorno y comunicación.
- Referentes consistentes y dependencias de adquisición/entrega respetadas.
- Distinguir protocolo generado de operación física no observada.

**Notas existentes de revisión:**

- 2026-10-17: el investigador confirmó en la conversación haber revisado las 60 fichas y encontrarlas en orden; aprobación sin cambios de órdenes, objetivos ni criterios. Aprobación para desarrollo, no dictamen sobre salidas de modelos.

**Decisión del investigador:**

- [x] Aprobada sin cambios.
- [ ] Requiere correcciones.
- [ ] No aprobada.

**Correcciones u observaciones:**

Sin correcciones solicitadas.

**Revisor y fecha:** Investigador (usuario), 2026-10-17.

<details>
<summary>Metadatos y trazabilidad de la ficha original</summary>

```json
{
  "reference_status": "approved",
  "split": "development",
  "development_version": "0.2",
  "overlap_status": "sin_coincidencia_detectada_v02",
  "overlap_audit_history": [
    {
      "development_version": "0.1",
      "input_audited": "please find Robin in the ofice",
      "development_sha256": "02103490f89367add79ae9b6aea90e01ecd7f9def7cb32c24d9fb51e6b0b5c7b",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    },
    {
      "development_version": "0.2",
      "input_audited": "please find Robin in the ofice",
      "development_sha256": "4c1a356fa50ac317ad6b428c101a48183968a41e2771e2ad2bd7c622f61d4480",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "audit_path": "reports/evaluation/auditoria_desarrollo_v02.json",
      "audit_sha256": "f4d5c3c3088dc5bd9f61d6ebef4b33716401dd4014491585317a184e647e0346",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    }
  ],
  "planned_assessment": {
    "semantic": "no_ejecutado",
    "plan_contract": "no_ejecutado",
    "task_fulfillment": "no_ejecutado",
    "latency_ms": null
  }
}
```

</details>

## DEV-022

**Intención:** INT-08 · **Grupo:** guia · **Variante:** canonica · **Bloque:** funcional_y_linguistico

**Orden original:**

> Find Morgan in the kitchen and guide them to the entrance.

**Propósito:** Origen, persona y destino

**Respuesta prevista:** `executable`.

**Objetivos propuestos:**

```text
go(kitchen)
find(Morgan, kind=person)
guide(Morgan, to=entrance)
```

**Subtareas requeridas:**

- Localizar a Morgan en kitchen.
- Indicar a Morgan que siga al robot y guiarle a entrance.

**Restricciones:**

- Resolver them como Morgan; conservar entrance como destino.
- Un desplazamiento sin vincular a la persona no cubre por sí solo la subtarea de guía.

**Conductas prohibidas:**

- Inventar entidades, destinos o subtareas no solicitados.

**Variaciones aceptables:**

- Variar el texto de anuncios conservando su sentido.
- Usar identificadores internos consistentes sin cambiar el referente.

**Límites de verificación:**

- Identidad de la persona sujeta al contrato de identificación; presencia física durante la guía fuera del alcance.

**Condiciones iniciales:**

```json
{
  "location": "unknown",
  "holding": "nothing",
  "focus": false,
  "manipulation_enabled": true,
  "independent_request": true
}
```

**Supuestos del escenario:**

- Las entidades mencionadas son referencias del dominio; su detección y disponibilidad física no se evalúan.
- Cada orden se procesa sin conversación previa.

**Comprobaciones comunes del plan:**

- Acciones y parámetros dentro del contrato compartido.
- No añadir tareas ajenas; se admiten los cierres convencionales de retorno y comunicación.
- Referentes consistentes y dependencias de adquisición/entrega respetadas.
- Distinguir protocolo generado de operación física no observada.

**Notas existentes de revisión:**

- 2026-10-17: el investigador confirmó en la conversación haber revisado las 60 fichas y encontrarlas en orden; aprobación sin cambios de órdenes, objetivos ni criterios. Aprobación para desarrollo, no dictamen sobre salidas de modelos.

**Decisión del investigador:**

- [x] Aprobada sin cambios.
- [ ] Requiere correcciones.
- [ ] No aprobada.

**Correcciones u observaciones:**

Sin correcciones solicitadas.

**Revisor y fecha:** Investigador (usuario), 2026-10-17.

<details>
<summary>Metadatos y trazabilidad de la ficha original</summary>

```json
{
  "reference_status": "approved",
  "split": "development",
  "development_version": "0.2",
  "overlap_status": "sin_coincidencia_detectada_v02",
  "overlap_audit_history": [
    {
      "development_version": "0.1",
      "input_audited": "Find Morgan in the kitchen and guide them to the entrance.",
      "development_sha256": "02103490f89367add79ae9b6aea90e01ecd7f9def7cb32c24d9fb51e6b0b5c7b",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    },
    {
      "development_version": "0.2",
      "input_audited": "Find Morgan in the kitchen and guide them to the entrance.",
      "development_sha256": "4c1a356fa50ac317ad6b428c101a48183968a41e2771e2ad2bd7c622f61d4480",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "audit_path": "reports/evaluation/auditoria_desarrollo_v02.json",
      "audit_sha256": "f4d5c3c3088dc5bd9f61d6ebef4b33716401dd4014491585317a184e647e0346",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    }
  ],
  "planned_assessment": {
    "semantic": "no_ejecutado",
    "plan_contract": "no_ejecutado",
    "task_fulfillment": "no_ejecutado",
    "latency_ms": null
  }
}
```

</details>

## DEV-023

**Intención:** INT-08 · **Grupo:** guia · **Variante:** parafrasis · **Bloque:** funcional_y_linguistico

**Orden original:**

> Meet Morgan in the kitchen, then lead Morgan to the entrance.

**Propósito:** Origen, persona y destino

**Respuesta prevista:** `executable`.

**Objetivos propuestos:**

```text
go(kitchen)
find(Morgan, kind=person)
guide(Morgan, to=entrance)
```

**Subtareas requeridas:**

- Localizar a Morgan en kitchen.
- Indicar a Morgan que siga al robot y guiarle a entrance.

**Restricciones:**

- Resolver them como Morgan; conservar entrance como destino.
- Un desplazamiento sin vincular a la persona no cubre por sí solo la subtarea de guía.

**Conductas prohibidas:**

- Inventar entidades, destinos o subtareas no solicitados.

**Variaciones aceptables:**

- Variar el texto de anuncios conservando su sentido.
- Usar identificadores internos consistentes sin cambiar el referente.

**Límites de verificación:**

- Identidad de la persona sujeta al contrato de identificación; presencia física durante la guía fuera del alcance.

**Condiciones iniciales:**

```json
{
  "location": "unknown",
  "holding": "nothing",
  "focus": false,
  "manipulation_enabled": true,
  "independent_request": true
}
```

**Supuestos del escenario:**

- Las entidades mencionadas son referencias del dominio; su detección y disponibilidad física no se evalúan.
- Cada orden se procesa sin conversación previa.

**Comprobaciones comunes del plan:**

- Acciones y parámetros dentro del contrato compartido.
- No añadir tareas ajenas; se admiten los cierres convencionales de retorno y comunicación.
- Referentes consistentes y dependencias de adquisición/entrega respetadas.
- Distinguir protocolo generado de operación física no observada.

**Notas existentes de revisión:**

- 2026-10-17: el investigador confirmó en la conversación haber revisado las 60 fichas y encontrarlas en orden; aprobación sin cambios de órdenes, objetivos ni criterios. Aprobación para desarrollo, no dictamen sobre salidas de modelos.

**Decisión del investigador:**

- [x] Aprobada sin cambios.
- [ ] Requiere correcciones.
- [ ] No aprobada.

**Correcciones u observaciones:**

Sin correcciones solicitadas.

**Revisor y fecha:** Investigador (usuario), 2026-10-17.

<details>
<summary>Metadatos y trazabilidad de la ficha original</summary>

```json
{
  "reference_status": "approved",
  "split": "development",
  "development_version": "0.2",
  "overlap_status": "sin_coincidencia_detectada_v02",
  "overlap_audit_history": [
    {
      "development_version": "0.1",
      "input_audited": "Meet Morgan in the kitchen, then lead Morgan to the entrance.",
      "development_sha256": "02103490f89367add79ae9b6aea90e01ecd7f9def7cb32c24d9fb51e6b0b5c7b",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    },
    {
      "development_version": "0.2",
      "input_audited": "Meet Morgan in the kitchen, then lead Morgan to the entrance.",
      "development_sha256": "4c1a356fa50ac317ad6b428c101a48183968a41e2771e2ad2bd7c622f61d4480",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "audit_path": "reports/evaluation/auditoria_desarrollo_v02.json",
      "audit_sha256": "f4d5c3c3088dc5bd9f61d6ebef4b33716401dd4014491585317a184e647e0346",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    }
  ],
  "planned_assessment": {
    "semantic": "no_ejecutado",
    "plan_contract": "no_ejecutado",
    "task_fulfillment": "no_ejecutado",
    "latency_ms": null
  }
}
```

</details>

## DEV-024

**Intención:** INT-08 · **Grupo:** guia · **Variante:** ruido_leve · **Bloque:** funcional_y_linguistico

**Orden original:**

> find Morgan in the kichen and guide them to the entrance please

**Propósito:** Origen, persona y destino

**Respuesta prevista:** `executable`.

**Objetivos propuestos:**

```text
go(kitchen)
find(Morgan, kind=person)
guide(Morgan, to=entrance)
```

**Subtareas requeridas:**

- Localizar a Morgan en kitchen.
- Indicar a Morgan que siga al robot y guiarle a entrance.

**Restricciones:**

- Resolver them como Morgan; conservar entrance como destino.
- Un desplazamiento sin vincular a la persona no cubre por sí solo la subtarea de guía.

**Conductas prohibidas:**

- Inventar entidades, destinos o subtareas no solicitados.

**Variaciones aceptables:**

- Variar el texto de anuncios conservando su sentido.
- Usar identificadores internos consistentes sin cambiar el referente.

**Límites de verificación:**

- Identidad de la persona sujeta al contrato de identificación; presencia física durante la guía fuera del alcance.

**Condiciones iniciales:**

```json
{
  "location": "unknown",
  "holding": "nothing",
  "focus": false,
  "manipulation_enabled": true,
  "independent_request": true
}
```

**Supuestos del escenario:**

- Las entidades mencionadas son referencias del dominio; su detección y disponibilidad física no se evalúan.
- Cada orden se procesa sin conversación previa.

**Comprobaciones comunes del plan:**

- Acciones y parámetros dentro del contrato compartido.
- No añadir tareas ajenas; se admiten los cierres convencionales de retorno y comunicación.
- Referentes consistentes y dependencias de adquisición/entrega respetadas.
- Distinguir protocolo generado de operación física no observada.

**Notas existentes de revisión:**

- 2026-10-17: el investigador confirmó en la conversación haber revisado las 60 fichas y encontrarlas en orden; aprobación sin cambios de órdenes, objetivos ni criterios. Aprobación para desarrollo, no dictamen sobre salidas de modelos.

**Decisión del investigador:**

- [x] Aprobada sin cambios.
- [ ] Requiere correcciones.
- [ ] No aprobada.

**Correcciones u observaciones:**

Sin correcciones solicitadas.

**Revisor y fecha:** Investigador (usuario), 2026-10-17.

<details>
<summary>Metadatos y trazabilidad de la ficha original</summary>

```json
{
  "reference_status": "approved",
  "split": "development",
  "development_version": "0.2",
  "overlap_status": "sin_coincidencia_detectada_v02",
  "overlap_audit_history": [
    {
      "development_version": "0.1",
      "input_audited": "find Morgan in the kichen and guide them to the entrance please",
      "development_sha256": "02103490f89367add79ae9b6aea90e01ecd7f9def7cb32c24d9fb51e6b0b5c7b",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    },
    {
      "development_version": "0.2",
      "input_audited": "find Morgan in the kichen and guide them to the entrance please",
      "development_sha256": "4c1a356fa50ac317ad6b428c101a48183968a41e2771e2ad2bd7c622f61d4480",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "audit_path": "reports/evaluation/auditoria_desarrollo_v02.json",
      "audit_sha256": "f4d5c3c3088dc5bd9f61d6ebef4b33716401dd4014491585317a184e647e0346",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    }
  ],
  "planned_assessment": {
    "semantic": "no_ejecutado",
    "plan_contract": "no_ejecutado",
    "task_fulfillment": "no_ejecutado",
    "latency_ms": null
  }
}
```

</details>

## DEV-025

**Intención:** INT-09 · **Grupo:** seguimiento · **Variante:** canonica · **Bloque:** funcional_y_linguistico

**Orden original:**

> Find the waving person in the bedroom and follow them.

**Propósito:** Gesto y referencia a la persona

**Respuesta prevista:** `executable`.

**Objetivos propuestos:**

```text
go(bedroom)
find(person, kind=person, gesture='waving person')
follow(person)
```

**Subtareas requeridas:**

- Localizar una persona que saluda con la mano en bedroom.
- Iniciar seguimiento de esa misma persona sin inventar un destino.

**Restricciones:**

- El gesto debe conservarse en la búsqueda.
- El seguimiento debe corresponder al referente encontrado.

**Conductas prohibidas:**

- Inventar entidades, destinos o subtareas no solicitados.

**Variaciones aceptables:**

- Variar el texto de anuncios conservando su sentido.
- Usar identificadores internos consistentes sin cambiar el referente.

**Límites de verificación:**

- instruct_follow_only es una clave de protocolo. Su presencia no demuestra seguimiento; cumplimiento operativo no verificable hasta precisar el contrato del ejecutor.

**Condiciones iniciales:**

```json
{
  "location": "unknown",
  "holding": "nothing",
  "focus": false,
  "manipulation_enabled": true,
  "independent_request": true
}
```

**Supuestos del escenario:**

- Las entidades mencionadas son referencias del dominio; su detección y disponibilidad física no se evalúan.
- Cada orden se procesa sin conversación previa.

**Comprobaciones comunes del plan:**

- Acciones y parámetros dentro del contrato compartido.
- No añadir tareas ajenas; se admiten los cierres convencionales de retorno y comunicación.
- Referentes consistentes y dependencias de adquisición/entrega respetadas.
- Distinguir protocolo generado de operación física no observada.

**Notas existentes de revisión:**

- 2026-10-17: el investigador confirmó en la conversación haber revisado las 60 fichas y encontrarlas en orden; aprobación sin cambios de órdenes, objetivos ni criterios. Aprobación para desarrollo, no dictamen sobre salidas de modelos.

**Decisión del investigador:**

- [x] Aprobada sin cambios.
- [ ] Requiere correcciones.
- [ ] No aprobada.

**Correcciones u observaciones:**

Sin correcciones solicitadas.

**Revisor y fecha:** Investigador (usuario), 2026-10-17.

<details>
<summary>Metadatos y trazabilidad de la ficha original</summary>

```json
{
  "reference_status": "approved",
  "split": "development",
  "development_version": "0.2",
  "overlap_status": "coincidencia_detectada_v02",
  "overlap_audit_history": [
    {
      "development_version": "0.1",
      "input_audited": "Find the waving person in the office and follow them.",
      "development_sha256": "02103490f89367add79ae9b6aea90e01ecd7f9def7cb32c24d9fb51e6b0b5c7b",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [
          37681
        ],
        "normalizador_real": [
          37681
        ]
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    },
    {
      "development_version": "0.2",
      "input_audited": "Find the waving person in the bedroom and follow them.",
      "development_sha256": "4c1a356fa50ac317ad6b428c101a48183968a41e2771e2ad2bd7c622f61d4480",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "audit_path": "reports/evaluation/auditoria_desarrollo_v02.json",
      "audit_sha256": "f4d5c3c3088dc5bd9f61d6ebef4b33716401dd4014491585317a184e647e0346",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [
          35245
        ],
        "normalizador_real": [
          35245
        ]
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    }
  ],
  "revision_history": [
    {
      "version": "0.2",
      "previous_input": "Find the waving person in the office and follow them.",
      "previous_goals_ref": [
        "go(office)",
        "find(person, kind=person, gesture='waving person')",
        "follow(person)"
      ],
      "reason": "Sustitución de las tres variantes de un grupo con coincidencias; nueva auditoría pendiente."
    }
  ],
  "planned_assessment": {
    "semantic": "no_ejecutado",
    "plan_contract": "no_ejecutado",
    "task_fulfillment": "no_ejecutado",
    "latency_ms": null
  }
}
```

</details>

## DEV-026

**Intención:** INT-09 · **Grupo:** seguimiento · **Variante:** parafrasis · **Bloque:** funcional_y_linguistico

**Orden original:**

> In the bedroom, locate the person who is waving and follow that person.

**Propósito:** Gesto y referencia a la persona

**Respuesta prevista:** `executable`.

**Objetivos propuestos:**

```text
go(bedroom)
find(person, kind=person, gesture='waving person')
follow(person)
```

**Subtareas requeridas:**

- Localizar una persona que saluda con la mano en bedroom.
- Iniciar seguimiento de esa misma persona sin inventar un destino.

**Restricciones:**

- El gesto debe conservarse en la búsqueda.
- El seguimiento debe corresponder al referente encontrado.

**Conductas prohibidas:**

- Inventar entidades, destinos o subtareas no solicitados.

**Variaciones aceptables:**

- Variar el texto de anuncios conservando su sentido.
- Usar identificadores internos consistentes sin cambiar el referente.

**Límites de verificación:**

- instruct_follow_only es una clave de protocolo. Su presencia no demuestra seguimiento; cumplimiento operativo no verificable hasta precisar el contrato del ejecutor.

**Condiciones iniciales:**

```json
{
  "location": "unknown",
  "holding": "nothing",
  "focus": false,
  "manipulation_enabled": true,
  "independent_request": true
}
```

**Supuestos del escenario:**

- Las entidades mencionadas son referencias del dominio; su detección y disponibilidad física no se evalúan.
- Cada orden se procesa sin conversación previa.

**Comprobaciones comunes del plan:**

- Acciones y parámetros dentro del contrato compartido.
- No añadir tareas ajenas; se admiten los cierres convencionales de retorno y comunicación.
- Referentes consistentes y dependencias de adquisición/entrega respetadas.
- Distinguir protocolo generado de operación física no observada.

**Notas existentes de revisión:**

- 2026-10-17: el investigador confirmó en la conversación haber revisado las 60 fichas y encontrarlas en orden; aprobación sin cambios de órdenes, objetivos ni criterios. Aprobación para desarrollo, no dictamen sobre salidas de modelos.

**Decisión del investigador:**

- [x] Aprobada sin cambios.
- [ ] Requiere correcciones.
- [ ] No aprobada.

**Correcciones u observaciones:**

Sin correcciones solicitadas.

**Revisor y fecha:** Investigador (usuario), 2026-10-17.

<details>
<summary>Metadatos y trazabilidad de la ficha original</summary>

```json
{
  "reference_status": "approved",
  "split": "development",
  "development_version": "0.2",
  "overlap_status": "sin_coincidencia_detectada_v02",
  "overlap_audit_history": [
    {
      "development_version": "0.1",
      "input_audited": "In the office, locate the person who is waving and follow that person.",
      "development_sha256": "02103490f89367add79ae9b6aea90e01ecd7f9def7cb32c24d9fb51e6b0b5c7b",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    },
    {
      "development_version": "0.2",
      "input_audited": "In the bedroom, locate the person who is waving and follow that person.",
      "development_sha256": "4c1a356fa50ac317ad6b428c101a48183968a41e2771e2ad2bd7c622f61d4480",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "audit_path": "reports/evaluation/auditoria_desarrollo_v02.json",
      "audit_sha256": "f4d5c3c3088dc5bd9f61d6ebef4b33716401dd4014491585317a184e647e0346",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    }
  ],
  "revision_history": [
    {
      "version": "0.2",
      "previous_input": "In the office, locate the person who is waving and follow that person.",
      "previous_goals_ref": [
        "go(office)",
        "find(person, kind=person, gesture='waving person')",
        "follow(person)"
      ],
      "reason": "Sustitución de las tres variantes de un grupo con coincidencias; nueva auditoría pendiente."
    }
  ],
  "planned_assessment": {
    "semantic": "no_ejecutado",
    "plan_contract": "no_ejecutado",
    "task_fulfillment": "no_ejecutado",
    "latency_ms": null
  }
}
```

</details>

## DEV-027

**Intención:** INT-09 · **Grupo:** seguimiento · **Variante:** ruido_leve · **Bloque:** funcional_y_linguistico

**Orden original:**

> please find the waving person in the bedrom and follow them

**Propósito:** Gesto y referencia a la persona

**Respuesta prevista:** `executable`.

**Objetivos propuestos:**

```text
go(bedroom)
find(person, kind=person, gesture='waving person')
follow(person)
```

**Subtareas requeridas:**

- Localizar una persona que saluda con la mano en bedroom.
- Iniciar seguimiento de esa misma persona sin inventar un destino.

**Restricciones:**

- El gesto debe conservarse en la búsqueda.
- El seguimiento debe corresponder al referente encontrado.

**Conductas prohibidas:**

- Inventar entidades, destinos o subtareas no solicitados.

**Variaciones aceptables:**

- Variar el texto de anuncios conservando su sentido.
- Usar identificadores internos consistentes sin cambiar el referente.

**Límites de verificación:**

- instruct_follow_only es una clave de protocolo. Su presencia no demuestra seguimiento; cumplimiento operativo no verificable hasta precisar el contrato del ejecutor.

**Condiciones iniciales:**

```json
{
  "location": "unknown",
  "holding": "nothing",
  "focus": false,
  "manipulation_enabled": true,
  "independent_request": true
}
```

**Supuestos del escenario:**

- Las entidades mencionadas son referencias del dominio; su detección y disponibilidad física no se evalúan.
- Cada orden se procesa sin conversación previa.

**Comprobaciones comunes del plan:**

- Acciones y parámetros dentro del contrato compartido.
- No añadir tareas ajenas; se admiten los cierres convencionales de retorno y comunicación.
- Referentes consistentes y dependencias de adquisición/entrega respetadas.
- Distinguir protocolo generado de operación física no observada.

**Notas existentes de revisión:**

- 2026-10-17: el investigador confirmó en la conversación haber revisado las 60 fichas y encontrarlas en orden; aprobación sin cambios de órdenes, objetivos ni criterios. Aprobación para desarrollo, no dictamen sobre salidas de modelos.

**Decisión del investigador:**

- [x] Aprobada sin cambios.
- [ ] Requiere correcciones.
- [ ] No aprobada.

**Correcciones u observaciones:**

Sin correcciones solicitadas.

**Revisor y fecha:** Investigador (usuario), 2026-10-17.

<details>
<summary>Metadatos y trazabilidad de la ficha original</summary>

```json
{
  "reference_status": "approved",
  "split": "development",
  "development_version": "0.2",
  "overlap_status": "coincidencia_detectada_v02",
  "overlap_audit_history": [
    {
      "development_version": "0.1",
      "input_audited": "please find the waving person in the ofice and follow them",
      "development_sha256": "02103490f89367add79ae9b6aea90e01ecd7f9def7cb32c24d9fb51e6b0b5c7b",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": [
          37681
        ]
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    },
    {
      "development_version": "0.2",
      "input_audited": "please find the waving person in the bedrom and follow them",
      "development_sha256": "4c1a356fa50ac317ad6b428c101a48183968a41e2771e2ad2bd7c622f61d4480",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "audit_path": "reports/evaluation/auditoria_desarrollo_v02.json",
      "audit_sha256": "f4d5c3c3088dc5bd9f61d6ebef4b33716401dd4014491585317a184e647e0346",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": [
          35245
        ]
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    }
  ],
  "revision_history": [
    {
      "version": "0.2",
      "previous_input": "please find the waving person in the ofice and follow them",
      "previous_goals_ref": [
        "go(office)",
        "find(person, kind=person, gesture='waving person')",
        "follow(person)"
      ],
      "reason": "Sustitución de las tres variantes de un grupo con coincidencias; nueva auditoría pendiente."
    }
  ],
  "planned_assessment": {
    "semantic": "no_ejecutado",
    "plan_contract": "no_ejecutado",
    "task_fulfillment": "no_ejecutado",
    "latency_ms": null
  }
}
```

</details>

## DEV-028

**Intención:** INT-10 · **Grupo:** entrega_persona · **Variante:** canonica · **Bloque:** funcional_y_linguistico

**Orden original:**

> Take an orange from the refrigerator and give it to Sarah in the kitchen.

**Propósito:** Cambio de referente objeto-persona

**Respuesta prevista:** `executable`.

**Objetivos propuestos:**

```text
go(refrigerator)
find(orange, kind=object)
take(orange)
go(kitchen)
find(Sarah, kind=person)
deliver(orange, to=Sarah)
```

**Subtareas requeridas:**

- Adquirir orange en refrigerator.
- Localizar a Sarah en kitchen.
- Entregar a Sarah la misma orange.

**Restricciones:**

- Conservar el objeto al cambiar de ubicación y buscar a Sarah.
- No entregar al operador ni confundir orange con un atributo de ropa.

**Conductas prohibidas:**

- Inventar entidades, destinos o subtareas no solicitados.

**Variaciones aceptables:**

- Variar el texto de anuncios conservando su sentido.
- Usar identificadores internos consistentes sin cambiar el referente.

**Límites de verificación:**

- Verificar el enlace entre el nombre Sarah y la referencia interna del destinatario.

**Condiciones iniciales:**

```json
{
  "location": "unknown",
  "holding": "nothing",
  "focus": false,
  "manipulation_enabled": true,
  "independent_request": true
}
```

**Supuestos del escenario:**

- Las entidades mencionadas son referencias del dominio; su detección y disponibilidad física no se evalúan.
- Cada orden se procesa sin conversación previa.

**Comprobaciones comunes del plan:**

- Acciones y parámetros dentro del contrato compartido.
- No añadir tareas ajenas; se admiten los cierres convencionales de retorno y comunicación.
- Referentes consistentes y dependencias de adquisición/entrega respetadas.
- Distinguir protocolo generado de operación física no observada.

**Notas existentes de revisión:**

- 2026-10-17: el investigador confirmó en la conversación haber revisado las 60 fichas y encontrarlas en orden; aprobación sin cambios de órdenes, objetivos ni criterios. Aprobación para desarrollo, no dictamen sobre salidas de modelos.

**Decisión del investigador:**

- [x] Aprobada sin cambios.
- [ ] Requiere correcciones.
- [ ] No aprobada.

**Correcciones u observaciones:**

Sin correcciones solicitadas.

**Revisor y fecha:** Investigador (usuario), 2026-10-17.

<details>
<summary>Metadatos y trazabilidad de la ficha original</summary>

```json
{
  "reference_status": "approved",
  "split": "development",
  "development_version": "0.2",
  "overlap_status": "sin_coincidencia_detectada_v02",
  "overlap_audit_history": [
    {
      "development_version": "0.1",
      "input_audited": "Take an orange from the refrigerator and give it to Sarah in the kitchen.",
      "development_sha256": "02103490f89367add79ae9b6aea90e01ecd7f9def7cb32c24d9fb51e6b0b5c7b",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    },
    {
      "development_version": "0.2",
      "input_audited": "Take an orange from the refrigerator and give it to Sarah in the kitchen.",
      "development_sha256": "4c1a356fa50ac317ad6b428c101a48183968a41e2771e2ad2bd7c622f61d4480",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "audit_path": "reports/evaluation/auditoria_desarrollo_v02.json",
      "audit_sha256": "f4d5c3c3088dc5bd9f61d6ebef4b33716401dd4014491585317a184e647e0346",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    }
  ],
  "planned_assessment": {
    "semantic": "no_ejecutado",
    "plan_contract": "no_ejecutado",
    "task_fulfillment": "no_ejecutado",
    "latency_ms": null
  }
}
```

</details>

## DEV-029

**Intención:** INT-10 · **Grupo:** entrega_persona · **Variante:** parafrasis · **Bloque:** funcional_y_linguistico

**Orden original:**

> Fetch an orange at the refrigerator, then find Sarah in the kitchen and hand the orange to her.

**Propósito:** Cambio de referente objeto-persona

**Respuesta prevista:** `executable`.

**Objetivos propuestos:**

```text
go(refrigerator)
find(orange, kind=object)
take(orange)
go(kitchen)
find(Sarah, kind=person)
deliver(orange, to=Sarah)
```

**Subtareas requeridas:**

- Adquirir orange en refrigerator.
- Localizar a Sarah en kitchen.
- Entregar a Sarah la misma orange.

**Restricciones:**

- Conservar el objeto al cambiar de ubicación y buscar a Sarah.
- No entregar al operador ni confundir orange con un atributo de ropa.

**Conductas prohibidas:**

- Inventar entidades, destinos o subtareas no solicitados.

**Variaciones aceptables:**

- Variar el texto de anuncios conservando su sentido.
- Usar identificadores internos consistentes sin cambiar el referente.

**Límites de verificación:**

- Verificar el enlace entre el nombre Sarah y la referencia interna del destinatario.

**Condiciones iniciales:**

```json
{
  "location": "unknown",
  "holding": "nothing",
  "focus": false,
  "manipulation_enabled": true,
  "independent_request": true
}
```

**Supuestos del escenario:**

- Las entidades mencionadas son referencias del dominio; su detección y disponibilidad física no se evalúan.
- Cada orden se procesa sin conversación previa.

**Comprobaciones comunes del plan:**

- Acciones y parámetros dentro del contrato compartido.
- No añadir tareas ajenas; se admiten los cierres convencionales de retorno y comunicación.
- Referentes consistentes y dependencias de adquisición/entrega respetadas.
- Distinguir protocolo generado de operación física no observada.

**Notas existentes de revisión:**

- 2026-10-17: el investigador confirmó en la conversación haber revisado las 60 fichas y encontrarlas en orden; aprobación sin cambios de órdenes, objetivos ni criterios. Aprobación para desarrollo, no dictamen sobre salidas de modelos.

**Decisión del investigador:**

- [x] Aprobada sin cambios.
- [ ] Requiere correcciones.
- [ ] No aprobada.

**Correcciones u observaciones:**

Sin correcciones solicitadas.

**Revisor y fecha:** Investigador (usuario), 2026-10-17.

<details>
<summary>Metadatos y trazabilidad de la ficha original</summary>

```json
{
  "reference_status": "approved",
  "split": "development",
  "development_version": "0.2",
  "overlap_status": "sin_coincidencia_detectada_v02",
  "overlap_audit_history": [
    {
      "development_version": "0.1",
      "input_audited": "Fetch an orange at the refrigerator, then find Sarah in the kitchen and hand the orange to her.",
      "development_sha256": "02103490f89367add79ae9b6aea90e01ecd7f9def7cb32c24d9fb51e6b0b5c7b",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    },
    {
      "development_version": "0.2",
      "input_audited": "Fetch an orange at the refrigerator, then find Sarah in the kitchen and hand the orange to her.",
      "development_sha256": "4c1a356fa50ac317ad6b428c101a48183968a41e2771e2ad2bd7c622f61d4480",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "audit_path": "reports/evaluation/auditoria_desarrollo_v02.json",
      "audit_sha256": "f4d5c3c3088dc5bd9f61d6ebef4b33716401dd4014491585317a184e647e0346",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    }
  ],
  "planned_assessment": {
    "semantic": "no_ejecutado",
    "plan_contract": "no_ejecutado",
    "task_fulfillment": "no_ejecutado",
    "latency_ms": null
  }
}
```

</details>

## DEV-030

**Intención:** INT-10 · **Grupo:** entrega_persona · **Variante:** ruido_leve · **Bloque:** funcional_y_linguistico

**Orden original:**

> take an orange from the refridgerator and give it to Sarah in the kichen

**Propósito:** Cambio de referente objeto-persona

**Respuesta prevista:** `executable`.

**Objetivos propuestos:**

```text
go(refrigerator)
find(orange, kind=object)
take(orange)
go(kitchen)
find(Sarah, kind=person)
deliver(orange, to=Sarah)
```

**Subtareas requeridas:**

- Adquirir orange en refrigerator.
- Localizar a Sarah en kitchen.
- Entregar a Sarah la misma orange.

**Restricciones:**

- Conservar el objeto al cambiar de ubicación y buscar a Sarah.
- No entregar al operador ni confundir orange con un atributo de ropa.

**Conductas prohibidas:**

- Inventar entidades, destinos o subtareas no solicitados.

**Variaciones aceptables:**

- Variar el texto de anuncios conservando su sentido.
- Usar identificadores internos consistentes sin cambiar el referente.

**Límites de verificación:**

- Verificar el enlace entre el nombre Sarah y la referencia interna del destinatario.

**Condiciones iniciales:**

```json
{
  "location": "unknown",
  "holding": "nothing",
  "focus": false,
  "manipulation_enabled": true,
  "independent_request": true
}
```

**Supuestos del escenario:**

- Las entidades mencionadas son referencias del dominio; su detección y disponibilidad física no se evalúan.
- Cada orden se procesa sin conversación previa.

**Comprobaciones comunes del plan:**

- Acciones y parámetros dentro del contrato compartido.
- No añadir tareas ajenas; se admiten los cierres convencionales de retorno y comunicación.
- Referentes consistentes y dependencias de adquisición/entrega respetadas.
- Distinguir protocolo generado de operación física no observada.

**Notas existentes de revisión:**

- 2026-10-17: el investigador confirmó en la conversación haber revisado las 60 fichas y encontrarlas en orden; aprobación sin cambios de órdenes, objetivos ni criterios. Aprobación para desarrollo, no dictamen sobre salidas de modelos.

**Decisión del investigador:**

- [x] Aprobada sin cambios.
- [ ] Requiere correcciones.
- [ ] No aprobada.

**Correcciones u observaciones:**

Sin correcciones solicitadas.

**Revisor y fecha:** Investigador (usuario), 2026-10-17.

<details>
<summary>Metadatos y trazabilidad de la ficha original</summary>

```json
{
  "reference_status": "approved",
  "split": "development",
  "development_version": "0.2",
  "overlap_status": "sin_coincidencia_detectada_v02",
  "overlap_audit_history": [
    {
      "development_version": "0.1",
      "input_audited": "take an orange from the refridgerator and give it to Sarah in the kichen",
      "development_sha256": "02103490f89367add79ae9b6aea90e01ecd7f9def7cb32c24d9fb51e6b0b5c7b",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    },
    {
      "development_version": "0.2",
      "input_audited": "take an orange from the refridgerator and give it to Sarah in the kichen",
      "development_sha256": "4c1a356fa50ac317ad6b428c101a48183968a41e2771e2ad2bd7c622f61d4480",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "audit_path": "reports/evaluation/auditoria_desarrollo_v02.json",
      "audit_sha256": "f4d5c3c3088dc5bd9f61d6ebef4b33716401dd4014491585317a184e647e0346",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    }
  ],
  "planned_assessment": {
    "semantic": "no_ejecutado",
    "plan_contract": "no_ejecutado",
    "task_fulfillment": "no_ejecutado",
    "latency_ms": null
  }
}
```

</details>

## DEV-031

**Intención:** INT-11 · **Grupo:** conteo_objetos · **Variante:** canonica · **Bloque:** funcional_y_linguistico

**Orden original:**

> Count the toys on the storage rack.

**Propósito:** Categoría y comunicación del resultado

**Respuesta prevista:** `executable`.

**Objetivos propuestos:**

```text
go(storage rack)
count(toys, kind=object)
```

**Subtareas requeridas:**

- Contar toys en storage rack y comunicar el conteo al operador.

**Restricciones:**

- No inventar una cantidad: el plan debe solicitar el análisis y la comunicación del resultado.
- La categoría completa toys debe preservarse.

**Conductas prohibidas:**

- Inventar entidades, destinos o subtareas no solicitados.

**Variaciones aceptables:**

- Variar el texto de anuncios conservando su sentido.
- Usar identificadores internos consistentes sin cambiar el referente.

**Límites de verificación:**

Sin elementos especificados en la ficha.

**Condiciones iniciales:**

```json
{
  "location": "unknown",
  "holding": "nothing",
  "focus": false,
  "manipulation_enabled": true,
  "independent_request": true
}
```

**Supuestos del escenario:**

- Las entidades mencionadas son referencias del dominio; su detección y disponibilidad física no se evalúan.
- Cada orden se procesa sin conversación previa.

**Comprobaciones comunes del plan:**

- Acciones y parámetros dentro del contrato compartido.
- No añadir tareas ajenas; se admiten los cierres convencionales de retorno y comunicación.
- Referentes consistentes y dependencias de adquisición/entrega respetadas.
- Distinguir protocolo generado de operación física no observada.

**Notas existentes de revisión:**

- 2026-10-17: el investigador confirmó en la conversación haber revisado las 60 fichas y encontrarlas en orden; aprobación sin cambios de órdenes, objetivos ni criterios. Aprobación para desarrollo, no dictamen sobre salidas de modelos.

**Decisión del investigador:**

- [x] Aprobada sin cambios.
- [ ] Requiere correcciones.
- [ ] No aprobada.

**Correcciones u observaciones:**

Sin correcciones solicitadas.

**Revisor y fecha:** Investigador (usuario), 2026-10-17.

<details>
<summary>Metadatos y trazabilidad de la ficha original</summary>

```json
{
  "reference_status": "approved",
  "split": "development",
  "development_version": "0.2",
  "overlap_status": "coincidencia_detectada_v02",
  "overlap_audit_history": [
    {
      "development_version": "0.1",
      "input_audited": "Count the dishes on the shelf.",
      "development_sha256": "02103490f89367add79ae9b6aea90e01ecd7f9def7cb32c24d9fb51e6b0b5c7b",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [
          3455
        ],
        "normalizador_real": [
          3455
        ]
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    },
    {
      "development_version": "0.2",
      "input_audited": "Count the toys on the storage rack.",
      "development_sha256": "4c1a356fa50ac317ad6b428c101a48183968a41e2771e2ad2bd7c622f61d4480",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "audit_path": "reports/evaluation/auditoria_desarrollo_v02.json",
      "audit_sha256": "f4d5c3c3088dc5bd9f61d6ebef4b33716401dd4014491585317a184e647e0346",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [
          6467
        ],
        "normalizador_real": [
          6467
        ]
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    }
  ],
  "revision_history": [
    {
      "version": "0.2",
      "previous_input": "Count the dishes on the shelf.",
      "previous_goals_ref": [
        "go(shelf)",
        "count(dishes, kind=object)"
      ],
      "reason": "Sustitución de las tres variantes de un grupo con coincidencias; nueva auditoría pendiente."
    }
  ],
  "planned_assessment": {
    "semantic": "no_ejecutado",
    "plan_contract": "no_ejecutado",
    "task_fulfillment": "no_ejecutado",
    "latency_ms": null
  }
}
```

</details>

## DEV-032

**Intención:** INT-11 · **Grupo:** conteo_objetos · **Variante:** parafrasis · **Bloque:** funcional_y_linguistico

**Orden original:**

> Tell me how many toys are on the storage rack.

**Propósito:** Categoría y comunicación del resultado

**Respuesta prevista:** `executable`.

**Objetivos propuestos:**

```text
go(storage rack)
count(toys, kind=object)
```

**Subtareas requeridas:**

- Contar toys en storage rack y comunicar el conteo al operador.

**Restricciones:**

- No inventar una cantidad: el plan debe solicitar el análisis y la comunicación del resultado.
- La categoría completa toys debe preservarse.

**Conductas prohibidas:**

- Inventar entidades, destinos o subtareas no solicitados.

**Variaciones aceptables:**

- Variar el texto de anuncios conservando su sentido.
- Usar identificadores internos consistentes sin cambiar el referente.

**Límites de verificación:**

Sin elementos especificados en la ficha.

**Condiciones iniciales:**

```json
{
  "location": "unknown",
  "holding": "nothing",
  "focus": false,
  "manipulation_enabled": true,
  "independent_request": true
}
```

**Supuestos del escenario:**

- Las entidades mencionadas son referencias del dominio; su detección y disponibilidad física no se evalúan.
- Cada orden se procesa sin conversación previa.

**Comprobaciones comunes del plan:**

- Acciones y parámetros dentro del contrato compartido.
- No añadir tareas ajenas; se admiten los cierres convencionales de retorno y comunicación.
- Referentes consistentes y dependencias de adquisición/entrega respetadas.
- Distinguir protocolo generado de operación física no observada.

**Notas existentes de revisión:**

- 2026-10-17: el investigador confirmó en la conversación haber revisado las 60 fichas y encontrarlas en orden; aprobación sin cambios de órdenes, objetivos ni criterios. Aprobación para desarrollo, no dictamen sobre salidas de modelos.

**Decisión del investigador:**

- [x] Aprobada sin cambios.
- [ ] Requiere correcciones.
- [ ] No aprobada.

**Correcciones u observaciones:**

Sin correcciones solicitadas.

**Revisor y fecha:** Investigador (usuario), 2026-10-17.

<details>
<summary>Metadatos y trazabilidad de la ficha original</summary>

```json
{
  "reference_status": "approved",
  "split": "development",
  "development_version": "0.2",
  "overlap_status": "sin_coincidencia_detectada_v02",
  "overlap_audit_history": [
    {
      "development_version": "0.1",
      "input_audited": "Tell me how many dishes are on the shelf.",
      "development_sha256": "02103490f89367add79ae9b6aea90e01ecd7f9def7cb32c24d9fb51e6b0b5c7b",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    },
    {
      "development_version": "0.2",
      "input_audited": "Tell me how many toys are on the storage rack.",
      "development_sha256": "4c1a356fa50ac317ad6b428c101a48183968a41e2771e2ad2bd7c622f61d4480",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "audit_path": "reports/evaluation/auditoria_desarrollo_v02.json",
      "audit_sha256": "f4d5c3c3088dc5bd9f61d6ebef4b33716401dd4014491585317a184e647e0346",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    }
  ],
  "revision_history": [
    {
      "version": "0.2",
      "previous_input": "Tell me how many dishes are on the shelf.",
      "previous_goals_ref": [
        "go(shelf)",
        "count(dishes, kind=object)"
      ],
      "reason": "Sustitución de las tres variantes de un grupo con coincidencias; nueva auditoría pendiente."
    }
  ],
  "planned_assessment": {
    "semantic": "no_ejecutado",
    "plan_contract": "no_ejecutado",
    "task_fulfillment": "no_ejecutado",
    "latency_ms": null
  }
}
```

</details>

## DEV-033

**Intención:** INT-11 · **Grupo:** conteo_objetos · **Variante:** ruido_leve · **Bloque:** funcional_y_linguistico

**Orden original:**

> please count the the toys on the storage rack

**Propósito:** Categoría y comunicación del resultado

**Respuesta prevista:** `executable`.

**Objetivos propuestos:**

```text
go(storage rack)
count(toys, kind=object)
```

**Subtareas requeridas:**

- Contar toys en storage rack y comunicar el conteo al operador.

**Restricciones:**

- No inventar una cantidad: el plan debe solicitar el análisis y la comunicación del resultado.
- La categoría completa toys debe preservarse.

**Conductas prohibidas:**

- Inventar entidades, destinos o subtareas no solicitados.

**Variaciones aceptables:**

- Variar el texto de anuncios conservando su sentido.
- Usar identificadores internos consistentes sin cambiar el referente.

**Límites de verificación:**

Sin elementos especificados en la ficha.

**Condiciones iniciales:**

```json
{
  "location": "unknown",
  "holding": "nothing",
  "focus": false,
  "manipulation_enabled": true,
  "independent_request": true
}
```

**Supuestos del escenario:**

- Las entidades mencionadas son referencias del dominio; su detección y disponibilidad física no se evalúan.
- Cada orden se procesa sin conversación previa.

**Comprobaciones comunes del plan:**

- Acciones y parámetros dentro del contrato compartido.
- No añadir tareas ajenas; se admiten los cierres convencionales de retorno y comunicación.
- Referentes consistentes y dependencias de adquisición/entrega respetadas.
- Distinguir protocolo generado de operación física no observada.

**Notas existentes de revisión:**

- 2026-10-17: el investigador confirmó en la conversación haber revisado las 60 fichas y encontrarlas en orden; aprobación sin cambios de órdenes, objetivos ni criterios. Aprobación para desarrollo, no dictamen sobre salidas de modelos.

**Decisión del investigador:**

- [x] Aprobada sin cambios.
- [ ] Requiere correcciones.
- [ ] No aprobada.

**Correcciones u observaciones:**

Sin correcciones solicitadas.

**Revisor y fecha:** Investigador (usuario), 2026-10-17.

<details>
<summary>Metadatos y trazabilidad de la ficha original</summary>

```json
{
  "reference_status": "approved",
  "split": "development",
  "development_version": "0.2",
  "overlap_status": "coincidencia_detectada_v02",
  "overlap_audit_history": [
    {
      "development_version": "0.1",
      "input_audited": "please count the the dishes on the shelf",
      "development_sha256": "02103490f89367add79ae9b6aea90e01ecd7f9def7cb32c24d9fb51e6b0b5c7b",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": [
          3455
        ]
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    },
    {
      "development_version": "0.2",
      "input_audited": "please count the the toys on the storage rack",
      "development_sha256": "4c1a356fa50ac317ad6b428c101a48183968a41e2771e2ad2bd7c622f61d4480",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "audit_path": "reports/evaluation/auditoria_desarrollo_v02.json",
      "audit_sha256": "f4d5c3c3088dc5bd9f61d6ebef4b33716401dd4014491585317a184e647e0346",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": [
          6467
        ]
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    }
  ],
  "revision_history": [
    {
      "version": "0.2",
      "previous_input": "please count the the dishes on the shelf",
      "previous_goals_ref": [
        "go(shelf)",
        "count(dishes, kind=object)"
      ],
      "reason": "Sustitución de las tres variantes de un grupo con coincidencias; nueva auditoría pendiente."
    }
  ],
  "planned_assessment": {
    "semantic": "no_ejecutado",
    "plan_contract": "no_ejecutado",
    "task_fulfillment": "no_ejecutado",
    "latency_ms": null
  }
}
```

</details>

## DEV-034

**Intención:** INT-12 · **Grupo:** informacion_fija · **Variante:** canonica · **Bloque:** funcional_y_linguistico

**Orden original:**

> Find Charlie in the living room and tell Charlie the current time.

**Propósito:** Información y persona destinataria

**Respuesta prevista:** `executable`.

**Objetivos propuestos:**

```text
go(living room)
find(Charlie, kind=person)
tell(current_time)
```

**Subtareas requeridas:**

- Localizar a Charlie en living room.
- Comunicarle la hora actual.

**Restricciones:**

- Normalizar la información a current_time y conservar el contexto de Charlie.
- No reemplazar la hora por fecha o nombre del equipo.

**Conductas prohibidas:**

- Inventar entidades, destinos o subtareas no solicitados.

**Variaciones aceptables:**

- Variar el texto de anuncios conservando su sentido.
- Usar identificadores internos consistentes sin cambiar el referente.

**Límites de verificación:**

- Comprobar que el diálogo se dirige a la persona identificada; no inferir identidad correcta de un simple acuse hablado.

**Condiciones iniciales:**

```json
{
  "location": "unknown",
  "holding": "nothing",
  "focus": false,
  "manipulation_enabled": true,
  "independent_request": true
}
```

**Supuestos del escenario:**

- Las entidades mencionadas son referencias del dominio; su detección y disponibilidad física no se evalúan.
- Cada orden se procesa sin conversación previa.

**Comprobaciones comunes del plan:**

- Acciones y parámetros dentro del contrato compartido.
- No añadir tareas ajenas; se admiten los cierres convencionales de retorno y comunicación.
- Referentes consistentes y dependencias de adquisición/entrega respetadas.
- Distinguir protocolo generado de operación física no observada.

**Notas existentes de revisión:**

- 2026-10-17: el investigador confirmó en la conversación haber revisado las 60 fichas y encontrarlas en orden; aprobación sin cambios de órdenes, objetivos ni criterios. Aprobación para desarrollo, no dictamen sobre salidas de modelos.

**Decisión del investigador:**

- [x] Aprobada sin cambios.
- [ ] Requiere correcciones.
- [ ] No aprobada.

**Correcciones u observaciones:**

Sin correcciones solicitadas.

**Revisor y fecha:** Investigador (usuario), 2026-10-17.

<details>
<summary>Metadatos y trazabilidad de la ficha original</summary>

```json
{
  "reference_status": "approved",
  "split": "development",
  "development_version": "0.2",
  "overlap_status": "sin_coincidencia_detectada_v02",
  "overlap_audit_history": [
    {
      "development_version": "0.1",
      "input_audited": "Find Charlie in the living room and tell Charlie the current time.",
      "development_sha256": "02103490f89367add79ae9b6aea90e01ecd7f9def7cb32c24d9fb51e6b0b5c7b",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    },
    {
      "development_version": "0.2",
      "input_audited": "Find Charlie in the living room and tell Charlie the current time.",
      "development_sha256": "4c1a356fa50ac317ad6b428c101a48183968a41e2771e2ad2bd7c622f61d4480",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "audit_path": "reports/evaluation/auditoria_desarrollo_v02.json",
      "audit_sha256": "f4d5c3c3088dc5bd9f61d6ebef4b33716401dd4014491585317a184e647e0346",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    }
  ],
  "planned_assessment": {
    "semantic": "no_ejecutado",
    "plan_contract": "no_ejecutado",
    "task_fulfillment": "no_ejecutado",
    "latency_ms": null
  }
}
```

</details>

## DEV-035

**Intención:** INT-12 · **Grupo:** informacion_fija · **Variante:** parafrasis · **Bloque:** funcional_y_linguistico

**Orden original:**

> Locate Charlie in the living room and say what time it is to Charlie.

**Propósito:** Información y persona destinataria

**Respuesta prevista:** `executable`.

**Objetivos propuestos:**

```text
go(living room)
find(Charlie, kind=person)
tell(current_time)
```

**Subtareas requeridas:**

- Localizar a Charlie en living room.
- Comunicarle la hora actual.

**Restricciones:**

- Normalizar la información a current_time y conservar el contexto de Charlie.
- No reemplazar la hora por fecha o nombre del equipo.

**Conductas prohibidas:**

- Inventar entidades, destinos o subtareas no solicitados.

**Variaciones aceptables:**

- Variar el texto de anuncios conservando su sentido.
- Usar identificadores internos consistentes sin cambiar el referente.

**Límites de verificación:**

- Comprobar que el diálogo se dirige a la persona identificada; no inferir identidad correcta de un simple acuse hablado.

**Condiciones iniciales:**

```json
{
  "location": "unknown",
  "holding": "nothing",
  "focus": false,
  "manipulation_enabled": true,
  "independent_request": true
}
```

**Supuestos del escenario:**

- Las entidades mencionadas son referencias del dominio; su detección y disponibilidad física no se evalúan.
- Cada orden se procesa sin conversación previa.

**Comprobaciones comunes del plan:**

- Acciones y parámetros dentro del contrato compartido.
- No añadir tareas ajenas; se admiten los cierres convencionales de retorno y comunicación.
- Referentes consistentes y dependencias de adquisición/entrega respetadas.
- Distinguir protocolo generado de operación física no observada.

**Notas existentes de revisión:**

- 2026-10-17: el investigador confirmó en la conversación haber revisado las 60 fichas y encontrarlas en orden; aprobación sin cambios de órdenes, objetivos ni criterios. Aprobación para desarrollo, no dictamen sobre salidas de modelos.

**Decisión del investigador:**

- [x] Aprobada sin cambios.
- [ ] Requiere correcciones.
- [ ] No aprobada.

**Correcciones u observaciones:**

Sin correcciones solicitadas.

**Revisor y fecha:** Investigador (usuario), 2026-10-17.

<details>
<summary>Metadatos y trazabilidad de la ficha original</summary>

```json
{
  "reference_status": "approved",
  "split": "development",
  "development_version": "0.2",
  "overlap_status": "sin_coincidencia_detectada_v02",
  "overlap_audit_history": [
    {
      "development_version": "0.1",
      "input_audited": "Locate Charlie in the living room and say what time it is to Charlie.",
      "development_sha256": "02103490f89367add79ae9b6aea90e01ecd7f9def7cb32c24d9fb51e6b0b5c7b",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    },
    {
      "development_version": "0.2",
      "input_audited": "Locate Charlie in the living room and say what time it is to Charlie.",
      "development_sha256": "4c1a356fa50ac317ad6b428c101a48183968a41e2771e2ad2bd7c622f61d4480",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "audit_path": "reports/evaluation/auditoria_desarrollo_v02.json",
      "audit_sha256": "f4d5c3c3088dc5bd9f61d6ebef4b33716401dd4014491585317a184e647e0346",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    }
  ],
  "planned_assessment": {
    "semantic": "no_ejecutado",
    "plan_contract": "no_ejecutado",
    "task_fulfillment": "no_ejecutado",
    "latency_ms": null
  }
}
```

</details>

## DEV-036

**Intención:** INT-12 · **Grupo:** informacion_fija · **Variante:** ruido_leve · **Bloque:** funcional_y_linguistico

**Orden original:**

> please find Charlie in the living  room and tell Charlie the current time

**Propósito:** Información y persona destinataria

**Respuesta prevista:** `executable`.

**Objetivos propuestos:**

```text
go(living room)
find(Charlie, kind=person)
tell(current_time)
```

**Subtareas requeridas:**

- Localizar a Charlie en living room.
- Comunicarle la hora actual.

**Restricciones:**

- Normalizar la información a current_time y conservar el contexto de Charlie.
- No reemplazar la hora por fecha o nombre del equipo.

**Conductas prohibidas:**

- Inventar entidades, destinos o subtareas no solicitados.

**Variaciones aceptables:**

- Variar el texto de anuncios conservando su sentido.
- Usar identificadores internos consistentes sin cambiar el referente.

**Límites de verificación:**

- Comprobar que el diálogo se dirige a la persona identificada; no inferir identidad correcta de un simple acuse hablado.

**Condiciones iniciales:**

```json
{
  "location": "unknown",
  "holding": "nothing",
  "focus": false,
  "manipulation_enabled": true,
  "independent_request": true
}
```

**Supuestos del escenario:**

- Las entidades mencionadas son referencias del dominio; su detección y disponibilidad física no se evalúan.
- Cada orden se procesa sin conversación previa.

**Comprobaciones comunes del plan:**

- Acciones y parámetros dentro del contrato compartido.
- No añadir tareas ajenas; se admiten los cierres convencionales de retorno y comunicación.
- Referentes consistentes y dependencias de adquisición/entrega respetadas.
- Distinguir protocolo generado de operación física no observada.

**Notas existentes de revisión:**

- 2026-10-17: el investigador confirmó en la conversación haber revisado las 60 fichas y encontrarlas en orden; aprobación sin cambios de órdenes, objetivos ni criterios. Aprobación para desarrollo, no dictamen sobre salidas de modelos.

**Decisión del investigador:**

- [x] Aprobada sin cambios.
- [ ] Requiere correcciones.
- [ ] No aprobada.

**Correcciones u observaciones:**

Sin correcciones solicitadas.

**Revisor y fecha:** Investigador (usuario), 2026-10-17.

<details>
<summary>Metadatos y trazabilidad de la ficha original</summary>

```json
{
  "reference_status": "approved",
  "split": "development",
  "development_version": "0.2",
  "overlap_status": "sin_coincidencia_detectada_v02",
  "overlap_audit_history": [
    {
      "development_version": "0.1",
      "input_audited": "please find Charlie in the living  room and tell Charlie the current time",
      "development_sha256": "02103490f89367add79ae9b6aea90e01ecd7f9def7cb32c24d9fb51e6b0b5c7b",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    },
    {
      "development_version": "0.2",
      "input_audited": "please find Charlie in the living  room and tell Charlie the current time",
      "development_sha256": "4c1a356fa50ac317ad6b428c101a48183968a41e2771e2ad2bd7c622f61d4480",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "audit_path": "reports/evaluation/auditoria_desarrollo_v02.json",
      "audit_sha256": "f4d5c3c3088dc5bd9f61d6ebef4b33716401dd4014491585317a184e647e0346",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    }
  ],
  "planned_assessment": {
    "semantic": "no_ejecutado",
    "plan_contract": "no_ejecutado",
    "task_fulfillment": "no_ejecutado",
    "latency_ms": null
  }
}
```

</details>

## DEV-037

**Intención:** INT-13 · **Grupo:** guardar_informacion · **Variante:** canonica · **Bloque:** funcional_y_linguistico

**Orden original:**

> Find a person in the bedroom, ask their name, and come back to tell me their name.

**Propósito:** Información adquirida y retorno

**Respuesta prevista:** `executable`.

**Objetivos propuestos:**

```text
go(bedroom)
find(person, kind=person)
save(name)
go(instruction_point)
tell(name)
```

**Subtareas requeridas:**

- Encontrar una persona en bedroom y adquirir su nombre.
- Regresar al operador y comunicar el nombre adquirido.

**Restricciones:**

- No inventar el nombre ni confundirlo con un nombre fijo del catálogo.
- La comunicación al operador debe referirse a la información adquirida.

**Conductas prohibidas:**

- Inventar entidades, destinos o subtareas no solicitados.

**Variaciones aceptables:**

- Variar el texto de anuncios conservando su sentido.
- Usar identificadores internos consistentes sin cambiar el referente.

**Límites de verificación:**

- La persistencia y recuperación de saved_name deben verificarse respecto del contrato del ejecutor.

**Condiciones iniciales:**

```json
{
  "location": "unknown",
  "holding": "nothing",
  "focus": false,
  "manipulation_enabled": true,
  "independent_request": true
}
```

**Supuestos del escenario:**

- Las entidades mencionadas son referencias del dominio; su detección y disponibilidad física no se evalúan.
- Cada orden se procesa sin conversación previa.

**Comprobaciones comunes del plan:**

- Acciones y parámetros dentro del contrato compartido.
- No añadir tareas ajenas; se admiten los cierres convencionales de retorno y comunicación.
- Referentes consistentes y dependencias de adquisición/entrega respetadas.
- Distinguir protocolo generado de operación física no observada.

**Notas existentes de revisión:**

- 2026-10-17: el investigador confirmó en la conversación haber revisado las 60 fichas y encontrarlas en orden; aprobación sin cambios de órdenes, objetivos ni criterios. Aprobación para desarrollo, no dictamen sobre salidas de modelos.

**Decisión del investigador:**

- [x] Aprobada sin cambios.
- [ ] Requiere correcciones.
- [ ] No aprobada.

**Correcciones u observaciones:**

Sin correcciones solicitadas.

**Revisor y fecha:** Investigador (usuario), 2026-10-17.

<details>
<summary>Metadatos y trazabilidad de la ficha original</summary>

```json
{
  "reference_status": "approved",
  "split": "development",
  "development_version": "0.2",
  "overlap_status": "sin_coincidencia_detectada_v02",
  "overlap_audit_history": [
    {
      "development_version": "0.1",
      "input_audited": "Find a person in the bedroom, ask their name, and come back to tell me their name.",
      "development_sha256": "02103490f89367add79ae9b6aea90e01ecd7f9def7cb32c24d9fb51e6b0b5c7b",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    },
    {
      "development_version": "0.2",
      "input_audited": "Find a person in the bedroom, ask their name, and come back to tell me their name.",
      "development_sha256": "4c1a356fa50ac317ad6b428c101a48183968a41e2771e2ad2bd7c622f61d4480",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "audit_path": "reports/evaluation/auditoria_desarrollo_v02.json",
      "audit_sha256": "f4d5c3c3088dc5bd9f61d6ebef4b33716401dd4014491585317a184e647e0346",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    }
  ],
  "planned_assessment": {
    "semantic": "no_ejecutado",
    "plan_contract": "no_ejecutado",
    "task_fulfillment": "no_ejecutado",
    "latency_ms": null
  }
}
```

</details>

## DEV-038

**Intención:** INT-13 · **Grupo:** guardar_informacion · **Variante:** parafrasis · **Bloque:** funcional_y_linguistico

**Orden original:**

> Go to the bedroom, learn the name of a person there, then return and report it to me.

**Propósito:** Información adquirida y retorno

**Respuesta prevista:** `executable`.

**Objetivos propuestos:**

```text
go(bedroom)
find(person, kind=person)
save(name)
go(instruction_point)
tell(name)
```

**Subtareas requeridas:**

- Encontrar una persona en bedroom y adquirir su nombre.
- Regresar al operador y comunicar el nombre adquirido.

**Restricciones:**

- No inventar el nombre ni confundirlo con un nombre fijo del catálogo.
- La comunicación al operador debe referirse a la información adquirida.

**Conductas prohibidas:**

- Inventar entidades, destinos o subtareas no solicitados.

**Variaciones aceptables:**

- Variar el texto de anuncios conservando su sentido.
- Usar identificadores internos consistentes sin cambiar el referente.

**Límites de verificación:**

- La persistencia y recuperación de saved_name deben verificarse respecto del contrato del ejecutor.

**Condiciones iniciales:**

```json
{
  "location": "unknown",
  "holding": "nothing",
  "focus": false,
  "manipulation_enabled": true,
  "independent_request": true
}
```

**Supuestos del escenario:**

- Las entidades mencionadas son referencias del dominio; su detección y disponibilidad física no se evalúan.
- Cada orden se procesa sin conversación previa.

**Comprobaciones comunes del plan:**

- Acciones y parámetros dentro del contrato compartido.
- No añadir tareas ajenas; se admiten los cierres convencionales de retorno y comunicación.
- Referentes consistentes y dependencias de adquisición/entrega respetadas.
- Distinguir protocolo generado de operación física no observada.

**Notas existentes de revisión:**

- 2026-10-17: el investigador confirmó en la conversación haber revisado las 60 fichas y encontrarlas en orden; aprobación sin cambios de órdenes, objetivos ni criterios. Aprobación para desarrollo, no dictamen sobre salidas de modelos.

**Decisión del investigador:**

- [x] Aprobada sin cambios.
- [ ] Requiere correcciones.
- [ ] No aprobada.

**Correcciones u observaciones:**

Sin correcciones solicitadas.

**Revisor y fecha:** Investigador (usuario), 2026-10-17.

<details>
<summary>Metadatos y trazabilidad de la ficha original</summary>

```json
{
  "reference_status": "approved",
  "split": "development",
  "development_version": "0.2",
  "overlap_status": "sin_coincidencia_detectada_v02",
  "overlap_audit_history": [
    {
      "development_version": "0.1",
      "input_audited": "Go to the bedroom, learn the name of a person there, then return and report it to me.",
      "development_sha256": "02103490f89367add79ae9b6aea90e01ecd7f9def7cb32c24d9fb51e6b0b5c7b",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    },
    {
      "development_version": "0.2",
      "input_audited": "Go to the bedroom, learn the name of a person there, then return and report it to me.",
      "development_sha256": "4c1a356fa50ac317ad6b428c101a48183968a41e2771e2ad2bd7c622f61d4480",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "audit_path": "reports/evaluation/auditoria_desarrollo_v02.json",
      "audit_sha256": "f4d5c3c3088dc5bd9f61d6ebef4b33716401dd4014491585317a184e647e0346",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    }
  ],
  "planned_assessment": {
    "semantic": "no_ejecutado",
    "plan_contract": "no_ejecutado",
    "task_fulfillment": "no_ejecutado",
    "latency_ms": null
  }
}
```

</details>

## DEV-039

**Intención:** INT-13 · **Grupo:** guardar_informacion · **Variante:** ruido_leve · **Bloque:** funcional_y_linguistico

**Orden original:**

> please find a person in the bedroom ask their name and come back to tell me their name

**Propósito:** Información adquirida y retorno

**Respuesta prevista:** `executable`.

**Objetivos propuestos:**

```text
go(bedroom)
find(person, kind=person)
save(name)
go(instruction_point)
tell(name)
```

**Subtareas requeridas:**

- Encontrar una persona en bedroom y adquirir su nombre.
- Regresar al operador y comunicar el nombre adquirido.

**Restricciones:**

- No inventar el nombre ni confundirlo con un nombre fijo del catálogo.
- La comunicación al operador debe referirse a la información adquirida.

**Conductas prohibidas:**

- Inventar entidades, destinos o subtareas no solicitados.

**Variaciones aceptables:**

- Variar el texto de anuncios conservando su sentido.
- Usar identificadores internos consistentes sin cambiar el referente.

**Límites de verificación:**

- La persistencia y recuperación de saved_name deben verificarse respecto del contrato del ejecutor.

**Condiciones iniciales:**

```json
{
  "location": "unknown",
  "holding": "nothing",
  "focus": false,
  "manipulation_enabled": true,
  "independent_request": true
}
```

**Supuestos del escenario:**

- Las entidades mencionadas son referencias del dominio; su detección y disponibilidad física no se evalúan.
- Cada orden se procesa sin conversación previa.

**Comprobaciones comunes del plan:**

- Acciones y parámetros dentro del contrato compartido.
- No añadir tareas ajenas; se admiten los cierres convencionales de retorno y comunicación.
- Referentes consistentes y dependencias de adquisición/entrega respetadas.
- Distinguir protocolo generado de operación física no observada.

**Notas existentes de revisión:**

- 2026-10-17: el investigador confirmó en la conversación haber revisado las 60 fichas y encontrarlas en orden; aprobación sin cambios de órdenes, objetivos ni criterios. Aprobación para desarrollo, no dictamen sobre salidas de modelos.

**Decisión del investigador:**

- [x] Aprobada sin cambios.
- [ ] Requiere correcciones.
- [ ] No aprobada.

**Correcciones u observaciones:**

Sin correcciones solicitadas.

**Revisor y fecha:** Investigador (usuario), 2026-10-17.

<details>
<summary>Metadatos y trazabilidad de la ficha original</summary>

```json
{
  "reference_status": "approved",
  "split": "development",
  "development_version": "0.2",
  "overlap_status": "sin_coincidencia_detectada_v02",
  "overlap_audit_history": [
    {
      "development_version": "0.1",
      "input_audited": "please find a person in the bedroom ask their name and come back to tell me their name",
      "development_sha256": "02103490f89367add79ae9b6aea90e01ecd7f9def7cb32c24d9fb51e6b0b5c7b",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    },
    {
      "development_version": "0.2",
      "input_audited": "please find a person in the bedroom ask their name and come back to tell me their name",
      "development_sha256": "4c1a356fa50ac317ad6b428c101a48183968a41e2771e2ad2bd7c622f61d4480",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "audit_path": "reports/evaluation/auditoria_desarrollo_v02.json",
      "audit_sha256": "f4d5c3c3088dc5bd9f61d6ebef4b33716401dd4014491585317a184e647e0346",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    }
  ],
  "planned_assessment": {
    "semantic": "no_ejecutado",
    "plan_contract": "no_ejecutado",
    "task_fulfillment": "no_ejecutado",
    "latency_ms": null
  }
}
```

</details>

## DEV-040

**Intención:** INT-14 · **Grupo:** respuesta_pregunta · **Variante:** canonica · **Bloque:** funcional_y_linguistico

**Orden original:**

> Find the waving person in the corridor and answer their question.

**Propósito:** Interacción y escucha previa

**Respuesta prevista:** `executable`.

**Objetivos propuestos:**

```text
go(corridor)
find(person, kind=person, gesture='waving person')
answer_question()
```

**Subtareas requeridas:**

- Localizar en corridor a la persona que saluda con la mano.
- Escuchar su pregunta y solicitar la respuesta.

**Restricciones:**

- Conservar el contexto de esa persona.
- No inventar la pregunta ni una respuesta concreta en el plan.

**Conductas prohibidas:**

- Inventar entidades, destinos o subtareas no solicitados.

**Variaciones aceptables:**

- Variar el texto de anuncios conservando su sentido.
- Usar identificadores internos consistentes sin cambiar el referente.

**Límites de verificación:**

Sin elementos especificados en la ficha.

**Condiciones iniciales:**

```json
{
  "location": "unknown",
  "holding": "nothing",
  "focus": false,
  "manipulation_enabled": true,
  "independent_request": true
}
```

**Supuestos del escenario:**

- Las entidades mencionadas son referencias del dominio; su detección y disponibilidad física no se evalúan.
- Cada orden se procesa sin conversación previa.

**Comprobaciones comunes del plan:**

- Acciones y parámetros dentro del contrato compartido.
- No añadir tareas ajenas; se admiten los cierres convencionales de retorno y comunicación.
- Referentes consistentes y dependencias de adquisición/entrega respetadas.
- Distinguir protocolo generado de operación física no observada.

**Notas existentes de revisión:**

- 2026-10-17: el investigador confirmó en la conversación haber revisado las 60 fichas y encontrarlas en orden; aprobación sin cambios de órdenes, objetivos ni criterios. Aprobación para desarrollo, no dictamen sobre salidas de modelos.

**Decisión del investigador:**

- [x] Aprobada sin cambios.
- [ ] Requiere correcciones.
- [ ] No aprobada.

**Correcciones u observaciones:**

Sin correcciones solicitadas.

**Revisor y fecha:** Investigador (usuario), 2026-10-17.

<details>
<summary>Metadatos y trazabilidad de la ficha original</summary>

```json
{
  "reference_status": "approved",
  "split": "development",
  "development_version": "0.2",
  "overlap_status": "coincidencia_detectada_v02",
  "overlap_audit_history": [
    {
      "development_version": "0.1",
      "input_audited": "Find the waving person in the laundry and answer their question.",
      "development_sha256": "02103490f89367add79ae9b6aea90e01ecd7f9def7cb32c24d9fb51e6b0b5c7b",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [
          23160
        ],
        "normalizador_real": [
          23160
        ]
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    },
    {
      "development_version": "0.2",
      "input_audited": "Find the waving person in the corridor and answer their question.",
      "development_sha256": "4c1a356fa50ac317ad6b428c101a48183968a41e2771e2ad2bd7c622f61d4480",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "audit_path": "reports/evaluation/auditoria_desarrollo_v02.json",
      "audit_sha256": "f4d5c3c3088dc5bd9f61d6ebef4b33716401dd4014491585317a184e647e0346",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [
          18455
        ],
        "normalizador_real": [
          18455
        ]
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    }
  ],
  "revision_history": [
    {
      "version": "0.2",
      "previous_input": "Find the waving person in the laundry and answer their question.",
      "previous_goals_ref": [
        "go(laundry)",
        "find(person, kind=person, gesture='waving person')",
        "answer_question()"
      ],
      "reason": "Sustitución de las tres variantes de un grupo con coincidencias; nueva auditoría pendiente."
    }
  ],
  "planned_assessment": {
    "semantic": "no_ejecutado",
    "plan_contract": "no_ejecutado",
    "task_fulfillment": "no_ejecutado",
    "latency_ms": null
  }
}
```

</details>

## DEV-041

**Intención:** INT-14 · **Grupo:** respuesta_pregunta · **Variante:** parafrasis · **Bloque:** funcional_y_linguistico

**Orden original:**

> In the corridor, locate the person who is waving and respond to that person's question.

**Propósito:** Interacción y escucha previa

**Respuesta prevista:** `executable`.

**Objetivos propuestos:**

```text
go(corridor)
find(person, kind=person, gesture='waving person')
answer_question()
```

**Subtareas requeridas:**

- Localizar en corridor a la persona que saluda con la mano.
- Escuchar su pregunta y solicitar la respuesta.

**Restricciones:**

- Conservar el contexto de esa persona.
- No inventar la pregunta ni una respuesta concreta en el plan.

**Conductas prohibidas:**

- Inventar entidades, destinos o subtareas no solicitados.

**Variaciones aceptables:**

- Variar el texto de anuncios conservando su sentido.
- Usar identificadores internos consistentes sin cambiar el referente.

**Límites de verificación:**

Sin elementos especificados en la ficha.

**Condiciones iniciales:**

```json
{
  "location": "unknown",
  "holding": "nothing",
  "focus": false,
  "manipulation_enabled": true,
  "independent_request": true
}
```

**Supuestos del escenario:**

- Las entidades mencionadas son referencias del dominio; su detección y disponibilidad física no se evalúan.
- Cada orden se procesa sin conversación previa.

**Comprobaciones comunes del plan:**

- Acciones y parámetros dentro del contrato compartido.
- No añadir tareas ajenas; se admiten los cierres convencionales de retorno y comunicación.
- Referentes consistentes y dependencias de adquisición/entrega respetadas.
- Distinguir protocolo generado de operación física no observada.

**Notas existentes de revisión:**

- 2026-10-17: el investigador confirmó en la conversación haber revisado las 60 fichas y encontrarlas en orden; aprobación sin cambios de órdenes, objetivos ni criterios. Aprobación para desarrollo, no dictamen sobre salidas de modelos.

**Decisión del investigador:**

- [x] Aprobada sin cambios.
- [ ] Requiere correcciones.
- [ ] No aprobada.

**Correcciones u observaciones:**

Sin correcciones solicitadas.

**Revisor y fecha:** Investigador (usuario), 2026-10-17.

<details>
<summary>Metadatos y trazabilidad de la ficha original</summary>

```json
{
  "reference_status": "approved",
  "split": "development",
  "development_version": "0.2",
  "overlap_status": "sin_coincidencia_detectada_v02",
  "overlap_audit_history": [
    {
      "development_version": "0.1",
      "input_audited": "In the laundry, locate the person who is waving and respond to that person's question.",
      "development_sha256": "02103490f89367add79ae9b6aea90e01ecd7f9def7cb32c24d9fb51e6b0b5c7b",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    },
    {
      "development_version": "0.2",
      "input_audited": "In the corridor, locate the person who is waving and respond to that person's question.",
      "development_sha256": "4c1a356fa50ac317ad6b428c101a48183968a41e2771e2ad2bd7c622f61d4480",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "audit_path": "reports/evaluation/auditoria_desarrollo_v02.json",
      "audit_sha256": "f4d5c3c3088dc5bd9f61d6ebef4b33716401dd4014491585317a184e647e0346",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    }
  ],
  "revision_history": [
    {
      "version": "0.2",
      "previous_input": "In the laundry, locate the person who is waving and respond to that person's question.",
      "previous_goals_ref": [
        "go(laundry)",
        "find(person, kind=person, gesture='waving person')",
        "answer_question()"
      ],
      "reason": "Sustitución de las tres variantes de un grupo con coincidencias; nueva auditoría pendiente."
    }
  ],
  "planned_assessment": {
    "semantic": "no_ejecutado",
    "plan_contract": "no_ejecutado",
    "task_fulfillment": "no_ejecutado",
    "latency_ms": null
  }
}
```

</details>

## DEV-042

**Intención:** INT-14 · **Grupo:** respuesta_pregunta · **Variante:** ruido_leve · **Bloque:** funcional_y_linguistico

**Orden original:**

> find the waving person in the corridor and and answer their question please

**Propósito:** Interacción y escucha previa

**Respuesta prevista:** `executable`.

**Objetivos propuestos:**

```text
go(corridor)
find(person, kind=person, gesture='waving person')
answer_question()
```

**Subtareas requeridas:**

- Localizar en corridor a la persona que saluda con la mano.
- Escuchar su pregunta y solicitar la respuesta.

**Restricciones:**

- Conservar el contexto de esa persona.
- No inventar la pregunta ni una respuesta concreta en el plan.

**Conductas prohibidas:**

- Inventar entidades, destinos o subtareas no solicitados.

**Variaciones aceptables:**

- Variar el texto de anuncios conservando su sentido.
- Usar identificadores internos consistentes sin cambiar el referente.

**Límites de verificación:**

Sin elementos especificados en la ficha.

**Condiciones iniciales:**

```json
{
  "location": "unknown",
  "holding": "nothing",
  "focus": false,
  "manipulation_enabled": true,
  "independent_request": true
}
```

**Supuestos del escenario:**

- Las entidades mencionadas son referencias del dominio; su detección y disponibilidad física no se evalúan.
- Cada orden se procesa sin conversación previa.

**Comprobaciones comunes del plan:**

- Acciones y parámetros dentro del contrato compartido.
- No añadir tareas ajenas; se admiten los cierres convencionales de retorno y comunicación.
- Referentes consistentes y dependencias de adquisición/entrega respetadas.
- Distinguir protocolo generado de operación física no observada.

**Notas existentes de revisión:**

- 2026-10-17: el investigador confirmó en la conversación haber revisado las 60 fichas y encontrarlas en orden; aprobación sin cambios de órdenes, objetivos ni criterios. Aprobación para desarrollo, no dictamen sobre salidas de modelos.

**Decisión del investigador:**

- [x] Aprobada sin cambios.
- [ ] Requiere correcciones.
- [ ] No aprobada.

**Correcciones u observaciones:**

Sin correcciones solicitadas.

**Revisor y fecha:** Investigador (usuario), 2026-10-17.

<details>
<summary>Metadatos y trazabilidad de la ficha original</summary>

```json
{
  "reference_status": "approved",
  "split": "development",
  "development_version": "0.2",
  "overlap_status": "coincidencia_detectada_v02",
  "overlap_audit_history": [
    {
      "development_version": "0.1",
      "input_audited": "find the waving person in the laundry and answer their question please",
      "development_sha256": "02103490f89367add79ae9b6aea90e01ecd7f9def7cb32c24d9fb51e6b0b5c7b",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": [
          23160
        ]
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    },
    {
      "development_version": "0.2",
      "input_audited": "find the waving person in the corridor and and answer their question please",
      "development_sha256": "4c1a356fa50ac317ad6b428c101a48183968a41e2771e2ad2bd7c622f61d4480",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "audit_path": "reports/evaluation/auditoria_desarrollo_v02.json",
      "audit_sha256": "f4d5c3c3088dc5bd9f61d6ebef4b33716401dd4014491585317a184e647e0346",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": [
          18455
        ]
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    }
  ],
  "revision_history": [
    {
      "version": "0.2",
      "previous_input": "find the waving person in the laundry and answer their question please",
      "previous_goals_ref": [
        "go(laundry)",
        "find(person, kind=person, gesture='waving person')",
        "answer_question()"
      ],
      "reason": "Sustitución de las tres variantes de un grupo con coincidencias; nueva auditoría pendiente."
    }
  ],
  "planned_assessment": {
    "semantic": "no_ejecutado",
    "plan_contract": "no_ejecutado",
    "task_fulfillment": "no_ejecutado",
    "latency_ms": null
  }
}
```

</details>

## DEV-043

**Intención:** INT-15 · **Grupo:** saludo · **Variante:** canonica · **Bloque:** funcional_y_linguistico

**Orden original:**

> Find Jane in the kitchen and greet her.

**Propósito:** Persona nombrada e interacción

**Respuesta prevista:** `executable`.

**Objetivos propuestos:**

```text
go(kitchen)
find(Jane, kind=person)
greet(Jane)
```

**Subtareas requeridas:**

- Localizar a Jane en kitchen y saludarla.

**Restricciones:**

- Resolver her como Jane; no saludar al operador ni a una persona distinta.

**Conductas prohibidas:**

- Inventar entidades, destinos o subtareas no solicitados.

**Variaciones aceptables:**

- Variar el texto de anuncios conservando su sentido.
- Usar identificadores internos consistentes sin cambiar el referente.

**Límites de verificación:**

- La identificación por nombre debe distinguirse de la búsqueda de una persona cualquiera.

**Condiciones iniciales:**

```json
{
  "location": "unknown",
  "holding": "nothing",
  "focus": false,
  "manipulation_enabled": true,
  "independent_request": true
}
```

**Supuestos del escenario:**

- Las entidades mencionadas son referencias del dominio; su detección y disponibilidad física no se evalúan.
- Cada orden se procesa sin conversación previa.

**Comprobaciones comunes del plan:**

- Acciones y parámetros dentro del contrato compartido.
- No añadir tareas ajenas; se admiten los cierres convencionales de retorno y comunicación.
- Referentes consistentes y dependencias de adquisición/entrega respetadas.
- Distinguir protocolo generado de operación física no observada.

**Notas existentes de revisión:**

- 2026-10-17: el investigador confirmó en la conversación haber revisado las 60 fichas y encontrarlas en orden; aprobación sin cambios de órdenes, objetivos ni criterios. Aprobación para desarrollo, no dictamen sobre salidas de modelos.

**Decisión del investigador:**

- [x] Aprobada sin cambios.
- [ ] Requiere correcciones.
- [ ] No aprobada.

**Correcciones u observaciones:**

Sin correcciones solicitadas.

**Revisor y fecha:** Investigador (usuario), 2026-10-17.

<details>
<summary>Metadatos y trazabilidad de la ficha original</summary>

```json
{
  "reference_status": "approved",
  "split": "development",
  "development_version": "0.2",
  "overlap_status": "sin_coincidencia_detectada_v02",
  "overlap_audit_history": [
    {
      "development_version": "0.1",
      "input_audited": "Find Jane in the kitchen and greet her.",
      "development_sha256": "02103490f89367add79ae9b6aea90e01ecd7f9def7cb32c24d9fb51e6b0b5c7b",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    },
    {
      "development_version": "0.2",
      "input_audited": "Find Jane in the kitchen and greet her.",
      "development_sha256": "4c1a356fa50ac317ad6b428c101a48183968a41e2771e2ad2bd7c622f61d4480",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "audit_path": "reports/evaluation/auditoria_desarrollo_v02.json",
      "audit_sha256": "f4d5c3c3088dc5bd9f61d6ebef4b33716401dd4014491585317a184e647e0346",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    }
  ],
  "planned_assessment": {
    "semantic": "no_ejecutado",
    "plan_contract": "no_ejecutado",
    "task_fulfillment": "no_ejecutado",
    "latency_ms": null
  }
}
```

</details>

## DEV-044

**Intención:** INT-15 · **Grupo:** saludo · **Variante:** parafrasis · **Bloque:** funcional_y_linguistico

**Orden original:**

> Look for Jane in the kitchen and say hello to Jane.

**Propósito:** Persona nombrada e interacción

**Respuesta prevista:** `executable`.

**Objetivos propuestos:**

```text
go(kitchen)
find(Jane, kind=person)
greet(Jane)
```

**Subtareas requeridas:**

- Localizar a Jane en kitchen y saludarla.

**Restricciones:**

- Resolver her como Jane; no saludar al operador ni a una persona distinta.

**Conductas prohibidas:**

- Inventar entidades, destinos o subtareas no solicitados.

**Variaciones aceptables:**

- Variar el texto de anuncios conservando su sentido.
- Usar identificadores internos consistentes sin cambiar el referente.

**Límites de verificación:**

- La identificación por nombre debe distinguirse de la búsqueda de una persona cualquiera.

**Condiciones iniciales:**

```json
{
  "location": "unknown",
  "holding": "nothing",
  "focus": false,
  "manipulation_enabled": true,
  "independent_request": true
}
```

**Supuestos del escenario:**

- Las entidades mencionadas son referencias del dominio; su detección y disponibilidad física no se evalúan.
- Cada orden se procesa sin conversación previa.

**Comprobaciones comunes del plan:**

- Acciones y parámetros dentro del contrato compartido.
- No añadir tareas ajenas; se admiten los cierres convencionales de retorno y comunicación.
- Referentes consistentes y dependencias de adquisición/entrega respetadas.
- Distinguir protocolo generado de operación física no observada.

**Notas existentes de revisión:**

- 2026-10-17: el investigador confirmó en la conversación haber revisado las 60 fichas y encontrarlas en orden; aprobación sin cambios de órdenes, objetivos ni criterios. Aprobación para desarrollo, no dictamen sobre salidas de modelos.

**Decisión del investigador:**

- [x] Aprobada sin cambios.
- [ ] Requiere correcciones.
- [ ] No aprobada.

**Correcciones u observaciones:**

Sin correcciones solicitadas.

**Revisor y fecha:** Investigador (usuario), 2026-10-17.

<details>
<summary>Metadatos y trazabilidad de la ficha original</summary>

```json
{
  "reference_status": "approved",
  "split": "development",
  "development_version": "0.2",
  "overlap_status": "sin_coincidencia_detectada_v02",
  "overlap_audit_history": [
    {
      "development_version": "0.1",
      "input_audited": "Look for Jane in the kitchen and say hello to Jane.",
      "development_sha256": "02103490f89367add79ae9b6aea90e01ecd7f9def7cb32c24d9fb51e6b0b5c7b",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    },
    {
      "development_version": "0.2",
      "input_audited": "Look for Jane in the kitchen and say hello to Jane.",
      "development_sha256": "4c1a356fa50ac317ad6b428c101a48183968a41e2771e2ad2bd7c622f61d4480",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "audit_path": "reports/evaluation/auditoria_desarrollo_v02.json",
      "audit_sha256": "f4d5c3c3088dc5bd9f61d6ebef4b33716401dd4014491585317a184e647e0346",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    }
  ],
  "planned_assessment": {
    "semantic": "no_ejecutado",
    "plan_contract": "no_ejecutado",
    "task_fulfillment": "no_ejecutado",
    "latency_ms": null
  }
}
```

</details>

## DEV-045

**Intención:** INT-15 · **Grupo:** saludo · **Variante:** ruido_leve · **Bloque:** funcional_y_linguistico

**Orden original:**

> please find Jane in the kichen and greet her

**Propósito:** Persona nombrada e interacción

**Respuesta prevista:** `executable`.

**Objetivos propuestos:**

```text
go(kitchen)
find(Jane, kind=person)
greet(Jane)
```

**Subtareas requeridas:**

- Localizar a Jane en kitchen y saludarla.

**Restricciones:**

- Resolver her como Jane; no saludar al operador ni a una persona distinta.

**Conductas prohibidas:**

- Inventar entidades, destinos o subtareas no solicitados.

**Variaciones aceptables:**

- Variar el texto de anuncios conservando su sentido.
- Usar identificadores internos consistentes sin cambiar el referente.

**Límites de verificación:**

- La identificación por nombre debe distinguirse de la búsqueda de una persona cualquiera.

**Condiciones iniciales:**

```json
{
  "location": "unknown",
  "holding": "nothing",
  "focus": false,
  "manipulation_enabled": true,
  "independent_request": true
}
```

**Supuestos del escenario:**

- Las entidades mencionadas son referencias del dominio; su detección y disponibilidad física no se evalúan.
- Cada orden se procesa sin conversación previa.

**Comprobaciones comunes del plan:**

- Acciones y parámetros dentro del contrato compartido.
- No añadir tareas ajenas; se admiten los cierres convencionales de retorno y comunicación.
- Referentes consistentes y dependencias de adquisición/entrega respetadas.
- Distinguir protocolo generado de operación física no observada.

**Notas existentes de revisión:**

- 2026-10-17: el investigador confirmó en la conversación haber revisado las 60 fichas y encontrarlas en orden; aprobación sin cambios de órdenes, objetivos ni criterios. Aprobación para desarrollo, no dictamen sobre salidas de modelos.

**Decisión del investigador:**

- [x] Aprobada sin cambios.
- [ ] Requiere correcciones.
- [ ] No aprobada.

**Correcciones u observaciones:**

Sin correcciones solicitadas.

**Revisor y fecha:** Investigador (usuario), 2026-10-17.

<details>
<summary>Metadatos y trazabilidad de la ficha original</summary>

```json
{
  "reference_status": "approved",
  "split": "development",
  "development_version": "0.2",
  "overlap_status": "sin_coincidencia_detectada_v02",
  "overlap_audit_history": [
    {
      "development_version": "0.1",
      "input_audited": "please find Jane in the kichen and greet her",
      "development_sha256": "02103490f89367add79ae9b6aea90e01ecd7f9def7cb32c24d9fb51e6b0b5c7b",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    },
    {
      "development_version": "0.2",
      "input_audited": "please find Jane in the kichen and greet her",
      "development_sha256": "4c1a356fa50ac317ad6b428c101a48183968a41e2771e2ad2bd7c622f61d4480",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "audit_path": "reports/evaluation/auditoria_desarrollo_v02.json",
      "audit_sha256": "f4d5c3c3088dc5bd9f61d6ebef4b33716401dd4014491585317a184e647e0346",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    }
  ],
  "planned_assessment": {
    "semantic": "no_ejecutado",
    "plan_contract": "no_ejecutado",
    "task_fulfillment": "no_ejecutado",
    "latency_ms": null
  }
}
```

</details>

## DEV-046

**Intención:** INT-16 · **Grupo:** propiedad_objeto · **Variante:** canonica · **Bloque:** funcional_y_linguistico

**Orden original:**

> Tell me which is the largest fruit on the sofa.

**Propósito:** Comparación de tamaño y reporte

**Respuesta prevista:** `executable`.

**Objetivos propuestos:**

```text
go(sofa)
find(fruit, kind=object, property=largest)
tell(fruit, property=largest)
```

**Subtareas requeridas:**

- Analizar el tamaño de las frutas en sofa y comunicar cuál es la mayor.

**Restricciones:**

- No sustituir tamaño por peso ni buscar un objeto arbitrario.
- biggest y largest son equivalentes semánticos aquí; registrar diferencia literal sin penalizar semántica.

**Conductas prohibidas:**

- Inventar entidades, destinos o subtareas no solicitados.

**Variaciones aceptables:**

- Variar el texto de anuncios conservando su sentido.
- Usar identificadores internos consistentes sin cambiar el referente.
- biggest/ largest: equivalencia semántica solo para la comparación de tamaño; conservar el resultado literal por separado.

**Límites de verificación:**

Sin elementos especificados en la ficha.

**Condiciones iniciales:**

```json
{
  "location": "unknown",
  "holding": "nothing",
  "focus": false,
  "manipulation_enabled": true,
  "independent_request": true
}
```

**Supuestos del escenario:**

- Las entidades mencionadas son referencias del dominio; su detección y disponibilidad física no se evalúan.
- Cada orden se procesa sin conversación previa.

**Comprobaciones comunes del plan:**

- Acciones y parámetros dentro del contrato compartido.
- No añadir tareas ajenas; se admiten los cierres convencionales de retorno y comunicación.
- Referentes consistentes y dependencias de adquisición/entrega respetadas.
- Distinguir protocolo generado de operación física no observada.

**Notas existentes de revisión:**

- 2026-10-17: el investigador confirmó en la conversación haber revisado las 60 fichas y encontrarlas en orden; aprobación sin cambios de órdenes, objetivos ni criterios. Aprobación para desarrollo, no dictamen sobre salidas de modelos.

**Decisión del investigador:**

- [x] Aprobada sin cambios.
- [ ] Requiere correcciones.
- [ ] No aprobada.

**Correcciones u observaciones:**

Sin correcciones solicitadas.

**Revisor y fecha:** Investigador (usuario), 2026-10-17.

<details>
<summary>Metadatos y trazabilidad de la ficha original</summary>

```json
{
  "reference_status": "approved",
  "split": "development",
  "development_version": "0.2",
  "overlap_status": "sin_coincidencia_detectada_v02",
  "overlap_audit_history": [
    {
      "development_version": "0.1",
      "input_audited": "Tell me which is the largest fruit on the sofa.",
      "development_sha256": "02103490f89367add79ae9b6aea90e01ecd7f9def7cb32c24d9fb51e6b0b5c7b",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    },
    {
      "development_version": "0.2",
      "input_audited": "Tell me which is the largest fruit on the sofa.",
      "development_sha256": "4c1a356fa50ac317ad6b428c101a48183968a41e2771e2ad2bd7c622f61d4480",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "audit_path": "reports/evaluation/auditoria_desarrollo_v02.json",
      "audit_sha256": "f4d5c3c3088dc5bd9f61d6ebef4b33716401dd4014491585317a184e647e0346",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    }
  ],
  "planned_assessment": {
    "semantic": "no_ejecutado",
    "plan_contract": "no_ejecutado",
    "task_fulfillment": "no_ejecutado",
    "latency_ms": null
  }
}
```

</details>

## DEV-047

**Intención:** INT-16 · **Grupo:** propiedad_objeto · **Variante:** parafrasis · **Bloque:** funcional_y_linguistico

**Orden original:**

> Identify the biggest fruit on the sofa and report which one it is.

**Propósito:** Comparación de tamaño y reporte

**Respuesta prevista:** `executable`.

**Objetivos propuestos:**

```text
go(sofa)
find(fruit, kind=object, property=largest)
tell(fruit, property=largest)
```

**Subtareas requeridas:**

- Analizar el tamaño de las frutas en sofa y comunicar cuál es la mayor.

**Restricciones:**

- No sustituir tamaño por peso ni buscar un objeto arbitrario.
- biggest y largest son equivalentes semánticos aquí; registrar diferencia literal sin penalizar semántica.

**Conductas prohibidas:**

- Inventar entidades, destinos o subtareas no solicitados.

**Variaciones aceptables:**

- Variar el texto de anuncios conservando su sentido.
- Usar identificadores internos consistentes sin cambiar el referente.
- biggest/ largest: equivalencia semántica solo para la comparación de tamaño; conservar el resultado literal por separado.

**Límites de verificación:**

Sin elementos especificados en la ficha.

**Condiciones iniciales:**

```json
{
  "location": "unknown",
  "holding": "nothing",
  "focus": false,
  "manipulation_enabled": true,
  "independent_request": true
}
```

**Supuestos del escenario:**

- Las entidades mencionadas son referencias del dominio; su detección y disponibilidad física no se evalúan.
- Cada orden se procesa sin conversación previa.

**Comprobaciones comunes del plan:**

- Acciones y parámetros dentro del contrato compartido.
- No añadir tareas ajenas; se admiten los cierres convencionales de retorno y comunicación.
- Referentes consistentes y dependencias de adquisición/entrega respetadas.
- Distinguir protocolo generado de operación física no observada.

**Notas existentes de revisión:**

- 2026-10-17: el investigador confirmó en la conversación haber revisado las 60 fichas y encontrarlas en orden; aprobación sin cambios de órdenes, objetivos ni criterios. Aprobación para desarrollo, no dictamen sobre salidas de modelos.

**Decisión del investigador:**

- [x] Aprobada sin cambios.
- [ ] Requiere correcciones.
- [ ] No aprobada.

**Correcciones u observaciones:**

Sin correcciones solicitadas.

**Revisor y fecha:** Investigador (usuario), 2026-10-17.

<details>
<summary>Metadatos y trazabilidad de la ficha original</summary>

```json
{
  "reference_status": "approved",
  "split": "development",
  "development_version": "0.2",
  "overlap_status": "sin_coincidencia_detectada_v02",
  "overlap_audit_history": [
    {
      "development_version": "0.1",
      "input_audited": "Identify the biggest fruit on the sofa and report which one it is.",
      "development_sha256": "02103490f89367add79ae9b6aea90e01ecd7f9def7cb32c24d9fb51e6b0b5c7b",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    },
    {
      "development_version": "0.2",
      "input_audited": "Identify the biggest fruit on the sofa and report which one it is.",
      "development_sha256": "4c1a356fa50ac317ad6b428c101a48183968a41e2771e2ad2bd7c622f61d4480",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "audit_path": "reports/evaluation/auditoria_desarrollo_v02.json",
      "audit_sha256": "f4d5c3c3088dc5bd9f61d6ebef4b33716401dd4014491585317a184e647e0346",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    }
  ],
  "planned_assessment": {
    "semantic": "no_ejecutado",
    "plan_contract": "no_ejecutado",
    "task_fulfillment": "no_ejecutado",
    "latency_ms": null
  }
}
```

</details>

## DEV-048

**Intención:** INT-16 · **Grupo:** propiedad_objeto · **Variante:** ruido_leve · **Bloque:** funcional_y_linguistico

**Orden original:**

> please tell me which is the largest fruit on the sofa

**Propósito:** Comparación de tamaño y reporte

**Respuesta prevista:** `executable`.

**Objetivos propuestos:**

```text
go(sofa)
find(fruit, kind=object, property=largest)
tell(fruit, property=largest)
```

**Subtareas requeridas:**

- Analizar el tamaño de las frutas en sofa y comunicar cuál es la mayor.

**Restricciones:**

- No sustituir tamaño por peso ni buscar un objeto arbitrario.
- biggest y largest son equivalentes semánticos aquí; registrar diferencia literal sin penalizar semántica.

**Conductas prohibidas:**

- Inventar entidades, destinos o subtareas no solicitados.

**Variaciones aceptables:**

- Variar el texto de anuncios conservando su sentido.
- Usar identificadores internos consistentes sin cambiar el referente.
- biggest/ largest: equivalencia semántica solo para la comparación de tamaño; conservar el resultado literal por separado.

**Límites de verificación:**

Sin elementos especificados en la ficha.

**Condiciones iniciales:**

```json
{
  "location": "unknown",
  "holding": "nothing",
  "focus": false,
  "manipulation_enabled": true,
  "independent_request": true
}
```

**Supuestos del escenario:**

- Las entidades mencionadas son referencias del dominio; su detección y disponibilidad física no se evalúan.
- Cada orden se procesa sin conversación previa.

**Comprobaciones comunes del plan:**

- Acciones y parámetros dentro del contrato compartido.
- No añadir tareas ajenas; se admiten los cierres convencionales de retorno y comunicación.
- Referentes consistentes y dependencias de adquisición/entrega respetadas.
- Distinguir protocolo generado de operación física no observada.

**Notas existentes de revisión:**

- 2026-10-17: el investigador confirmó en la conversación haber revisado las 60 fichas y encontrarlas en orden; aprobación sin cambios de órdenes, objetivos ni criterios. Aprobación para desarrollo, no dictamen sobre salidas de modelos.

**Decisión del investigador:**

- [x] Aprobada sin cambios.
- [ ] Requiere correcciones.
- [ ] No aprobada.

**Correcciones u observaciones:**

Sin correcciones solicitadas.

**Revisor y fecha:** Investigador (usuario), 2026-10-17.

<details>
<summary>Metadatos y trazabilidad de la ficha original</summary>

```json
{
  "reference_status": "approved",
  "split": "development",
  "development_version": "0.2",
  "overlap_status": "sin_coincidencia_detectada_v02",
  "overlap_audit_history": [
    {
      "development_version": "0.1",
      "input_audited": "please tell me which is the largest fruit on the sofa",
      "development_sha256": "02103490f89367add79ae9b6aea90e01ecd7f9def7cb32c24d9fb51e6b0b5c7b",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    },
    {
      "development_version": "0.2",
      "input_audited": "please tell me which is the largest fruit on the sofa",
      "development_sha256": "4c1a356fa50ac317ad6b428c101a48183968a41e2771e2ad2bd7c622f61d4480",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "audit_path": "reports/evaluation/auditoria_desarrollo_v02.json",
      "audit_sha256": "f4d5c3c3088dc5bd9f61d6ebef4b33716401dd4014491585317a184e647e0346",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    }
  ],
  "planned_assessment": {
    "semantic": "no_ejecutado",
    "plan_contract": "no_ejecutado",
    "task_fulfillment": "no_ejecutado",
    "latency_ms": null
  }
}
```

</details>

## DEV-049

**Intención:** INT-17 · **Grupo:** atributos_conjuntos · **Variante:** diagnostico · **Bloque:** limites_y_composicion

**Orden original:**

> Find the person waving and wearing a blue coat in the office, then guide them to the entrance.

**Propósito:** atributos_conjuntos

**Respuesta prevista:** `executable`.

**Objetivos propuestos:**

```text
go(office)
find(person, kind=person, gesture='waving person', wearing='blue coat')
guide(person, to=entrance)
```

**Subtareas requeridas:**

- Buscar en office una única persona que cumpla ambos atributos.
- Guiar a esa persona a entrance.

**Restricciones:**

- La conjunción gesto y vestimenta debe mantenerse; no basta con cualquiera de ellos.

**Conductas prohibidas:**

- Declarar cumplida una propiedad o capacidad sustituida por una aproximación no justificada.

**Variaciones aceptables:**

- Planes alternativos que satisfagan las subtareas y restricciones.

**Límites de verificación:**

- El adaptador conserva un único qualifier y puede perder un atributo; registrar la pérdida.

**Condiciones iniciales:**

```json
{
  "location": "unknown",
  "holding": "nothing",
  "focus": false,
  "manipulation_enabled": true,
  "independent_request": true
}
```

**Supuestos del escenario:**

- Las entidades mencionadas son referencias del dominio; su detección y disponibilidad física no se evalúan.
- Cada orden se procesa sin conversación previa.

**Comprobaciones comunes del plan:**

- Acciones y parámetros dentro del contrato compartido.
- No añadir tareas ajenas; se admiten los cierres convencionales de retorno y comunicación.
- Referentes consistentes y dependencias de adquisición/entrega respetadas.
- Distinguir protocolo generado de operación física no observada.

**Notas existentes de revisión:**

- 2026-10-17: el investigador confirmó en la conversación haber revisado las 60 fichas y encontrarlas en orden; aprobación sin cambios de órdenes, objetivos ni criterios. Aprobación para desarrollo, no dictamen sobre salidas de modelos.

**Decisión del investigador:**

- [x] Aprobada sin cambios.
- [ ] Requiere correcciones.
- [ ] No aprobada.

**Correcciones u observaciones:**

Sin correcciones solicitadas.

**Revisor y fecha:** Investigador (usuario), 2026-10-17.

<details>
<summary>Metadatos y trazabilidad de la ficha original</summary>

```json
{
  "reference_status": "approved",
  "split": "development",
  "development_version": "0.2",
  "overlap_status": "sin_coincidencia_detectada_v02",
  "overlap_audit_history": [
    {
      "development_version": "0.1",
      "input_audited": "Find the person waving and wearing a blue coat in the office, then guide them to the entrance.",
      "development_sha256": "02103490f89367add79ae9b6aea90e01ecd7f9def7cb32c24d9fb51e6b0b5c7b",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    },
    {
      "development_version": "0.2",
      "input_audited": "Find the person waving and wearing a blue coat in the office, then guide them to the entrance.",
      "development_sha256": "4c1a356fa50ac317ad6b428c101a48183968a41e2771e2ad2bd7c622f61d4480",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "audit_path": "reports/evaluation/auditoria_desarrollo_v02.json",
      "audit_sha256": "f4d5c3c3088dc5bd9f61d6ebef4b33716401dd4014491585317a184e647e0346",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    }
  ],
  "planned_assessment": {
    "semantic": "no_ejecutado",
    "plan_contract": "no_ejecutado",
    "task_fulfillment": "no_ejecutado",
    "latency_ms": null
  }
}
```

</details>

## DEV-050

**Intención:** INT-18 · **Grupo:** conteo_personas_filtrado · **Variante:** diagnostico · **Bloque:** limites_y_composicion

**Orden original:**

> Count the people wearing red shirts in the living room.

**Propósito:** conteo_personas_filtrado

**Respuesta prevista:** `executable`.

**Objetivos propuestos:**

```text
go(living room)
count(person, kind=person, wearing='red shirts')
```

**Subtareas requeridas:**

- Contar exclusivamente las personas con camisa roja en living room.
- Comunicar el resultado al operador.

**Restricciones:**

- El plan debe conservar el filtro de vestimenta; un conteo de todas las personas no cumple.

**Conductas prohibidas:**

- Declarar cumplida una propiedad o capacidad sustituida por una aproximación no justificada.

**Variaciones aceptables:**

- Planes alternativos que satisfagan las subtareas y restricciones.

**Límites de verificación:**

- La expansión actual de count puede omitir el filtro; comprobarlo sin equiparar planificabilidad con cumplimiento.

**Condiciones iniciales:**

```json
{
  "location": "unknown",
  "holding": "nothing",
  "focus": false,
  "manipulation_enabled": true,
  "independent_request": true
}
```

**Supuestos del escenario:**

- Las entidades mencionadas son referencias del dominio; su detección y disponibilidad física no se evalúan.
- Cada orden se procesa sin conversación previa.

**Comprobaciones comunes del plan:**

- Acciones y parámetros dentro del contrato compartido.
- No añadir tareas ajenas; se admiten los cierres convencionales de retorno y comunicación.
- Referentes consistentes y dependencias de adquisición/entrega respetadas.
- Distinguir protocolo generado de operación física no observada.

**Notas existentes de revisión:**

- 2026-10-17: el investigador confirmó en la conversación haber revisado las 60 fichas y encontrarlas en orden; aprobación sin cambios de órdenes, objetivos ni criterios. Aprobación para desarrollo, no dictamen sobre salidas de modelos.

**Decisión del investigador:**

- [x] Aprobada sin cambios.
- [ ] Requiere correcciones.
- [ ] No aprobada.

**Correcciones u observaciones:**

Sin correcciones solicitadas.

**Revisor y fecha:** Investigador (usuario), 2026-10-17.

<details>
<summary>Metadatos y trazabilidad de la ficha original</summary>

```json
{
  "reference_status": "approved",
  "split": "development",
  "development_version": "0.2",
  "overlap_status": "sin_coincidencia_detectada_v02",
  "overlap_audit_history": [
    {
      "development_version": "0.1",
      "input_audited": "Count the people wearing red shirts in the living room.",
      "development_sha256": "02103490f89367add79ae9b6aea90e01ecd7f9def7cb32c24d9fb51e6b0b5c7b",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    },
    {
      "development_version": "0.2",
      "input_audited": "Count the people wearing red shirts in the living room.",
      "development_sha256": "4c1a356fa50ac317ad6b428c101a48183968a41e2771e2ad2bd7c622f61d4480",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "audit_path": "reports/evaluation/auditoria_desarrollo_v02.json",
      "audit_sha256": "f4d5c3c3088dc5bd9f61d6ebef4b33716401dd4014491585317a184e647e0346",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    }
  ],
  "planned_assessment": {
    "semantic": "no_ejecutado",
    "plan_contract": "no_ejecutado",
    "task_fulfillment": "no_ejecutado",
    "latency_ms": null
  }
}
```

</details>

## DEV-051

**Intención:** INT-19 · **Grupo:** propiedad_peso · **Variante:** diagnostico · **Bloque:** limites_y_composicion

**Orden original:**

> Tell me which is the heaviest fruit on the sofa.

**Propósito:** propiedad_peso

**Respuesta prevista:** `domain_capability_review`.

**Objetivos propuestos:**

```text
go(sofa)
find(fruit, kind=object, property=heaviest)
tell(fruit, property=heaviest)
```

**Subtareas requeridas:**

- Determinar qué fruta tiene mayor peso en sofa y comunicarlo.

**Restricciones:**

- No sustituir peso por tamaño.

**Conductas prohibidas:**

- Declarar cumplida una propiedad o capacidad sustituida por una aproximación no justificada.

**Variaciones aceptables:**

- Planes alternativos que satisfagan las subtareas y restricciones.

**Límites de verificación:**

- heaviest pertenece al vocabulario pero la expansión usa tamaño como aproximación; clasificar proxy_insuficiente si no existe evidencia del peso. No exigir un plan exitoso cuando el repertorio no permite satisfacerlo.

**Condiciones iniciales:**

```json
{
  "location": "unknown",
  "holding": "nothing",
  "focus": false,
  "manipulation_enabled": true,
  "independent_request": true
}
```

**Supuestos del escenario:**

- Las entidades mencionadas son referencias del dominio; su detección y disponibilidad física no se evalúan.
- Cada orden se procesa sin conversación previa.

**Comprobaciones comunes del plan:**

- Acciones y parámetros dentro del contrato compartido.
- No añadir tareas ajenas; se admiten los cierres convencionales de retorno y comunicación.
- Referentes consistentes y dependencias de adquisición/entrega respetadas.
- Distinguir protocolo generado de operación física no observada.

**Notas existentes de revisión:**

- 2026-10-17: el investigador confirmó en la conversación haber revisado las 60 fichas y encontrarlas en orden; aprobación sin cambios de órdenes, objetivos ni criterios. Aprobación para desarrollo, no dictamen sobre salidas de modelos.

**Decisión del investigador:**

- [x] Aprobada sin cambios.
- [ ] Requiere correcciones.
- [ ] No aprobada.

**Correcciones u observaciones:**

Sin correcciones solicitadas.

**Revisor y fecha:** Investigador (usuario), 2026-10-17.

<details>
<summary>Metadatos y trazabilidad de la ficha original</summary>

```json
{
  "reference_status": "approved",
  "split": "development",
  "development_version": "0.2",
  "overlap_status": "sin_coincidencia_detectada_v02",
  "overlap_audit_history": [
    {
      "development_version": "0.1",
      "input_audited": "Tell me which is the heaviest fruit on the sofa.",
      "development_sha256": "02103490f89367add79ae9b6aea90e01ecd7f9def7cb32c24d9fb51e6b0b5c7b",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    },
    {
      "development_version": "0.2",
      "input_audited": "Tell me which is the heaviest fruit on the sofa.",
      "development_sha256": "4c1a356fa50ac317ad6b428c101a48183968a41e2771e2ad2bd7c622f61d4480",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "audit_path": "reports/evaluation/auditoria_desarrollo_v02.json",
      "audit_sha256": "f4d5c3c3088dc5bd9f61d6ebef4b33716401dd4014491585317a184e647e0346",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    }
  ],
  "planned_assessment": {
    "semantic": "no_ejecutado",
    "plan_contract": "no_ejecutado",
    "task_fulfillment": "no_ejecutado",
    "latency_ms": null
  }
}
```

</details>

## DEV-052

**Intención:** INT-20 · **Grupo:** seguimiento_destino · **Variante:** diagnostico · **Bloque:** limites_y_composicion

**Orden original:**

> Find Simone at the coatrack and follow Simone to the bedroom.

**Propósito:** seguimiento_destino

**Respuesta prevista:** `executable`.

**Objetivos propuestos:**

```text
go(coatrack)
find(Simone, kind=person)
follow(Simone, to=bedroom)
```

**Subtareas requeridas:**

- Localizar a Simone en coatrack.
- Seguir a Simone hasta bedroom.

**Restricciones:**

- No convertir seguimiento en guía.
- No ir solo a bedroom antes de localizar a Simone.

**Conductas prohibidas:**

- Declarar cumplida una propiedad o capacidad sustituida por una aproximación no justificada.

**Variaciones aceptables:**

- Planes alternativos que satisfagan las subtareas y restricciones.

**Límites de verificación:**

- El protocolo instruct_follow_to requiere precisar los efectos del ejecutor; un anuncio no acredita llegar siguiendo a Simone.

**Condiciones iniciales:**

```json
{
  "location": "unknown",
  "holding": "nothing",
  "focus": false,
  "manipulation_enabled": true,
  "independent_request": true
}
```

**Supuestos del escenario:**

- Las entidades mencionadas son referencias del dominio; su detección y disponibilidad física no se evalúan.
- Cada orden se procesa sin conversación previa.

**Comprobaciones comunes del plan:**

- Acciones y parámetros dentro del contrato compartido.
- No añadir tareas ajenas; se admiten los cierres convencionales de retorno y comunicación.
- Referentes consistentes y dependencias de adquisición/entrega respetadas.
- Distinguir protocolo generado de operación física no observada.

**Notas existentes de revisión:**

- 2026-10-17: el investigador confirmó en la conversación haber revisado las 60 fichas y encontrarlas en orden; aprobación sin cambios de órdenes, objetivos ni criterios. Aprobación para desarrollo, no dictamen sobre salidas de modelos.

**Decisión del investigador:**

- [x] Aprobada sin cambios.
- [ ] Requiere correcciones.
- [ ] No aprobada.

**Correcciones u observaciones:**

Sin correcciones solicitadas.

**Revisor y fecha:** Investigador (usuario), 2026-10-17.

<details>
<summary>Metadatos y trazabilidad de la ficha original</summary>

```json
{
  "reference_status": "approved",
  "split": "development",
  "development_version": "0.2",
  "overlap_status": "sin_coincidencia_detectada_v02",
  "overlap_audit_history": [
    {
      "development_version": "0.1",
      "input_audited": "Find Simone at the coatrack and follow Simone to the bedroom.",
      "development_sha256": "02103490f89367add79ae9b6aea90e01ecd7f9def7cb32c24d9fb51e6b0b5c7b",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    },
    {
      "development_version": "0.2",
      "input_audited": "Find Simone at the coatrack and follow Simone to the bedroom.",
      "development_sha256": "4c1a356fa50ac317ad6b428c101a48183968a41e2771e2ad2bd7c622f61d4480",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "audit_path": "reports/evaluation/auditoria_desarrollo_v02.json",
      "audit_sha256": "f4d5c3c3088dc5bd9f61d6ebef4b33716401dd4014491585317a184e647e0346",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    }
  ],
  "planned_assessment": {
    "semantic": "no_ejecutado",
    "plan_contract": "no_ejecutado",
    "task_fulfillment": "no_ejecutado",
    "latency_ms": null
  }
}
```

</details>

## DEV-053

**Intención:** INT-21 · **Grupo:** composicion_dos_entregas · **Variante:** diagnostico · **Bloque:** limites_y_composicion

**Orden original:**

> Bring me a mug from the refrigerator, then bring me a spoon from the bed.

**Propósito:** composicion_dos_entregas

**Respuesta prevista:** `executable`.

**Objetivos propuestos:**

```text
go(refrigerator)
find(mug, kind=object)
take(mug)
deliver(mug, to=me)
go(bed)
find(spoon, kind=object)
take(spoon)
deliver(spoon, to=me)
```

**Subtareas requeridas:**

- Entregar al operador mug desde refrigerator.
- Después entregar al operador spoon desde bed.

**Restricciones:**

- Completar la primera entrega antes de buscar el segundo objeto.
- Reiniciar la posesión tras cada entrega; no reutilizar el identificador de mug para spoon.

**Conductas prohibidas:**

- Declarar cumplida una propiedad o capacidad sustituida por una aproximación no justificada.

**Variaciones aceptables:**

- Planes alternativos que satisfagan las subtareas y restricciones.

**Límites de verificación:**

- Caso para comprobar truncamiento por límite de tokens, conservación de orden y reinicio del estado de posesión.

**Condiciones iniciales:**

```json
{
  "location": "unknown",
  "holding": "nothing",
  "focus": false,
  "manipulation_enabled": true,
  "independent_request": true
}
```

**Supuestos del escenario:**

- Las entidades mencionadas son referencias del dominio; su detección y disponibilidad física no se evalúan.
- Cada orden se procesa sin conversación previa.

**Comprobaciones comunes del plan:**

- Acciones y parámetros dentro del contrato compartido.
- No añadir tareas ajenas; se admiten los cierres convencionales de retorno y comunicación.
- Referentes consistentes y dependencias de adquisición/entrega respetadas.
- Distinguir protocolo generado de operación física no observada.

**Notas existentes de revisión:**

- 2026-10-17: el investigador confirmó en la conversación haber revisado las 60 fichas y encontrarlas en orden; aprobación sin cambios de órdenes, objetivos ni criterios. Aprobación para desarrollo, no dictamen sobre salidas de modelos.

**Decisión del investigador:**

- [x] Aprobada sin cambios.
- [ ] Requiere correcciones.
- [ ] No aprobada.

**Correcciones u observaciones:**

Sin correcciones solicitadas.

**Revisor y fecha:** Investigador (usuario), 2026-10-17.

<details>
<summary>Metadatos y trazabilidad de la ficha original</summary>

```json
{
  "reference_status": "approved",
  "split": "development",
  "development_version": "0.2",
  "overlap_status": "sin_coincidencia_detectada_v02",
  "overlap_audit_history": [
    {
      "development_version": "0.1",
      "input_audited": "Bring me a mug from the refrigerator, then bring me a spoon from the bed.",
      "development_sha256": "02103490f89367add79ae9b6aea90e01ecd7f9def7cb32c24d9fb51e6b0b5c7b",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    },
    {
      "development_version": "0.2",
      "input_audited": "Bring me a mug from the refrigerator, then bring me a spoon from the bed.",
      "development_sha256": "4c1a356fa50ac317ad6b428c101a48183968a41e2771e2ad2bd7c622f61d4480",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "audit_path": "reports/evaluation/auditoria_desarrollo_v02.json",
      "audit_sha256": "f4d5c3c3088dc5bd9f61d6ebef4b33716401dd4014491585317a184e647e0346",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    }
  ],
  "planned_assessment": {
    "semantic": "no_ejecutado",
    "plan_contract": "no_ejecutado",
    "task_fulfillment": "no_ejecutado",
    "latency_ms": null
  }
}
```

</details>

## DEV-054

**Intención:** INT-22 · **Grupo:** tipo_independiente_mayusculas · **Variante:** diagnostico · **Bloque:** limites_y_composicion

**Orden original:**

> Find Water in the kitchen, take it, and bring it to me.

**Propósito:** tipo_independiente_mayusculas

**Respuesta prevista:** `executable`.

**Objetivos propuestos:**

```text
go(kitchen)
find(Water, kind=object)
take(Water)
deliver(Water, to=me)
```

**Subtareas requeridas:**

- Buscar y adquirir el objeto Water en kitchen.
- Entregarlo al operador.

**Restricciones:**

- La mayúscula de Water no debe convertir el objeto en una persona.

**Conductas prohibidas:**

- Declarar cumplida una propiedad o capacidad sustituida por una aproximación no justificada.

**Variaciones aceptables:**

- Planes alternativos que satisfagan las subtareas y restricciones.

**Límites de verificación:**

- Examinar la predicción original y el kind calculado por el adaptador por separado.

**Condiciones iniciales:**

```json
{
  "location": "unknown",
  "holding": "nothing",
  "focus": false,
  "manipulation_enabled": true,
  "independent_request": true
}
```

**Supuestos del escenario:**

- Las entidades mencionadas son referencias del dominio; su detección y disponibilidad física no se evalúan.
- Cada orden se procesa sin conversación previa.

**Comprobaciones comunes del plan:**

- Acciones y parámetros dentro del contrato compartido.
- No añadir tareas ajenas; se admiten los cierres convencionales de retorno y comunicación.
- Referentes consistentes y dependencias de adquisición/entrega respetadas.
- Distinguir protocolo generado de operación física no observada.

**Notas existentes de revisión:**

- 2026-10-17: el investigador confirmó en la conversación haber revisado las 60 fichas y encontrarlas en orden; aprobación sin cambios de órdenes, objetivos ni criterios. Aprobación para desarrollo, no dictamen sobre salidas de modelos.

**Decisión del investigador:**

- [x] Aprobada sin cambios.
- [ ] Requiere correcciones.
- [ ] No aprobada.

**Correcciones u observaciones:**

Sin correcciones solicitadas.

**Revisor y fecha:** Investigador (usuario), 2026-10-17.

<details>
<summary>Metadatos y trazabilidad de la ficha original</summary>

```json
{
  "reference_status": "approved",
  "split": "development",
  "development_version": "0.2",
  "overlap_status": "sin_coincidencia_detectada_v02",
  "overlap_audit_history": [
    {
      "development_version": "0.1",
      "input_audited": "Find Water in the kitchen, take it, and bring it to me.",
      "development_sha256": "02103490f89367add79ae9b6aea90e01ecd7f9def7cb32c24d9fb51e6b0b5c7b",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    },
    {
      "development_version": "0.2",
      "input_audited": "Find Water in the kitchen, take it, and bring it to me.",
      "development_sha256": "4c1a356fa50ac317ad6b428c101a48183968a41e2771e2ad2bd7c622f61d4480",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "audit_path": "reports/evaluation/auditoria_desarrollo_v02.json",
      "audit_sha256": "f4d5c3c3088dc5bd9f61d6ebef4b33716401dd4014491585317a184e647e0346",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    }
  ],
  "planned_assessment": {
    "semantic": "no_ejecutado",
    "plan_contract": "no_ejecutado",
    "task_fulfillment": "no_ejecutado",
    "latency_ms": null
  }
}
```

</details>

## DEV-055

**Intención:** INT-23 · **Grupo:** referente_ausente · **Variante:** limite_dominio · **Bloque:** ambiguedad_y_fuera_dominio

**Orden original:**

> Go to the kitchen and bring it to me.

**Propósito:** referente_ausente

**Respuesta prevista:** `clarification`.

**Objetivos propuestos:**

No aplican objetivos ejecutables (`goals_ref: null`).

**Subtareas requeridas:**

Sin elementos especificados en la ficha.

**Restricciones:**

- No completar datos faltantes ni generar un plan completo apoyado en suposiciones no autorizadas.

**Conductas prohibidas:**

- Inventar el dato faltante o sustituir una acción no soportada por otra.

**Variaciones aceptables:**

- Cualquier formulación clara de la pregunta o razón esperada.

**Límites de verificación:**

- Qwen no implementa el mismo contrato conversacional: registrar su respuesta observada sin equiparar error de esquema y aclaración.

**Sentido de la respuesta esperada:**

¿Qué objeto debe llevarse al operador?

**Información faltante:**

- Identificar el objeto referido por it.

**Condiciones iniciales:**

```json
{
  "location": "unknown",
  "holding": "nothing",
  "focus": false,
  "manipulation_enabled": true,
  "independent_request": true
}
```

**Supuestos del escenario:**

- Las entidades mencionadas son referencias del dominio; su detección y disponibilidad física no se evalúan.
- Cada orden se procesa sin conversación previa.

**Comprobaciones comunes del plan:**

- Acciones y parámetros dentro del contrato compartido.
- No añadir tareas ajenas; se admiten los cierres convencionales de retorno y comunicación.
- Referentes consistentes y dependencias de adquisición/entrega respetadas.
- Distinguir protocolo generado de operación física no observada.

**Notas existentes de revisión:**

- 2026-10-17: el investigador confirmó en la conversación haber revisado las 60 fichas y encontrarlas en orden; aprobación sin cambios de órdenes, objetivos ni criterios. Aprobación para desarrollo, no dictamen sobre salidas de modelos.

**Decisión del investigador:**

- [x] Aprobada sin cambios.
- [ ] Requiere correcciones.
- [ ] No aprobada.

**Correcciones u observaciones:**

Sin correcciones solicitadas.

**Revisor y fecha:** Investigador (usuario), 2026-10-17.

<details>
<summary>Metadatos y trazabilidad de la ficha original</summary>

```json
{
  "reference_status": "approved",
  "split": "development",
  "development_version": "0.2",
  "overlap_status": "sin_coincidencia_detectada_v02",
  "overlap_audit_history": [
    {
      "development_version": "0.1",
      "input_audited": "Go to the kitchen and bring it to me.",
      "development_sha256": "02103490f89367add79ae9b6aea90e01ecd7f9def7cb32c24d9fb51e6b0b5c7b",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    },
    {
      "development_version": "0.2",
      "input_audited": "Go to the kitchen and bring it to me.",
      "development_sha256": "4c1a356fa50ac317ad6b428c101a48183968a41e2771e2ad2bd7c622f61d4480",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "audit_path": "reports/evaluation/auditoria_desarrollo_v02.json",
      "audit_sha256": "f4d5c3c3088dc5bd9f61d6ebef4b33716401dd4014491585317a184e647e0346",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    }
  ],
  "planned_assessment": {
    "semantic": "no_ejecutado",
    "plan_contract": "no_ejecutado",
    "task_fulfillment": "no_ejecutado",
    "latency_ms": null
  }
}
```

</details>

## DEV-056

**Intención:** INT-24 · **Grupo:** destino_ausente · **Variante:** limite_dominio · **Bloque:** ambiguedad_y_fuera_dominio

**Orden original:**

> Find Robin in the office and guide Robin to the destination.

**Propósito:** destino_ausente

**Respuesta prevista:** `clarification`.

**Objetivos propuestos:**

No aplican objetivos ejecutables (`goals_ref: null`).

**Subtareas requeridas:**

Sin elementos especificados en la ficha.

**Restricciones:**

- No completar datos faltantes ni generar un plan completo apoyado en suposiciones no autorizadas.

**Conductas prohibidas:**

- Inventar el dato faltante o sustituir una acción no soportada por otra.

**Variaciones aceptables:**

- Cualquier formulación clara de la pregunta o razón esperada.

**Límites de verificación:**

- Qwen no implementa el mismo contrato conversacional: registrar su respuesta observada sin equiparar error de esquema y aclaración.

**Sentido de la respuesta esperada:**

¿Cuál es el destino al que debe guiarse a Robin?

**Información faltante:**

- Identificar la ubicación denominada the destination; no está especificada.

**Condiciones iniciales:**

```json
{
  "location": "unknown",
  "holding": "nothing",
  "focus": false,
  "manipulation_enabled": true,
  "independent_request": true
}
```

**Supuestos del escenario:**

- Las entidades mencionadas son referencias del dominio; su detección y disponibilidad física no se evalúan.
- Cada orden se procesa sin conversación previa.

**Comprobaciones comunes del plan:**

- Acciones y parámetros dentro del contrato compartido.
- No añadir tareas ajenas; se admiten los cierres convencionales de retorno y comunicación.
- Referentes consistentes y dependencias de adquisición/entrega respetadas.
- Distinguir protocolo generado de operación física no observada.

**Notas existentes de revisión:**

- 2026-10-17: el investigador confirmó en la conversación haber revisado las 60 fichas y encontrarlas en orden; aprobación sin cambios de órdenes, objetivos ni criterios. Aprobación para desarrollo, no dictamen sobre salidas de modelos.

**Decisión del investigador:**

- [x] Aprobada sin cambios.
- [ ] Requiere correcciones.
- [ ] No aprobada.

**Correcciones u observaciones:**

Sin correcciones solicitadas.

**Revisor y fecha:** Investigador (usuario), 2026-10-17.

<details>
<summary>Metadatos y trazabilidad de la ficha original</summary>

```json
{
  "reference_status": "approved",
  "split": "development",
  "development_version": "0.2",
  "overlap_status": "sin_coincidencia_detectada_v02",
  "overlap_audit_history": [
    {
      "development_version": "0.1",
      "input_audited": "Find Robin in the office and guide Robin to the destination.",
      "development_sha256": "02103490f89367add79ae9b6aea90e01ecd7f9def7cb32c24d9fb51e6b0b5c7b",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    },
    {
      "development_version": "0.2",
      "input_audited": "Find Robin in the office and guide Robin to the destination.",
      "development_sha256": "4c1a356fa50ac317ad6b428c101a48183968a41e2771e2ad2bd7c622f61d4480",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "audit_path": "reports/evaluation/auditoria_desarrollo_v02.json",
      "audit_sha256": "f4d5c3c3088dc5bd9f61d6ebef4b33716401dd4014491585317a184e647e0346",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    }
  ],
  "planned_assessment": {
    "semantic": "no_ejecutado",
    "plan_contract": "no_ejecutado",
    "task_fulfillment": "no_ejecutado",
    "latency_ms": null
  }
}
```

</details>

## DEV-057

**Intención:** INT-25 · **Grupo:** destinatario_ausente · **Variante:** limite_dominio · **Bloque:** ambiguedad_y_fuera_dominio

**Orden original:**

> Take a fork from the shelf and give it to her.

**Propósito:** destinatario_ausente

**Respuesta prevista:** `clarification`.

**Objetivos propuestos:**

No aplican objetivos ejecutables (`goals_ref: null`).

**Subtareas requeridas:**

Sin elementos especificados en la ficha.

**Restricciones:**

- No completar datos faltantes ni generar un plan completo apoyado en suposiciones no autorizadas.

**Conductas prohibidas:**

- Inventar el dato faltante o sustituir una acción no soportada por otra.

**Variaciones aceptables:**

- Cualquier formulación clara de la pregunta o razón esperada.

**Límites de verificación:**

- Qwen no implementa el mismo contrato conversacional: registrar su respuesta observada sin equiparar error de esquema y aclaración.

**Sentido de la respuesta esperada:**

¿A quién se refiere her?

**Información faltante:**

- Identificar a la persona referida por her, sin antecedente en la orden.

**Condiciones iniciales:**

```json
{
  "location": "unknown",
  "holding": "nothing",
  "focus": false,
  "manipulation_enabled": true,
  "independent_request": true
}
```

**Supuestos del escenario:**

- Las entidades mencionadas son referencias del dominio; su detección y disponibilidad física no se evalúan.
- Cada orden se procesa sin conversación previa.

**Comprobaciones comunes del plan:**

- Acciones y parámetros dentro del contrato compartido.
- No añadir tareas ajenas; se admiten los cierres convencionales de retorno y comunicación.
- Referentes consistentes y dependencias de adquisición/entrega respetadas.
- Distinguir protocolo generado de operación física no observada.

**Notas existentes de revisión:**

- 2026-10-17: el investigador confirmó en la conversación haber revisado las 60 fichas y encontrarlas en orden; aprobación sin cambios de órdenes, objetivos ni criterios. Aprobación para desarrollo, no dictamen sobre salidas de modelos.

**Decisión del investigador:**

- [x] Aprobada sin cambios.
- [ ] Requiere correcciones.
- [ ] No aprobada.

**Correcciones u observaciones:**

Sin correcciones solicitadas.

**Revisor y fecha:** Investigador (usuario), 2026-10-17.

<details>
<summary>Metadatos y trazabilidad de la ficha original</summary>

```json
{
  "reference_status": "approved",
  "split": "development",
  "development_version": "0.2",
  "overlap_status": "sin_coincidencia_detectada_v02",
  "overlap_audit_history": [
    {
      "development_version": "0.1",
      "input_audited": "Take a fork from the shelf and give it to her.",
      "development_sha256": "02103490f89367add79ae9b6aea90e01ecd7f9def7cb32c24d9fb51e6b0b5c7b",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    },
    {
      "development_version": "0.2",
      "input_audited": "Take a fork from the shelf and give it to her.",
      "development_sha256": "4c1a356fa50ac317ad6b428c101a48183968a41e2771e2ad2bd7c622f61d4480",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "audit_path": "reports/evaluation/auditoria_desarrollo_v02.json",
      "audit_sha256": "f4d5c3c3088dc5bd9f61d6ebef4b33716401dd4014491585317a184e647e0346",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    }
  ],
  "planned_assessment": {
    "semantic": "no_ejecutado",
    "plan_contract": "no_ejecutado",
    "task_fulfillment": "no_ejecutado",
    "latency_ms": null
  }
}
```

</details>

## DEV-058

**Intención:** INT-26 · **Grupo:** accion_fuera_repertorio · **Variante:** limite_dominio · **Bloque:** ambiguedad_y_fuera_dominio

**Orden original:**

> Fly to the ceiling and inspect the lamp.

**Propósito:** accion_fuera_repertorio

**Respuesta prevista:** `rejected`.

**Objetivos propuestos:**

No aplican objetivos ejecutables (`goals_ref: null`).

**Subtareas requeridas:**

Sin elementos especificados en la ficha.

**Restricciones:**

- No completar datos faltantes ni generar un plan completo apoyado en suposiciones no autorizadas.

**Conductas prohibidas:**

- Inventar el dato faltante o sustituir una acción no soportada por otra.

**Variaciones aceptables:**

- Cualquier formulación clara de la pregunta o razón esperada.

**Límites de verificación:**

- Qwen no implementa el mismo contrato conversacional: registrar su respuesta observada sin equiparar error de esquema y aclaración.

**Sentido de la respuesta esperada:**

Volar e inspeccionar la lámpara excede el repertorio definido.

**Información faltante:**

Sin elementos especificados en la ficha.

**Condiciones iniciales:**

```json
{
  "location": "unknown",
  "holding": "nothing",
  "focus": false,
  "manipulation_enabled": true,
  "independent_request": true
}
```

**Supuestos del escenario:**

- Las entidades mencionadas son referencias del dominio; su detección y disponibilidad física no se evalúan.
- Cada orden se procesa sin conversación previa.

**Comprobaciones comunes del plan:**

- Acciones y parámetros dentro del contrato compartido.
- No añadir tareas ajenas; se admiten los cierres convencionales de retorno y comunicación.
- Referentes consistentes y dependencias de adquisición/entrega respetadas.
- Distinguir protocolo generado de operación física no observada.

**Notas existentes de revisión:**

- 2026-10-17: el investigador confirmó en la conversación haber revisado las 60 fichas y encontrarlas en orden; aprobación sin cambios de órdenes, objetivos ni criterios. Aprobación para desarrollo, no dictamen sobre salidas de modelos.

**Decisión del investigador:**

- [x] Aprobada sin cambios.
- [ ] Requiere correcciones.
- [ ] No aprobada.

**Correcciones u observaciones:**

Sin correcciones solicitadas.

**Revisor y fecha:** Investigador (usuario), 2026-10-17.

<details>
<summary>Metadatos y trazabilidad de la ficha original</summary>

```json
{
  "reference_status": "approved",
  "split": "development",
  "development_version": "0.2",
  "overlap_status": "sin_coincidencia_detectada_v02",
  "overlap_audit_history": [
    {
      "development_version": "0.1",
      "input_audited": "Fly to the ceiling and inspect the lamp.",
      "development_sha256": "02103490f89367add79ae9b6aea90e01ecd7f9def7cb32c24d9fb51e6b0b5c7b",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    },
    {
      "development_version": "0.2",
      "input_audited": "Fly to the ceiling and inspect the lamp.",
      "development_sha256": "4c1a356fa50ac317ad6b428c101a48183968a41e2771e2ad2bd7c622f61d4480",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "audit_path": "reports/evaluation/auditoria_desarrollo_v02.json",
      "audit_sha256": "f4d5c3c3088dc5bd9f61d6ebef4b33716401dd4014491585317a184e647e0346",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    }
  ],
  "planned_assessment": {
    "semantic": "no_ejecutado",
    "plan_contract": "no_ejecutado",
    "task_fulfillment": "no_ejecutado",
    "latency_ms": null
  }
}
```

</details>

## DEV-059

**Intención:** INT-27 · **Grupo:** dispositivo_fuera_repertorio · **Variante:** limite_dominio · **Bloque:** ambiguedad_y_fuera_dominio

**Orden original:**

> Set the thermostat to twenty degrees.

**Propósito:** dispositivo_fuera_repertorio

**Respuesta prevista:** `rejected`.

**Objetivos propuestos:**

No aplican objetivos ejecutables (`goals_ref: null`).

**Subtareas requeridas:**

Sin elementos especificados en la ficha.

**Restricciones:**

- No completar datos faltantes ni generar un plan completo apoyado en suposiciones no autorizadas.

**Conductas prohibidas:**

- Inventar el dato faltante o sustituir una acción no soportada por otra.

**Variaciones aceptables:**

- Cualquier formulación clara de la pregunta o razón esperada.

**Límites de verificación:**

- Qwen no implementa el mismo contrato conversacional: registrar su respuesta observada sin equiparar error de esquema y aclaración.

**Sentido de la respuesta esperada:**

Controlar el termostato no pertenece al repertorio de acciones.

**Información faltante:**

Sin elementos especificados en la ficha.

**Condiciones iniciales:**

```json
{
  "location": "unknown",
  "holding": "nothing",
  "focus": false,
  "manipulation_enabled": true,
  "independent_request": true
}
```

**Supuestos del escenario:**

- Las entidades mencionadas son referencias del dominio; su detección y disponibilidad física no se evalúan.
- Cada orden se procesa sin conversación previa.

**Comprobaciones comunes del plan:**

- Acciones y parámetros dentro del contrato compartido.
- No añadir tareas ajenas; se admiten los cierres convencionales de retorno y comunicación.
- Referentes consistentes y dependencias de adquisición/entrega respetadas.
- Distinguir protocolo generado de operación física no observada.

**Notas existentes de revisión:**

- 2026-10-17: el investigador confirmó en la conversación haber revisado las 60 fichas y encontrarlas en orden; aprobación sin cambios de órdenes, objetivos ni criterios. Aprobación para desarrollo, no dictamen sobre salidas de modelos.

**Decisión del investigador:**

- [x] Aprobada sin cambios.
- [ ] Requiere correcciones.
- [ ] No aprobada.

**Correcciones u observaciones:**

Sin correcciones solicitadas.

**Revisor y fecha:** Investigador (usuario), 2026-10-17.

<details>
<summary>Metadatos y trazabilidad de la ficha original</summary>

```json
{
  "reference_status": "approved",
  "split": "development",
  "development_version": "0.2",
  "overlap_status": "sin_coincidencia_detectada_v02",
  "overlap_audit_history": [
    {
      "development_version": "0.1",
      "input_audited": "Set the thermostat to twenty degrees.",
      "development_sha256": "02103490f89367add79ae9b6aea90e01ecd7f9def7cb32c24d9fb51e6b0b5c7b",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    },
    {
      "development_version": "0.2",
      "input_audited": "Set the thermostat to twenty degrees.",
      "development_sha256": "4c1a356fa50ac317ad6b428c101a48183968a41e2771e2ad2bd7c622f61d4480",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "audit_path": "reports/evaluation/auditoria_desarrollo_v02.json",
      "audit_sha256": "f4d5c3c3088dc5bd9f61d6ebef4b33716401dd4014491585317a184e647e0346",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    }
  ],
  "planned_assessment": {
    "semantic": "no_ejecutado",
    "plan_contract": "no_ejecutado",
    "task_fulfillment": "no_ejecutado",
    "latency_ms": null
  }
}
```

</details>

## DEV-060

**Intención:** INT-28 · **Grupo:** restriccion_contradictoria · **Variante:** limite_dominio · **Bloque:** ambiguedad_y_fuera_dominio

**Orden original:**

> Pick up the apple on the shelf, but do not pick up the apple.

**Propósito:** restriccion_contradictoria

**Respuesta prevista:** `rejected`.

**Objetivos propuestos:**

No aplican objetivos ejecutables (`goals_ref: null`).

**Subtareas requeridas:**

Sin elementos especificados en la ficha.

**Restricciones:**

- No completar datos faltantes ni generar un plan completo apoyado en suposiciones no autorizadas.

**Conductas prohibidas:**

- Inventar el dato faltante o sustituir una acción no soportada por otra.

**Variaciones aceptables:**

- Cualquier formulación clara de la pregunta o razón esperada.

**Límites de verificación:**

- Qwen no implementa el mismo contrato conversacional: registrar su respuesta observada sin equiparar error de esquema y aclaración.

**Sentido de la respuesta esperada:**

La misma adquisición se exige y se prohíbe en la instrucción.

**Información faltante:**

Sin elementos especificados en la ficha.

**Condiciones iniciales:**

```json
{
  "location": "unknown",
  "holding": "nothing",
  "focus": false,
  "manipulation_enabled": true,
  "independent_request": true
}
```

**Supuestos del escenario:**

- Las entidades mencionadas son referencias del dominio; su detección y disponibilidad física no se evalúan.
- Cada orden se procesa sin conversación previa.

**Comprobaciones comunes del plan:**

- Acciones y parámetros dentro del contrato compartido.
- No añadir tareas ajenas; se admiten los cierres convencionales de retorno y comunicación.
- Referentes consistentes y dependencias de adquisición/entrega respetadas.
- Distinguir protocolo generado de operación física no observada.

**Notas existentes de revisión:**

- 2026-10-17: el investigador confirmó en la conversación haber revisado las 60 fichas y encontrarlas en orden; aprobación sin cambios de órdenes, objetivos ni criterios. Aprobación para desarrollo, no dictamen sobre salidas de modelos.

**Decisión del investigador:**

- [x] Aprobada sin cambios.
- [ ] Requiere correcciones.
- [ ] No aprobada.

**Correcciones u observaciones:**

Sin correcciones solicitadas.

**Revisor y fecha:** Investigador (usuario), 2026-10-17.

<details>
<summary>Metadatos y trazabilidad de la ficha original</summary>

```json
{
  "reference_status": "approved",
  "split": "development",
  "development_version": "0.2",
  "overlap_status": "sin_coincidencia_detectada_v02",
  "overlap_audit_history": [
    {
      "development_version": "0.1",
      "input_audited": "Pick up the apple on the shelf, but do not pick up the apple.",
      "development_sha256": "02103490f89367add79ae9b6aea90e01ecd7f9def7cb32c24d9fb51e6b0b5c7b",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    },
    {
      "development_version": "0.2",
      "input_audited": "Pick up the apple on the shelf, but do not pick up the apple.",
      "development_sha256": "4c1a356fa50ac317ad6b428c101a48183968a41e2771e2ad2bd7c622f61d4480",
      "dataset_sha256": "0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406",
      "normalizer": "command_normalizer:normalize_command",
      "audit_path": "reports/evaluation/auditoria_desarrollo_v02.json",
      "audit_sha256": "f4d5c3c3088dc5bd9f61d6ebef4b33716401dd4014491585317a184e647e0346",
      "matching_dataset_lines": {
        "literal": [],
        "limpieza_basica": [],
        "normalizador_real": []
      },
      "scope": "Igualdad literal y de transformaciones indicadas; no certifica independencia semántica ni novedad de plantilla."
    }
  ],
  "planned_assessment": {
    "semantic": "no_ejecutado",
    "plan_contract": "no_ejecutado",
    "task_fulfillment": "no_ejecutado",
    "latency_ms": null
  }
}
```

</details>
