import unittest
from unittest.mock import patch
from tests.test_experiments import CampaignFixture
from experiments.campaign import initialize
from experiments.common import append_jsonl, read_jsonl, ExperimentError, utc
from experiments.runner import run_campaign

class FakeWorker:
    status=500
    calls=0
    closed=0
    startup={}
    setup_error=None
    def __init__(self,*args):pass
    def close(self):type(self).closed+=1
    def run(self,record,*args):
        type(self).calls+=1
        record['finished_at_utc']=utc()
        record['execution_status']='error'
        record['error']={'stage':'model_request','type':'APIStatusError','message':'fixture','limit_ms':None}
        record['gpt']={'http_status':self.status}
        record['timing']['total_ms']=100
        return record

class PacingTests(CampaignFixture):
    def prepare(self):
        append_jsonl(self.inputs,{'id':'CASE-2','input':'Go to the office.'})
        FakeWorker.calls=FakeWorker.closed=0
        return initialize(self.campaign,self.inputs,['gpt_direct'],model='fixture',gpt_pause_seconds=2)
    def test_pause_is_outside_trial_and_no_wait_after_last(self):
        m=self.prepare();FakeWorker.status=500
        self.assertEqual(m['configs'][0]['request_policy']['pause_seconds'],2)
        with patch('experiments.runner.time.monotonic',return_value=100),patch('experiments.runner.time.sleep') as sleep:
            self.assertEqual(run_campaign(self.campaign,worker_factory=FakeWorker),(2,2))
        sleep.assert_called_once_with(2)
        self.assertTrue(all(r['timing']['total_ms']==100 for r in read_jsonl(self.campaign/'resultados.jsonl')))
    def test_429_preserved_stops_and_resume_skips_failed(self):
        self.prepare();FakeWorker.status=429
        with self.assertRaisesRegex(ExperimentError,'429'):
            run_campaign(self.campaign,worker_factory=FakeWorker)
        self.assertEqual(FakeWorker.calls,1);self.assertEqual(FakeWorker.closed,1)
        before=read_jsonl(self.campaign/'resultados.jsonl')
        self.assertEqual(len(before),1)
        self.assertEqual(before[0]['gpt']['http_status'],429)
        FakeWorker.status=500
        self.assertEqual(run_campaign(self.campaign,worker_factory=FakeWorker),(1,1))
        after=read_jsonl(self.campaign/'resultados.jsonl')
        self.assertEqual(after[0],before[0]);self.assertNotEqual(after[0]['case_id'],after[1]['case_id'])
    def test_invalid_pause(self):
        for pause in [-1,61,float('nan'),float('inf')]:
            with self.assertRaises(ValueError):
                initialize(self.campaign,self.inputs,['gpt_direct'],model='fixture',gpt_pause_seconds=pause)
