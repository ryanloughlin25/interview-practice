import unittest
from longest_substring_without_repeating_characters import get_longest_length 

class LongestSubstringTestCase(unittest.TestCase):
    def test_empty_string(self):
        string = ''
        self.assertEqual(get_longest_length(string), 0)

    def test_weird_case(self):
        string = 'pwwkew'
        import pdb;pdb.set_trace()
        self.assertEqual(get_longest_length(string), 3)

    def test_optimal_contains_prefix(self):
        string = 'dvdf'
        self.assertEqual(get_longest_length(string), 3)

    def test_longest_starts_with_repeated_char(self):
        string = 'aab'
        self.assertEqual(get_longest_length(string), 2)
    
    def test_single_char(self):
        string = 'x'
        self.assertEqual(get_longest_length(string), 1)

    def test_only_one_char(self):
        string = 'aaaaaaaaaaaa'
        self.assertEqual(get_longest_length(string), 1)

    def test_all_different_char(self):
        string = 'abcdefghij'
        self.assertEqual(get_longest_length(string), 10)

    def test_longest_in_middle(self):
        string = 'bbbdefcc'
        self.assertEqual(get_longest_length(string), 5)

    def test_longest_overlap(self):
        string = 'bbbdefbb'
        self.assertEqual(get_longest_length(string),4)

    def test_multiple_bests(self):
        string = 'abcdeeedcba'
        self.assertEqual(get_longest_length(string), 5)

    def test_best_before_second_best(self):
        string = 'ababababcdeabababcd'
        self.assertEqual(get_longest_length(string), 5)


if __name__ == '__main__':
    unittest.main()
