from code import interact

def find_num_combos(coins, max_val):
    if not coins or max_val < 0:
        raise NotImplementedError
    values = [0]*(max_val + 1)
    values[0] = 1
    val = 0
    while val <= max_val:
        for coin in coins:
            prev_val = val - coin
            if val - coin < 0:
                continue
            values[val] += values[prev_val]
        val += 1
    interact(local=locals())
    return values[max_val]


if __name__ == '__main__':
    find_num_combos([1,2,3], 4)
