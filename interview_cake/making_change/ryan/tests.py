import unittest
from making_change import making_change


class MakingChangeTestCase(unittest.TestCase):
    def test_zero_ways(self):
        self.assertCountEqual(making_change(1, [2]), [])

    def test_one_way(self):
        self.assertCountEqual(making_change(3, [3]), [[3]])

    def test_simple(self):
        #import pdb; pdb.set_trace()
        self.assertCountEqual(making_change(2, [1,2]), [[1,1], [2]])

    def test_blah(self):
        self.assertCountEqual(making_change(3, [1,2]), [[1,1,1], [1,2]])

    def test_problem_statement_example(self):
        self.assertCountEqual(
            making_change(4, [1,2,3]),
            [[1,1,1,1], [1,1,2], [1,3], [2,2]],
        )

    def test_amount_not_divisible_by_any_denomination(self):
        self.assertCountEqual(
            making_change(11, [2,3,5]),
            [[2,2,2,2,3], [2,2,2,5], [2,3,3,3], [3,3,5]],
        )


if __name__ == '__main__':
    unittest.main()
