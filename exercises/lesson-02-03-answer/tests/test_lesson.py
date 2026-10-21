import sys
import unittest
import json
import hashlib
from pathlib import Path
from notes import find_notes, find_notes_alt, read_notes
from assistant import build_messages, extract_answer, answer_question
from transport import send_fixture
ROOT = Path(__file__).resolve().parents[1]


class LessonTests(unittest.TestCase):
    def test_contract(self):
        (ROOT / "scratch").mkdir(exist_ok=True)
        calls = []
        def fake_send(messages):
            calls.append(messages)
            return {'status':'completed', 'output':[{'type':'message','content':[{'type':'output_text','text':'Answer'}]}]}
        self.assertEqual(answer_question('Question', ['Note'], fake_send), 'Answer')
        self.assertEqual(calls[0], build_messages('Question', ['Note']))
        self.assertEqual(len(calls), 1)
        self.assertEqual(answer_question('Question', [], fake_send), 'No matching notes.')
        self.assertEqual(len(calls), 1)


if __name__ == "__main__":
    unittest.main()
