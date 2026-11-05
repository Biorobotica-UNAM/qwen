import json,csv,hashlib,collections,statistics
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
P=Path(__file__).resolve().parent
rr=[json.loads(l) for l in (P/'revision_por_ejecucion.jsonl').read_text().splitlines()]
models=['Qwen3B','Qwen7B','GPT'];groups=collections.defaultdict(list)
for r in rr:groups[r['model'],r['case_id']].append(r)
def op(r):
 return [(s['action'],s['params']) for s in r['evidence']['plan'] or [] if s['action']!='say' or not any(str(p).startswith(('I will ','I have ')) for p in s['params'])]
summary=[]
for m in models:
 rows=[r for r in rr if r['model']==m]
 g=[v for (model,cid),v in groups.items() if model==m]
 summary.append({'model':m,'changed_literal_plans':sum(len({json.dumps(r['evidence']['plan'],sort_keys=True) for r in v})>1 for v in g),
 'changed_operational_sequence':sum(len({json.dumps(op(r),sort_keys=True) for r in v})>1 for v in g),
 'G_all5_pass':sum(all(r['strict_fulfillment']=='pass' for r in v) for v in g if v[0]['block']=='G'),
 'G_verdict_changes':sum(len({r['strict_fulfillment'] for r in v})>1 for v in g if v[0]['block']=='G'),
 'AFX_adequate':sum(r['domain_response_correct'] is True for r in rows if r['block'] in 'AFX')})
(P/'consistencia.json').write_text(json.dumps(summary,indent=2)+'\n')
categories=[]
for cat in sorted({r['analysis_category'] for r in rr if r['analysis_category']}):
 rows=[r for r in rr if r['analysis_category']==cat]
 categories.append({'category':cat,'runs':len(rows),'commands':len({r['case_id'] for r in rows}),'cases':sorted({r['case_id'] for r in rows})})
(P/'categorias_variantes.json').write_text(json.dumps(categories,ensure_ascii=False,indent=2)+'\n')
spaces=[{'run_id':r['run_id'],'case_id':r['case_id'],'repetition':r['global_repetition'],'action':s['action'],'params':s['params']} for r in rr if r['model']=='GPT' for s in r['evidence']['plan'] or [] if s['action']!='say' and any(' ' in str(a) for a in s['params'])]
(P/'argumentos_con_espacios.json').write_text(json.dumps(spaces,indent=2)+'\n')
# Standalone bilingual publication figures.
bs=json.loads((P/'resumen_por_bloque.json').read_text())
for lang in ['es','en']:
 es=lang=='es';fig,axes=plt.subplots(1,2,figsize=(11,4.1))
 ax=axes[0];bottom=[0]*3
 for key,label,color in [('pass','Cumple' if es else 'Fulfills','#318b68'),('fail','Incumple' if es else 'Fails','#c75a54'),('not_verifiable','No verificable' if es else 'Not verifiable','#a3aab4')]:
  values=[next(b[key] for b in bs if b['block']=='G' and b['model']==m) for m in models]
  if not any(values):continue  # Hide categories absent from this plot.
  ax.bar(models,values,bottom=bottom,label=label,color=color)
  for i,v in enumerate(values):
   if v:ax.text(i,bottom[i]+v/2,str(v),ha='center',va='center',fontsize=8)
  bottom=[a+b for a,b in zip(bottom,values)]
 ax.set_ylim(0,250);ax.set_title('(a) '+('Cumplimiento en G' if es else 'Fulfillment in G'));ax.set_ylabel('Ejecuciones (46 órdenes × 5)' if es else 'Runs (46 commands × 5)');ax.legend(loc='lower center',fontsize=8)
 ax=axes[1]
 for offset,key,label,col in [(-.18,'changed_literal_plans','Plan literal' if es else 'Literal plan','#477eac'),(.18,'changed_operational_sequence','Secuencia operativa*' if es else 'Operational sequence*','#b38a42')]:
  v=[x[key] for x in summary];ax.bar([i+offset for i in range(3)],v,.34,label=label,color=col)
  for i,n in enumerate(v):ax.text(i+offset,n+.4,str(n),ha='center')
 ax.set_xticks(range(3),models);ax.set_ylim(0,30);ax.set_ylabel('Órdenes con cambios / 60' if es else 'Commands with changes / 60');ax.set_title('(b) '+('Variación entre ejecuciones' if es else 'Variation across runs'));ax.legend(fontsize=8)
 fig.tight_layout()
 for ext in ['pdf','svg','png']:fig.savefig(P/f'comparacion_repeticiones_{lang}.{ext}',dpi=200,bbox_inches='tight')
 plt.close(fig)
 fig,axes=plt.subplots(1,2,figsize=(10,3.7),sharey=True)
 for ax,phase in zip(axes,['R1','R2–R5']):
  vals=[[r['total_seconds'] for r in rr if r['model']==m and r['block']=='G' and (r['global_repetition']==1)==(phase=='R1')] for m in models]
  ax.boxplot(vals,tick_labels=models,showmeans=True);ax.set_title(phase);ax.set_ylabel('Latencia total (s)' if es else 'Total latency (s)');ax.grid(axis='y',alpha=.2)
 fig.tight_layout()
 for ext in ['pdf','png']:fig.savefig(P/f'latencia_repeticiones_{lang}.{ext}',dpi=200,bbox_inches='tight')
 plt.close(fig)
