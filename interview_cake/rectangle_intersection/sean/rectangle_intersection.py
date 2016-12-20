def find_intersection(rectangle_1, rectangle_2):
    rect_1 = find_corners_and_edges(rectangle_1)
    rect_2 = find_corners_and_edges(rectangle_2)


class Rectangle:
    def __init__(self, rectangle_dict):
        self.corners = self.find_corners_and_edges(rectangle_dict)
        self.left_edge = rectangle['left_x']
        self.bottom_edge = rectangle['bottom_x']
        self.right_edge = left_edge + rectangle['width']
        self.top_edge = bottom_edge + rectangle['height']

    def find_corners_and_edges(self, rectangle_dict):
        bl_corner = (self.left_edge, self.bottom_edge)
        tl_corner = (self.left_edge, self.top_edge)
        br_corner = (self.right_edge, self.bottom_edge)
        tr_corner = (self.right_edge, self.top_edge)
        new_dict = {
            (1, 1) : bl_corner,
            (-1, 1) : br_corner,
            (1, -1) : tl_corner,
            (-1, -1) : tr_corner,
        }
        return new_dict

    def find_interior_corners(self, other_rectangle):
        interior_corners = []
        for vector, corner in self.corners.iteritems():
            x_inside = other_rectangle.left_edge < corner[0] < other_rectangle.right_edge
            y_inside = other_rectangle.bottom_edge < corner[1] < other_rectangle.top_edge
            if x_inside and y_inside:
                interior_corners.append(vector)
