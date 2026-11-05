"""Aplica revisión del investigador conservando el dictamen previo y las campañas."""
import csv, hashlib, html, json
from pathlib import Path
from collections import Counter
ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
PREV=ROOT/'reports/comparativo_bloques_20261021'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
source=PREV/'revision_por_caso.jsonl'
rows=[json.loads(x) for x in source.read_text().splitlines()]
trace=json.loads((PREV/'trazabilidad.json').read_text())
for p,h in trace['campaign_inventory'].items():assert sha(ROOT/p)==h
named=set(range(19,25))|set(range(28,31))|set(range(34,37))|set(range(43,46))
follow=set(range(25,28));memory=set(range(37,40));confirmed=set(range(40,43))|set(range(46,49))
models=['Qwen3B','Qwen7B','GPT'];blocks='GLCMAFX'
labels={'pass':'Cumple bajo supuestos declarados','fail':'Incumple criterio estricto','not_verifiable':'No verificable','not_applicable':'No aplicable'}
changes=[]
for r in rows:
 n=int(r['case_id'][-3:]);v=r['proposed_review'];old=v['task_fulfillment']
 r['prior_review']=json.loads(json.dumps(v))
 r['researcher_acceptance']=None;r['decision_basis']=None;r['exception']=None
 if n in named|follow|memory|confirmed:
  if n in named:
   basis='El investigador declara que, en estos escenarios con destinatario nombrado, la única persona de la habitación representa a la persona solicitada. Supuesto del escenario experimental, no propiedad universal certificada de GPSR.'
  elif n in follow:
   basis='El investigador confirma que el plan concuerda con el supervisor; el código actual reconoce instruct_follow_only. Aceptación del contrato simbólico, no ejecución física ni certificación de versión histórica.'
  elif n in memory:
   basis='El investigador acepta el protocolo de consulta/memoria/reporte bajo su escenario GPSR. Se registra como aceptación declarada; no se afirma haber ejecutado o verificado íntegramente la cadena de memoria.'
  else:basis='El investigador acepta la funcionalidad simbólica de respuesta/interacción o selección por tamaño bajo el escenario definido.'
  r['decision_basis']=basis
  # La aclaración sobre identidad no subsana un objeto incorrecto ni un cierre anticipado de focus.
  if old=='not_verifiable':
   v['task_fulfillment']='pass';v['review_notes']=basis+' El resto de las comprobaciones de la revisión previa se conserva.'
   r['researcher_acceptance']='accepted_under_declared_assumptions'
  elif old=='pass':r['researcher_acceptance']='accepted'
  else:
   r['researcher_acceptance']='scope_clarified_other_failure_retained'
   r['decision_basis']+=' Se conserva el incumplimiento distinto de identidad: '+v['review_notes']
 if n in (50,51):
  r['researcher_acceptance']='accepted_by_exception'
  r['exception']='Filtro de vestimenta omitido en el plan histórico; corrección futura pendiente.' if n==50 else 'Se acepta tamaño como proxy de peso para el escenario; no equivale a determinar heaviest.'
  r['decision_basis']='Aceptación excepcional solicitada por el investigador el 22 de octubre de 2026. La referencia original y el incumplimiento estricto se conservan.'
 r['strict_task_fulfillment']=v['task_fulfillment']
 r['scenario_acceptance']='accepted_by_exception' if r['researcher_acceptance']=='accepted_by_exception' else v['task_fulfillment']
 r['review_status']='researcher_scope_applied_other_judgments_not_automatically_approved'
 r['reviewed_on']='2026-10-22'
 if r['decision_basis']:changes.append({'model':r['model'],'case_id':r['case_id'],'run_id':r['run_id'],'previous':old,'strict':r['strict_task_fulfillment'],'scenario':r['scenario_acceptance'],'basis':r['decision_basis'],'exception':r['exception']})
