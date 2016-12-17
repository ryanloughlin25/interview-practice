import unittest
from median_of_arrays import Solution


class MedianOfTwoSortedArraysTestCase(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_empty_arrays(self):
        array1 = []
        array2 = []
        self.assertEqual(self.sol.findMedianSortedArrays(array1, array2), None)

    def test_array1_one_number(self):
        array1 = [5]
        array2 = []
        self.assertEqual(self.sol.findMedianSortedArrays(array1, array2), 5)

    def test_array2_one_number(self):
        array1 = []
        array2 = [5]
        self.assertEqual(self.sol.findMedianSortedArrays(array1, array2), 5)

    def test_two_single_numbers(self):
        array1 = [4]
        array2 = [3]
        self.assertEqual(self.sol.findMedianSortedArrays(array1, array2), 3.5)

    def test_short_asymmetric_arrays(self):
        array1 = [1,3]
        array2 = [2]
        self.assertEqual(self.sol.findMedianSortedArrays(array1, array2), 2)

    def test_even_array1(self):
        array1 = [1,2,3,4]
        array2 = []
        self.assertEqual(self.sol.findMedianSortedArrays(array1, array2), 2.5)

    def test_even_array2(self):
        array1 = []
        array2 = [1,2,3,4]
        self.assertEqual(self.sol.findMedianSortedArrays(array1, array2), 2.5)

    def test_odd_array1(self):
        array1 = [1,2,3,4,5]
        array2 = []
        self.assertEqual(self.sol.findMedianSortedArrays(array1, array2), 3)

    def test_odd_array2(self):
        array1 = []
        array2 = [1,2,3,4,5]
        self.assertEqual(self.sol.findMedianSortedArrays(array1, array2), 3)

    def test_two_disjoint_even_arrays(self):
        array1 = [1,2]
        array2 = [3,4]
        self.assertEqual(self.sol.findMedianSortedArrays(array1, array2), 2.5)

    def test_overlapping_uneven_arrays(self):
        array1 = [1,2]
        array2 = [1,2,3]
        #import pdb;pdb.set_trace()
        self.assertEqual(self.sol.findMedianSortedArrays(array1, array2), 2)

if __name__ == '__main__':
    unittest.main()