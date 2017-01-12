import unittest
from find_pairs import find_pairs


class FindPairsTestCase(unittest.TestCase):
    def test_simple_case(self):
        numbers = [1,2,3]
        total = 3
        target = [(1, 2)]
        result = find_pairs(numbers, total)
        self.assertCountEqual(result, target)

    def test_zeros(self):
        numbers = [0,0]
        total = 0
        target = [(0, 0)]
        result = find_pairs(numbers, total)
        self.assertCountEqual(result, target)

    def test_negative_numbers(self):
        numbers = [1,2,5,-2,4,-2]
        total = 3
        target = [(1,2), (5, -2)]
        result = find_pairs(numbers, total)
        self.assertCountEqual(result, target)


if __name__ == '__main__':
    unittest.main()