assert len(rows)==180
summary=[]
for b in blocks:
 for m in models:
  rr=[r for r in rows if r['approved_block']==b and r['model']==m]
  c=Counter(r['strict_task_fulfillment'] for r in rr)
  summary.append(dict(block=b,model=m,n=len(rr),**{k:c[k] for k in labels},accepted_exceptions=sum(r['scenario_acceptance']=='accepted_by_exception' for r in rr),accepted_in_scenario=sum(r['scenario_acceptance'] in ('pass','accepted_by_exception') for r in rr)))
assert all(sum(s[k] for k in labels)==s['n'] for s in summary)
(OUT/'revision_por_caso.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows))
dump(OUT/'decisiones_investigador.json',{'date':'2026-10-22','source':'Declaración explícita del investigador en la conversación','scope':'Aceptación de escenarios y protocolos para los casos indicados; excepciones separadas de cumplimiento estricto','dev050_resolution':{'status':'deferred_capability','decision':'Documentar capacidad pendiente y aceptación excepcional','authorized_changes':'Solo documentación y reporte; no modificar ejecutor, CLIPS ni prompt'},'decisions':changes})
dump(OUT/'resumen_por_bloque.json',summary)
with (OUT/'revision_por_caso.csv').open('w',newline='',encoding='utf-8-sig') as f:
 flat=[dict(model=r['model'],case_id=r['case_id'],block=r['approved_block'],strict=r['strict_task_fulfillment'],scenario=r['scenario_acceptance'],researcher_acceptance=r['researcher_acceptance'],reason=r['proposed_review']['review_notes'],decision_basis=r['decision_basis'],exception=r['exception'],run_id=r['run_id']) for r in rows]
 w=csv.DictWriter(f,fieldnames=list(flat[0]));w.writeheader();w.writerows(flat)
intro='''# Revisión con decisiones del investigador — 22 de octubre de 2026

Se aplican las aclaraciones del investigador a los 180 primeros intentos guardados.
Las campañas, objetivos, planes y referencias originales permanecen intactos.
La clasificación por bloques sigue aprobada. Se conserva por fila el dictamen anterior,
la decisión, su fundamento y la identificación del resultado original.

## Supuestos aceptados y alcance

- DEV-019–024, 028–030, 034–036 y 043–045: la única persona presente en la habitación
  representa al destinatario nombrado. Es una condición declarada de estos escenarios,
  no una afirmación general sobre toda prueba GPSR. No se aplica al conteo de personas.
- DEV-025–027: el investigador confirma compatibilidad con el supervisor; se acepta el
  protocolo de seguimiento. No se afirma éxito físico ni se inventa una huella histórica.
- DEV-037–039: se acepta el protocolo de memoria/reporte por declaración del investigador.
  La cadena ejecutora completa no ha sido probada por este análisis.
- DEV-040–042 y 046–048: se ratifica el cumplimiento simbólico ya propuesto.
- GPT/DEV-024 conserva el fallo de focus y Qwen7B/DEV-029 conserva orange coat en lugar de
  orange: el supuesto sobre identidad no corrige esos errores independientes.
- DEV-052 no fue incluido en esta aprobación: Qwen mantiene no verificable por identidad
  y contrato histórico; GPT mantiene la omisión del disparador de seguimiento.

## Dos lecturas para evitar confundir aceptación con equivalencia

**Criterio estricto:** preserva las restricciones originales (peso distinto de tamaño;
conteo filtrado distinto de conteo total), aplicando los supuestos de identidad/protocolo
que el investigador acaba de declarar.

**Aceptación en el escenario:** añade DEV-050 y DEV-051 como excepciones expresamente
aceptadas por el investigador. No se denominan correcciones exitosas del plan histórico.
DEV-051 usa tamaño como proxy aceptado de peso; DEV-050 conserva un filtro omitido.
Ambas excepciones son retrospectivas y deben aparecer como tales en tesis/artículo.
Una futura regla o prompt no modifica lo que devolvieron estas campañas.

## Bloque G: 46 órdenes por sistema

| Modelo | Cumple bajo supuestos | Incumple estricto | No verificable | Excepciones aceptadas (incluidas en incumple) | Aceptados en escenario |
|---|---:|---:|---:|---:|---:|
'''
md=intro
for s in summary:
 if s['block']=='G':md+=f"| {s['model']} | {s['pass']} | {s['fail']} | {s['not_verifiable']} | {s['accepted_exceptions']} | {s['accepted_in_scenario']}/46 |\n"
md+='''
Las excepciones no son una quinta categoría que se sume a las anteriores: son un subconjunto
de incumplimientos estrictos. La columna final corresponde únicamente al criterio relajado
del escenario. No sumar ni comparar tasas de criterios diferentes sin identificarlo.

## Corrección pendiente de DEV-050

La regla histórica emite analyze_objects count_person. El investigador propone analyze_person
red_shirt. Al inspeccionar AnalyzePerson.cpp actual, red_shirt no es un argumento admitido:
la forma reconocida es color_red_shirt, que localiza una persona por atributo. El componente
no implementa un conteo filtrado ni guarda el resultado que reportaría say count_category.
Cambiar solamente el nombre de acción/argumento no completa la tarea solicitada.
El investigador decidió expresamente documentar la capacidad pendiente y mantener la
aceptación excepcional en el reporte. La implementación del conteo filtrado queda aplazada;
no hay una decisión pendiente sobre implementar ahora. Ejecutor, CLIPS y prompt permanecen
sin cambios. La aceptación excepcional no convierte el plan histórico en conteo filtrado correcto.

## Todos los bloques

| Bloque | Modelo | n | Cumple bajo supuestos | Incumple estricto | No verificable | No aplicable | Excepciones |
|---|---|---:|---:|---:|---:|---:|---:|
'''
for s in summary:md+=f"| {s['block']} | {s['model']} | {s['n']} | {s['pass']} | {s['fail']} | {s['not_verifiable']} | {s['not_applicable']} | {s['accepted_exceptions']} |\n"
md+='''
A/F/X conservan su evaluación separada de aclaración/rechazo: GPT responde adecuadamente
6/6; los Qwen 0/6. Los fallos HTTP no son rechazos deliberados. En M, GPT reconoce limitación
sin cumplir la tarea; los Qwen pierden una condición. Latencia y recursos no cambian:
consultar el reporte previo, donde los recursos internos GPT son no disponibles.

Los resultados son exploratorios sobre desarrollo y una repetición; no establecen éxito
físico ni sustituyen el conjunto independiente final. Las decisiones registradas no aprueban
automáticamente otros dictámenes que el investigador no mencionó.

## Reproducción

Desde la raíz: `MPLCONFIGDIR=/tmp/matplotlib-piloto python3 reports/comparativo_revision_investigador_20261022/generar_reporte.py`.
El programa verifica las huellas de las campañas antes y después. Guardar una copia del CSV
antes de editar observaciones porque la regeneración sobrescribe las salidas derivadas.
'''
(OUT/'INFORME.md').write_text(md)
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ss=[s for s in summary if s['block']=='G']
fig,ax=plt.subplots(figsize=(9,5));bottom=[0]*3
for k,label,col in [('pass','Cumple bajo supuestos','#27875c'),('fail','Incumple estricto','#c74d46'),('not_verifiable','No verificable','#9ca7b5')]:
 vals=[s[k] for s in ss];ax.bar(models,vals,bottom=bottom,label=label,color=col)
 for i,v in enumerate(vals):
  if v:ax.text(i,bottom[i]+v/2,str(v),ha='center',va='center')
 bottom=[x+y for x,y in zip(bottom,vals)]
ax.set_ylim(0,50);ax.set_ylabel('Órdenes del bloque G');ax.set_title('Revisión bajo supuestos declarados · 46 órdenes por sistema')
ax.legend(loc='lower center');fig.text(.5,.015,'DEV-050 y DEV-051: aceptados por excepción, conservados como incumplimientos estrictos.',ha='center',fontsize=9);fig.tight_layout(rect=(0,.04,1,1))
for ext in ['svg','png']:fig.savefig(OUT/f'bloque_G.{ext}',dpi=180)
plt.close(fig)
esc=lambda x:html.escape(str(x))
parts=['''<!doctype html><html lang="es"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Revisión del investigador</title><style>body{font:16px system-ui;max-width:1250px;margin:auto;padding:24px;background:#f5f7fa}details{background:white;padding:15px;margin:12px 0}summary{cursor:pointer;font-weight:bold}pre{white-space:pre-wrap;overflow-wrap:anywhere}.cols{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px}img{max-width:100%}input,select{padding:10px}@media(max-width:850px){.cols{display:block}}</style><h1>Revisión del investigador · 22 de octubre de 2026</h1><p>Supuestos declarados y excepciones separados del cumplimiento estricto. Campañas originales intactas.</p><p><a href="INFORME.md">Informe y tablas</a> · <a href="revision_por_caso.csv">CSV</a> · <a href="decisiones_investigador.json">Decisiones registradas</a> · <a href="../comparativo_bloques_20261021/index.html">Revisión anterior y recursos</a></p><img src="bloque_G.svg" alt="Cumplimiento bajo supuestos declarados en bloque G"><p>DEV-050 y DEV-051 se aceptan por excepción, sin afirmar que el plan original filtre vestimenta o mida peso.</p><label>Bloque <select id="block"><option value="">Todos</option>'''+''.join(f'<option>{b}</option>' for b in blocks)+'''</select></label> <label>Buscar <input id="q" placeholder="DEV-050, nombre…"></label><p id="count"></p>''']
for cid in sorted({r['case_id'] for r in rows}):
 rr=[r for r in rows if r['case_id']==cid];a=rr[0]
 parts.append(f'<details class="case" data-block="{a["approved_block"]}"><summary>{cid} · {a["approved_block"]} · {esc(a["evidence"]["input"])}</summary><p>{esc(a["translation_es"])}</p><div class="cols">')
 for r in rr:
  parts.append(f'<section><h3>{r["model"]}: {labels[r["strict_task_fulfillment"]]}</h3><p>{esc(r["decision_basis"] or r["proposed_review"]["review_notes"])}</p>')
  if r['exception']:parts.append('<p><strong>Excepción aceptada:</strong> '+esc(r['exception'])+'</p>')
  parts.append('<p>Dictamen previo: '+esc(r['prior_review']['task_fulfillment'])+'</p><pre>'+esc(json.dumps(r['evidence']['goals_pred'],ensure_ascii=False,indent=2))+'</pre>')
  plan='\n'.join(f"{s['step']}: {s['action']} {s['params']}" for s in r['evidence']['plan'] or [])
  parts.append('<pre>'+esc(plan or r['evidence']['message'] or r['evidence']['error'])+'</pre><small>'+esc(r['run_id'])+'</small></section>')
 parts.append('</div></details>')
parts.append('''<script>function filter(){let n=0;const b=document.querySelector('#block').value,q=document.querySelector('#q').value.toLowerCase();document.querySelectorAll('.case').forEach(e=>{e.hidden=!!((b&&e.dataset.block!==b)||!e.textContent.toLowerCase().includes(q));if(!e.hidden)n++});document.querySelector('#count').textContent=n+' de 60 órdenes'}document.querySelector('#block').onchange=filter;document.querySelector('#q').oninput=filter;filter()</script></html>''')
(OUT/'index.html').write_text('\n'.join(parts))
for p,h in trace['campaign_inventory'].items():assert sha(ROOT/p)==h
consumer=Path('/home/sergio/Justina/src/Executor/executor_tools/src/AnalyzePerson.cpp')
dump(OUT/'trazabilidad.json',{'date':'2026-10-22','previous_review_sha256':sha(source),'script_sha256':sha(Path(__file__)),'campaigns_unchanged':True,'campaign_inventory':trace['campaign_inventory'],'consumer_inspected':str(consumer),'consumer_sha256':sha(consumer),'outputs':{p.name:sha(p) for p in OUT.iterdir() if p.is_file() and p.name not in ['trazabilidad.json','generar_reporte.py']}})
print(json.dumps(ss,ensure_ascii=False,indent=2))
