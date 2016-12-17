def get_longest_length(string):
    """
    :type s: str
    :rtype: int
    """
    char_dict = {}
    max_len = 0
    j = 0
    i = 0
    while j < len(string):
        char = string[j]
        if char in char_dict and char_dict[char] >= i:
            i = char_dict[char] + 1
            char_dict[char] = j
            max_len = max(max_len, j - i + 1)
            j += 1
        else:
            char_dict[char] = j
            max_len = max(max_len, j - i + 1)
            j += 1
    return max_len
