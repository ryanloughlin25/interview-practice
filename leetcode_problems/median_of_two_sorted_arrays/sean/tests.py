import unittest
from median_of_arrays import find_median


class MedianOfTwoSortedArraysTestCase(unittest.testcase):
    def test_empty_arrays(self):
        array1 = []
        array2 = []
        self.assertEqual(self.find_median(array1, array2), None)

    def test_one_array_one_number(self):
        array1 = [5]
        array2 = []
        self.assertEqual(self.find_median(array1, array2), 5)
