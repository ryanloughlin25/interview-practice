import operator
import functools

def find_three(integers):
    if len(integers) <= 3:
        return functools.reduce(operator.mul, integers, 1)
    highest = [0,0,0]
    lowest = [0,0,0]
    num_pos = num_neg = num_zer = 0
    for num in integers:
        lowest.append(num)
        highest.append(num)
        highest.remove(min(highest))
        lowest.remove(max(lowest))
        if num > 0:
            num_pos += 1
        elif num < 0:
            num_neg += 1
        else:
            num_zer += 1
    if num_pos < 3:
    return functools.reduce(operator.mul, highest, 1)
