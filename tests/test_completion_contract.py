"""El cierre no debe aparecer antes de la tarea ni repetirse."""
import unittest

from experiments.validation import plan_issues


def step(number, action, argument):
    return dict(step=number, robot='Justina', action=action, params=[argument])


class CompletionContractTests(unittest.TestCase):
    def test_one_final_completion_is_valid(self):
        self.assertEqual(plan_issues([step(1,'say','I will navigate'),
            step(1001,'go_to','kitchen'), step(1002,'say','task completed')]), [])

    def test_initial_completion_even_with_valid_terminal_is_rejected(self):
        issues=plan_issues([step(1,'say','task completed'),
            step(1001,'go_to','kitchen'), step(1002,'say','task completed')])
        self.assertIn('plan: duplicated completion step', issues)
        self.assertIn('plan: completion must appear only as the final operation', issues)

    def test_only_initial_completion_is_rejected(self):
        issues=plan_issues([step(1,'say','task completed'),step(1001,'go_to','kitchen')])
        self.assertIn('plan: missing completion step', issues)
        self.assertIn('plan: completion must appear only as the final operation', issues)

    def test_operational_duplicate_or_action_after_completion_is_rejected(self):
        for final in (step(1002,'say','task completed'),step(1002,'focus','disable')):
            with self.subTest(final=final):
                self.assertTrue(plan_issues([step(1001,'say','task completed'),final]))
