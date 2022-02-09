def encrypt(char, n):
    """
    takes an alphabetic character and a number as input. Converts the character to its ascii value. adds n to the ascii
    value. If this sum will make the new ascii value outside of the latin character range on the ascii table, shifts the
    value to the other side of the range in the ascii table (e.g. 122 (z) + 1 = 97 (a)). Converts the new calculated
    ascii value back to a latin character and returns this character.
    args:
        :param char: (str) a latin (/alpha) character
        :param n: (int) a number that will be the amount of steps the character will shift in the alphabet
        (with char = a (97), an n of 3 will give d (100) )
    returns:
        :return: (str) a latin (/alpha) character
    """
    ascii_value = ord(char)
    temp_ascii = ascii_value + n
    if 65 <= ascii_value <= 90:
        if temp_ascii < 65:
            shifted_char = 91 - (65 - temp_ascii)
        elif temp_ascii > 90:
            shifted_char = 64 + (temp_ascii - 90)
        else:
            shifted_char = temp_ascii
    else:  # 97 <= ascii_value <= 122
        if temp_ascii < 97:
            shifted_char = 123 - (97 - temp_ascii)
        elif temp_ascii > 122:
            shifted_char = 96 + (temp_ascii - 122)
        else:
            shifted_char = temp_ascii
    return chr(shifted_char)


def caeser_cypher():
    """
    asks user for a string and a rotation coefficient. encrypts the given string with a caesar-cypher. The rotation
    coefficient is the amount of steps taken, with steps to the right for a positive rotation coefficient. With a
    negative one, the steps are taken to the left. Prints the encrypted string.
    returns:
        :return: doesn't return anything; string has been gathered, encrypted and printed.
    """
    plain_txt = input('Give text: ')
    try:
        rotation = int(input('Give rotation: '))
    except ValueError:
        print('Please give the symbol of a number (1, 2, etc.)\nThe program will restart now')
        caeser_cypher()

    result = ''

    for char in plain_txt:
        if char.isalpha():
            result += encrypt(char, rotation)
        else:
            result += char
    print('Caesar code: {}'.format(result))


caeser_cypher()
