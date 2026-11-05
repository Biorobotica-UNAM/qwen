"""Propuestas de revisión sobre evidencia congelada; no modifica campañas ni aprueba dictámenes."""
import csv, hashlib, html, json, sys
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT))
from experiments.common import object_digest
OUT=Path(__file__).resolve().parent
CAMPAIGNS={'Qwen3B':'qwen3b_piloto_60_01','Qwen7B':'qwen7b_piloto_60_01','GPT':'gpt_piloto_60_01'}
BASE=ROOT/'reports/experiments'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def jsonl(p):return [json.loads(l) for l in p.read_text().splitlines() if l.strip()]
def inventory():return {str(p.relative_to(ROOT)):sha(p) for name in CAMPAIGNS.values() for p in (BASE/name).rglob('*') if p.is_file()}
before=inventory(); refs={r['id']:r for r in jsonl(BASE/CAMPAIGNS['GPT']/'assets/referencias.jsonl')}
source={};rows={};proposals=[]
for model,name in CAMPAIGNS.items():
 p=BASE/name;rows[model]={r['case_id']:r for r in jsonl(p/'resultados.jsonl')}
 assert len(rows[model])==60 and all(r['attempt']==1 and r['repetition']==1 for r in rows[model].values())
 assert {r['id']:r for r in jsonl(p/'assets/referencias.jsonl')}==refs
 source[model]={'campaign':str(p.relative_to(ROOT)),'manifest_sha256':sha(p/'manifest.json'),'resultados_sha256':sha(p/'resultados.jsonl'),'reference_version':sha(p/'assets/referencias.jsonl')}

# Requirements for the unambiguous symbolic tasks, explicitly selected from their rubrics.
# All operations listed must appear in order. Dialogue may occur between operations.
def seq(plan,required):
 i=0
 for s in plan or []:
  if s['step']<1001:continue
  if i<len(required) and (s['action'],s['params'][0])==required[i]:i+=1
 return i==len(required)
