import random


def input_int_safe():
    """
    asks the user for a number. checks if the number is given in the correct format (as a symbol). returns this number
    when it passes the check. asks the user if they want to stop if they give the wrong input. returns None if the user
    quits. Otherwise, returns another instance of this function.
    returns:
        :return: (int) input from the user when this input is valid
        :return: None when the user quits the program
    """
    try:
        return int(input('Give a number: '))
    except ValueError:
        print('Ohh... you broke me. Please give the symbol of a number (i.e. 1, 2, ...)')
        if input('Press 1 to try again! enter anything else to exit the system') == '1':
            return input_int_safe()


def guess_the_number():
    """
    Asks the user for a number. Generates a number between 0 and the given number. Lets the user guess until they guess
    the generated number, or they quit the program. Prints the amount of rounds it took the user to guess the number
    when the program quits.
    returns:
        :return: doesn't return anything; the game has been played.
    """
    print('This is a game where we think of a number and you try to guess it!\n'
          'First, please give the maximum number we think of\n')

    maximum = input_int_safe()
    if not maximum:
        print('Goodbye!')
        return None
    print('\nI have chosen a number between 1 and {}\n'
          'You can start guessing.\n'.format(maximum))

    answer = random.randint(1, maximum)
    guess = -1
    tries = 0

    while guess != answer:
        tries += 1
        guess = input_int_safe()
        if not guess:
            print('Goodbye!')
            return None
        print('Your {} guess is {}'.format(tries, guess))
    print('That is correct!\n'
          'The answer was {}.\n'
          'it took you {} rounds to guess it'.format(answer, tries))


guess_the_number()