md='''# Consistencia, argumentos y pasos adicionales

Este análisis complementa INFORME.md y registra la revisión del asistente bajo criterios aprobados por el investigador. La revisión mediante IA conserva su procedencia. El 24 de octubre se añadió la confirmación explícita del autor para DEV-052: sus 14 ejecuciones con disparador cumplen bajo condiciones del escenario. GPT R1 conserva el fallo por omisión. No quedan casos no verificables; no se midió ejecución física ni se aprobaron automáticamente otros dictámenes.

## Criterios aplicados

Los argumentos simbólicos se evalúan en su acción: una ubicación go_to requiere su identificador canónico; una frase descriptiva say puede contener espacios. En las 300 respuestas GPT no se observó go_to con instruction point ni otro argumento de navegación con espacios. Las diferencias observadas de esos nombres corresponden a anuncios. No se presentan como errores de ubicación.

La inspección de los argumentos operativos con espacios encontró cuatro pasos de DEV-043/R5, en una sola ejecución: focus enable/focus disable dentro del argumento de focus. El código actual compara enable de forma exacta; focus enable devuelve false y no activa la atención. Es un incumplimiento del contrato, no un fallo físico observado. En DEV-051/R4–R5, heaviest_fruit se interpreta como clase para conteo, no como selección por peso. Ambos casos pasaron el validador estructural registrado.

No se observaron nombres nuevos de acción en estas variantes. El término «instrucción inventada» se concreta aquí como argumento o consulta no admitida para la operación pretendida. No se infiere un error de ejecución solo a partir de la apariencia del texto.

DEV-056/058/059/060 conservan respuestas sin plan y explicaciones adecuadas pese a cambios de redacción. GPT mantiene 30/30 respuestas adecuadas en A/F/X; Qwen 0/30 con el contrato configurado. DEV-049 se distingue: pasa de rechazo prudente en R1 a planes que omiten vestimenta en R2–R5.

## Resultados consolidados

| Sistema | Cumple G / 230 | Incumple | No verificable | Órdenes G que cumplen 5/5 |
|---|---:|---:|---:|---:|
| Qwen3B | 220 | 10 | 0 | 44/46 |
| Qwen7B | 215 | 15 | 0 | 43/46 |
| GPT | 216 | 14 | 0 | 40/46 |

Las excepciones del escenario siguen separadas del cumplimiento estricto: 10, 10 y 8 ejecuciones respectivamente. GPT tiene dos ejecuciones con heaviest_fruit a las que no se extiende la excepción de usar tamaño como proxy de peso. No convertir la aceptación excepcional en equivalencia semántica.

La consistencia literal de planes cambia en 0/60, 0/60 y 24/60 órdenes. Una proyección operativa, que elimina únicamente anuncios say iniciados por I will/I have y la numeración, cambia en 0/60, 0/60 y 9/60. Se preservan instrucciones de diálogo y todas las demás acciones y argumentos. Esta proyección no demuestra equivalencia funcional: cuenta redundancias y cambios de mayúsculas, y no evalúa adecuación de respuestas sin plan. La estabilidad de cumplimiento se informa aparte. GPT alterna dictamen de cumplimiento en cuatro órdenes G (024,030,043,052); 052 pasa de incumple en R1 a cumple bajo las condiciones confirmadas en R2–R5. GPT sigue con 40/46 órdenes que cumplen cinco veces, porque R1 de DEV-052 mantiene el fallo.

Las redundancias de focus y la consulta duplicada del nombre conservan el cumplimiento de las subtareas, pero se etiquetan como desviaciones de protocolo/eficiencia; no se confunden con una secuencia operativa idéntica. DEV-028 omite un objetivo de búsqueda, aunque el plan lo conserva; DEV-030 pierde además la visita a kitchen y sí incumple. DEV-052 añade el disparador de seguimiento. La identidad y el caso especial del ejecutor quedaron confirmados por el autor como condiciones del escenario. Las diez ejecuciones Qwen y cuatro GPT que lo incluyen cumplen; la ejecución GPT R1 que lo omite no cumple.

## Frecuencias de cambios revisados

La tabla siguiente describe las 70 ejecuciones que difieren de R1; no es una taxonomía exhaustiva de todos los fallos en 900 ensayos. Cada fila cuenta ejecuciones y órdenes distintas. Algunas categorías son variaciones aceptables, no errores. Las diferencias observadas no se corrigen en los datos originales.

| Categoría | Ejecuciones | Órdenes |
|---|---:|---:|
'''
for c in categories:md+=f'| {c["category"]} | {c["runs"]} | {c["commands"]} |\n'
md+='''
## Coste y alcance

US$0.42 + US$1.65 = US$2.07 para 300 solicitudes, según declaración del investigador desde Usage; promedio US$0.0069. Recursos internos de GPT: no disponibles. No se usa el cliente como sustituto ni se asigna coste cero a Qwen. Las comparaciones son descriptivas sobre desarrollo; cinco repeticiones no son cinco órdenes independientes.
'''
(P/'ANALISIS_CONSISTENCIA.md').write_text(md)
# Keep viewer directly accessible and display the supplemental analysis.
h=P/'index.html';s=h.read_text();prefix=s[:s.index('<h1>Comparación')];s=s.replace(prefix[prefix.index('<p><a href="ANALISIS_CONSISTENCIA.md"'):], '') if '<p><a href="ANALISIS_CONSISTENCIA.md"' in prefix else s
s=s.replace('<h1>Comparación', '<p><a href="ANALISIS_CONSISTENCIA.md">Criterios, hallazgos y consistencia</a></p><img src="comparacion_repeticiones_es.svg" alt="Cumplimiento y variación entre ejecuciones"><h1>Comparación')
s=s.replace('Registrar decisión y comentario en una copia del CSV; regenerar el reporte no incorpora decisiones editadas.', 'Las decisiones nuevas están documentadas en decisiones_variantes.json; la hoja CSV permite registrar observaciones del investigador.')
h.write_text(s)
t=P/'trazabilidad.json';trace=json.loads(t.read_text());trace['executor_inspection']={}
for name in ['Focus.cpp','Analyze.cpp','Say.cpp','FindObject.cpp']:
 p=Path('/home/sergio/Justina/src/Executor/executor_tools/src')/name
 trace['executor_inspection'][str(p)]=hashlib.sha256(p.read_bytes()).hexdigest()
trace['outputs']={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in P.iterdir() if p.is_file() and p.name!='trazabilidad.json'}
t.write_text(json.dumps(trace,indent=2)+'\n')
print(summary)
