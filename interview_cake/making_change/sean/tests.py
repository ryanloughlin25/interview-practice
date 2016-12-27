import unittest
from making_change import find_num_combos


class MakingChangeTestCase(unittest.TestCase):
    def test_zero_ammount(self):
        total = 0
        coins = [1, 2, 3]
        target = 1
        result = find_num_combos(coins, total)
        self.assertEqual(result, target)
    
    def test_negative_ammount(self):
        total = -5
        coins = [1, 2, 3]
        self.assertRaises(RuntimeError, find_num_combos, coins, total)

    def test_no_coins(self):
        total = 5
        coins = []
        self.assertRaises(RuntimeError, find_num_combos, coins, total)

    def test_example_case(self):
        total = 4
        coins = [1, 2, 3]
        target = 4
        #import pdb;pdb.set_trace()
        result = find_num_combos(coins, total)
        self.assertEqual(result, target)


if __name__ == '__main__':
    unittest.main()
