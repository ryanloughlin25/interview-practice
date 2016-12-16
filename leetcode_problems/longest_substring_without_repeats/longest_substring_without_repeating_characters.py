def lengthOfLongestSubstring(string):
    """
    :type s: str
    :rtype: int
    """
    char_set = set()
    max_len = 0
    for i in range(len(string)):
        for char in string[i:]:
            if char in char_set:
                max_len = max(max_len, len(char_set))
                char_set = set()
                break
            else:
                char_set.add(char)
                max_len = max(max_len, len(char_set))
    return max_len
