from pathlib import Path
import json,sys,hashlib
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from experiments.campaign import initialize,load_campaign
OUT=Path(__file__).resolve().parent
old=ROOT/'reports/experiments/gpt_repeticiones_60_20261023'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(old/'manifest.json')==(old/'manifest.sha256').read_text().strip()
m=json.loads((old/'manifest.json').read_text());c=m['configs'][0]
assert not (old/'resultados.jsonl').exists() or not (old/'resultados.jsonl').read_text().strip(), 'La campaña antigua tiene resultados; no preparar duplicados'
for artifact in [m['inputs'],m['references'],c['prompt'],c['response_schema']]:
 assert sha(old/artifact['path'])==artifact['sha256']
new=ROOT/'reports/experiments/gpt_repeticiones_60_pausa_20261023'
n=initialize(new,old/m['inputs']['path'],['gpt_direct'],model=c['model'],references=old/m['references']['path'],repetitions=4,order_seed=m['schedule']['order_seed'],request_timeout=c['timeouts_seconds']['model_request'],total_timeout=c['timeouts_seconds']['total'],prompt=old/c['prompt']['path'],response_schema=old/c['response_schema']['path'],gpt_parameters=c['generation'],gpt_pause_seconds=2)
load_campaign(new)
entry={'date':'2026-10-23','supersedes_unexecuted_campaign':str(old.relative_to(ROOT)),'active_campaign':str(new.relative_to(ROOT)),'previous_manifest_sha256':sha(old/'manifest.json'),'new_manifest_sha256':sha(new/'manifest.json'),'request_policy':n['configs'][0]['request_policy'],'generation_unchanged':n['configs'][0]['generation']==c['generation'],'model':c['model'],'expected_requests':240,'reason':'Ejecutor versionado con pausa fuera de latencia y parada después de guardar HTTP 429. No se modificaron campañas antiguas.','historical_comparability':'Política de envío diferente de R1; reportar esta diferencia, especialmente para latencia/caché.','local_to_global_repetition':{str(i):i+1 for i in range(1,5)}}
(OUT/'transicion.json').write_text(json.dumps(entry,ensure_ascii=False,indent=2)+'\n')
print('Campaña GPT con pausa preparada; 240 ensayos; sin consultas.')
