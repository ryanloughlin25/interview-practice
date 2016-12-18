import unittest
from highest_product_of_three import highest_product_of_three


class HighestProductOfThreeTestCase(unittest.TestCase):
    def test_only_three(self):
        self.assertEqual(highest_product_of_three([2,3,4]), 24)

    def test_one_positive(self):
        self.assertEqual(highest_product_of_three([-5,-10,-2,-20,2]), 400)

    def test_two_positives(self):
        self.assertEqual(highest_product_of_three([-10,-10,-10,8,8]), 800)

    def test_blah(self):
        self.assertEqual(highest_product_of_three([-2,-2,-2,8,8]), 32)

    def test_all_positive(self):
        self.assertEqual(highest_product_of_three([15,2,3,4,10]), 600)

    def test_one_negative(self):
        self.assertEqual(highest_product_of_three([15,2,3,4,-10,8]), 480)

    def test_two_negatives(self):
        self.assertEqual(highest_product_of_three([-10,10,-10,8,8]), 1000)

    def test_all_negative(self):
        self.assertEqual(highest_product_of_three([-5,-10,-20,-2,-8]), -80)


if __name__ == '__main__':
    unittest.main()
