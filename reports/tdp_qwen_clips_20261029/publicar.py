from pathlib import Path
import hashlib,shutil,json
p=Path(__file__).resolve().parent
dest=Path('/home/sergio/TDP_Justina/sections/current_research/clips.tex')
def sha(f):return hashlib.sha256(f.read_bytes()).hexdigest()
assert sha(dest)==sha(p/'clips_original.tex'),'La sección original cambió durante la edición'
shutil.copy2(p/'clips.tex',dest)
(p/'trazabilidad.json').write_text(json.dumps({'date':'2026-10-29','target':str(dest),'original_sha256':sha(p/'clips_original.tex'),'updated_sha256':sha(dest),'standalone_compilation':'passed; 2 pages'},indent=2)+'\n')
print('Sección actualizada; respaldo y vista previa conservados.')
