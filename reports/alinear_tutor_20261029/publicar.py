from pathlib import Path
import hashlib,json,shutil,subprocess
P=Path(__file__).resolve().parent
trace=json.loads((P/'trazabilidad.json').read_text())
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
for lang,info in trace.items():
 assert sha(Path(info['source'])/'articulo.tex')==info['tex_sha256'],'El original cambió'
 log=(P/lang/'articulo.log').read_text(errors='replace')
 assert 'Output written' in log and 'Overfull' not in log and 'undefined' not in log
 text=subprocess.check_output(['pdftotext',str(P/lang/'articulo.pdf'),'-'],text=True)
 assert '??' not in text and 'general porpoise' not in text
 assert 'Sergio Cano <sergio081096@gmail.com>' in text
 assert ('50 %' in text or '50%' in text)
for lang,info in trace.items():
 info['published']={}
 for name in ['articulo.tex','articulo.pdf','figures/virbot_general.pdf','figures/virbot_ros2.pdf']:
  target=Path(info['source'])/name;shutil.copy2(P/lang/name,target);info['published'][name]=sha(target)
(P/'publicacion.json').write_text(json.dumps(trace,ensure_ascii=False,indent=2)+'\n')
print('Versiones publicadas con imágenes originales, correos originales y tres correcciones acordadas.')
