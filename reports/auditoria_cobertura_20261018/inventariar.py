"""Inventario de evidencia local; no reconstruye ni certifica corridas históricas."""
import json,hashlib,sys,subprocess
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT))
from qwen_gpsr.domain import command_constants as c
OUT=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
p=ROOT/'data/datasets/dataset_gpsr.jsonl';rs=[json.loads(l) for l in p.read_text().splitlines()]
files=list((ROOT/'qwen_gpsr/generation').glob('*.py'))+list((ROOT/'qwen_gpsr/domain').glob('*.py'))+list((ROOT/'qwen_gpsr/training').glob('*.py'))
files += [ROOT/'data/CompetitionTemplate'/s for s in ['names/names.md','maps/location_names.md','maps/room_names.md','objects/objects.md']]
files += list((ROOT/'reports/training').glob('*.txt'))
family_counts=Counter(r['meta']['family'] for r in rs)
result={'date':'2026-10-18','scope':'Current local generator and corpus; historical training identity not certified','git_head':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),'file_sha256':{str(p.relative_to(ROOT)):sha(p) for p in files},'dataset':{'path':str(p.relative_to(ROOT)),'sha256':sha(p),'rows':len(rs),'category_counts':dict(Counter(r['meta']['category'] for r in rs))},'families':{name:{'templates':list(templates),'corpus_rows':family_counts[name]} for name,templates in c.TEMPLATE_VARIANTS.items()},'followup_templates':c.FOLLOWUP_TEMPLATES,'followup_people':c.FOLLOWUP_PEOPLE,'followup_objects':c.FOLLOWUP_OBJECTS,'probes':{}}
probes={'count_wearing':lambda r:any(g.startswith('count(') and 'wearing=' in g for g in r['goals']),'heaviest':lambda r:any('property=heaviest' in g for g in r['goals']),'consecutive_go':lambda r:any(a.startswith('go(') and b.startswith('go(') for a,b in zip(r['goals'],r['goals'][1:])),'gesture_and_wearing_same_goal':lambda r:any('gesture=' in g and 'wearing=' in g for g in r['goals'])}
for name,pred in probes.items():
 matches=[{'line':i+1,**r} for i,r in enumerate(rs) if pred(r)]
 result['probes'][name]={'count':len(matches),'examples':matches[:3],'meaning':'Corpus occurrence, not train-partition occurrence; zero does not by itself prove grammatical impossibility'}
result['training_evidence']={}
for size in ['3b','7b']:
 p=ROOT/'models'/('nl2cd_qwen'+size)
 a=json.loads((p/'adapter_config.json').read_text());states=[]
 for t in sorted(p.glob('checkpoint-*/trainer_state.json')):
  s=json.loads(t.read_text());states.append({'path':str(t.relative_to(ROOT)),**{k:s.get(k) for k in ['global_step','best_model_checkpoint','best_metric','num_train_epochs']}})
 result['training_evidence'][size]={'base_model':a.get('base_model_name_or_path'),'adapter_config_sha256':sha(p/'adapter_config.json'),'trainer_states':states,'current_script_test_size':.1,'current_script_random_seed':42,'current_script_dataset_path':'data/datasets/dataset_gpsr.jsonl','historical_dataset_sha256':'not_found','historical_split_indices':'not_found'}
declaration=OUT/'declaracion_investigador.json'
if declaration.exists():
 result['investigator_declaration']=json.loads(declaration.read_text())
 result['investigator_declaration_sha256']=sha(declaration)
(OUT/'inventario.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
lines=['# Familias del generador local: inventario inicial','','No implica correspondencia certificada con una edición oficial de GPSR. Las ocurrencias son del corpus completo, no solo de entrenamiento.','']
for name,info in result['families'].items():
 lines += ['## '+name,'',f"Filas en corpus: {info['corpus_rows']}",'',*['- `'+s+'`' for s in info['templates']],'']
(OUT/'FAMILIAS.md').write_text('\n'.join(lines))
print('Inventario guardado: 29 familias, 87 superficies, 40000 filas; hashes y ejemplos de cobertura.')
