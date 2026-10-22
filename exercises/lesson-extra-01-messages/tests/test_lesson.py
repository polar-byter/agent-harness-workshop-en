import json
import unittest
from decisions import build_decision_messages, RULES


class MessagesTests(unittest.TestCase):
    def test_task_and_events_keep_their_values(self):
        events = [{'tool': 'find_notes', 'result': ['Returns are accepted within 14 days.']}]
        messages = build_decision_messages('Find the return clauses in the policy', events)
        self.assertEqual(messages[0], {'role': 'developer', 'content': RULES})
        self.assertEqual(messages[1]['role'], 'user')
        self.assertEqual(json.loads(messages[1]['content']),
                         {'task': 'Find the return clauses in the policy', 'events': events})
        self.assertIn('Find', messages[1]['content'])
        self.assertEqual(events[0]['result'], ['Returns are accepted within 14 days.'])

    def test_initial_history_can_be_empty(self):
        self.assertEqual(json.loads(build_decision_messages('Task', [])[1]['content'])['events'], [])
