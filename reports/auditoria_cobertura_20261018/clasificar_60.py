"""Construye una propuesta de revisión; no modifica estímulos, referencias ni campañas."""
from pathlib import Path
import csv
import hashlib
import json
from collections import Counter

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
DOC = ROOT / 'docs/experiment/Clasificacion_60_para_revision.md'
INPUT = ROOT / 'data/development/desarrollo_60_entradas.jsonl'
REF = ROOT / 'data/development/desarrollo_60_referencias.jsonl'
AUDIT = ROOT / 'reports/evaluation/auditoria_desarrollo_v02.json'

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def read(p):
    return [json.loads(s) for s in p.read_text().splitlines() if s.strip()]

translations = '''Ve al pasillo y después al punto de inspección.
Visita primero el pasillo y después el punto de inspección.
Por favor, ve al pasillo y después al punto de inspección.
Encuentra un durazno en el baño.
Busca un durazno dentro del baño.
Por favor, encuentra un durazno en el baño.
Encuentra una cuchara en la cama y tómala.
Recoge la cuchara que encuentres en la cama.
Por favor, encuentra una cuchara en la cama y tómala.
Tráeme una taza (mug) del gabinete.
Recoge una taza (mug) en el gabinete y entrégamela.
Por favor, tráeme una taza (mug) del gabinete.
Lleva un tazón de la cama a la estantería de almacenamiento.
Recoge un tazón en la cama y déjalo en la estantería de almacenamiento.
Por favor, lleva un tazón de la cama a la estantería de almacenamiento.
En la cocina, encuentra una taza (cup), tómala y ponla sobre la mesa.
Localiza una taza (cup) en la cocina y recógela; después colócala sobre la mesa de allí.
En la cocina, encuentra una taza (cup), tómala y ponla sobre la mesa, por favor.
Encuentra a Robin en la oficina.
Busca a Robin dentro de la oficina.
Por favor, encuentra a Robin en la oficina.
Encuentra a Morgan en la cocina y guía a esa persona hasta la entrada.
Encuéntrate con Morgan en la cocina y después guía a Morgan hasta la entrada.
Encuentra a Morgan en la cocina y guía a esa persona hasta la entrada, por favor.
Encuentra en el dormitorio a la persona que saluda con la mano y síguela.
En el dormitorio, localiza a la persona que saluda con la mano y sigue a esa persona.
Por favor, encuentra en el dormitorio a la persona que saluda con la mano y síguela.
Toma una naranja del refrigerador y dásela a Sarah en la cocina.
Recoge una naranja en el refrigerador; después encuentra a Sarah en la cocina y entrégasela.
Toma una naranja del refrigerador y dásela a Sarah en la cocina.
Cuenta los juguetes que están sobre la estantería de almacenamiento.
Dime cuántos juguetes hay sobre la estantería de almacenamiento.
Por favor, cuenta los juguetes que están sobre la estantería de almacenamiento.
Encuentra a Charlie en la sala y dile la hora actual.
Localiza a Charlie en la sala y dile qué hora es.
Por favor, encuentra a Charlie en la sala y dile la hora actual.
Encuentra a una persona en el dormitorio, pregúntale su nombre y regresa para decírmelo.
Ve al dormitorio, averigua el nombre de una persona que esté allí y después regresa para informármelo.
Por favor, encuentra a una persona en el dormitorio, pregúntale su nombre y regresa para decírmelo.
Encuentra en el pasillo a la persona que saluda con la mano y responde a su pregunta.
En el pasillo, localiza a la persona que saluda con la mano y responde a la pregunta de esa persona.
Encuentra en el pasillo a la persona que saluda con la mano y responde a su pregunta, por favor.
Encuentra a Jane en la cocina y salúdala.
Busca a Jane en la cocina y dile hola.
Por favor, encuentra a Jane en la cocina y salúdala.
Dime cuál es la fruta de mayor tamaño que está sobre el sofá.
Identifica la fruta más grande que está sobre el sofá e informa cuál es.
Por favor, dime cuál es la fruta de mayor tamaño que está sobre el sofá.
Encuentra en la oficina a la persona que saluda con la mano y lleva un abrigo azul; después guíala hasta la entrada.
Cuenta las personas que llevan camisas rojas en la sala.
Dime cuál es la fruta más pesada que está sobre el sofá.
Encuentra a Simone junto al perchero y sigue a Simone hasta el dormitorio.
Tráeme una taza (mug) del refrigerador y después tráeme una cuchara de la cama.
Encuentra Water (agua, etiqueta del objeto) en la cocina, tómalo y tráemelo.
Ve a la cocina y tráemelo.
Encuentra a Robin en la oficina y guía a Robin hasta el destino.
Toma un tenedor de la repisa y dáselo a ella.
Vuela hasta el techo e inspecciona la lámpara.
Ajusta el termostato a veinte grados.
Recoge la manzana que está sobre la repisa, pero no recojas la manzana.'''.splitlines()

