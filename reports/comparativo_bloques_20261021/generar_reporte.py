"""Revisión estratificada de evidencia existente. No consulta modelos ni escribe campañas."""
import csv, hashlib, html, json, statistics, sys
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from experiments.common import object_digest
OUT=Path(__file__).resolve().parent
AUDIT=ROOT/'reports/auditoria_cobertura_20261018'
PREV=ROOT/'reports/revision_cumplimiento_20261018'
MODELS={'Qwen3B':'qwen3b_piloto_60_01','Qwen7B':'qwen7b_piloto_60_01','GPT':'gpt_piloto_60_01'}
STATES={'pass':'Cumple','fail':'Incumple','not_verifiable':'No verificable','not_applicable':'No aplicable'}
BLOCKS={'G':'Dentro del generador local','L':'Extensión léxica','C':'Composición adicional','M':'Atributos conjuntos','A':'Información ausente','F':'Acciones no disponibles','X':'Contradicción'}
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return [json.loads(x) for x in p.read_text().splitlines() if x.strip()]
def dump(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def inventory():return {str(p.relative_to(ROOT)):sha(p) for c in MODELS.values() for p in (ROOT/'reports/experiments'/c).rglob('*') if p.is_file()}
before=inventory()
approval=json.loads((AUDIT/'aprobacion_clasificacion_20261021.json').read_text())
assert approval['review_status']=='approved'
assert approval['proposal_sha256']==sha(AUDIT/'clasificacion_60.jsonl')
classes={r['id']:r for r in read(AUDIT/'clasificacion_60.jsonl')}
blocks={d['id']:d['approved_block'] for d in approval['decisions'] if d['review_decision']=='aprobar'}
assert len(classes)==len(blocks)==60
assert all(classes[k]['proposed_block']==v for k,v in blocks.items())
# Reejecutar solo el tramo de comprobación del evaluador anterior (antes de cualquier escritura).
# Comprueba secuencias, contratos, referencias compartidas y los 180 primeros intentos.
evaluator=PREV/'preparar_dictamenes.py'
code=evaluator.read_text().split("(OUT/'dictamenes_propuestos.jsonl').write_text",1)[0]
assert 'assert inventory()==before' in code
namespace={'__file__':str(evaluator),'__name__':'revalidacion_sin_escritura'}
exec(compile(code,str(evaluator),'exec'),namespace)
old=read(PREV/'dictamenes_propuestos.jsonl')
assert namespace['proposals']==old, 'Cambió la revisión previa; investigar antes de continuar'
raw={}
for model,campaign in MODELS.items():
    records=read(ROOT/'reports/experiments'/campaign/'resultados.jsonl')
    assert len(records)==60 and all(r['attempt']==r['repetition']==1 for r in records)
    for r in records:raw[(model,r['case_id'])]=r
refs={r['id']:r for r in read(ROOT/'reports/experiments/gpt_piloto_60_01/assets/referencias.jsonl')}

# Evidencia complementaria del contrato ACTUAL: no se convierte en evidencia histórica.
consumer_paths=[Path('/home/sergio/Justina/src')/p for p in [
 'Supervisor/supervisor_manager/src/recovery/follow_sequence.cpp',
 'Executor/executor_tools/src/Say.cpp','Executor/executor_tools/src/Listen.cpp']]
consumer_hashes={str(p):sha(p) for p in consumer_paths}
follow=consumer_paths[0].read_text()
assert all(s in follow for s in ['instruct_follow_only','instruct_follow_to_','Justina follow enable','Justina follow disable','WAIT_DESTINATION'])

rows=[]
for previous in old:
    r=json.loads(json.dumps(previous)); key=(r['model'],r['case_id']); result=raw[key]
    assert r['run_id']==result['run_id'] and r['result_sha256']==object_digest(result)
    c=classes[r['case_id']]; b=blocks[r['case_id']]
    assert c['input']==result['input_original']==refs[r['case_id']]['input']
    r.update(original_block=r.pop('block'),approved_block=b,block_label=BLOCKS[b],translation_es=c['translation_es'],linguistic_variant=c['linguistic_variant'],classification_review_status='approved',reviewed_on='2026-10-21',review_status='assistant_review_pending_investigator',review_basis='Revalidación de evidencia guardada y estratificación aprobada; no ejecución física')
    # Eliminar recomendaciones de selección de bloques que la clasificación aprobada dejó obsoletas.
    r['previous_decisions_to_review']=r.pop('decisions_to_review')
    r['decisions_to_review']=[]
    if r['case_id']=='DEV-051':
        r['decisions_to_review']=['Mantener el incumplimiento dentro de G: generador admite peso, pero el plan sustituye peso por tamaño.']
    if r['case_id']=='DEV-049':
        r['decisions_to_review']=['M separado; distinguir cumplimiento de la tarea y reconocimiento explícito de limitación.']
    r['limit_handling']=None
    if b in ('A','F','X'):
        r['limit_handling']={'appropriate':r['proposed_review']['domain_response_correct'],'basis':'Criterio original de aclaración/rechazo y contenido de la respuesta; HTTP 422 no es rechazo deliberado.','retrospective':False}
    if b=='M':
        r['limit_handling']={'appropriate':r['model']=='GPT','basis':'GPT reconoce explícitamente que no admite gesto y vestimenta conjuntos; Qwen genera planes que pierden una condición. Esto no cumple la tarea executable de la referencia original.','retrospective':True}
    r['current_contract_note']=None
    if r['case_id'] in ('DEV-025','DEV-026','DEV-027'):
        r['current_contract_note']='El supervisor actual reconoce instruct_follow_only y activa/desactiva seguimiento mediante una secuencia de escucha. Hay compatibilidad estática con ese protocolo; no se ha establecido la huella histórica del ejecutor. Se conserva no_verificable para cumplimiento histórico.'
        r['proposed_review']['review_notes']='El plan contiene el disparador de seguimiento. La inspección del supervisor actual da significado ejecutable a instruct_follow_only; la versión correspondiente a la campaña no está congelada. Cumplimiento histórico no verificable; no es ausencia demostrada de capacidad.'
    if r['case_id']=='DEV-052':
        r['current_contract_note']='El supervisor actual reconoce instruct_follow_to_<destino> y controla llegada/timeout. GPT omite este disparador. En Qwen persisten la identidad Simone y la trazabilidad histórica del consumidor.'
    if r['case_id'] in ('DEV-037','DEV-038','DEV-039'):
        r['current_contract_note']='Listen actual almacena el nombre por categoría/índice y Say resuelve claves vía Knowledge. No se verificó aquí la cadena histórica completa guest_name_last → saved_name; no convertirla automáticamente en éxito.'
    r['reference_requirements']={k:refs[r['case_id']][k] for k in ['required_subtasks','constraints','verification_limits']}
    r['timing_seconds']=result['timing']['total_ms']/1000
    r['execution_status']=result['execution_status']
    r['plan_contract_valid']=result['validation']['plan_contract_valid']
    rows.append(r)
assert len(rows)==len({r['run_id'] for r in rows})==180

summary=[]
for b in BLOCKS:
 for model in MODELS:
    selected=[r for r in rows if r['approved_block']==b and r['model']==model]
    counts=Counter(r['proposed_review']['task_fulfillment'] for r in selected)
    semantics=Counter(str(r['proposed_review']['semantic_correct']) for r in selected)
    handling=[r['limit_handling'] for r in selected if r['limit_handling'] is not None]
    values=[r['timing_seconds'] for r in selected]
    internals=[raw[(r['model'],r['case_id'])]['resources']['model_internal'] for r in selected]
    available=[x for x in internals if x['status']=='available'] if model!='GPT' else []
    gpu=[max(d['allocated_peak_sampled_bytes'] for d in x['gpu']['devices'])/2**30 for x in available if x.get('gpu',{}).get('status')=='available' and x['gpu'].get('devices')]
    rss=[x['rss_peak_sampled_bytes']/2**20 for x in available if x.get('rss_peak_sampled_bytes') is not None]
    summary.append(dict(block=b,model=model,n=len(selected),intentions=len({r['intent_id'] for r in selected}),**{k:counts[k] for k in STATES},
      confirmed_symbolic_fraction=counts['pass']/len(selected) if b not in ('A','F','X') else None,
      semantic_true=semantics['True'],semantic_false=semantics['False'],semantic_not_evaluable=semantics['None'],
      appropriate_limit_responses=sum(x['appropriate'] is True for x in handling),limit_response_denominator=len(handling),
      valid_plan_contract=sum(r['plan_contract_valid'] is True for r in selected),errors=sum(r['execution_status']!='completed' for r in selected),
      latency_mean_seconds=statistics.mean(values),latency_median_seconds=statistics.median(values),latency_n=len(values),latency_includes_errors=True,
      model_internal_status='no disponibles' if model=='GPT' else 'available' if available else 'unavailable',model_internal_n=len(available),
      model_gpu_peak_GiB_median=statistics.median(gpu) if gpu else None,model_gpu_n=len(gpu),model_rss_peak_MiB_median=statistics.median(rss) if rss else None,model_rss_n=len(rss)))
assert all(s['n']==sum(s[k] for k in STATES) for s in summary)
assert all(s['semantic_true']+s['semantic_false']+s['semantic_not_evaluable']==s['n'] for s in summary)
assert sum(s['n'] for s in summary)==180
assert all(s['model_gpu_peak_GiB_median'] is None and s['model_rss_peak_MiB_median'] is None for s in summary if s['model']=='GPT')
(OUT/'revision_por_caso.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows))
def csvout(name,records):
 with (OUT/name).open('w',newline='',encoding='utf-8-sig') as f:
    w=csv.DictWriter(f,fieldnames=list(records[0]));w.writeheader();w.writerows(records)
csvout('resumen_por_bloque.csv',summary)
csvout('revision_por_caso.csv',[dict(model=r['model'],case_id=r['case_id'],intent_id=r['intent_id'],block=r['approved_block'],input=r['evidence']['input'],translation_es=r['translation_es'],**r['proposed_review'],limit_response_appropriate=(r['limit_handling'] or {}).get('appropriate'),current_contract_note=r['current_contract_note'],run_id=r['run_id'],classification_status='approved',judgment_status=r['review_status'],investigator_decision='',investigator_notes='') for r in rows])
dump(OUT/'resumen_por_bloque.json',summary)

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
colors=['#29845a','#c74d46','#a4adb9','#e1e5eb']
fig,axes=plt.subplots(1,7,figsize=(20,5),sharey=False)
for ax,b in zip(axes,BLOCKS):
    ss=[s for s in summary if s['block']==b];bottom=[0]*3
    for k,col in zip(STATES,colors):
        vals=[s[k] for s in ss];ax.bar(list(MODELS),vals,bottom=bottom,color=col,label=STATES[k]);bottom=[a+v for a,v in zip(bottom,vals)]
    ax.set_title(f'{b} · n={ss[0]["n"]} por modelo');ax.tick_params(axis='x',rotation=45);ax.set_ylim(0,ss[0]['n']+1);ax.yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(integer=True))
axes[0].set_ylabel('Órdenes: dictamen propuesto')
fig.legend(*axes[0].get_legend_handles_labels(),loc='lower center',ncol=4)
fig.suptitle('Cumplimiento simbólico por bloque aprobado · revisión del asistente, pendiente de aprobación')
fig.tight_layout(rect=(0,.1,1,.94))
for ext in ('png','svg'):fig.savefig(OUT/f'cumplimiento_por_bloque.{ext}',dpi=180)
plt.close(fig)
fig,axes=plt.subplots(1,4,figsize=(12,4))
for ax,b in zip(axes,('M','A','F','X')):
    ss=[s for s in summary if s['block']==b]
    ax.bar(list(MODELS),[s['appropriate_limit_responses'] for s in ss],color=['#2166ac','#d6604d','#5e3c99'])
    for i,s in enumerate(ss):ax.text(i,s['appropriate_limit_responses']+.04,f"{s['appropriate_limit_responses']}/{s['limit_response_denominator']}",ha='center')
    ax.set_title(b+' · '+BLOCKS[b]);ax.set_ylim(0,ss[0]['n']+.6);ax.yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(integer=True))
