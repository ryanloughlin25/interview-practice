import unittest
from stocks import buy_stock


class BuyStockTestCase(unittest.TestCase):
    def test_no_prices(self):
        prices = []
        self.assertEqual(buy_stock(prices), 0)

    def test_no_change(self):
        prices = [10, 10, 10, 10, 10]
        self.assertEqual(buy_stock(prices), 0)

    def test_only_decrease(self):
        prices = [50, 40, 30, 20, 10]
        self.assertEqual(buy_stock(prices), 0)

    def test_only_increase(self):
        prices = [10, 20, 30, 40, 50]
        self.assertEqual(buy_stock(prices), 40)

    def test_lowest_before_highest(self):
        prices = [10, 2, 8, 17, 5]
        self.assertEqual(buy_stock(prices), 15)

    def test_lowest_after_highest(self):
        prices = [11, 4, 25, 1, 15]
        self.assertEqual(buy_stock(prices), 21)

    def test_multiple_bests(self):
        prices = [20, 22, 10, 15, 1, 9]
        self.assertEqual(buy_stock(prices), 8)


if __name__ == '__main__':
    unittest.main()
