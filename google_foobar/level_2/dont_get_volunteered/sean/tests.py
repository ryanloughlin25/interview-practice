import unittest
from knight_shortest_path import find_path_length, find_moves


class ShortestPathTestCase(unittest.TestCase):
    def test_case_google_1(self):
        src, dest = 19, 36
        target = 1
        result = find_path_length(src, dest)
        self.assertEqual(target, result)

    def test_case_google_2(self):
        src, dest = 0, 1
        target = 3
        result = find_path_length(src, dest)
        self.assertEqual(target, result)

    def test_find_moves_corner(self):
        start = 0
        target = [10, 17]
        result = find_moves(start)
        self.assertItemsEqual(target, result)

    def test_find_moves_10(self):
        start = 10
        target = [0, 16, 4, 20, 25, 27]
        result = find_moves(start)
        self.assertItemsEqual(target, result)

    def test_find_moves_17(self):
        start = 17
        target = [0, 2, 32, 34, 11, 27]
        result = find_moves(start)
        self.assertItemsEqual(target, result)


if __name__ == '__main__':
    unittest.main()