axes[0].set_ylabel('Respuestas de límite adecuadas')
fig.suptitle('Aclaración/rechazo: eje separado del cumplimiento · M es diagnóstico retrospectivo',fontsize=11)
fig.tight_layout(rect=(0,0,1,.93))
for ext in ('png','svg'):fig.savefig(OUT/f'respuestas_limites.{ext}',dpi=180)
plt.close(fig)

intro='''# Comparativo por bloques aprobados y revisión de cumplimiento

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
'''
md=intro
for s in summary:
 if s['block']=='G':md+=f"| {s['model']} | {s['pass']} | {s['fail']} | {s['not_verifiable']} | {s['pass']}/46 ({100*s['pass']/46:.1f} %) | {s['semantic_true']}/46 |\n"
md+='''
La fidelidad de objetivos admite equivalencias semánticas revisadas (por ejemplo sintaxis de
entrega, singular/plural de vestimenta y capitalización); no sustituye la métrica histórica
de coincidencia literal. La exactitud del objetivo y el cumplimiento del plan son ejes distintos.

## Todos los bloques

| Bloque | Sistema | n | Intenciones | Cumple | Incumple | No verificable | No aplicable | Respuesta de límite adecuada |
|---|---|---:|---:|---:|---:|---:|---:|---:|
'''
for s in summary:
 h=f"{s['appropriate_limit_responses']}/{s['limit_response_denominator']}" if s['limit_response_denominator'] else '—'
 md+=f"| {s['block']} | {s['model']} | {s['n']} | {s['intentions']} | {s['pass']} | {s['fail']} | {s['not_verifiable']} | {s['not_applicable']} | {h} |\n"
