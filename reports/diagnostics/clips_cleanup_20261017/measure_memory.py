import sys,json,importlib.util,gc
from pathlib import Path
from experiments.common import INITIAL_STATE
from experiments.symbolic import SymbolicPlanner
import psutil
if sys.argv[1]=='before':
 spec=importlib.util.spec_from_file_location('experiments.old_symbolic',str(Path(__file__).with_name('symbolic_before.py')));m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);SymbolicPlanner=m.SymbolicPlanner
p=SymbolicPlanner(['experiments/vendor/goals_planning.clp']);_,facts=p.adapt(['go(cabinet)','find(mug, kind=object)','take(mug)','deliver(mug, to=me)'])
samples=[]
for i in range(1,3001):
 p.extract(p.plan(facts,INITIAL_STATE))
 if i in (1,100,500,1000,2000,3000):
  gc.collect();samples.append({'iterations':i,'rss_bytes':psutil.Process().memory_info().rss,'clips_mem_used':int(p.env.eval('(mem-used)'))})
p.close();del p;gc.collect()
print(json.dumps({'mode':sys.argv[1],'iterations':3000,'samples':samples}))
