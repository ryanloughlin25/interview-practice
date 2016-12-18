def overlapping_ranges(ranges):
    result = sorted(ranges, key=lambda range: range[0])
    if len(result) < 2:
        return result
    i = 1
    while i < len(result):
        previous = result[i-1]
        current = result[i]
        if previous[1] < current[0]:
            i += 1
        elif previous[0] <= current[0] and previous[1] >= current[1]:
            # subset or repeat
            result[i-1] = (
                min(previous[0], current[0]),
                max(previous[1], current[1]),
            )
            result.pop(i)
        elif previous[0] < current[0] and previous[1] < current[1]:
            # overlap or touching
            result[i-1] = (
                min(previous[0], current[0]),
                max(previous[1], current[1]),
            )
            result.pop(i)
        else:
            i += 1
    return result
