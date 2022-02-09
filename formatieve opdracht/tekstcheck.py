def different_index_strings(string_1, string_2):
    """
    Takes two strings as input. Compares each index of the two strings with each other until it finds two indexes that
    aren't identical. Returns the index on which the difference was found. Returns -1 if the strings are identical
    args:
        :param string_1: (str) a string you want to compare
        :param string_2: (str) a string you want to compare
    returns:
        :return: (int) index of the strings on which the first difference was found
        :return: (int) -1 if the strings are identical
    """
    len_s1 = len(string_1)
    for i in range(len_s1):
        try:
            if string_1[i] != string_2[i]:
                return i
        # if the first string is longer than the second, returns the index where the second string is no longer found.
        except KeyError:
            return i
    # if the second string is longer than the first string, the length of the first string will also be the index where
    # the first string will no longer coincide with the second
    if string_2 > string_1:
        return len_s1
    return -1


first = input('Give a string: ')
second = input('Give another string: ')
print(different_index_strings(first, second))