base_sequences={
1:[('go_to','corridor'),('go_to','inspection_point')],
2:[('go_to','bathroom'),('find_object','peach_1')],
3:[('go_to','bed'),('find_object','spoon_1'),('take','spoon_1')],
4:[('go_to','cabinet'),('find_object','mug_1'),('take','mug_1'),('go_to','instruction_point'),('approach','host_1'),('give','mug_1')],
5:[('go_to','bed'),('find_object','bowl_1'),('take','bowl_1'),('go_to','storage_rack'),('find_space','shelf'),('drop','bowl_1')],
6:[('go_to','kitchen'),('find_object','cup_1'),('take','cup_1'),('find_space','table'),('drop','cup_1')],
11:[('go_to','storage_rack'),('analyze_objects','count_toys'),('go_to','instruction_point'),('say','count_category')],
14:[('go_to','corridor'),('find_pose','waving_1'),('approach','customer_1'),('focus','enable'),('listen','answer_question'),('say','answer_question'),('focus','disable')],
16:[('go_to','sofa'),('analyze_objects','biggest_fruit'),('say','biggest_category')],
21:[('go_to','refrigerator'),('find_object','mug_1'),('take','mug_1'),('go_to','instruction_point'),('approach','host_1'),('give','mug_1'),('go_to','bed'),('find_object','spoon_1'),('take','spoon_1'),('go_to','instruction_point'),('approach','host_1'),('give','spoon_1')],
}
limits={7:'El plan pregunta y escucha el nombre, pero no contiene evidencia de comparación con Robin. Falta precisar el contrato de identificación.',
8:'La guía y su destino se expresan, pero no se acredita que la persona identificada sea Morgan; falta el contrato de identificación.',
9:'Se emite instruct_follow_only, pero no están establecidos sus efectos ejecutables de seguimiento.',
10:'Se conserva el objeto y se entrega a guest_last, pero el vínculo verificado entre guest_last y Sarah depende del contrato de identificación.',
12:'Se comunica current_time tras ask_name/listen, pero no se verifica que el interlocutor sea Charlie.',
13:'Se solicita el nombre y se emite saved_name al regresar; falta establecer la persistencia y recuperación del dato entre esas acciones.',
15:'Se localiza una persona y se saluda a guest_last; la identificación efectiva como Jane no está acreditada por el plan.',
20:'Se emite instruct_follow_to_bedroom, pero sus efectos de seguimiento y la identidad Simone dependen de un contrato aún no precisado.'}
allowed_literal_differences={'Qwen3B':{26,28,29,30,34,35,36,41,46,47,48,50,51,54},'Qwen7B':{28,30,34,35,36,46,47,48,50,51,54},'GPT':{47}}
for cid,ref in sorted(refs.items()):
 n=int(cid[-3:]);intent=int(ref['intent_id'].split('-')[1])
 for model in CAMPAIGNS:
  r=rows[model][cid]; applicable=ref['goals_ref'] is not None
  semantic=None if not applicable or r['execution_status']!='completed' or r['response_kind']!='plan' else r['goals_pred']==ref['goals_ref'] or n in allowed_literal_differences[model]
  status='not_verifiable';reason='';failed=[];categories=[];domain=None;checks=[];decisions=[];limitation=None
  if not applicable:
   status='not_applicable'
   domain=r['execution_status']=='completed' and r['response_kind']==ref['expected_status']
   if domain:
    reason='La respuesta pide la información faltante o explica el rechazo previsto; no inventa objetivos ni plan.'
    checks.append('Respuesta original: '+r['message'])
   elif r['execution_status']!='completed':
    reason='No se obtuvo aclaración ni rechazo deliberado. HTTP 422 por salida de modelo inválida; no confundir el error con una respuesta correcta de dominio.'
    failed.append('No hay respuesta de dominio conforme a la ficha.');categories=['interpretation']
    checks.append('Error observado: '+json.dumps(r['error'],ensure_ascii=False))
   else:
    reason='Produce un plan pese a información faltante o acciones fuera del dominio; no cumple la respuesta de dominio prevista.'
    failed.append('La salida completa datos ausentes o sustituye una acción no soportada.');categories=['interpretation']
  elif r['execution_status']!='completed':
   status='fail';reason='No se obtuvo un plan. HTTP 422 conserva texto generado inválido; el servidor respondió, por lo que no se clasifica como caída de infraestructura.'
   failed.append('No existe plan evaluable para la orden ejecutable.');categories=['interpretation'];semantic=None
  elif n==49:
   status='fail';limitation='atributos_conjuntos'
   if model=='GPT':
    semantic=None;reason='Rechazo explícito por límite de capacidad. No realiza la tarea que la ficha aprobada describe como executable; no se atribuye fallo lingüístico ni plan incorrecto.'
    failed.append('No se produjo un plan para la tarea solicitada.')
    decisions.append('Reconocer el rechazo como conducta prudente adicional, sin cambiar retrospectivamente cumplimiento ni expected_status de la ficha.')
   else:
    semantic=False;categories=['interpretation','planning']
    reason='No se representa la conjunción con ambos campos de búsqueda utilizables; el plan solo verifica el gesto y no el abrigo azul.'
    failed.append('Falta la comprobación conjunta de gesto y vestimenta.')
   decisions.append('Mantener el caso como límite de capacidad y separado del bloque resoluble.')
  elif n==50:
   status='fail';semantic=True;categories=['planning'];limitation='filtro_no_expandido'
   reason='La interpretación conserva el filtro rojo, pero el plan solo ejecuta count_person y no expresa un conteo filtrado. La ficha prohíbe contar todas las personas como sustituto.'
   failed.append('El plan omite el filtro wearing=red shirt(s).')
  elif n==51:
   status='fail';semantic=True;categories=['planning'];limitation='proxy_insuficiente'
   reason='Interpreta heaviest, pero sustituye la medición de peso por biggest_fruit. Es una incompatibilidad explícita con la restricción «No sustituir peso por tamaño», no mera ausencia de prueba física.'
   failed.append('Análisis de tamaño seguido de anuncio de peso, sin operación que determine peso.')
   decisions.append('Analizar proxy_insuficiente en el bloque de capacidades; no incorporarlo a la tasa del bloque resoluble ni culpar a la interpretación correcta.')
  elif model=='GPT' and n==24:
   status='fail';semantic=True;categories=['planning']
   reason='Desactiva focus antes de Please follow me to entrance, aunque la interacción continúa. Además persiste la limitación de identificación de Morgan.'
   failed.append('focus disable precede a la última intervención dirigida a la misma persona.')
   decisions.append('Aplicar el requisito de focus continuo del prompt y reglas congelados; el validador estructural actual no lo comprueba.')
  elif model=='GPT' and n==52:
   status='fail';semantic=True;categories=['planning'];limitation='protocolo_seguimiento'
   reason='Solo anuncia I will follow Simone to bedroom; omite instruct_follow_to_bedroom y regresa al operador. Falta el elemento de protocolo, aun antes de verificar sus efectos.'
   failed.append('No aparece la instrucción de seguimiento al destino.')
  elif model=='Qwen7B' and n in (1,3):
   status='fail';semantic=False;categories=['interpretation'];reason='Sustituye visitar inspection point por buscarlo como objeto.';failed.append('No visita el segundo destino solicitado.')
  elif model=='Qwen7B' and n==29:
   status='fail';semantic=False;categories=['interpretation'];reason='Busca, toma y entrega orange coat en lugar de orange; la referencia prohíbe confundir objeto y ropa.';failed.append('Objeto incorrecto en la entrega.')
  elif model=='Qwen3B' and n==53:
   status='fail';semantic=False;categories=['interpretation'];reason='Coloca mug en bed en vez de entregarla al operador; la segunda entrega no compensa la primera omitida.';failed.append('Primera entrega sustituida por colocación.')
  elif intent in limits:
   status='not_verifiable';reason=limits[intent];limitation='contrato_ejecutor_pendiente'
   decisions.append('Precisar el contrato del ejecutor para identidad, memoria o seguimiento; por ahora no convertir concordancia del protocolo en cumplimiento.')
  elif n==54:
   item='Water_1' if model=='GPT' else 'water_1'
   required=[('go_to','kitchen'),('find_object',item),('take',item),('go_to','instruction_point'),('approach','host_1'),('give',item)]
   assert seq(r['plan'],required)
   status='pass';semantic=True;reason='Conserva Water como objeto y lo entrega al operador; la diferencia de capitalización no cambia el referente. No reproduce el defecto del control que lo trata como persona.'
   checks.append('Secuencia comprobada: '+str(required))
  elif intent in base_sequences:
   required=base_sequences[intent];assert seq(r['plan'],required),(cid,model)
   assert semantic is True,(cid,model,'semantic unresolved')
   assert r['validation']['plan_contract_valid'] is True
   operations=[s for s in r['plan'] if s['step']>=1001]
   if intent==2:assert not any(s['action'] in ('take','give','drop') for s in operations)
   if intent==6:assert not any(s['action']=='go_to' and s['params']==['table'] for s in operations)
   status='pass';reason='La secuencia cubre las subtareas y dependencias de esta ficha, con referentes consistentes y sin sustituciones observadas. Es cumplimiento simbólico propuesto, no ejecución física.'
   checks.append('Secuencia comprobada en orden: '+str(required))
  else:raise AssertionError((cid,model,'unreviewed case'))
  if semantic is True and r['goals_pred']!=ref['goals_ref']:checks.append('Diferencia literal admitida en esta revisión: sintaxis de destinatario, espacio, sinónimo de información/gesto/tamaño, singular de vestimenta o capitalización de objeto; conservar métrica literal original.')
  if applicable and status=='not_verifiable':assert semantic is True
  proposal={'proposal_id':model+'_'+cid,'model':model,'case_id':cid,'intent_id':ref['intent_id'],'block':ref['block'],'run_id':r['run_id'],
    'reference_version':source[model]['reference_version'],'result_sha256':object_digest(r),'review_status':'pending_investigator_review','proposed_by':'assistant','proposed_on':'2026-10-18',
    'proposed_review':{'semantic_correct':semantic,'task_fulfillment':status,'domain_response_correct':domain,'failed_checks':failed,'error_categories':categories,'review_notes':reason},
    'limitation_label':limitation,'checks':checks,'decisions_to_review':decisions,
    'evidence':{'input':r['input_original'],'expected_status':ref['expected_status'],'response_kind':r['response_kind'],'execution_status':r['execution_status'],'goals_ref':ref['goals_ref'],'goals_pred':r['goals_pred'],'plan':r['plan'],'message':r['message'],'error':r['error'],'raw_output':r['raw_output']},
    'investigator_decision':None,'investigator_notes':None}
  proposals.append(proposal)
