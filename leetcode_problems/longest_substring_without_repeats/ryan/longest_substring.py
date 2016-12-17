def longest_substring(string):
    substring = ''
    for char in string:
        try:
            index = substring.index(char)
        except ValueError:
            substring += char
        else:
            substring = substring[index+1:] + char

    return substring
