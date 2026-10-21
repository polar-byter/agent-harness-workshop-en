import sys
import unittest
import json
import hashlib
from pathlib import Path
from notes import find_notes, find_notes_alt, read_notes
from journal import write_result
from app import run_search
ROOT = Path(__file__).resolve().parents[1]


class LessonTests(unittest.TestCase):
    def test_contract(self):
        (ROOT / "scratch").mkdir(exist_ok=True)
        path = ROOT / 'scratch' / 'journal.jsonl'
        path.write_text('', encoding='utf-8')
        first = {'query': 'note', 'matches': ['First']}
        self.assertIsNone(write_result(path, first))
        write_result(path, {'query': 'missing', 'matches': []})
        text = path.read_text(encoding='utf-8')
        self.assertTrue(text.endswith('\n'))
        self.assertIn('First', text)
        self.assertEqual([json.loads(line) for line in text.splitlines()], [first, {'query': 'missing', 'matches': []}])


if __name__ == "__main__":
    unittest.main()