md+='''
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
'''
(OUT/'INFORME.md').write_text(md)
# Tabla de las 60 órdenes, manteniendo los tres resultados juntos.
case_md='# Revisión por caso y bloque aprobado\n\nDictámenes del asistente; aprobación humana pendiente. Evidencia completa en el visor HTML.\n\n| Caso | Bloque | Qwen3B | Qwen7B | GPT |\n|---|---|---|---|---|\n'
for cid in classes:
 case_md+='| '+cid+' | '+blocks[cid]+' | '+' | '.join(STATES[next(r for r in rows if r['model']==m and r['case_id']==cid)['proposed_review']['task_fulfillment']] for m in MODELS)+' |\n'
for cid in classes:
 c=classes[cid];case_md+=f"\n## {cid} · {blocks[cid]}\n\n{c['input']}\n\n{c['translation_es']}\n"
 for r in [x for x in rows if x['case_id']==cid]:
  case_md+=f"\n**{r['model']} — {STATES[r['proposed_review']['task_fulfillment']]}:** {r['proposed_review']['review_notes']}\n"
  if r['limit_handling']:case_md+=f"\nRespuesta de límite adecuada: {r['limit_handling']['appropriate']}. {r['limit_handling']['basis']}\n"
(OUT/'REVISION_POR_CASO.md').write_text(case_md)

