import unittest


class BuyStocksSolver:
    # dynamic programming solution
    def solve_stocks(self, price_list):
        if not price_list:
            return 0
        max_profit = price_list[1] - price_list[0]
        min_val = min(price_list[:2])
        for i in range(2, len(price_list)):
            value = price_list[i]
            if value < min_val:
                min_val = value
                continue
            if value - min_val > max_profit:
                max_profit = value - min_val
        return max(0, max_profit)


class TestBuyStocks(unittest.TestCase):
    def setUp(self):
        self.solver = BuyStocksSolver()

    def test_solve_stocks_null(self):
        price_list = []
        target = 0
        profit = self.solver.solve_stocks(price_list)
        self.assertEqual(profit, target)

    def test_solve_stocks_1(self):
        price_list = [10, 10, 10, 10, 10]
        target = 0
        profit = self.solver.solve_stocks(price_list)
        self.assertEqual(profit, target)

    def test_solve_stocks_2(self):
        price_list = [50, 40, 30, 20, 10]
        target = 0
        profit = self.solver.solve_stocks(price_list)
        self.assertEqual(profit, target)

    def test_solve_stocks_3(self):
        price_list = [10, 20, 30, 40, 50]
        target = 40
        profit = self.solver.solve_stocks(price_list)
        self.assertEqual(profit, target)

    def test_solve_stocks_4(self):
        price_list = [10, 2, 8, 17, 5]
        target = 15
        profit = self.solver.solve_stocks(price_list)
        self.assertEqual(profit, target)

    def test_solve_stocks_5(self):
        price_list = [11, 4, 25, 1, 15]
        target = 21
        profit = self.solver.solve_stocks(price_list)
        self.assertEqual(profit, target)

    def test_solve_stocks_6(self):
        price_list = [20, 22, 10, 15, 1, 9]
        target = 8
        profit = self.solver.solve_stocks(price_list)
        self.assertEqual(profit, target)


if __name__ == '__main__':
    unittest.main()
