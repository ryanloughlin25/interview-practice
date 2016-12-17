import unittest
from median_two_sorted_arrays import median_two_sorted_arrays


class MedianTwoSortedArraysTestCase(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(median_two_sorted_arrays([], []), None)

    def test_left_empty(self):
        self.assertEqual(median_two_sorted_arrays([], [1,2,3]), 2)

    def test_right_empty(self):
        self.assertEqual(median_two_sorted_arrays([4,5,6,7,8], []), 6)

    def test_sorted(self):
        self.assertEqual(median_two_sorted_arrays([1,2,3,4], [5,6,7,8]), 4.5)

    def test_sorted_reverse(self):
        self.assertEqual(median_two_sorted_arrays([3,4], [1,2]), 2.5)

    def test_repeat_number(self):
        self.assertEqual(median_two_sorted_arrays([1,1,2], [2,3]), 2)

    def test_only_1_number(self):
        self.assertEqual(median_two_sorted_arrays([4,4,4,4], [4,4,4]), 4)

    def test_almost_only_1_number(self):
        self.assertEqual(median_two_sorted_arrays([2,4,4,4], [4,4,5]), 4)

    def test_same_array(self):
        self.assertEqual(median_two_sorted_arrays([1,2,3], [1,2,3]), 2)

    def test_overlapping(self):
        self.assertEqual(median_two_sorted_arrays([1,2,3], [2,3,4]), 3)

    def test_small_and_large(self):
        self.assertEqual(median_two_sorted_arrays([1,2,3], [10**6, 10**6 + 1, 10**6 + 2]), 500001.5)

    def test_small_and_some_large(self):
        self.assertEqual(median_two_sorted_arrays([1,2,3,4], [3, 10**6, 10**6 + 1, 10**6 + 2]), 3.5)

    def test_interleaved(self):
        self.assertEqual(median_two_sorted_arrays([10,12,14,16], [9,11,13,15]), 12.5)

    def test_interleaved_repeat_number(self):
        self.assertEqual(median_two_sorted_arrays([5,5,7,7], [6,8]), 6.5)

    def test_slightly_interleaved(self):
        self.assertEqual(median_two_sorted_arrays([99, 100, 102], [101, 103]), 101)


if __name__ == '__main__':
    unittest.main()
