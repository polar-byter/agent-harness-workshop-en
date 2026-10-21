import unittest
from model_stats import format_usage


class UsageTests(unittest.TestCase):
    def test_zero_and_missing_values_are_different(self):
        self.assertEqual(format_usage({'input_tokens': 10, 'output_tokens': 0, 'cached_tokens': None}),
                         ['Input tokens: 10', 'Output tokens: 0', 'Cached tokens: not reported'])

    def test_absent_fields_are_not_reported(self):
        self.assertEqual(format_usage({}), ['Input tokens: not reported', 'Output tokens: not reported', 'Cached tokens: not reported'])

    def test_source_dictionary_is_unchanged(self):
        stats = {'input_tokens': 10, 'output_tokens': 3, 'cached_tokens': 0}
        before = dict(stats)
        format_usage(stats)
        self.assertEqual(stats, before)


if __name__ == '__main__':
    unittest.main()
