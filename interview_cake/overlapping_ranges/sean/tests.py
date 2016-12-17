import unittest
from overlapping_ranges import find_range_set


class OverlappingRangesTestCase(unittest.TestCase):
    def test_empty_list(self):
        ranges = []
        target = []
        result = find_range_set(ranges)
        self.assertEqual(result, target)

    def test_one_range(self):
        ranges = [[4, 15]]
        target = [[4, 15]]
        result = find_range_set(ranges)
        self.assertEqual(result, target)

    def test_example_case(self):
        ranges = [[0, 1], [3, 5], [4, 8], [10, 12], [9, 10]]
        target = [[0, 1], [3, 8], [9, 12]]
        result = find_range_set(ranges)
        self.assertEqual(result, target)

    def test_all_disjoint(self):
        ranges = [[0,1], [10, 15], [20, 25]]
        target = [[0,1], [10, 15], [20, 25]]
        result = find_range_set(ranges)
        self.assertEqual(result, target)

    def test_not_sorted(self):
        ranges = [[10, 12], [0, 1], [9, 10], [3, 5], [4,8]]
        target = [[0, 1], [3, 8], [9, 12]]
        result = find_range_set(ranges)
        self.assertEqual(result, target)

    def test_all_overlapping(self):
        ranges = [[4, 6], [5, 10], [6, 11]]
        target = [[4, 11]]
        result = find_range_set(ranges)
        self.assertEqual(result, target)

    def test_touching(self):
        ranges = [[0, 5], [5, 10], [10, 15]]
        target = [[0, 15]]
        result = find_range_set(ranges)
        self.assertEqual(result, target)

if __name__ == '__main__':
    unittest.main()
