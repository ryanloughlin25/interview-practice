def longest_substring(string):
    substring = ''
    for char in string:
        if char not in substring:
            substring += char
        else:
            index = substring.index(char)
            substring = substring[index+1:] + char

    return substring
