def find_pairs(nums, target):
    # no duplicates
    seen = set([])
    pairs = set([])
    for num in nums:
        seen.add(num)
    for num in nums:
        compliment = target - num
        pair = (num, compliment)
        reversed_pair = (compliment, num)
        if compliment in seen and reversed_pair not in pairs:
            pairs.add(pair)
    output_list = [tuple(pair) for pair in pairs]
    return output_list
