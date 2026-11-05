"""Native lifetime regression: capture C-level diagnostics in a child process."""
import subprocess
import sys
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]


class ClipsCleanupTests(unittest.TestCase):
    def test_repeated_extraction_and_explicit_close(self):
        script = r'''
from experiments.symbolic import SymbolicPlanner
from experiments.common import INITIAL_STATE
for cycle in range(3):
    planner = SymbolicPlanner(['experiments/vendor/goals_planning.clp'])
    _, facts = planner.adapt(['go(cabinet)', 'find(mug, kind=object)',
                             'take(mug)', 'deliver(mug, to=me)'])
    first = None
    for i in range(100):
        result = planner.extract(planner.plan(facts, INITIAL_STATE))
        if first is None:
            first = result
        assert result == first, 'Plan or evidence changed between resets'
        assert result[1]['planning_done']
        assert result[0][-1]['params'] == ['task completed']
    planner.close()
    planner.close()
    assert planner.env is None
print('cleanup-ok')
'''
        result = subprocess.run([sys.executable, '-c', script], cwd=REPO,
                                capture_output=True, text=True, timeout=60)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(result.stdout.strip(), 'cleanup-ok', result.stdout + result.stderr)
        self.assertEqual(result.stderr, '')
