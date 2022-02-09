def palindrome_check(string):
    """
    Takes a string as input. Checks if the string is a palindrome (a word that remains the same when you reverse it
    i.e. noon). Returns True when the string is a palindrome, otherwise returns False.
    args:
        :param string: (str) a possible palindrome
    returns:
        :return: (bool) True when the string is a palindrome, otherwise False
    """
    len_s = len(string)
    if len_s in (0, 1):
        return True
    if string[0] == string[-1]:
        return palindrome_check(string[1:-1])
    # only option left is:  string[0] != string[-1]
    return False


print(palindrome_check('noon'))
print(palindrome_check('nomon'))
print(palindrome_check('nomnon'))
