import unittest
from rectangle_intersection import find_intersection


class RectangleIntersectionTestCase(unittest.TestCase):

    def test_same_rectangle(self):
        rectangle1 = {
            'left_x': 1,
            'bottom_y': 2,
            'width': 4,
            'height': 5,
        }
        rectangle2 = {
            'left_x': 1,
            'bottom_y': 2,
            'width': 4,
            'height': 5,
        }
        target = {
            'left_x': 1,
            'bottom_y': 2,
            'width': 4,
            'height': 5,
        }
        result = find_intersection(rectangle1, rectangle2)
        self.assertEqual(result, target)

    def test_disjoint_rectangle(self):
        rectangle1 = {
            'left_x': 1,
            'bottom_y': 2,
            'width': 2,
            'height': 3,
        }
        rectangle2 = {
            'left_x': 10,
            'bottom_y': 20,
            'width': 2,
            'height': 3,
        }
        target = None
        result = find_intersection(rectangle1, rectangle2)
        self.assertEqual(result, target)

    def test_touching_at_one_corner(self):
        rectangle1 = {
            'left_x': 1,
            'bottom_y': 1,
            'width': 2,
            'height': 2,
        }
        rectangle2 = {
            'left_x': 3,
            'bottom_y': 3,
            'width': 2,
            'height': 2,
        }
        target = {
            'left_x': 3,
            'bottom_y': 3,
            'width': 0,
            'height': 0,
        }
        result = find_intersection(rectangle1, rectangle2)
        self.assertEqual(result, target)

    def test_touching_at_one_corner(self):
        rectangle1 = {
            'left_x': 1,
            'bottom_y': 1,
            'width': 2,
            'height': 2,
        }
        rectangle2 = {
            'left_x': 1,
            'bottom_y': 3,
            'width': 2,
            'height': 2,
        }
        target = {
            'left_x': 1,
            'bottom_y': 3,
            'width': 2,
            'height': 0,
        }
        result = find_intersection(rectangle1, rectangle2)
        self.assertEqual(result, target)
