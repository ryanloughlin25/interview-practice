import unittest
from highest_product import find_three

class HighestProductTestCase(unittest.TestCase):
    def test_3_ints(self):
        integers = [3,4,5]
        target = 60
        result = find_three(integers)
        self.assertEqual(result, target)

    def test_all_same_ints(self):
        integers = [2,2,2,2,2,2,2,2]
        target = 8
        result = find_three(integers)
        self.assertEqual(result, target)

    def test_increasing_ints(self):
        integers = [1,2,3,4,5]
        target = 60
        result = find_three(integers)
        self.assertEqual(result, target)

    def test_decreasing_ints(self):
        integers = [5,4,3,2,1]
        target = 60
        result = find_three(integers)
        self.assertEqual(result, target)

    def test_random_ints(self):
        integers = [5,3,1,4,2]
        target = 60
        result = find_three(integers)
        self.assertEqual(result, target)

    def test_repeating_highest(self):
        integers = [1,2,5,3,5,4,5,5,5]
        target = 125
        result = find_three(integers)
        self.assertEqual(result, target)

    def test_repeating_middle(self):
        integers = [1,2,4,3,4,4,5,4]
        target = 80
        result = find_three(integers)
        self.assertEqual(result, target)

    def test_repeating_lowest(self):
        integers[1,4,5,3,2,3,3,3]
        target = 60
        result = find_three(integers)
        self.assertEqual(result, target)


if __name__ == '__main__':
    unittest.main()
