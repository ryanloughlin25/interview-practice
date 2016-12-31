def range_overlap(range1_start, range1_end, range2_start, range2_end):
    high_range_start = max(range1_start, range2_start)
    low_range_end = min(range1_end, range2_end)

    if high_range_start < low_range_end:
        return high_range_start, low_range_end - high_range_start
    return None

def rectangle_intersection(r1, r2):
    x_overlap = range_overlap(
        r1['left_x'], r1['left_x'] + r1['width'],
        r2['left_x'], r2['left_x'] + r2['width'],
    )
    y_overlap = range_overlap(
        r1['bottom_y'], r1['bottom_y'] + r1['height'],
        r2['bottom_y'], r2['bottom_y'] + r2['height'],
    )
    if x_overlap and y_overlap:
        return {
            'left_x': x_overlap[0],
            'bottom_y': y_overlap[0],
            'width': x_overlap[1],
            'height': y_overlap[1],
        }
    return None
