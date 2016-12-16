import unittest


class BuyStocksSolver:
    def solve_stocks(self, price_list):
        if not price_list:
            return 0
        interval = self.find_interval(price_list)
        profit = price_list[interval[1]] - price_list[interval[0]]
        return max(profit, 0)

    def find_interval(self, price_list):
        if len(price_list) <= 3:
            return self.base_case(price_list)
        left_list, right_list = self.split_list(price_list)
        left_sol = self.find_interval(left_list)
        right_sol = self.find_interval(right_list)
        result = self.combine_solutions(
            left_sol,
            right_sol,
            left_list,
            right_list
        )
        return result
    
    def base_case(self, price_list):
        if len(price_list) == 2:
            return [0,1]
        a = price_list[1] - price_list[0]
        b = price_list[2] - price_list[0]
        c = price_list[2] - price_list[1]
        m = max(a, b, c)
        if a == m:
            return [0, 1]
        elif b == m:
            return [0, 2]
        else:
            return [1, 2]

    def combine_solutions(self, left_sol, right_sol, left_list, right_list):
        left_profit = left_list[left_sol[1]] - left_list[left_sol[0]]
        right_profit = right_list[right_sol[1]] - right_list[right_sol[0]]
        
        left_min = min(left_list)
        right_max = max(right_list)
        combined_profit = max(right_list) - min(left_list)

        max_profit = max(left_profit, right_profit, combined_profit)
        if left_profit == max_profit:
            return left_sol
        elif right_profit == max_profit:
            right_sol = [
                len(left_list) + right_sol[0],
                len(left_list) + right_sol[1],
            ]
            return right_sol
        else:
            left_ind = left_list.index(left_min)
            right_ind = len(left_list) + right_list.index(right_max)
            return [left_ind, right_ind]

    def split_list(self, lst):
        mid = len(lst) // 2
        left_list = lst[:mid]
        right_list = lst[mid:]
        return left_list, right_list


class TestBuyStocks(unittest.TestCase):
    def setUp(self):
        self.solver = BuyStocksSolver()

    def test_split_list_even(self):
        left, right = self.solver.split_list([0,1,2,3,4,5,6,7])
        self.assertEqual(left, [0,1,2,3])
        self.assertEqual(right, [4,5,6,7])

    def test_split_list_odd(self):
        left, right = self.solver.split_list([0,1,2,3,4])
        self.assertEqual(left, [0,1])
        self.assertEqual(right, [2,3,4])

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
