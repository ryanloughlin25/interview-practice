import unittest
from longest_substring import longest_substring


class LongestSubstringTestCase(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(longest_substring(''), '')

    def test_only_repeat(self):
        self.assertEqual(longest_substring('aaa'), 'a')

    def test_no_repeat(self):
        self.assertEqual(longest_substring('abcd'), 'abcd')

    def test_simple_repeat(self):
        self.assertEqual(longest_substring('1231234'), '1234')

    def test_hard_repeat(self):
        self.assertEqual(longest_substring('dvdf'), 'vdf')

    def test_sean_gave_me(self):
        self.assertEqual(longest_substring('pwwkew'), 'kew')


if __name__ == '__main__':
    unittest.main()