labels = {
 'G': 'Estructura y entidades contempladas por el generador local',
 'L': 'Estructura contemplada con extensión léxica de ubicación',
 'C': 'Composición fuera de las rutas del generador local',
 'M': 'Conjunción de atributos fuera de las plantillas locales',
 'A': 'Información necesaria ausente',
 'F': 'Acciones fuera del repertorio actual',
 'X': 'Instrucción contradictoria',
}
# Cada evidencia se refiere al generador local, no a una edición oficial certificada.
# Para G se contrasta intención y entidades; no se afirma derivabilidad literal de la frase.
groups = [
 ('C', 'simpleGoToLoc / goToLoc', 'Dos go consecutivos. simpleGoToLoc produce uno; goToLoc continúa con buscar objeto/persona, no con otro desplazamiento aislado.', 'Las acciones go existen. Evaluar generalización composicional; inspection point no es instruction_point.'),
 ('G', 'findObjectInRoomSimple', 'Ruta go(room) → find(objeto); peach y bathroom están en los catálogos.', 'Conservar objeto y habitación.'),
 ('G', 'takeObjInRoom', 'Ruta go(loc_room) → find(objeto) → take; spoon y bed están en los catálogos.', 'Conservar la dependencia encontrar antes de tomar.'),
 ('G', 'bringMeObjFromPlcmt', 'Ruta go → find → take → deliver(to=me); mug y cabinet están en los catálogos.', 'Entregar al solicitante; no basta con tomar el objeto.'),
 ('G', 'bringObjFromTo', 'Ruta go → find → take → place(at=destino); bowl, bed y storage rack están en los catálogos.', 'Conservar origen y destino, sin confundir traslado con entrega a persona.'),
 ('L', 'findObjInRoom → takeObj → placeObjOnPlcmt', 'La estructura está contemplada. cup y kitchen existen, pero table no es una entrada literal del catálogo: sí existe kitchen table.', 'Revisar si table se acepta como alias contextual. No sustituirlo automáticamente ni cambiar las órdenes históricas.'),
 ('G', 'findNameInRoom', 'Ruta go → find(kind=person); Robin y office están en los catálogos.', 'La corrección del plan requiere que la identidad solicitada se preserve; una búsqueda genérica no la demuestra.'),
 ('G', 'meetPrsAtBeac → guidePrsToBeacon', 'Ruta go → find(nombre) → guide; Morgan, kitchen y entrance están en los catálogos.', 'Verificar identidad y destino en el contrato del ejecutor.'),
 ('G', 'findPrsInRoom → followPrs / followPrsAtLoc', 'Ruta go → find(gesture=waving) → follow; bedroom está en el catálogo y waving es gesto admitido.', 'Conservar el gesto y el referente de la persona seguida.'),
 ('G', 'takeObjFromPlcmt → deliverObjToNameAtBeac', 'Ruta de recoger y entregar a una persona nombrada en otra habitación; orange, refrigerator, Sarah y kitchen están en los catálogos.', 'orange es el objeto, no una prenda o atributo; verificar identidad de destinataria.'),
 ('G', 'countObjOnPlcmt', 'Ruta go → count(categoría); toys y storage rack están en los catálogos.', 'Verificar categoría contada; expresar el resultado según el contrato del plan.'),
 ('G', 'meetPrsAtBeac → talkInfo', 'Buscar persona nombrada y comunicar información; TALK_LIST incluye the time, equivalente semántico de current time en estas órdenes.', 'Verificar identidad y comunicación de la hora; no inventar una hora constante.'),
 ('G', 'tellPrsInfoInLoc', 'persInfo=name produce go → find(person) → save(name) → go(instruction_point) → tell(name).', 'Verificar consulta, memoria y reporte de la misma respuesta; el plan no demuestra que la persona responda físicamente.'),
 ('G', 'answerQuestionOfPersInRoom', 'Ruta go → find(person,gesture) → answer_question; corridor y waving son admisibles.', 'Revisar ciclo de interacción y conservación de la persona encontrada.'),
 ('G', 'greetNameInRoomSimple', 'Ruta go → find(nombre) → greet; Jane y kitchen están en los catálogos.', 'Verificar saludo a Jane y ciclo de interacción.'),
 ('G', 'tellCatPropOnPlcmt', 'Ruta go → find(categoría,property) → tell; fruit, sofa y largest/biggest son admisibles.', 'Comparación de tamaño; distinguirla de peso. Verificar que el plan conserva la selección solicitada.'),
]
special = {
 49: ('M', 'guidePrsFromBeacToBeac / guideClothPrsFromBeacToBeac', 'Hay rutas para gesto y para vestimenta por separado, no para su conjunción en la misma búsqueda. Color + prenda sí constituye un atributo wearing admitido.', 'El adaptador serializa un solo qualifier. No perder silenciosamente una de las dos condiciones; evaluar manejo de solicitud no soportada.'),
 50: ('G', 'countClothPrsInRoom', 'Plantilla explícita para contar personas con colorClothes; el corpus contiene 1163 filas count con wearing (ejemplo línea 13).', 'Brecha simbólica: count-query devuelve count_person sin conservar el filtro de vestimenta. No excluir como fuera del generador.'),
 51: ('G', 'tellCatPropOnPlcmt', 'heaviest figura en OBJECT_COMP_LIST; hay 167 filas con property=heaviest (ejemplo línea 98). fruit y sofa son admisibles.', 'Brecha simbólica: size-filter agrupa heaviest con mayor tamaño. El peso no se demuestra mediante biggest_fruit. No excluir del ámbito del generador.'),
 52: ('G', 'followNameFromBeacToRoom', 'Ruta go → find(nombre) → follow(to=room); Simone, coatrack y bedroom están en los catálogos.', 'Verificar identidad y destino del seguimiento, incluida la instrucción asociada al destino si la exige el ejecutor.'),
 53: ('C', 'Dos instancias de bringMeObjFromPlcmt', 'Cada entrega es admisible aisladamente; las rutas actuales no concatenan dos tareas completas de recogida/entrega con objetos distintos.', 'Las acciones individuales existen. Evaluar orden de las dos entregas y separación de referentes, no solo longitud textual.'),
 54: ('G', 'findObjInRoom → takeObj → deliverObjToMe', 'Water aparece con mayúscula en objects.md; la ruta buscar → tomar → entregar al solicitante está contemplada.', 'Comprobar kind=object. La heurística de mayúsculas del adaptador puede tratar Water como persona; no atribuirlo automáticamente al modelo.'),
 55: ('A', 'Objeto ausente en entrega', 'it no tiene antecedente en esta orden independiente; kitchen identifica lugar, no objeto.', 'Pedir aclaración del objeto; no inventarlo.'),
 56: ('A', 'Destino ausente en guía', 'the destination no identifica un destino concreto y no hay conversación previa que lo determine.', 'Pedir aclaración del destino; no asumir entrance u otra ubicación.'),
 57: ('A', 'Destinataria ausente en entrega', 'her no tiene antecedente en esta orden independiente; fork y shelf no identifican a la destinataria.', 'Pedir aclaración de la destinataria; no inventar persona.'),
 58: ('F', 'Vuelo e inspección no disponibles', 'No hay objetivos canónicos para volar e inspeccionar la lámpara; volar es una acción solicitada, no un atributo de búsqueda.', 'Reconocer limitación sin convertir silenciosamente la orden en navegación/búsqueda terrestre.'),
 59: ('F', 'Control de termostato no disponible', 'No hay objetivo canónico ni acción del repertorio evaluado para ajustar un termostato.', 'Reconocer limitación; no generar una acción inexistente.'),
 60: ('X', 'Tomar y no tomar el mismo objeto', 'La misma orden exige y prohíbe recoger la misma manzana; los referentes sí están especificados.', 'Reconocer contradicción y solicitar resolución o rechazar justificadamente, según el criterio aprobado; no ejecutar solo una mitad.'),
}

