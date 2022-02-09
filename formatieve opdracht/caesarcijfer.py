def encrypt(char, n):
    """
    Takes an alphabetic character and a number as input.
    Converts the character to its ascii value. Adds n to the ascii value. If this sum will make the new ascii value
    outside the range of latin characters, shifts the value to the other side of this range (e.g. 122 (z) + 1 = 97 (a)).
    Converts this value back to a latin character and returns it.
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
    Asks user for a string and a rotation coefficient.
    Encrypts the given string with a caesar-cypher. The coefficient signifies the amount of steps taken, with steps
    taken to the right for a positive coefficient. With a negative one, the steps are taken to the left.
    Prints the encrypted string.
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
