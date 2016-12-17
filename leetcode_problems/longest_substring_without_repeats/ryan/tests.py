import unittest
from longest_substring import longest_substring
from length_of_longest_substring import length_of_longest_substring


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


class LengthOfLongestSubstringTestCase(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(length_of_longest_substring(''), 0)

    def test_only_repeat(self):
        self.assertEqual(length_of_longest_substring('aaa'), 1)

    def test_no_repeat(self):
        self.assertEqual(length_of_longest_substring('abcd'), 4)

    def test_simple_repeat(self):
        self.assertEqual(length_of_longest_substring('1231234'), 4)

    def test_hard_repeat(self):
        self.assertEqual(length_of_longest_substring('dvdf'), 3)

    def test_sean_gave_me(self):
        self.assertEqual(length_of_longest_substring('pwwkew'), 3)


if __name__ == '__main__':
    unittest.main()
