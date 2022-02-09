def pyramid():
    """
    Asks the user for a number n. Prints a pyramid made of star characters (*). The pyramid is n high and n + n - 1
    wide. The Pyramid is anchored to the left side.
    """
    try:
        amount = int(input('How big? '))
        for i in range(1, amount + 1):
            print('*' * i)
        for i in range(amount - 1, 0, -1):
            print('*' * i)
    except ValueError:
        print('Please give a number as a numeric symbol (1, 2 ...)')
        pyramid()


def pyramid_while():
    """
    Asks the user for a number n. Prints a pyramid made of star characters (*). The pyramid is n high and n + n - 1
    wide. The Pyramid is anchored to the left side.
    """
    try:
        amount = int(input('How big? '))
        i = 1
        while i < amount:
            print('*' * i)
            i += 1
        while i >= 1:
            print('*' * i)
            i -= 1
    except ValueError:
        print('Please give a number as a numeric symbol (1, 2 ...)')
        pyramid_while()


def pyramid_reverse():
    """
    Asks the user for a number n. Prints a pyramid made of star characters (*). The pyramid is n high and n + n - 1
    wide. The Pyramid is anchored to the right side.
    """
    try:
        amount = int(input('How big? '))
        for i in range(1, amount + 1):
            print(' ' * (amount - i) + '*' * i)
        for i in range(amount - 1, 0, -1):
            print(' ' * (amount - i) + '*' * i)
    except ValueError:
        print('Please give a number as a numeric symbol (1, 2 ...)')
        pyramid()


def pyramid_reverse_while():
    """
    Asks the user for a number n. Prints a pyramid made of star characters (*). The pyramid is n high and n + n - 1
    wide. The Pyramid is anchored to the right side.
    """
    try:
        amount = int(input('How big? '))
        i = 1
        while i < amount:
            print(' ' * (amount - i) + '*' * i)
            i += 1
        while i >= 1:
            print(' ' * (amount - i) + '*' * i)
            i -= 1
    except ValueError:
        print('Please give a number as a numeric symbol (1, 2 ...)')
        pyramid_while()


pyramid()
pyramid_while()
pyramid_reverse()
pyramid_reverse_while()