sources = [INPUT, REF, AUDIT, ROOT/'data/datasets/dataset_gpsr.jsonl']
sources += [ROOT/p for p in ['qwen_gpsr/generation/command_goals.py', 'qwen_gpsr/generation/command_utils.py', 'qwen_gpsr/domain/command_constants.py', 'qwen_gpsr/domain/goal_schema.py', 'experiments/vendor/goal_adapter.py', 'experiments/vendor/goals_planning.clp', 'data/CompetitionTemplate/maps/location_names.md', 'data/CompetitionTemplate/maps/room_names.md', 'data/CompetitionTemplate/objects/objects.md', 'data/CompetitionTemplate/names/names.md']]
before = {str(p.relative_to(ROOT)): sha(p) for p in sources}
entries, refs = read(INPUT), {r['id']: r for r in read(REF)}
audit = json.loads(AUDIT.read_text())
assert sha(INPUT) == audit['desarrollo_sha256']
assert sha(ROOT/'data/datasets/dataset_gpsr.jsonl') == audit['dataset_sha256']
assert len(entries) == len(translations) == 60
rows = []
for n, (entry, es) in enumerate(zip(entries, translations), 1):
    assert entry['id'] == f'DEV-{n:03d}'
    ref = refs[entry['id']]
    assert ref['input'] == entry['input']
    block, family, why, capability = groups[(n-1)//3] if n <= 48 else special[n]
    matches = {k: [x['linea_dataset'] for x in v if x['id'] == entry['id']] for k,v in audit['coincidencias'].items()}
    rows.append(dict(id=entry['id'], intent_id=ref['intent_id'], input=entry['input'], translation_es=es,
      proposed_block=block, proposed_block_label=labels[block], linguistic_variant=ref['variant'],
      original_block=ref['block'], family_or_route=family, evidence=why, capability_review=capability,
      corpus_matches=matches, corpus_intent_overlap_status=ref['intent_overlap_status'],
      historical_train_membership='no_verificada', literal_generator_derivability='no_verificada',
      review_status='pending', reviewer='', review_decision='', review_notes=''))

(OUT/'clasificacion_60.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows))
with (OUT/'clasificacion_60.csv').open('w', newline='', encoding='utf-8-sig') as f:
    writer = csv.DictWriter(f, fieldnames=list(rows[0]))
    writer.writeheader()
    for r in rows:
        writer.writerow({k:json.dumps(v,ensure_ascii=False) if isinstance(v,dict) else v for k,v in r.items()})
counts = Counter(r['proposed_block'] for r in rows)
intro = '''# Clasificación de las 60 órdenes — propuesta para revisión

Fecha: 18 de octubre de 2026. **Las 60 clasificaciones están pendientes de aprobación.**
La aprobación previa de las referencias no aprueba automáticamente esta clasificación.

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
'''
for k, label in labels.items():
    intro += f'| {k} | {label} | {counts[k]} |\n'
intro += '''
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
'''
text = intro
for r in rows:
    hits = r['corpus_matches']['normalizador_real']
    overlap = ('Coincidencia normalizada, línea(s) '+', '.join(map(str,hits))) if hits else 'Sin coincidencia normalizada detectada'
    text += f"\n### {r['id']} · {r['intent_id']} · {r['proposed_block']}\n\n"
    text += f"**Inglés — entrada original:** {r['input']}\n\n**Español — ayuda de lectura:** {r['translation_es']}\n\n"
    text += f"- **Bloque propuesto:** {r['proposed_block_label']}.\n- **Variante original:** `{r['linguistic_variant']}`.\n- **Familia/ruta:** `{r['family_or_route']}`.\n- **Justificación:** {r['evidence']}\n- **Capacidad a revisar:** {r['capability_review']}\n- **Corpus:** {overlap}; pertenencia histórica a train no verificada. Grupo: `{r['corpus_intent_overlap_status']}`.\n- **Revisión:** pendiente. Decisión: _____ · Comentario: _____\n"
DOC.write_text(text)
assert before == {str(p.relative_to(ROOT)): sha(p) for p in sources}
assert [r['input'] for r in read(OUT/'clasificacion_60.jsonl')] == [e['input'] for e in entries]
(OUT/'clasificacion_trazabilidad.json').write_text(json.dumps(dict(date='2026-10-18',status='pending',scope='generador_local_actual',counts=dict(counts),rows=len(rows),intentions=len(set(r['intent_id'] for r in rows)),source_hashes=before,outputs={str(p.relative_to(ROOT)):sha(p) for p in [DOC,OUT/'clasificacion_60.jsonl',OUT/'clasificacion_60.csv']},script_sha256=sha(Path(__file__))),ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(rows=len(rows),counts=dict(counts),english_preserved=True,source_hashes_unchanged=True),ensure_ascii=False))
