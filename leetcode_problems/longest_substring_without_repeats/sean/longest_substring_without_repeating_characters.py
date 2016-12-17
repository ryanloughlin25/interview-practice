def get_longest_length(string):
    """
    :type s: str
    :rtype: int
    """
    char_dict = {}
    max_len = 0
    j = 0
    while j < len(string):
        char = string[j]
        if char in char_dict:
            char_dict.remove(char)
        else:
            char_dict.add(char)
            max_len = max(max_len, len(char_set))
            j += 1
    return max_len