esc=lambda s:html.escape(str(s))
parts=['''<!doctype html><html lang="es"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Comparativo por bloques aprobados</title><style>body{font:16px system-ui;max-width:1300px;margin:auto;padding:24px;background:#f5f7fa;color:#19283e}table{border-collapse:collapse;width:100%;background:white}td,th{border:1px solid #ccd3dd;padding:8px;text-align:left}details{background:white;padding:16px;margin:12px 0;border:1px solid #cdd6e3;border-radius:8px}summary{cursor:pointer;font-weight:bold}pre{white-space:pre-wrap;overflow-wrap:anywhere;font-size:13px}input,select{padding:10px;margin:6px}.columns{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px}img{width:100%}@media(max-width:900px){.columns{display:block}}</style><h1>Comparativo por bloques aprobados</h1><p>21 de octubre de 2026 · 180 primeros intentos. Clasificación aprobada; dictámenes del asistente pendientes de aprobación humana.</p><p><a href="INFORME.md">Informe y criterios</a> · <a href="REVISION_POR_CASO.md">Revisión de las 60 órdenes</a> · <a href="revision_por_caso.csv">CSV de revisión</a> · <a href="resumen_por_bloque.csv">Métricas por bloque</a> · <a href="trazabilidad.json">Trazabilidad</a> · <a href="../comparativo_piloto60_20261017/index.html">Reporte histórico y recursos</a></p><p>Cumple se refiere al plan simbólico. No verificable no cuenta como acierto ni fallo. A/F/X se evalúan por aclaración/rechazo; sus planes no tienen cumplimiento aplicable.</p><img src="cumplimiento_por_bloque.svg" alt="Conteos de cumplimiento simbólico por bloque y modelo"><img src="respuestas_limites.svg" alt="Respuestas adecuadas de aclaración o rechazo por bloque"><h2>Resumen por bloque</h2><table><tr><th>Bloque</th><th>Modelo</th><th>n</th><th>Cumple</th><th>Incumple</th><th>No verificable</th><th>No aplicable</th><th>Límite adecuado</th></tr>''']
for s in summary:
 parts.append('<tr>'+''.join('<td>'+esc(x)+'</td>' for x in [s['block'],s['model'],s['n'],s['pass'],s['fail'],s['not_verifiable'],s['not_applicable'],f"{s['appropriate_limit_responses']}/{s['limit_response_denominator']}" if s['limit_response_denominator'] else '—'])+'</tr>')
