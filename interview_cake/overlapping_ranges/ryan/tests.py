import unittest
from overlapping_ranges import overlapping_ranges


class OverlappingRangesTestCase(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(overlapping_ranges([]), [])

    def test_one_range(self):
        self.assertEqual(overlapping_ranges([(1,2)]), [(1,2)])

    def test_no_overlap(self):
        self.assertEqual(
            overlapping_ranges([(5,8), (9,10), (15,16)]),
            [(5,8), (9,10), (15,16)],
        )

    def test_repeat(self):
        self.assertEqual(
            overlapping_ranges([(1,2), (1,2)]),
            [(1,2)],
        )

    def test_touching(self):
        self.assertEqual(
            overlapping_ranges([(20,21), (3,4), (4,5)]),
            [(3,5), (20,21)],
        )

    def test_subset(self):
        self.assertEqual(
            overlapping_ranges([(10,15), (12,13)]),
            [(10,15)],
        )

    def test_overlap(self):
        self.assertEqual(
            overlapping_ranges([(8,12), (10,17), (15,20)]),
            [(8,20)],
        )

    def test_many(self):
        self.assertEqual(
            overlapping_ranges([(15,16), (16,17), (10, 12), (11, 14), (2, 3), (1, 5), (1, 5)]),
            [(1,5), (10,14), (15,17)],
        )


if __name__ == '__main__':
    unittest.main()
