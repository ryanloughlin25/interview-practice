def find_intersection(rectangle_1, rectangle_2):
    rect_1 = find_corners_and_edges(rectangle_1)
    rect_2 = find_corners_and_edges(rectangle_2)

def 

def find_corners_and_edges(rectangle):
    left_edge = rectangle['left_x']
    bottom_edge = rectangle['bottom_x']
    right_edge = left_edge + rectangle['width']
    top_edge = bottom_edge + rectangle['height']
    bl_corner = (left_edge, bottom_edge)
    tl_corner = (left_edge, top_edge)
    br_corner = (right_edge, bottom_edge)
    tr_corner = (right_edge, top_edge)

    new_dict = {
        'l_edge': left_edge,
        'r_edge': right_edge,
        't_edge': top_edge,
        'b_edge': bottom_edge,
        'bl_corner': bl_corner,
        'br_corner': br_corner,
        'tl_corner': tl_corner,
        'tr_corner': tr_corner,
    }
    return new_dict
