from itertools import combinations


def highest_product_of_three(ints):
    if len(ints) < 6:
        combs = combinations(ints, 3)
    else:
        low_copy = list(ints)
        high_copy = list(ints)

        high_lows = []
        for i in range(3):
            low = min(low_copy)
            high_lows.append(low)
            low_copy.remove(low)
        for i in range(3):
            high = max(high_copy)
            high_lows.append(high)
            high_copy.remove(high)

        combs = combinations(high_lows, 3)
    return max([comb[0] * comb[1] * comb[2] for comb in combs])
