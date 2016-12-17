def median_two_sorted_arrays(left, right):
    if left and right:
        if left[0] > right[0]:
            median_two_sorted_arrays(right, left)
        elif left[-1] <= right[0]:
            return median(left + right)
        else:
            left_left, left_right = halves(left)
            right_left, right_right = halves(right)
            #
    elif not left and not right:
        return
    else:
        return median(left) or median(right)

def median(sorted_list):
    if not sorted_list:
        return
    length = len(sorted_list)
    mid = length // 2
    if length % 2 == 0:
        # even
        return (sorted_list[mid - 1] + sorted_list[mid]) / 2
    else:
        # odd
        return sorted_list[mid]

def halves(seq):
    length = len(seq)
    return seq[:length//2], seq[length//2:]
