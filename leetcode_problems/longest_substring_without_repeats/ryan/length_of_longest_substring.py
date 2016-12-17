def length_of_longest_substring(string):
    output_length = 0
    char_indexes = {}

    start_index = 0
    for end_index, char in enumerate(string):
        if char in char_indexes:
            start_index = max(char_indexes[char], start_index) + 1
        output_length = max(output_length, end_index - start_index + 1)
        char_indexes[char] = end_index

    return output_length
