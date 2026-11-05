"""Consolida evidencia histórica; no consulta modelos ni modifica campañas o dictámenes previos."""
import csv, hashlib, html, json, statistics, difflib
from collections import Counter, defaultdict
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
MODELS = ['Qwen3B', 'Qwen7B', 'GPT']
BLOCKS = 'GLCMAFX'
SOURCES = {
 'Qwen3B': ['qwen3b_piloto_60_01', 'qwen3b_repeticiones_60_20261023'],
 'Qwen7B': ['qwen7b_piloto_60_01', 'qwen7b_repeticiones_60_20261023'],
 'GPT': ['gpt_piloto_60_01', 'gpt_repeticiones_60_pausa_20261023'],
}
PREV = ROOT/'reports/comparativo_revision_investigador_20261022/revision_por_caso.jsonl'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def readl(p): return [json.loads(x) for x in p.read_text().splitlines() if x.strip()]
def dump(name, obj): (OUT/name).write_text(json.dumps(obj, ensure_ascii=False, indent=2)+'\n')
def csvout(name, rows):
 if not rows: return
 with (OUT/name).open('w', newline='', encoding='utf-8-sig') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
def canonical(obj): return json.dumps(obj, sort_keys=True, ensure_ascii=False)
def evidence(r):
 # Text of clarifications/rejections matters. Volatile resource/latency data does not.
 return {k:r.get(k) for k in ['execution_status','response_kind','goals_pred','plan','message']} | {'error_type':(r.get('error') or {}).get('type')}
def stats(vals):
 return {'n':len(vals), 'mean':statistics.mean(vals) if vals else None,
         'median':statistics.median(vals) if vals else None,
         'q25':float(np.percentile(vals,25)) if vals else None,
         'q75':float(np.percentile(vals,75)) if vals else None}
def inventory():
 paths=[p for names in SOURCES.values() for name in names for p in (ROOT/'reports/experiments'/name).rglob('*') if p.is_file()]
 paths += [PREV,ROOT/'reports/comparativo_revision_investigador_20261022/decisiones_investigador.json']
 return {str(p.relative_to(ROOT)):sha(p) for p in paths}
before=inventory()
old={(r['model'],r['case_id']):r for r in readl(PREV)}
records=[]; raw={}; manifests={}; validation=[]
for model,names in SOURCES.items():
 for offset,name in enumerate(names):
  folder=ROOT/'reports/experiments'/name
  manifest=json.loads((folder/'manifest.json').read_text()); manifests[name]=manifest
  mh=sha(folder/'manifest.json')
  assert (folder/'manifest.sha256').read_text().strip().split()[0]==mh
  rr=readl(folder/'resultados.jsonl')
  assert len(rr)==(60 if offset==0 else 240)
  assert all(r['attempt']==1 and r['manifest_sha256']==mh for r in rr)
  def check_assets(v):
   if isinstance(v,dict):
    if isinstance(v.get('path'),str) and v['path'].startswith('assets/') and 'sha256' in v:
     assert sha(folder/v['path'])==v['sha256'],v['path']
    for x in v.values():check_assets(x)
   elif isinstance(v,list):
    for x in v:check_assets(x)
  check_assets(manifest)
  validation.append({'campaign':name,'rows':len(rr),'manifest_sha256':mh,'referenced_asset_hashes_valid':True})
  for r in rr:
   key=(model,r['case_id']); prior=old[key]; rep=r['repetition']+offset
   assert r['input_original']==prior['evidence']['input']
   if offset==0:
    assert r['run_id']==prior['run_id']
    assert evidence(r)==evidence(prior['evidence'])
   same=evidence(r)==evidence(prior['evidence'])
   rec={'model':model,'case_id':r['case_id'],'intent_id':prior['intent_id'],'block':prior['approved_block'],
    'linguistic_variant':prior['linguistic_variant'],'global_repetition':rep,'local_repetition':r['repetition'],
    'campaign':name,'run_id':r['run_id'],'baseline_run_id':prior['run_id'],'input':r['input_original'],
    'translation_es':prior['translation_es'],'execution_status':r['execution_status'],'response_kind':r['response_kind'],
    'strict_fulfillment':prior['strict_task_fulfillment'] if same else 'pending_review',
    'scenario_acceptance':prior['scenario_acceptance'] if same else 'pending_review',
    'domain_response_correct':prior['proposed_review']['domain_response_correct'] if same else None,
    'review_origin':'historical_R1' if offset==0 else ('identical_evidence_to_R1' if same else 'new_variant_pending'),
    'historical_review_status':prior['review_status'],
    'review_notes':prior['proposed_review']['review_notes'] if same else 'Evidencia diferente de R1; requiere dictamen específico.',
    'decision_basis':prior.get('decision_basis') if same else None,'exception':prior.get('exception') if same else None,
    'baseline_strict_fulfillment':prior['strict_task_fulfillment'],
    'total_seconds':r['timing']['total_ms']/1000,'plan_contract_valid':r['validation']['plan_contract_valid'],
    'response_schema_valid':r['validation']['response_schema_valid'],
    'evidence':evidence(r)}
   records.append(rec);raw[r['run_id']]=r
