def find_range_set(ranges):
    if not ranges:
        return []
    ranges.sort(key=lambda x: x[0])
    current_start = ranges[0][0]
    current_end = ranges[0][1]
    merged_ranges = []
    for interval in ranges[1:]:
        if interval[0] > current_end:
            merged_ranges.append([current_start, current_end])
            current_start = interval[0]
            current_end = interval[1]
        else:
            current_end = interval[1]
    merged_ranges.append([current_start, current_end])
    return merged_ranges
