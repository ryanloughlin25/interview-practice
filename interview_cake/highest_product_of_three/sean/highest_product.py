import operator
import functools

def find_three(integers):
    highest = [0,0,0]
    for num in integers:
        highest.append(num)
        highest.remove(min(highest))
    return functools.reduce(operator.mul, highest, 1)