parts+=['</table><h2>Comparación por caso</h2><label>Bloque <select id="block"><option value="">Todos</option>'+''.join(f'<option value="{k}">{k}: {v}</option>' for k,v in BLOCKS.items())+'</select></label><label>Buscar <input id="search" placeholder="DEV-050, peso, Robin…"></label><p id="count"></p>']
for cid,c in classes.items():
 rr=[r for r in rows if r['case_id']==cid]
 parts.append(f'<details class="case" data-block="{blocks[cid]}"><summary>{cid} · {blocks[cid]} · {esc(c["input"])}</summary><p>{esc(c["translation_es"])}</p><p>{esc(c["evidence"])}</p><h3>Subtareas y restricciones de referencia</h3><ul>'+''.join('<li>'+esc(x)+'</li>' for x in refs[cid]['required_subtasks']+refs[cid]['constraints'])+'</ul><div class="columns">')
 for r in rr:
  v=r['proposed_review'];e=r['evidence']
  parts.append(f'<section><h3>{r["model"]}: {STATES[v["task_fulfillment"]]}</h3><p>{esc(v["review_notes"])}</p><p>Interpretación semántica: {esc(v["semantic_correct"])} · {r["timing_seconds"]:.3f} s</p>')
  if r['limit_handling']:parts.append('<p>Respuesta de límite: '+esc(r['limit_handling'])+'</p>')
  if r['current_contract_note']:parts.append('<p>'+esc(r['current_contract_note'])+'</p>')
  plan='\n'.join(f"{s['step']}: {s['action']} {s['params']}" for s in e['plan'] or [])
  parts.append('<h4>Objetivos</h4><pre>'+esc(json.dumps(e['goals_pred'],ensure_ascii=False,indent=2))+'</pre><h4>Plan o respuesta</h4><pre>'+esc(plan or e['message'] or json.dumps(e['error'],ensure_ascii=False))+'</pre><small>run_id: '+esc(r['run_id'])+'</small></section>')
 parts.append('</div></details>')
parts.append('''<script>function filter(){let n=0;const b=document.querySelector('#block').value,q=document.querySelector('#search').value.toLowerCase();document.querySelectorAll('.case').forEach(e=>{const ok=(!b||e.dataset.block===b)&&e.textContent.toLowerCase().includes(q);e.hidden=!ok;if(ok)n++});document.querySelector('#count').textContent=n+' de 60 órdenes visibles · tres modelos por orden'}document.querySelector('#block').addEventListener('change',filter);document.querySelector('#search').addEventListener('input',filter);filter()</script></html>''')
(OUT/'index.html').write_text('\n'.join(parts))
assert inventory()==before,'Se modificó una campaña'
dump(OUT/'trazabilidad.json',dict(date='2026-10-21',classification_status='approved',judgment_status='assistant_review_pending_investigator',first_attempts=180,review_source_sha256=sha(PREV/'dictamenes_propuestos.jsonl'),review_evaluator_sha256=sha(evaluator),approval_sha256=sha(AUDIT/'aprobacion_clasificacion_20261021.json'),classification_sha256=sha(AUDIT/'clasificacion_60.jsonl'),script_sha256=sha(Path(__file__)),campaign_inventory_unchanged=True,campaign_inventory=before,current_consumer_sources=consumer_hashes,current_consumer_not_historical_snapshot=True,output_hashes={p.name:sha(p) for p in OUT.iterdir() if p.is_file() and p.name not in ('trazabilidad.json','generar_reporte.py')}))
print(json.dumps([s for s in summary if s['block']=='G'],ensure_ascii=False,indent=2))