assert len(records)==900 and len(raw)==900
records.sort(key=lambda r:(r['case_id'],MODELS.index(r['model']),r['global_repetition']))
# Apply explicit, versioned variant judgments. Preserve their provenance.
review_source=OUT/'decisiones_variantes.json'
review_decisions=json.loads(review_source.read_text())['decisions']
by_run={rid:d for d in review_decisions for rid in d['run_ids']}
for r in records:
 r['analysis_category']=None
 if r['run_id'] in by_run:
  d=by_run[r['run_id']]
  assert r['strict_fulfillment']=='pending_review'
  r['strict_fulfillment']=d['decision']
  r['scenario_acceptance']='accepted_by_exception' if d['scenario_exception'] else d['decision']
  r['domain_response_correct']=d['domain_response_correct']
  r['review_origin']='assistant_variant_review_under_approved_criteria'
  r['review_notes']=d['note']; r['analysis_category']=d['category']
  r['exception']=old[r['model'],r['case_id']]['exception'] if d['scenario_exception'] else None
assert len(by_run)==70
# Apply the author's explicit scenario decision, retaining the previous judgment.
scenario_source=OUT/'decision_DEV052.json'
scenario_decision=json.loads(scenario_source.read_text())
scenario_runs=set(scenario_decision['run_ids'])
for r in records:
 r['previous_scenario_review']=None
 r['scenario_decision_id']=None
 if r['run_id'] in scenario_runs:
  assert r['case_id']=='DEV-052' and r['strict_fulfillment']=='not_verifiable'
  assert any(step['action']=='say' and step['params']==['instruct_follow_to_bedroom'] for step in r['evidence']['plan'])
  r['previous_scenario_review']={k:r[k] for k in ['strict_fulfillment','review_origin','review_notes','analysis_category']}
  r['strict_fulfillment']='pass';r['scenario_acceptance']='pass'
  r['review_origin']='author_confirmed_scenario_20261024'
  r['review_notes']=scenario_decision['basis'];r['decision_basis']=scenario_decision['basis']
  r['scenario_decision_id']=scenario_decision['decision_id']
  if r['model']=='GPT':r['analysis_category']='protocol_added_confirmed_scenario'
  assert r['exception'] is None
assert len(scenario_runs)==14
assert all(r['strict_fulfillment']=='fail' for r in records if r['model']=='GPT' and r['case_id']=='DEV-052' and r['global_repetition']==1)
groups=defaultdict(list)
for r in records:groups[r['model'],r['case_id']].append(r)
assert len(groups)==180 and all(sorted(r['global_repetition'] for r in rr)==[1,2,3,4,5] for rr in groups.values())
# Relevant configuration fields must remain equal; request pacing is reported separately.
config_checks=[]
for model,names in SOURCES.items():
 a,b=[manifests[n]['configs'][0] for n in names]
 keys=['model','prompt','response_schema','generation','prompt_version'] if model=='GPT' else ['qwen','goal_adapter_sha256','clips_rules','normalizer_sha256','catalogs_sha256']
 comparison={k:a.get(k)==b.get(k) for k in keys}
 # Qwen metadata asset paths/hashes may differ: report any differences rather than hide them.
 config_checks.append({'model':model,'field_equality':comparison,'baseline_policy':a.get('request_policy'),'new_policy':b.get('request_policy')})
