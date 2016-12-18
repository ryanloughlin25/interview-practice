import unittest
from list_product import find_product_list


class ListProductTestCase(unittest.TestCase):
    def test_empty_list(self):
        integers = []
        target = []
        result = find_product_list(integers)
        self.assertEqual(result, target)

    def test_one_number(self):
        integers = [5]
        target = [1]
        result = find_product_list(integers)
        self.assertEqual(result, target)

    def test_all_ones(self):
        integers = [1,1,1,1,1,1,1,1,1]
        target = [1,1,1,1,1,1,1,1,1]
        result = find_product_list(integers)
        self.assertEqual(result, target)

    def test_increasing(self):
        integers = [1,2,3,4,5]
        target = [120,60,40,30,24]
        result = find_product_list(integers)
        self.assertEqual(result, target)

    def test_decreasing(self):
        integers = [5,4,3,2,1]
        target = [24,30,40,60,120]
        result = find_product_list(integers)
        self.assertEqual(result, target)

    def test_random(self):
        integers = [3,6,23,5,1,18]
        target = [12420,6210,1620,7452,37260,2070]
        result = find_product_list(integers)
        self.assertEqual(result, target)

if __name__ == '__main__':
    unittest.main()
