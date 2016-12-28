import unittest

from making_money import max_profit, max_profit_faster


class TestMakingMoney(unittest.TestCase):
    def setUp(self):
        self.market_not_open = []
        self.open_price = [5]
        self.zero_profit = [5, 5]
        self.neg_profit = [5, 3, 1]
        self.pos_profit = [1, 3, 5]

    def test_max_profit_n_squared(self):
        zero_profit = max_profit(self.zero_profit)
        self.assertEqual(zero_profit, 0)
        neg_profit = max_profit(self.neg_profit)
        self.assertEqual(neg_profit, 0)
        pos_profit = max_profit(self.pos_profit)
        self.assertEqual(pos_profit, 4)

    def test_max_profit_n(self):
        not_open = max_profit_faster(self.market_not_open)
        self.assertEqual(not_open, 0)
        open_price_profit = max_profit_faster(self.open_price)
        self.assertEqual(open_price_profit, 0)
        zero_profit = max_profit_faster(self.zero_profit)
        self.assertEqual(zero_profit, 0)
        neg_profit = max_profit_faster(self.neg_profit)
        self.assertEqual(neg_profit, 0)
        pos_profit = max_profit_faster(self.pos_profit)
        self.assertEqual(pos_profit, 4)


if __name__ == '__main__':
    unittest.main()
