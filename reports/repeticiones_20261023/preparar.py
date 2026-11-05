"""Preparar, sin inferencias, cuatro repeticiones con las condiciones históricas."""
from pathlib import Path
import json,sys,hashlib
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT))
from experiments.campaign import initialize,load_campaign
OUT=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
entries=[]
for model in ['qwen3b','qwen7b','gpt']:
 old=ROOT/'reports/experiments'/f'{model}_piloto_60_01'
 # Rechaza diferencias en código, paquetes, manifiesto o artefactos históricos.
 m=load_campaign(old);c=m['configs'][0]
 new=ROOT/'reports/experiments'/f'{model}_repeticiones_60_20261023'
 kwargs=dict(inputs=old/'assets/entradas.jsonl',conditions=[c['architecture']],references=old/'assets/referencias.jsonl',repetitions=4,order_seed=20261023,request_timeout=c['timeouts_seconds']['model_request'],total_timeout=c['timeouts_seconds']['total'],response_schema=old/'assets/response_schema.json')
 if model=='gpt':kwargs.update(model=c['model'],prompt=old/c['prompt']['path'],gpt_parameters=c['generation'])
 else:kwargs.update(planning_timeout=c['timeouts_seconds']['planning'],metadata_file=old/c['qwen']['metadata']['path'])
 n=load_campaign(new) if new.exists() else initialize(new,**kwargs)
 assert n['schedule']['repetitions']==4 and n['configs'][0]['config_id']==c['config_id'], 'Configuración distinta'
 entries.append(dict(model=model,baseline=str(old.relative_to(ROOT)),new_campaign=str(new.relative_to(ROOT)),baseline_manifest_sha256=sha(old/'manifest.json'),new_manifest_sha256=sha(new/'manifest.json'),config_id=c['config_id'],local_to_global_repetition={str(i):i+1 for i in range(1,5)},new_expected_runs=240))
(OUT/'protocolo.json').write_text(json.dumps(dict(date='2026-10-23',status='prepared_not_executed',additional_runs=720,gpt_additional_requests=240,total_with_baseline=900,baseline_repetition=1,first_attempts_only=True,automatic_retries=0,seed=20261023,configs=entries,gpt_snapshot_caveat='Mismo identificador de modelo y parámetros explícitos no garantizan pesos idénticos del servicio entre fechas. Analizar nuevas repeticiones también separadas de la primera.'),ensure_ascii=False,indent=2)+'\n')
print('Preparadas tres campañas, 240 ensayos adicionales cada una; ninguna consulta a modelos.')
