"""Reproduce el análisis local del piloto; no consulta modelos ni cambia campañas."""
import csv
import hashlib
import html
import json
import statistics
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from experiments.campaign import load_campaign
from experiments.symbolic import SymbolicPlanner
from experiments.common import INITIAL_STATE

OUT = Path(__file__).resolve().parent
NAMES = {'Qwen3B': 'qwen3b_piloto_60_01', 'Qwen7B': 'qwen7b_piloto_60_01', 'GPT': 'gpt_piloto_60_01'}
COLORS = ['#2166ac', '#d6604d', '#5e3c99']
GOALS = ['go','find','take','deliver','place','guide','follow','count','tell','save','greet','answer_question']
def digest(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def readlines(path): return [json.loads(l) for l in path.read_text().splitlines() if l.strip()]
def writejson(name, value): (OUT/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
def ops(plan):
    return [(s['action'],[p.replace('_',' ') for p in s['params']] if s['action']=='say' else s['params'])
            for s in plan or [] if s['step']>=1001]
def goalset(value): return {g.split('(',1)[0].strip() for g in value or []}
def med(values): return statistics.median(values) if values else None

data = {}; manifests = {}; refs = {}; provenance = {}
for label, name in NAMES.items():
    folder = ROOT/'reports/experiments'/name
    manifest = load_campaign(folder)  # Integrity, source and artifact checks; no HTTP.
    manifests[label] = manifest
    rows = readlines(folder/'resultados.jsonl')
    first = {}
    for row in rows:
        key = (row['case_id'], row['repetition'])
        if key not in first or row['attempt'] < first[key]['attempt']: first[key] = row
    assert len(first)==60 and all(r['attempt']==1 and r['repetition']==1 for r in first.values())
    data[label] = {r['case_id']:r for r in first.values()}
    refrows = readlines(folder/manifest['references']['path'])
    assert len(refrows)==60 and all(r['reference_status']=='approved' for r in refrows)
    if not refs: refs = {r['id']:r for r in refrows}
    else: assert refs == {r['id']:r for r in refrows}
    assert all(refs[k]['input']==r['input_original'] for k,r in data[label].items())
    provenance[label] = {'campaign': name, 'campaign_id':manifest['campaign_id'],
        'manifest_sha256':digest(folder/'manifest.json'), 'result_sha256':digest(folder/'resultados.jsonl'),
        'inputs_sha256':manifest['inputs']['sha256'], 'references_sha256':manifest['references']['sha256'],
        'config':manifest['configs'][0], 'first_started_at_utc':min(r['started_at_utc'] for r in first.values()),
        'last_finished_at_utc':max(r['finished_at_utc'] for r in first.values())}
assert len({m['inputs']['sha256'] for m in manifests.values()})==1
assert manifests['Qwen3B']['software']['source_inventory']==manifests['Qwen7B']['software']['source_inventory']==manifests['GPT']['software']['source_inventory']
assert manifests['Qwen3B']['configs'][0]['clips_rules']==manifests['Qwen7B']['configs'][0]['clips_rules']

# Diagnostic reference expansion only: not invented official control trials/timings.
config = manifests['Qwen3B']['configs'][0]
planner = SymbolicPlanner([ROOT/'reports/experiments'/NAMES['Qwen3B']/r['path'] for r in config['clips_rules']])
control = {}
try:
    for cid, ref in refs.items():
        if ref['goals_ref'] is None: continue
        adapted, facts = planner.adapt(ref['goals_ref'])
        plan, details = planner.extract(planner.plan(facts, INITIAL_STATE))
        control[cid] = {'goals':ref['goals_ref'],'adapted':adapted,'facts':facts,'plan':plan,'details':details}
finally: planner.close()
writejson('control_diagnostico.json',{'scope':'Local reference expansion; no official run IDs or timing/resource claims','cases':control})

NOTES = {
'DEV-001':'Composición de dos desplazamientos: Qwen7B busca inspection point como objeto. Qwen3B y GPT conservan las visitas.',
'DEV-002':'Qwen7B devuelve HTTP 422 con tareas añadidas y texto tras el JSON. Composición, clasificación exploratoria posterior a observar resultados.',
'DEV-003':'Qwen7B busca inspection point como objeto. Conservar como diagnóstico de composición.',
'DEV-024':'GPT desactiva focus antes de Please follow me to entrance; la interacción aún no ha terminado. No detectado por el contrato estructural.',
'DEV-029':'Qwen7B sustituye orange por orange coat; cambia el objeto solicitado.',
'DEV-049':'Dos atributos personales: Qwen3B los mezcla, Qwen7B omite vestimenta, GPT rechaza por límite del ejecutor. La referencia aprobada espera executable; el rechazo es explícito, no cumplimiento. El control tampoco garantiza ambos atributos.',
'DEV-050':'Los objetivos conservan vestimenta (con variante singular/plural); los planes no expresan el filtro rojo y ejecutan count_person. Igualdad con control no demuestra cumplimiento.',
'DEV-051':'Los tres planes usan biggest_fruit y anuncian heaviest_category. Se conserva heaviest en objetivos, pero tamaño no demuestra peso. Caso de capacidad, no éxito automático.',
'DEV-052':'GPT omite instruct_follow_to_bedroom y solo anuncia I will follow Simone to bedroom. Aun con la clave, la ejecución física del seguimiento no queda verificada.',
'DEV-053':'Qwen3B deja la taza en bed en vez de entregarla. Qwen7B y GPT conservan las dos entregas. La causa por longitud/composición no está demostrada.',
'DEV-054':'El control convierte Water en búsqueda de persona pese a kind=object. Qwen3B/7B usan water como objeto y GPT mantiene Water como objeto. No penalizar por no copiar el defecto del control.',
'DEV-055':'Falta objeto: Qwen usa it/item; GPT pide aclaración.',
'DEV-056':'Falta destino: Qwen usa destination; GPT pide aclaración.',
'DEV-057':'Falta destinatario: 3B usa her, 7B HTTP 422; GPT pide aclaración.',
'DEV-058':'Volar/inspeccionar: Qwen sustituye por ir/buscar; GPT rechaza. Aproximación no equivale a cumplimiento.',
'DEV-059':'Termostato: ambos Qwen devuelven HTTP 422 con caracteres posteriores y set fuera del repertorio; GPT rechaza.',
'DEV-060':'Contradicción tomar/no tomar: ambos Qwen devuelven HTTP 422; GPT rechaza por contradicción.'}
metrics = {}; cases = []; confusion = {}; response_confusion = {}
expected_categories = ['executable','clarification','rejected','domain_capability_review']
observed_categories = ['plan','clarification','rejected','error','timeout']
for label, rows in data.items():
    values = list(rows.values()); applicable=[r for r in values if refs[r['case_id']]['goals_ref'] is not None]
    plans = [r for r in values if r['response_kind']=='plan' and r['plan'] is not None]
    times = [r['timing']['total_ms']/1000 for r in values]
    internal = [r['resources']['model_internal'] for r in values if r['resources']['model_internal']['status']=='available']
    rss = [r['rss_peak_sampled_bytes']/2**20 for r in internal if r.get('rss_peak_sampled_bytes') is not None]
    gpu = [max(d['allocated_peak_sampled_bytes'] for d in r['gpu']['devices'])/2**30 for r in internal if r.get('gpu',{}).get('status')=='available' and r['gpu'].get('devices')]
    clients = [r['resources']['client'] for r in values if r['resources']['client']['status']=='available']
    m = {'attempts':len(values),'execution_counts':dict(Counter(r['execution_status'] for r in values)),
         'response_counts':dict(Counter(r['response_kind'] or 'none' for r in values)),
         'plans':len(plans),'valid_plan_contract':sum(r['validation']['plan_contract_valid'] is True for r in values),
         'exact_goals':{'numerator':sum(r['goals_pred']==refs[r['case_id']]['goals_ref'] for r in applicable),'denominator':len(applicable)},
         'exact_control_plans':{'numerator':sum(r['plan']==control[r['case_id']]['plan'] for r in applicable),'denominator':len(applicable)},
         'normalized_control_operations':{'numerator':sum(r['plan'] is not None and ops(r['plan'])==ops(control[r['case_id']]['plan']) for r in applicable),'denominator':len(applicable)},
         'latency_seconds':{'mean':statistics.mean(times),'median':med(times),'p95':float(np.percentile(times,95)), 'min':min(times),'max':max(times),'includes_errors':True},
         'client_peak_rss_MiB_median':med([r['rss_peak_sampled_bytes']/2**20 for r in clients if r.get('rss_peak_sampled_bytes') is not None]),
         'model_internal':{'status':'no disponibles' if label=='GPT' else 'available' if internal else 'unavailable','sampled_records':len(internal), 'peak_rss_MiB_median':med(rss),'gpu_allocated_peak_GiB_median':med(gpu)},
         'formal_task_fulfillment':'pending_human_review'}
    if label=='GPT':
        m['provider_tokens']={key:sum((r.get('gpt',{}).get('usage') or {}).get(key,0) or 0 for r in values) for key in ['input_tokens','output_tokens','total_tokens','cached_input_tokens']}
        m['returned_models']=dict(Counter(r['gpt'].get('returned_model') for r in values))
    metrics[label]=m
    eligible=[r for r in applicable if r['execution_status']=='completed' and r['goals_pred'] is not None]
    # Missing/invalid responses excluded, not silently converted to all-negative predictions.
    confusion[label]={'eligible_cases':len(eligible),'excluded_cases':[r['case_id'] for r in applicable if r not in eligible], 'counts':{}}
    for goal in GOALS:
        counts=dict(TP=0,FP=0,FN=0,TN=0)
        for r in eligible:
            expected=goal in goalset(refs[r['case_id']]['goals_ref']); predicted=goal in goalset(r['goals_pred'])
            counts['TP' if expected and predicted else 'FN' if expected else 'FP' if predicted else 'TN']+=1
        confusion[label]['counts'][goal]=counts
    matrix=np.zeros((len(expected_categories),len(observed_categories)),dtype=int)
    for cid,r in sorted(rows.items()):
        ref=refs[cid]; kind=r['response_kind'] if r['execution_status']=='completed' else r['execution_status']
        matrix[expected_categories.index(ref['expected_status']),observed_categories.index(kind)]+=1
        entry={'model':label,'case_id':cid,'intent_id':ref['intent_id'],'block':ref['block'],'input':r['input_original'],
               'expected_status':ref['expected_status'],'observed_response':kind,'execution_status':r['execution_status'],
               'plan_contract_valid':r['validation']['plan_contract_valid'],'goals_literal_match':r['goals_pred']==ref['goals_ref'] if ref['goals_ref'] is not None else None,
               'plan_exact_match_to_control':r['plan']==control[cid]['plan'] if cid in control else None,
               'operations_match_to_control':ops(r['plan'])==ops(control[cid]['plan']) if cid in control and r['plan'] is not None else None,
               'total_seconds':r['timing']['total_ms']/1000,'note':NOTES.get(cid,''),'run_id':r['run_id'],'attempt':r['attempt']}
        cases.append(entry)
    response_confusion[label]=matrix.tolist()
summary={'scope':'Development pilot; descriptive paired comparison, first attempts, one repetition; no physical evaluation',
         'date':'2026-10-17','unique_orders':60,'independent_intent_groups':28,'metrics':metrics,'goal_presence_confusion':confusion,
         'response_confusion':{'expected':expected_categories,'observed':observed_categories,'matrices':response_confusion},'provenance':provenance,
         'limitations':['Development data used to tune prompt','Known corpus overlaps; audit does not prove semantic independence or inspect unknown GPT pretraining','Single repetition; formulations within intent are dependent','Different generation budgets and structured-output mechanisms','Sequential blocks; hardware warmup and external API conditions not controlled','Control may contain adaptation/capability defects','No final human-reviewed task success rate']}
writejson('resumen_comparativo.json',summary);writejson('comparacion_por_caso.json',cases)
with (OUT/'comparacion_por_caso.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(cases[0]));w.writeheader();w.writerows(cases)

plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})
def save(fig,name):
    fig.savefig(OUT/(name+'.png'),dpi=170,bbox_inches='tight');fig.savefig(OUT/(name+'.svg'),bbox_inches='tight');plt.close(fig)
fig,axes=plt.subplots(1,2,figsize=(12,4))
responses=['plan','clarification','rejected','error'];bottom=np.zeros(3)
for kind,color in zip(responses,['#4c9f70','#4385be','#d99a32','#c54a4a']):
    v=[sum(1 for r in data[label].values() if (r['response_kind'] if r['execution_status']=='completed' else r['execution_status'])==kind) for label in NAMES]
    axes[0].bar(list(NAMES),v,bottom=bottom,label=kind,color=color)
    for j,n in enumerate(v):
        if n:axes[0].text(j,bottom[j]+n/2,str(n),ha='center',va='center',color='white')
    bottom+=v
axes[0].set(title='Respuesta observada (60 órdenes)',ylabel='Casos');axes[0].legend(fontsize=8)
x=np.arange(3);vals=[metrics[n]['exact_goals']['numerator'] for n in NAMES]
axes[1].bar(x,vals,color=COLORS);axes[1].set(xticks=x,xticklabels=list(NAMES),ylim=(0,60),title='Coincidencia literal de objetivos (54 aplicables)',ylabel='Casos')
for i,n in enumerate(vals):axes[1].text(i,n+1,f'{n}/54',ha='center')
fig.suptitle('Descriptivos; ninguna barra representa éxito semántico total');fig.tight_layout();save(fig,'01_resultados')
fig,ax=plt.subplots(figsize=(8,4));times=[[r['timing']['total_ms']/1000 for r in data[n].values()] for n in NAMES]
ax.boxplot(times,tick_labels=list(NAMES),showmeans=True)
for i,v in enumerate(times):ax.scatter(np.full(len(v),i+1)+np.linspace(-.10,.10,len(v)),v,s=10,alpha=.45,color=COLORS[i])
ax.set(title='Tiempo total por solicitud: incluye errores; una pasada',ylabel='Segundos');fig.tight_layout();save(fig,'02_tiempos')
fig,axes=plt.subplots(1,2,figsize=(11,4))
for ax,key,title,unit in [(axes[0],'peak_rss_MiB_median','RAM del proceso servidor','MiB'),(axes[1],'gpu_allocated_peak_GiB_median','GPU asignada por PyTorch','GiB')]:
    for i,n in enumerate(NAMES):
        value=metrics[n]['model_internal'][key]
        if value is not None:ax.bar(i,value,color=COLORS[i]);ax.text(i,value,f'{value:.2f}',ha='center',va='bottom')
        else:ax.text(i,.5,'No disponibles',transform=ax.get_xaxis_transform(),ha='center',rotation=90)
    ax.set(xticks=range(3),xticklabels=list(NAMES),ylabel=unit,title=title,xlim=(-.6,2.6))
fig.suptitle('Mediana de picos muestreados por solicitud; excluye carga y espera en cola');fig.tight_layout();save(fig,'03_recursos')
fig,axes=plt.subplots(1,3,figsize=(15,4.8),sharey=True)
for ax,label in zip(axes,NAMES):
    mat=np.array(response_confusion[label]);ax.imshow(mat,cmap='Blues',vmin=0,vmax=60)
    ax.set(xticks=range(5),xticklabels=observed_categories,yticks=range(4),yticklabels=expected_categories,title=label,xlabel='Respuesta observada')
    ax.tick_params(axis='x',rotation=45)
    for (i,j),n in np.ndenumerate(mat):ax.text(j,i,str(n),ha='center',va='center',color='white' if n>30 else 'black')
axes[0].set_ylabel('Respuesta prevista en ficha');fig.suptitle('Matriz de respuestas: discrepancia no equivale por sí sola a error semántico');fig.tight_layout();save(fig,'04_matriz_respuestas')
fig,axes=plt.subplots(1,3,figsize=(12,7),sharey=True)
for ax,label in zip(axes,NAMES):
    mat=np.array([[confusion[label]['counts'][g][k] for k in ['TP','FP','FN','TN']] for g in GOALS]);ax.imshow(mat,cmap='Blues',vmin=0,vmax=54,aspect='auto')
    ax.set(xticks=range(4),xticklabels=['TP','FP','FN','TN'],yticks=range(12),yticklabels=GOALS,title=f"{label}: n={confusion[label]['eligible_cases']}")
    for (i,j),n in np.ndenumerate(mat):ax.text(j,i,str(n),ha='center',va='center',color='white' if n>27 else 'black')
fig.suptitle('Confusión binaria por presencia de objetivo; no evalúa argumentos, orden ni multiplicidad\n54 referencias aplicables; respuestas fallidas excluidas y declaradas');fig.tight_layout();save(fig,'05_confusion_objetivos')
# A compact 60x3 map uses categories of evidence, never an invented pass/fail judgment.
fig,ax=plt.subplots(figsize=(7,15));grid=[]
for cid in sorted(refs):
    vals=[]
    for n in NAMES:
        r=data[n][cid];ref=refs[cid]
        vals.append(0 if r['execution_status']!='completed' else 1 if r['response_kind']!='plan' else 2 if ref['goals_ref'] is None else 4 if r['goals_pred']==ref['goals_ref'] else 3)
    grid.append(vals)
from matplotlib.colors import ListedColormap
ax.imshow(grid,cmap=ListedColormap(['#c54a4a','#7b6aaf','#dcac57','#70a7ce','#37745b']),vmin=-.5,vmax=4.5,aspect='auto')
ax.set(xticks=range(3),xticklabels=list(NAMES),yticks=range(60),yticklabels=sorted(refs),title='Evidencia por orden (no es matriz de éxito)')
from matplotlib.patches import Patch
ax.legend(handles=[Patch(color=c,label=t) for c,t in zip(['#c54a4a','#7b6aaf','#dcac57','#70a7ce','#37745b'],['Error técnico','Aclaración/rechazo','Plan sin referencia aplicable','Objetivos distintos literalmente','Objetivos iguales literalmente'])],loc='upper left',bbox_to_anchor=(1,1),fontsize=8)
fig.tight_layout();save(fig,'06_matriz_casos')

# Static self-contained report with filterable paired case details; no CDN or service.
esc=lambda v:html.escape(str(v))
md=['# Comparativo exploratorio: piloto de 60 órdenes','',
'Fecha del informe: 17 de octubre de 2026. Tres condiciones, 60 órdenes, 28 grupos de intención y una repetición: **180 primeros intentos**. No es la evaluación final ni una evaluación física.','',
'## Resultados observados','',
'| Indicador | Qwen3B | Qwen7B | GPT |','|---|---:|---:|---:|']
for title,fn in [('Procesamientos completados',lambda m:str(m['execution_counts'].get('completed',0))+'/60'),('Planes / aclaraciones / rechazos',lambda m:' / '.join(str(m['response_counts'].get(k,0)) for k in ['plan','clarification','rejected'])),('Errores técnicos',lambda m:str(m['execution_counts'].get('error',0))),('Planes con contrato válido',lambda m:f"{m['valid_plan_contract']}/{m['plans']}"),('Objetivos literales iguales',lambda m:f"{m['exact_goals']['numerator']}/54"),('Planes exactamente iguales al control',lambda m:f"{m['exact_control_plans']['numerator']}/54"),('Operaciones iguales al control, normalizando espacios de say',lambda m:f"{m['normalized_control_operations']['numerator']}/54"),('Tiempo total medio (s)',lambda m:f"{m['latency_seconds']['mean']:.3f}"),('Tiempo total mediano (s)',lambda m:f"{m['latency_seconds']['median']:.3f}"),('Tiempo total p95 (s)',lambda m:f"{m['latency_seconds']['p95']:.3f}")]:
    md.append('| '+title+' | '+' | '.join(fn(metrics[n]) for n in NAMES)+' |')
md += ['', 'Los tiempos incluyen fallos. Los denominadores 54 excluyen las seis fichas sin objetivos aplicables; incluyen el diagnóstico de peso y los demás límites. Ninguna coincidencia equivale automáticamente a cumplimiento. No se puntúa null == null como acierto.','',
'## Interpretación','',
'GPT maneja las tres ambigüedades (DEV-055–057) mediante aclaración y los tres rechazos previstos (DEV-058–060) mediante rechazo explícito. También rechaza DEV-049 por la limitación de búsqueda con dos atributos: la ficha esperaba executable; registrar esta discrepancia sin reclasificar retrospectivamente el caso como éxito.','',
'GPT tiene objetivos literales iguales en 52/54 fichas aplicables. Las dos diferencias son el rechazo DEV-049 y el sinónimo biggest en DEV-047. Sus 53 planes pasan el contrato estructural, pero DEV-024 cierra focus antes de acabar la interacción y DEV-052 omite instruct_follow_to_bedroom. Los límites comunes de conteo filtrado y peso también persisten. No se afirma 100 % de éxito.','',
'Qwen3B y 7B tienen igual coincidencia literal (38/54), pero fallan en casos distintos. 3B falla en la doble entrega DEV-053; 7B resuelve esa orden y falla en DEV-001–003 y cambia orange a orange coat en DEV-029. La igualdad del indicador agregado oculta diferencias relevantes.','',
'En esta pasada 7B presenta menor tiempo total medio que 3B. Es una observación del servicio medido, no una ley sobre el tamaño de los modelos: las condiciones se ejecutaron por bloques, sin repeticiones, y no se controlaron calentamiento y carga concurrente.','',
'## Casos que requieren revisión','']
for cid,note in NOTES.items():md.append(f'- **{cid}:** {note}')
md += ['', '## Recursos y tokens','',
'RAM del servidor y GPU asignada por PyTorch son ámbitos distintos del cliente. Los valores de las gráficas son medianas de picos muestreados, no consumo total de la GPU ni energía. El muestreo puede omitir picos breves. CPU/RAM/GPU internos de GPT: **no disponibles**, nunca cero.','',
'GPT informó estos tokens agregados: `'+json.dumps(metrics['GPT']['provider_tokens'])+'`. No se calcula coste monetario sin una tarifa verificada.','',
'## Matrices','',
'- Matriz de respuestas: filas = respuesta prevista; columnas = plan/aclaración/rechazo/error/timeout. El caso domain_capability_review conserva su fila propia.','- Confusión de objetivos: doce tareas binarias de presencia. TP = presente en referencia y predicción; FP = predicho sin referencia; FN = omitido; TN = ausente en ambos. Se excluyen respuestas fallidas, indicando el denominador por modelo. La negativa de GPT en DEV-049 se representa como ausencia de objetivos, no como dictamen semántico.','- Estas matrices no detectan por sí solas argumentos erróneos, multiplicidad, dependencias u orden. Por ejemplo, conservar go pero perder una segunda visita puede pasar inadvertido.','- La matriz por caso describe evidencia, no una tasa de cumplimiento humano.','',
'## Trazabilidad y limitaciones','',
'Los tres conjuntos de entradas y referencias tienen las mismas huellas; las referencias están aprobadas y el inventario de fuentes de los tres clientes coincide. Las reglas CLIPS de ambos Qwen también coinciden. Se verificó la integridad de las campañas antes de analizar. El modelo GPT solicitado fue gpt-5.6-terra, prompt v1.6; los modelos devueltos y parámetros completos constan en resumen_comparativo.json.','',
'Qwen usa do_sample=false, max_new_tokens=128 y repetition_penalty=1.05. GPT usa Structured Outputs, max_output_tokens=8192 y store=false. Son sistemas configurados de manera diferente; no se atribuyen diferencias solamente al tamaño ni a CLIPS.','',
'Este conjunto se usó para desarrollo y cambios de prompt. Existen coincidencias conocidas con el corpus de Qwen; no se auditó aquí de nuevo la procedencia exacta de ambos entrenamientos. Los 60 textos no son 60 intenciones independientes. No se hicieron pruebas de significación ni intervalos que traten paráfrasis como independientes.','',
'La expansión local de las 54 referencias usa las reglas congeladas; queda guardada como control_diagnostico.json. No se inventan registros oficiales ni tiempos de control. Ese control puede contener defectos (Water) y limitaciones, por lo que no sustituye la rúbrica.','',
'La revisión humana final de cumplimiento queda pendiente. Las notas de este informe son diagnósticos exploratorios posteriores a observar las respuestas, no cambios de referencias o categorías oficiales.','',
'## Siguiente paso','',
'Revisar los hallazgos por intención, completar los dictámenes humanos y decidir ajustes como una nueva versión de desarrollo. Después congelar la configuración y preparar un conjunto final independiente, con referencias aprobadas antes de observar resultados. Conservar intactas estas tres campañas.','',
'## Archivos','',
'- index.html: reporte visual local con filtro por ID y comparación de planes.','- 01–06 en PNG/SVG: figuras exportables.','- comparacion_por_caso.csv / .json: 180 registros de comparación.','- resumen_comparativo.json: métricas, matrices, modelos, parámetros y huellas.','- control_diagnostico.json: evidencia de expansión de referencias.','- generar_reporte.py: reproducción local; no consulta modelos.']
(OUT/'INFORME.md').write_text('\n'.join(md)+'\n')
# Render plain Markdown report in an expandable preformatted block plus explicit dashboard.
parts=['<!doctype html><html lang="es"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Piloto de 60 órdenes</title>',
'<style>body{font:16px system-ui;background:#f4f6fa;color:#18243a;margin:0}main{max-width:1200px;margin:auto;padding:28px}h1{font-size:30px}.card,details{background:white;border:1px solid #d9dfeb;border-radius:10px;padding:16px;margin:16px 0}img{max-width:100%;height:auto}table{border-collapse:collapse;width:100%;font-size:14px}td,th{border-bottom:1px solid #ddd;padding:9px;text-align:left;vertical-align:top}pre{white-space:pre-wrap;overflow-wrap:anywhere;font-size:13px}input{padding:12px;width:90%;font-size:16px}summary{cursor:pointer;font-weight:650}.warning{border-left:5px solid #d99a32}.cols{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}@media(max-width:800px){.cols{display:block}}</style><main>',
'<h1>Piloto de 60 órdenes · Comparativo</h1><p>Qwen3B–CLIPS · Qwen7B–CLIPS · GPT directo | 180 primeros intentos | 28 grupos de intención</p>',
'<div class="card warning"><b>Resultados de desarrollo, no evaluación final.</b> Formato válido e igualdad con CLIPS no equivalen a cumplimiento. GPT presenta fallos en focus/seguimiento y comparte límites de capacidad. Recursos internos GPT: no disponibles.</div>',
'<p><a href="INFORME.md">Informe completo</a> · <a href="comparacion_por_caso.csv">CSV por caso</a> · <a href="resumen_comparativo.json">Métricas y trazabilidad</a></p>']
for name in ['01_resultados','02_tiempos','03_recursos','04_matriz_respuestas','05_confusion_objetivos','06_matriz_casos']:
    parts.append(f'<div class="card"><img src="{name}.svg" alt="{name}"><p><a href="{name}.png">PNG</a> · <a href="{name}.svg">SVG</a></p></div>')
parts += ['<h2>Comparador por orden</h2><p>Los avisos son exploratorios; se conservan objetivos y planes sin corregir.</p><input id="filter" placeholder="Buscar: DEV-053, focus, kitchen…" aria-label="Filtrar casos">']
for cid,ref in sorted(refs.items()):
    parts += [f'<details class="case"><summary>{cid} · {esc(ref["input"])}</summary><p>Intención {esc(ref["intent_id"])} · {esc(ref["block"])} · Previsto: {esc(ref["expected_status"])}</p>',f'<p>{esc(NOTES.get(cid,"Sin nota específica; no implica aprobación semántica."))}</p>',f'<pre>Objetivos de referencia: {esc(json.dumps(ref["goals_ref"],ensure_ascii=False,indent=2))}</pre><div class="cols">']
    for label in NAMES:
        r=data[label][cid]
        parts += [f'<section><h3>{label}</h3><p>{esc(r["execution_status"])} / {esc(r["response_kind"])} · {r["timing"]["total_ms"]/1000:.3f} s</p>',f'<p>{esc(r.get("message") or "")}</p>',f'<pre>{esc(json.dumps(r["goals_pred"],ensure_ascii=False,indent=2))}</pre>']
        planlines='\n'.join(f"{s['step']} {s['action']} {' '.join(s['params'])}" for s in r['plan'] or [])
        parts += [f'<pre>{esc(planlines)}</pre><details><summary>Respuesta cruda guardada</summary><pre>{esc(r.get("raw_output"))}</pre></details></section>']
    parts += ['</div></details>']
parts += ['<details><summary>Informe y criterios completos</summary><pre>'+esc('\n'.join(md))+'</pre></details>',"<script>document.getElementById('filter').addEventListener('input',function(){const q=this.value.toLowerCase();document.querySelectorAll('details.case').forEach(el=>el.hidden=!el.textContent.toLowerCase().includes(q));});</script></main></html>"]
(OUT/'index.html').write_text('\n'.join(parts))
assert len(cases)==180
assert {g.split('(',1)[0].strip() for ref in refs.values() for g in ref['goals_ref'] or []} <= set(GOALS)
for label in NAMES:
    assert sum(map(sum,response_confusion[label]))==60
    assert all(sum(c.values())==confusion[label]['eligible_cases'] for c in confusion[label]['counts'].values())
assert metrics['GPT']['model_internal']['peak_rss_MiB_median'] is None
print(json.dumps(metrics,ensure_ascii=False,indent=2))
print('Reporte generado:',OUT/'index.html')