assert len(proposals)==180 and len({r['run_id'] for r in proposals})==180
assert inventory()==before,'Campaign changed'
(OUT/'dictamenes_propuestos.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in proposals))
flat=[{'model':r['model'],'case_id':r['case_id'],'intent_id':r['intent_id'],**r['proposed_review'],'review_status':r['review_status'],'investigator_decision':'','investigator_notes':''} for r in proposals]
with (OUT/'dictamenes_para_revision.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(flat[0]));w.writeheader();w.writerows(flat)
counts={model:dict(Counter(r['proposed_review']['task_fulfillment'] for r in proposals if r['model']==model)) for model in CAMPAIGNS}
meta={'scope':'Assistant proposals only; not final human judgments or physical success','date':'2026-10-18','sources':source,'campaign_inventory':before,'proposed_counts':counts,'all_180_pending':True}
(OUT/'trazabilidad.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n')
intro='''# Revisión de cumplimiento: propuestas para las 60 órdenes

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
'''
labels={'pass':'Cumple simbólico','fail':'Incumple','not_verifiable':'No verificable','not_applicable':'No aplicable'}
lines=[intro,'','| Condición | Cumple simbólico | Incumple | No verificable | No aplicable |','|---|---:|---:|---:|---:|']
for model,c in counts.items():lines.append('| '+model+' | '+' | '.join(str(c.get(k,0)) for k in labels)+' |')
lines+=['','## Índice de propuestas','','| Caso | Qwen3B | Qwen7B | GPT |','|---|---|---|---|']
for cid in sorted(refs):lines.append('| ['+cid+'](#'+cid.lower()+') | '+' | '.join(labels[next(r for r in proposals if r['case_id']==cid and r['model']==m)['proposed_review']['task_fulfillment']] for m in CAMPAIGNS)+' |')
for cid,ref in sorted(refs.items()):
 lines+=['',f'## {cid}','',f"**Orden:** {ref['input']}",'',f"**Intención:** {ref['intent_id']}. **Bloque:** {ref['block']}.",'','**Subtareas:**','',*['- '+s for s in ref['required_subtasks']], '', '**Restricciones:**','',*['- '+s for s in ref['constraints']], '', '**Límites de verificación de la ficha:**','',*['- '+s for s in ref['verification_limits']]]
 for r in [r for r in proposals if r['case_id']==cid]:
  v=r['proposed_review'];e=r['evidence']
  lines+=['',f"### {r['model']} — {labels[v['task_fulfillment']]}",'',v['review_notes'],'',f"Interpretación propuesta: `{v['semantic_correct']}`. Respuesta de dominio: `{v['domain_response_correct']}`.",'', '**Objetivos originales:**','', '```json',json.dumps(e['goals_pred'],ensure_ascii=False,indent=2),'```','', '**Evidencia del plan (incluye anuncios y operaciones):**','', '```text']
  lines += [f"{s['step']}: {s['action']} {' '.join(s['params'])}" for s in e['plan'] or []]
  if not e['plan']:lines += [e['message'] or json.dumps(e['error'],ensure_ascii=False)]
  lines+=['```','',f"run_id: `{r['run_id']}`",'','Decisión del investigador: **pendiente**. Observaciones: __________________']
(OUT/'DICTAMENES.md').write_text('\n'.join(lines)+'\n')
# Lightweight HTML for navigating evidence; decisions exported via editable CSV, not browser state.
esc=html.escape
parts=['<!doctype html><html lang="es"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Dictámenes propuestos</title><style>body{font:16px system-ui;max-width:1150px;margin:auto;padding:24px;background:#f5f7fa;color:#19283e}details{background:white;padding:16px;margin:12px 0;border:1px solid #cdd6e3;border-radius:8px}summary{cursor:pointer;font-weight:bold}pre{white-space:pre-wrap;overflow-wrap:anywhere;font-size:13px}input{padding:12px;width:90%}.cols{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px}@media(max-width:850px){.cols{display:block}}</style><h1>180 dictámenes propuestos · Pendientes de revisión</h1><p>Cumplimiento simbólico; no ejecución física. Ninguna campaña ha sido modificada.</p><p><a href="DICTAMENES.md">Criterios y fichas completas</a> · <a href="dictamenes_para_revision.csv">CSV para registrar decisiones</a> · <a href="trazabilidad.json">Trazabilidad</a></p><input id="filter" placeholder="Buscar DEV-050, peso, identidad…" aria-label="Filtrar fichas">']
for cid,ref in sorted(refs.items()):
 parts += [f'<details class="case"><summary>{cid} · {esc(ref["input"])}</summary><p>Restricciones: {esc("; ".join(ref["constraints"]))}</p><p>Límites: {esc("; ".join(ref["verification_limits"]))}</p><div class="cols">']
 for r in [r for r in proposals if r['case_id']==cid]:
  v=r['proposed_review'];e=r['evidence']
  plan='\n'.join(f"{s['step']} {s['action']} {' '.join(s['params'])}" for s in e['plan'] or [])
  parts += [f'<section><h2>{r["model"]}</h2><b>{labels[v["task_fulfillment"]]} (propuesto)</b><p>{esc(v["review_notes"])}</p><pre>Objetivos: {esc(json.dumps(e["goals_pred"],ensure_ascii=False,indent=2))}</pre><pre>{esc(plan or e["message"] or str(e["error"]))}</pre><p>Decisión del investigador: pendiente</p></section>']
 parts+=['</div></details>']
parts += ["<script>document.getElementById('filter').addEventListener('input',function(){const q=this.value.toLowerCase();document.querySelectorAll('details.case').forEach(d=>d.hidden=!d.textContent.toLowerCase().includes(q));});</script></html>"]
(OUT/'index.html').write_text('\n'.join(parts))
assert inventory()==before
print(json.dumps(counts,ensure_ascii=False,indent=2))
print('180 propuestas pendientes; campañas intactas según inventario SHA-256.')