summary=[];latencies=[];case_summary=[];resources=[]
for model in MODELS:
 rr=[r for r in records if r['model']==model]
 c=Counter(r['response_kind'] or r['execution_status'] for r in rr)
 summary.append({'model':model,'n':len(rr),**{k:c[k] for k in ['plan','clarification','rejected','error']}})
 for block in ['ALL',*BLOCKS]:
  for phase in ['ALL','R1','R2-R5']:
   ss=[r for r in rr if (block=='ALL' or r['block']==block) and (phase=='ALL' or (r['global_repetition']==1)==(phase=='R1'))]
   for response in ['ALL','plan','clarification','rejected','error']:
    vs=[r['total_seconds'] for r in ss if response=='ALL' or (r['response_kind'] or r['execution_status'])==response]
    if vs:latencies.append({'model':model,'block':block,'phase':phase,'response':response,**stats(vs)})
 for phase in ['R1','R2-R5']:
  ss=[r for r in rr if (r['global_repetition']==1)==(phase=='R1')]
  internal=[raw[r['run_id']]['resources']['model_internal'] for r in ss]
  def values(field):return [x[field] for x in internal if x.get(field) is not None]
  gpu=[sum(d['allocated_peak_sampled_bytes'] for d in (x.get('gpu') or {}).get('devices') or []) / 2**30 for x in internal if (x.get('gpu') or {}).get('devices')]
  resources.append({'model':model,'phase':phase,'internal_status':'no disponibles' if model=='GPT' else 'observables locales',
    'cpu_seconds':stats(values('cpu_seconds')),'rss_peak_GiB':stats([v/2**30 for v in values('rss_peak_sampled_bytes')]),'gpu_allocator_peak_GiB':stats(gpu)})
for (model,cid),rr in groups.items():
 c=Counter(r['strict_fulfillment'] for r in rr)
 case_summary.append({'model':model,'case_id':cid,'block':rr[0]['block'],'intent_id':rr[0]['intent_id'],
  **{k:c[k] for k in ['pass','fail','not_verifiable','not_applicable','pending_review']},
  'unique_goals':len({canonical(r['evidence']['goals_pred']) for r in rr}),
  'unique_plans':len({canonical(r['evidence']['plan']) for r in rr}),
  'unique_response_kinds':len({r['response_kind'] for r in rr}),
  'response_with_plan_runs':sum(r['response_kind']=='plan' for r in rr),
  'accepted_exceptions':sum(r['scenario_acceptance']=='accepted_by_exception' for r in rr)})
blocks=[]
for block in BLOCKS:
 for model in MODELS:
  rr=[r for r in records if r['block']==block and r['model']==model]; c=Counter(r['strict_fulfillment'] for r in rr)
  blocks.append({'block':block,'model':model,'commands':len({r['case_id'] for r in rr}),'runs':len(rr),
   **{k:c[k] for k in ['pass','fail','not_verifiable','not_applicable','pending_review']},
   'exceptions':sum(r['scenario_acceptance']=='accepted_by_exception' for r in rr),
   'domain_response_correct':sum(r['domain_response_correct'] is True for r in rr),
   'domain_response_incorrect':sum(r['domain_response_correct'] is False for r in rr),
   'domain_response_unassessed':sum(r['domain_response_correct'] is None for r in rr)})
# Group review work by unique evidence, never by presumed semantic equivalence.
variants=defaultdict(list)
for r in records:
 if r['run_id'] in by_run:variants[(r['model'],r['case_id'],canonical(r['evidence']))].append(r)
queue=[]
for i,((model,cid,sig),rr) in enumerate(sorted(variants.items()),1):
 prior=old[model,cid]
 queue.append({'variant_id':f'V{i:03d}','model':model,'case_id':cid,'block':rr[0]['block'],
  'global_repetitions':','.join(str(r['global_repetition']) for r in rr),'run_ids':','.join(r['run_id'] for r in rr),
  'baseline_verdict':prior['strict_task_fulfillment'],'decision':rr[0]['strict_fulfillment'],'comment':rr[0]['review_notes'],
  'evidence':json.loads(sig),'baseline_evidence':evidence(prior['evidence']),
  'requirements':prior['reference_requirements'],'baseline_notes':prior['proposed_review']['review_notes']})
linguistic=[]
for model in MODELS:
 intents=defaultdict(list)
 for r in records:
  if r['model']==model:intents[r['intent_id']].append(r)
 for intent,rr in sorted(intents.items()):
  if len({r['case_id'] for r in rr})!=3:continue
  for rep in range(1,6):
   ss=[r for r in rr if r['global_repetition']==rep];c=Counter(r['strict_fulfillment'] for r in ss)
   linguistic.append({'model':model,'intent_id':intent,'block':ss[0]['block'],'global_repetition':rep,'commands':','.join(r['case_id'] for r in ss),
     'pass':c['pass'],'fail':c['fail'],'not_verifiable':c['not_verifiable'],'pending_review':c['pending_review'],
     'all_three_pass':None if c['pending_review'] else c['pass']==3})
cost={'currency':'USD','source':'Importes comunicados por el investigador desde OpenAI Usage; sin verificación independiente de facturas.',
 'baseline':{'requests':60,'usd':0.42},'additional':{'requests':240,'usd':1.65},'total':{'requests':300,'usd':2.07},
 'mean_usd_per_request':0.0069,'scope':'Solo solicitudes de estas campañas GPT, según atribución declarada; no incluye desarrollo ni costes locales.',
 'internal_GPT_resources':None,'internal_GPT_resources_display':'no disponibles'}
