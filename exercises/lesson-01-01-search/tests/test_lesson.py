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
    def test_find_notes(self):
        self.check_search(find_notes)

    def test_find_notes_alt(self):
        # The one-line version is an optional part of the lesson.
        try:
            find_notes_alt(['Returns'], 'return')
        except NotImplementedError:
            self.skipTest('find_notes_alt is not finished yet: this task is optional')
        self.check_search(find_notes_alt)

    def check_search(self, function):
        original = ['Returns are accepted within 14 days.', 'Delivery within the city takes 1 day.', 'RETURNED money goes back to the original card.', 'Returns are accepted within 14 days.']
        self.assertEqual(function(original, ' Return '), ['Returns are accepted within 14 days.', 'RETURNED money goes back to the original card.', 'Returns are accepted within 14 days.'])
        self.assertEqual(original, ['Returns are accepted within 14 days.', 'Delivery within the city takes 1 day.', 'RETURNED money goes back to the original card.', 'Returns are accepted within 14 days.'])
        self.assertEqual(function(['Straße'], 'STRASSE'), ['Straße'])
        self.assertEqual(function(['Returns'], 'exchange'), [])
        with self.assertRaises(ValueError):
            function(['Returns'], '   ')


if __name__ == "__main__":
    unittest.main()
