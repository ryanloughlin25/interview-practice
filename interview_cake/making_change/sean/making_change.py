def find_num_combos(coins, max_val):
    if max_val < 0:
        raise RuntimeError("Target value must be > 0")
    if not coins:
        raise RuntimeError(
            "Coins must contain at least one non-zero denomination"
        )
    values = [0]*(max_val + 1)
    values[0] = 1
    val = 0
    while val <= max_val:
        for coin in coins:
            prev_val = val - coin
            if prev_val < 0:
                continue
            values[val] += values[prev_val]
        val += 1
    return values[max_val]


if __name__ == '__main__':
    find_num_combos([1,2,3], 4)