usage=[]
for phase in ['R1','R2-R5','ALL']:
 rr=[raw[r['run_id']] for r in records if r['model']=='GPT' and (phase=='ALL' or (r['global_repetition']==1)==(phase=='R1'))]
 keys=['input_tokens','output_tokens','total_tokens','cached_input_tokens','reasoning_tokens']
 usage.append({'phase':phase,'requests':len(rr),'records_with_usage':sum(bool(r['gpt'].get('usage')) for r in rr),**{k:sum((r['gpt'].get('usage') or {}).get(k,0) or 0 for r in rr) for k in keys}})
dump('costo_declarado.json',cost);dump('tokens.json',usage);dump('recursos.json',resources);dump('resumen_por_bloque.json',blocks)
dump('resumen_tecnico.json',summary);dump('comprobaciones.json',{'campaigns':validation,'configuration_comparison':config_checks})
(OUT/'revision_por_ejecucion.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in records))
csvout('revision_por_ejecucion.csv',[{k:v for k,v in r.items() if k!='evidence'} for r in records])
csvout('resumen_por_caso.csv',case_summary);csvout('resumen_por_bloque.csv',blocks);csvout('latencias.csv',latencies);csvout('robustez_tripletas.csv',linguistic)
csvout('variantes_para_revision.csv',[{k:v for k,v in q.items() if k not in ['evidence','baseline_evidence','requirements','baseline_notes']} for q in queue])
dump('variantes_para_revision.json',queue)
# Export standalone publication-compatible plots.
plt.rcParams.update({'font.size':10})
def save(fig,name):
 fig.tight_layout()
 for ext in ['png','pdf','svg']:fig.savefig(OUT/f'{name}.{ext}',dpi=180,bbox_inches='tight')
 plt.close(fig)
fig,ax=plt.subplots(figsize=(8,4));bottom=np.zeros(3)
for k,label,col in [('plan','Plan','#247c9c'),('clarification','Aclaración','#e2b744'),('rejected','Rechazo','#8a65aa'),('error','Error','#cb574b')]:
 v=[r[k] for r in summary];ax.bar(MODELS,v,bottom=bottom,label=label,color=col)
 for i,n in enumerate(v):
  if n:ax.text(i,bottom[i]+n/2,str(n),ha='center',va='center',fontsize=9)
 bottom+=v
ax.set_ylabel('Ensayos (300 por sistema)');ax.set_title('Tipo de resultado; no equivale a cumplimiento');ax.legend(bbox_to_anchor=(1,1));save(fig,'resultados_tecnicos')
fig,axes=plt.subplots(1,2,figsize=(10,4),sharey=True)
for ax,phase in zip(axes,['R1','R2-R5']):
 vals=[[r['total_seconds'] for r in records if r['model']==m and r['block']=='G' and (r['global_repetition']==1)==(phase=='R1')] for m in MODELS]
 ax.boxplot(vals,tick_labels=MODELS,showmeans=True);ax.set_title(f'Bloque G · {phase}');ax.set_ylabel('Latencia total (s), incluidos errores');ax.grid(axis='y',alpha=.2)
save(fig,'latencias_G')
caseids=sorted({r['case_id'] for r in records},key=lambda c:(BLOCKS.index(old['GPT',c]['approved_block']),c))
fig,ax=plt.subplots(figsize=(11,17));matrix=[]
colors={'pass':0,'fail':1,'not_verifiable':2,'not_applicable':3,'pending_review':4}
from matplotlib.colors import ListedColormap
from matplotlib.patches import Patch
for cid in caseids:matrix.append([colors[r['strict_fulfillment']] for m in MODELS for r in groups[m,cid]])
ax.imshow(matrix,aspect='auto',interpolation='nearest',cmap=ListedColormap(['#48a77d','#d86963','#a2a8af','#e5e5e5','#e9bd4c']),vmin=-.5,vmax=4.5)
ax.set_yticks(range(60),[f'{c} · {old["GPT",c]["approved_block"]}' for c in caseids],fontsize=8)
ax.set_xticks(range(15),[f'{m}\nR{n}' for m in MODELS for n in range(1,6)],fontsize=8)
ax.set_title('Dictámenes históricos y revisión de variantes\nCriterio estricto bajo supuestos declarados')
for x in [4.5,9.5]:ax.axvline(x,color='white',lw=3)
labels=['Cumple*','Incumple*','No verificable','No aplicable','Pendiente']
present={r['strict_fulfillment'] for r in records}
handles=[Patch(color=c,label=l) for k,c,l in zip(colors,['#48a77d','#d86963','#a2a8af','#e5e5e5','#e9bd4c'],labels) if k in present]
ax.legend(handles=handles,loc='upper center',bbox_to_anchor=(.5,-.02),ncol=len(handles))
fig.text(.15,.005,'* Criterio histórico bajo supuestos declarados; excepciones separadas en tablas.',fontsize=9)
save(fig,'mapa_revision')
# Static offline viewer: keeps all speech and shows exact differences.
esc=lambda v:html.escape(str(v))

def output_lines(e):
 lines=['Objetivos']
 lines += list(e.get('goals_pred') or ['Sin objetivos generados.'])
 lines += ['', 'Plan o respuesta']
 for step in e.get('plan') or []:
  lines.append(f"{step['step']}: {step['action']} {step['params']!r}")
 if e.get('message'): lines.append(e['message'])
 if e.get('error_type'): lines.append('Error: '+str(e['error_type']))
 if not (e.get('plan') or e.get('message') or e.get('error_type')):
  lines.append('Sin plan ni mensaje registrado.')
 return lines

def render_output(e):
 kind={'plan':'Plan','clarification':'Solicitud de aclaración','rejected':'Rechazo'}.get(e.get('response_kind'),e.get('execution_status') or 'Sin respuesta')
 goals='\n'.join(e.get('goals_pred') or ['Sin objetivos generados.'])
 lines=output_lines(e)
 response='\n'.join(lines[lines.index('Plan o respuesta')+1:])
 return f'<p><strong>Respuesta:</strong> {esc(kind)}</p><h4>Objetivos</h4><pre>{esc(goals)}</pre><h4>Plan o respuesta</h4><pre>{esc(response)}</pre>'

def render_requirements(req):
 labels={'required_subtasks':'Subtareas esperadas','constraints':'Restricciones','verification_limits':'Límites de verificación'}
 return ''.join('<h4>'+esc(labels.get(k,k))+'</h4><ul>'+''.join('<li>'+esc(v)+'</li>' for v in values)+'</ul>' for k,values in req.items() if values)
parts=['''<!doctype html><html lang="es"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Comparación de cinco ejecuciones</title><style>body{font:16px system-ui;max-width:1200px;margin:auto;padding:24px;background:#f4f6f8}details,section{background:white;padding:14px;margin:12px 0}summary{cursor:pointer;font-weight:bold}pre{white-space:pre-wrap;overflow-wrap:anywhere;font-size:13px}img{max-width:100%}table{border-collapse:collapse}td,th{border:1px solid #ccd;padding:8px}input,select{padding:9px}.pending{border-left:5px solid #daa625}.comparison{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px}.comparison section{border:1px solid #dbe1e7;min-width:0}h4{margin-bottom:8px}pre{line-height:1.6}@media(max-width:850px){.comparison{grid-template-columns:1fr}}</style><h1>Comparación de cinco ejecuciones · 900 ensayos</h1><p><strong>Actualización DEV-052:</strong> 14 ejecuciones aceptadas bajo condiciones del escenario confirmadas por el autor. GPT R1 sigue incumpliendo. <a href="decision_DEV052.json">Decisión y registros afectados</a>.</p><p>60 órdenes, cinco ejecuciones por sistema. Evidencia histórica conservada. Revisión de variantes por el asistente bajo criterios acordados; no equivale a nueva aprobación humana por caso.</p><p><a href="INFORME.md">Informe</a> · <a href="variantes_para_revision.csv">Hoja de revisión</a> · <a href="revision_por_ejecucion.csv">900 registros</a> · <a href="resumen_por_bloque.csv">Bloques</a></p><p>Coste GPT declarado: US$0.42 + US$1.65 = US$2.07 (300 solicitudes). Recursos internos GPT: no disponibles.</p><img src="resultados_tecnicos.svg" alt="Tipos de resultado"><img src="latencias_G.svg" alt="Latencias del bloque G"><h2>Variantes analizadas</h2><p>Comparar requisitos, resultado R1 y variante. Registrar decisión y comentario en una copia del CSV; regenerar el reporte no incorpora decisiones editadas. No retirar todas las acciones say: algunas disparan protocolos del ejecutor.</p><label>Buscar <input id="q" placeholder="DEV-049, focus…"></label> <label>Bloque <select id="block"><option value="">Todos</option>'''+''.join(f'<option>{b}</option>' for b in BLOCKS)+'''</select></label><p id="count"></p>''']
for q in queue:
 delta='\n'.join(difflib.unified_diff(output_lines(q['baseline_evidence']),output_lines(q['evidence']),fromfile='R1',tofile=q['variant_id'],lineterm=''))
 parts.append(f'<details class="variant pending" data-block="{q["block"]}"><summary>{q["variant_id"]} · {q["case_id"]} · {q["block"]} · {q["model"]} · R{q["global_repetitions"]}</summary><p>{esc(old[q["model"],q["case_id"]]["evidence"]["input"])}</p><p>{esc(old[q["model"],q["case_id"]]["translation_es"])}</p>{render_requirements(q["requirements"])}<p><strong>Dictamen de la variante: {esc(q["decision"])}.</strong> {esc(q["comment"])}</p><p>Dictamen R1: {esc(q["baseline_verdict"])}. {esc(q["baseline_notes"])}</p><div class="comparison"><section><h3>Primera ejecución · R1</h3>{render_output(q["baseline_evidence"])}</section><section><h3>Variante · R{q["global_repetitions"]}</h3>{render_output(q["evidence"])}</section></div><details><summary>Ver líneas modificadas (− R1 / + variante)</summary><pre>{esc(delta)}</pre></details></details>')
parts.append('<h2>Las 60 órdenes y sus cinco ejecuciones</h2>')
for cid in sorted(caseids):
 prior=old['GPT',cid]; parts.append(f'<details><summary>{cid} · {prior["approved_block"]} · {esc(prior["evidence"]["input"])}</summary><p>{esc(prior["translation_es"])}</p>')
 for m in MODELS:
  for r in groups[m,cid]:
   parts.append(f'<details><summary>{m} R{r["global_repetition"]}: {r["strict_fulfillment"]} · {r["total_seconds"]:.3f} s</summary><p>{esc(r["review_origin"])} · {esc(r["review_notes"])}<br>{esc(r["decision_basis"] or "")}<br>{esc(r["exception"] or "")}</p>{render_output(r["evidence"])}<small>{esc(r["campaign"])} · {r["run_id"]}</small></details>')
 parts.append('</details>')
parts.append('''<h2>Estado de revisión</h2><img src="mapa_revision.svg" alt="Dictámenes y variantes pendientes"><script>function filter(){let n=0;const b=document.getElementById('block').value,q=document.getElementById('q').value.toLowerCase();document.querySelectorAll('.variant').forEach(e=>{e.hidden=!!((b&&e.dataset.block!==b)||!e.textContent.toLowerCase().includes(q));if(!e.hidden)n++});document.getElementById('count').textContent=n+' variantes visibles'}document.getElementById('q').oninput=filter;document.getElementById('block').onchange=filter;filter()</script></html>''')
(OUT/'index.html').write_text('\n'.join(parts))
pending=sum(r['strict_fulfillment']=='pending_review' for r in records)
md=f'''# Comparación de cinco ejecuciones — 24 de octubre de 2026

## Alcance y estado

Se consolidan 900 primeros intentos: 60 órdenes × cinco ejecuciones × tres sistemas.
Son 60 órdenes y 28 intenciones, no 300 observaciones lingüísticas independientes por modelo.
R1 procede de las campañas iniciales; R2–R5 corresponden a las repeticiones locales 1–4 de las campañas adicionales.
Se usa la campaña GPT con pausa; la campaña preparada anteriormente sin pausa queda excluida.
No se hicieron nuevas consultas ni se modificaron campañas, referencias o prompts. Esta versión incorpora la decisión explícita sobre DEV-052 y es fuente de los artículos actualizados.

El análisis técnico está completo. El cumplimiento conserva el alcance de la revisión histórica:
no convierte dictámenes propuestos por el asistente en aprobaciones humanas.
Se transfieren dictámenes solo cuando estado, tipo de respuesta, objetivos, plan, mensaje y tipo de error coinciden con R1.
Se revisaron **70 ejecuciones**, agrupadas en **{len(queue)} variantes de {len({q['case_id'] for q in queue})} órdenes**, bajo los criterios acordados. La revisión original de variantes fue del asistente. La decisión posterior del autor confirma DEV-052 en las 14 ejecuciones con disparador de seguimiento; el resto conserva su procedencia.
Una variante pendiente no cuenta como fallo ni como acierto; las tablas muestran siempre el denominador completo.

## Decisión del escenario DEV-052

La primera persona encontrada representa a Simone. El ejecutor implementa el caso especial instruct_follow_to_* y sus pasos adicionales. Se acepta el cumplimiento simbólico de 14 ejecuciones, conservando el fallo de GPT R1 que omite ese disparador. Es una condición documentada del escenario, no una excepción que relaje la tarea ni una nueva ejecución física. La decisión y los identificadores figuran en decision_DEV052.json. No quedan dictámenes no verificables en esta versión.

## Resultados técnicos

| Sistema | Ensayos | Plan | Aclaración | Rechazo | Error |
|---|---:|---:|---:|---:|---:|
'''
for s in summary:md+=f'| {s["model"]} | 300 | {s["plan"]} | {s["clarification"]} | {s["rejected"]} | {s["error"]} |\n'
md+='''
Generar un plan no implica cumplir la orden. Un error de ejecución tampoco equivale a un rechazo deliberado.

## Consistencia literal

| Sistema | Órdenes con objetivos distintos | Con planes distintos | Con tipo de respuesta distinto |
|---|---:|---:|---:|
'''
for m in MODELS:
 ss=[s for s in case_summary if s['model']==m]
 md+=f'| {m} | {sum(s["unique_goals"]>1 for s in ss)}/60 | {sum(s["unique_plans"]>1 for s in ss)}/60 | {sum(s["unique_response_kinds"]>1 for s in ss)}/60 |\n'
md+='''
Qwen usa generación sin muestreo según los manifiestos: la repetibilidad observada es coherente con esa configuración.
Los valores nulos de los ensayos fallidos también se repiten; no son planes válidos estables.
GPT cambia objetivos en DEV-028,030,049,050; cambia de rechazo a plan en DEV-049.
La variación literal puede ser inocua o funcional: requiere revisar las variantes. No se eliminan indiscriminadamente
acciones say porque varias activan protocolos. La igualdad literal no demuestra corrección ni ejecución física.

## Cumplimiento por bloque bajo criterios declarados

Criterio estricto bajo supuestos declarados. G es el ámbito aprobado del generador; L extensión léxica,
C composición adicional, M múltiples restricciones, A ambigüedad, F fuera de capacidad y X contradicción.
Los supuestos de identidad/protocolo y las excepciones DEV-050/051 siguen la revisión histórica.
Las excepciones solo se transfieren con evidencia idéntica; no se aplican automáticamente a nuevas variantes.

| Bloque | Sistema | Órdenes | Ensayos | Cumple | Incumple | No verificable | No aplicable | Pendiente | Excepciones* |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
'''
for s in blocks:md+='| '+' | '.join(str(s[k]) for k in ['block','model','commands','runs','pass','fail','not_verifiable','not_applicable','pending_review','exceptions'])+' |\n'
md+='''
* Las excepciones son una lectura adicional del escenario, no una categoría sumable a los dictámenes estrictos.
Consultar ANALISIS_CONSISTENCIA.md para argumentos, redundancias y cambios de redacción. Los dictámenes nuevos de GPT son revisión del asistente con evidencia; no atribuirlos a aprobación manual completa del investigador.
Para A/F/X se conserva además domain_response_correct: aclarar/rechazar adecuadamente se evalúa por separado.

## Robustez lingüística

`robustez_tripletas.csv` agrupa las 16 intenciones con tres formulaciones (14 de G, una de C y una de L),
por sistema y repetición. Las 12 órdenes diagnósticas restantes no se mezclan con estas tripletas.
Contiene cuántas formulaciones cumplen y si las tres cumplen; un grupo con pendientes no se declara robusto.
Cinco repeticiones miden consistencia; no amplían el repertorio lingüístico ni son cinco órdenes nuevas.
Reportar éxito por formulación y tripletas completas, conservando separación por bloque.

## Latencia y recursos

`latencias.csv` separa bloque, fase R1/R2–R5 y tipo de respuesta, con n, media, mediana y cuartiles.
La gráfica compara G e incluye los errores. No interpretar fallos rápidos como mayor eficiencia útil.
Las solicitudes adicionales GPT tienen pausa de dos segundos fuera de la latencia individual;
por eso se presentan también separadas de R1. No atribuir diferencias temporales únicamente al modelo.

| Sistema | Fase | n (G, todos los resultados) | Mediana (s) | Q25–Q75 (s) |
|---|---|---:|---:|---:|
'''
for s in latencies:
 if s['block']=='G' and s['phase']!='ALL' and s['response']=='ALL':md+=f'| {s["model"]} | {s["phase"]} | {s["n"]} | {s["median"]:.3f} | {s["q25"]:.3f}–{s["q75"]:.3f} |\n'
md+='\n| Sistema | Fase | CPU mediana (s) | RAM RSS pico mediano (GiB) | GPU asignador pico mediano (GiB) |\n|---|---|---:|---:|---:|\n'
for s in resources:
 def fmt(stat):return 'no disponibles' if stat['median'] is None else f"{stat['median']:.3f} (n={stat['n']})"
 md+=f"| {s['model']} | {s['phase']} | {fmt(s['cpu_seconds'])} | {fmt(s['rss_peak_GiB'])} | {fmt(s['gpu_allocator_peak_GiB'])} |\n"
md+='''
Los recursos internos GPT figuran como **no disponibles**, nunca cero ni consumo del cliente.
`recursos.json` resume solo mediciones internas disponibles, con n observado; los faltantes no se imputan.
En Qwen, CPU y RAM son del proceso servidor durante inferencia; GPU es el pico muestreado del asignador PyTorch,
no memoria total de la tarjeta, energía, coste monetario ni recursos de toda la arquitectura CLIPS.
Las fases se mantienen separadas para no ocultar diferencias de carga o condiciones de ejecución.

## Coste GPT y tokens

Según los importes comunicados por el investigador desde OpenAI Usage:

| Fase | Solicitudes | Coste declarado | Promedio por solicitud |
|---|---:|---:|---:|
| R1 | 60 | US$0.42 | US$0.007000 |
| R2–R5 | 240 | US$1.65 | US$0.006875 |
| Total | 300 | **US$2.07** | **US$0.006900** |

Son importes declarados para estas campañas, no una estimación por tarifa ni una factura verificada independientemente.
No incluyen desarrollo previo ni representan el coste total de propiedad. No se asigna coste cero a Qwen.
`tokens.json` contiene el uso registrado por fase; cached_input_tokens es subconjunto de entrada y
reasoning_tokens de salida: no sumarlos de nuevo a total_tokens.

## Revisión y presentación en el artículo

Abrir `index.html`: cada variante tiene requisitos, texto español/inglés, diferencias respecto de R1 y evidencia completa.
En una **copia** de `variantes_para_revision.csv`, completar decision (pass, fail, not_verifiable o not_applicable) y comment
con justificación y referencia a requisitos. Para aclaraciones/rechazos, indicar también en comment
si la respuesta ante la limitación es adecuada y por qué; not_applicable no significa respuesta adecuada. Las excepciones deben declararse explícitamente, sin convertirlas en
cumplimiento estricto. Este generador no ingiere decisiones editadas: deben integrarse en una nueva versión del reporte,
conservando fuente, autor y fecha de revisión. No editar los registros originales.

La revisión de variantes se detalla en ANALISIS_CONSISTENCIA.md. Presentar: cumplimiento por bloque; mapa de éxito 0/5 por orden y sistema;
robustez de tripletas; consistencia literal frente a funcional; latencia y recursos; coste declarado.
Conservar los ejemplos de fallos persistentes y variaciones relevantes, sin escoger solo el mejor intento.
Si se calculan intervalos o contrastes, agrupar por intención/orden y mantener el emparejamiento entre sistemas;
no tratar los 900 ensayos como muestras independientes. Esta evaluación de desarrollo no demuestra generalización
sobre un conjunto independiente ni ejecución física en el robot.

## Trazabilidad y reproducción

`comprobaciones.json` registra huellas de manifiestos, activos referenciados y comparaciones de configuración.
`trazabilidad.json` inventaría las seis campañas antes y después y verifica que permanecen intactas.
Es lectura histórica: no certifica reproducibilidad del servicio remoto ni igualdad de pesos detrás de un alias.
No se usa el cargador estricto con el código actual para reejecutar campañas antiguas.

Desde la raíz del repositorio:

```bash
MPLCONFIGDIR=/tmp/matplotlib-comparativo python3 reports/comparativo_escenario_20261024/generar_reporte.py
MPLCONFIGDIR=/tmp/matplotlib-comparativo python3 reports/comparativo_escenario_20261024/completar_analisis.py
```

La regeneración sobrescribe los productos derivados; guardar la hoja de decisiones en un archivo distinto.
Este reporte sirve de fuente para la actualización de los artículos; se conserva la versión previa.
'''
(OUT/'INFORME.md').write_text(md)
assert inventory()==before,'Se modificaron fuentes durante el análisis'
dump('trazabilidad.json',{'source_inventory':before,'sources_unchanged':True,'script_sha256':sha(Path(__file__)), 'variant_decisions_sha256':sha(review_source), 'scenario_decision_sha256':sha(scenario_source),
 'outputs':{p.name:sha(p) for p in OUT.iterdir() if p.is_file() and p.name not in ['trazabilidad.json','generar_reporte.py']},
 'records':900,'pending_runs':pending,'unique_pending_variants':len(queue)})
print(json.dumps({'rows':len(records),'pending_runs':pending,'variants':len(queue),'pending_cases':len({q['case_id'] for q in queue}),'config_checks':config_checks},ensure_ascii=False,indent=2))
