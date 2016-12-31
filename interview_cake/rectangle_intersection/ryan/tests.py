import unittest
from rectangle import rectangle_intersection


class RectangleIntersectionTestCase(unittest.TestCase):
    def test_no_overlap(self):
        r1 = {
            'left_x': 1,
            'bottom_y': 5,
            'width': 10,
            'height': 4,
        }
        r2 = {
            'left_x': 10,
            'bottom_y': 50,
            'width': 10,
            'height': 4,
        }
        self.assertEqual(rectangle_intersection(r1, r2), None)

    def test_complete_overlap(self):
        r1 = {
            'left_x': 1,
            'bottom_y': 1,
            'width': 10,
            'height': 10,
        }
        r2 = {
            'left_x': 2,
            'bottom_y': 2,
            'width': 2,
            'height': 2,
        }
        self.assertEqual(rectangle_intersection(r1, r2), r2)

    def test_partial_overlap(self):
        r1 = {
            'left_x': 5,
            'bottom_y': 10,
            'width': 10,
            'height': 20,
        }
        r2 = {
            'left_x': 10,
            'bottom_y': 20,
            'width': 30,
            'height': 40,
        }
        expected_intersection = {
            'left_x': 10,
            'bottom_y': 20,
            'width': 5,
            'height': 10,
        }
        self.assertEqual(rectangle_intersection(r1, r2), expected_intersection)


if __name__ == '__main__':
    unittest.main()
