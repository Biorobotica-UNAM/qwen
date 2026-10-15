"""Regresiones del protocolo observadas en el piloto; sin consultas a modelos."""
import unittest

from experiments.common import INITIAL_STATE, ROOT
from experiments.symbolic import SymbolicPlanner


class PlanningProtocolTests(unittest.TestCase):
    def setUp(self):
        self.planner = SymbolicPlanner([ROOT/'vendor/goals_planning.clp'])

    def tearDown(self):
        self.planner.close()

    def operations(self, goals):
        _, facts = self.planner.adapt(goals)
        plan, details = self.planner.extract(self.planner.plan(facts, INITIAL_STATE))
        self.assertTrue(details['planning_done'])
        self.assertEqual(details['remaining_goals'], [])
        self.assertEqual(details['diagnostics'], [])
        numbered = [s['step'] for s in plan if s['step'] >= 1001]
        self.assertEqual(numbered, list(range(1001, 1001+len(numbered))))
        return [(s['action'], s['params'][0]) for s in plan if s['step'] >= 1001]

    def test_named_person_and_tell_share_one_continuous_focus(self):
        ops = self.operations(['go(kitchen)', 'find(Jane, kind=person)', 'tell(current_time)'])
        start = ops.index(('find_person', 'anybody'))
        self.assertEqual(ops[start:start+7], [
            ('find_person', 'anybody'), ('focus', 'enable'),
            ('say', 'ask_name'), ('listen', 'guest_name_last'),
            ('say', 'acknowledge_name_last'), ('say', 'current_time'),
            ('focus', 'disable')])

    def test_approach_splits_name_exchange_and_greeting(self):
        ops = self.operations(['find(Jane, kind=person)', 'greet(Jane)'])
        i = ops.index(('approach', 'guest_last'))
        self.assertEqual(ops[i-1:i+4], [('focus', 'disable'), ('approach', 'guest_last'),
            ('focus', 'enable'), ('say', 'greet'), ('focus', 'disable')])

    def test_navigation_and_manipulation_are_boundaries(self):
        for middle in ('go(kitchen)', 'take(cup)'):
            with self.subTest(middle=middle):
                ops = self.operations(['tell(current_time)', middle, 'tell(team_name)'])
                first = ops.index(('say', 'current_time'))
                self.assertEqual(ops[first+1], ('focus', 'disable'))
                if middle.startswith('go'):
                    # Navigation clears the interlocutor; no invented person in kitchen.
                    self.assertEqual(ops.count(('focus', 'enable')), 1)
                else:
                    self.assertEqual(ops.count(('focus', 'enable')), 2)

    def test_general_announcements_and_search_alone_have_no_focus(self):
        for goals in (['go(kitchen)'], ['find(person, kind=person)']):
            with self.subTest(goals=goals):
                self.assertFalse(any(a == 'focus' for a, _ in self.operations(goals)))
        ops = self.operations(['tell(current_time)', 'tell(team_name)'])
        self.assertEqual(ops.count(('focus', 'enable')), 1)
        self.assertEqual(ops.count(('focus', 'disable')), 1)
        self.assertEqual(ops[-1], ('say', 'task completed'))
        self.assertLess(ops.index(('focus', 'disable')), len(ops)-1)

    def test_person_switch_even_when_runtime_source_is_guest_last(self):
        env = self.planner.env
        env.reset()
        env.assert_string('(action-step (step 1001) (action say) (arg "hello") (interlocutor "Jane|guest_last"))')
        env.assert_string('(action-step (step 1002) (action listen) (arg "name") (interlocutor "John|guest_last"))')
        env.eval('(normalize-interactions)')
        steps = sorted((f for f in env.facts() if f.template.name == 'finalized-step'), key=lambda f:f['step'])
        self.assertEqual([(str(f['action']), str(f['arg'])) for f in steps], [
            ('focus', 'enable'), ('say', 'hello'), ('focus', 'disable'),
            ('focus', 'enable'), ('listen', 'name'), ('focus', 'disable')])
        self.assertEqual([f['step'] for f in steps], list(range(1001,1007)))

    def test_reused_visual_person_context_for_follow_and_tell(self):
        ops = self.operations(["find(person, kind=person, gesture='waving person')",
                               'follow(person)', 'tell(current_time)'])
        i = ops.index(('say', 'instruct_follow_only'))
        self.assertEqual(ops[i-1:i+3], [('focus', 'enable'),
            ('say', 'instruct_follow_only'), ('say', 'current_time'), ('focus', 'disable')])

    def test_return_to_operator_does_not_reuse_previous_person(self):
        ops = self.operations(['go(kitchen)', 'find(Jane, kind=person)',
                               'go(instruction_point)', 'tell(name)'])
        i = ops.index(('go_to', 'instruction_point'))
        self.assertEqual(ops[i-1], ('focus', 'disable'))
        j = ops.index(('say', 'saved_name'))
        self.assertEqual(ops[j-1:j+3], [('focus', 'enable'), ('say', 'saved_name'),
                                      ('focus', 'disable'), ('say', 'task completed')])

    def test_compound_rack_and_local_table_have_distinct_surfaces(self):
        ops = self.operations(['go(bed)', 'find(bowl, kind=object)',
                               'take(bowl)', 'place(bowl, at=storage rack)'])
        self.assertIn(('find_space', 'shelf'), ops)
        self.assertLess(ops.index(('go_to', 'storage_rack')), ops.index(('find_space', 'shelf')))
        ops = self.operations(['go(kitchen)', 'find(cup, kind=object)',
                               'take(cup)', 'place(cup, on=table)'])
        self.assertIn(('find_space', 'table'), ops)
        self.assertNotIn(('find_space', 'container_top'), ops)
        self.assertNotIn(('go_to', 'table'), ops)

    def test_full_waving_qualifier_preserves_executor_parameter(self):
        ops = self.operations(['go(corridor)',
            "find(person, kind=person, gesture='waving person')", 'answer_question()'])
        self.assertIn(('find_pose', 'waving_1'), ops)
        self.assertIn(('approach', 'customer_1'), ops)
        self.assertLess(ops.index(('focus', 'enable')), ops.index(('listen', 'answer_question')))
