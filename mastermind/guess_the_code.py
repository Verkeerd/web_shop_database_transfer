import general_functions as gf


def ask_user_for_guess(n, colour_range):
    """
    Takes n (int) and colour_range (int) as input. Asks user for a guess. Checks if guess meets the requirements.
    requirements:
        - n amount of entries seperated by a whitespace
        - all entries are in the colour list on an index that is lower than colour_range.
    Gives user the option to try again or quit when they give input that does not meet the requirements.
    Returns the user input when the requirements were met. Else, returns False.
    """
    # asks the user for input. strips the input of empty spaces.
    # input is split on spaces. puts these new values in a list.
    unrefined_guess = input('Give your guess:\n').strip().split(sep=' ')
    # makes sure the values in this list are lowercase.
    guess = list(map(gf.make_lowercase, unrefined_guess))
    len_guess = len(guess)

    if len_guess != n:
        print('Input was not recognized.\n'
              'It looks like you did not give the correct amount of pegs.\n'
              'We found {} in your answer, but our combination only has {} pegs.\n'
              'Please review your input of {}.'.format(len_guess, n, guess))
        if gf.input_escape_path():
            return False
        ask_user_for_guess(n, colour_range)
    for colour in guess:
        # checks if the entered values are known colours inside the colour range
        if not gf.check_colour(colour):
            print('Input was not recognized. {} is not a known colour\n'
                  'Please give your guess by entering the first letter of the colour you want to use\n'
                  '(e.g. "r r b b" (without the quotes) when you want to guess red, red, blue, blue)'.format(colour))
            # returns False if the user wants to quit
            if gf.input_escape_path():
                return False
            # restarts this function to get correct input from user
            return ask_user_for_guess(n, colour_range)

    return guess


def code_creator(n_pegs, colour_range):
    """
    Takes n_pegs (int) and colour_range (int) as input. Generates a random code n_pegs slots long. All numbers in the
    code are smaller than colour_range. Asks user to guess the code until they guess the code or quit. Prints a
    congratulation message and the amount of rounds it took to guess the code when the user guesses it.
    returns to the selection menu when the user quits.
    """
    # quits the program if the user gives "end" as input
    input("""
##########################################################################################
You have chosen to Crack the Code!
The code is {} pegs long.

You can choose from the following colours: 
    - Red (r)
    - Blue (b)
    - Green (g)
    - Yellow (y)
    - Purple (p)
    - Orange (o)

Please give your guess by entering the first letter of the colour you want to use
(e.g. "r r b b" (without the quotes) when you want to guess red, red, blue, blue)

Press Enter to continue
""".format(n_pegs))

    print("""
##########################################################################################

Thinking of a code...
...
""")

    # generates a random secret code.
    # Passes the amount of pegs (n_peg) and the amount of colours (colour_range)
    secret_code = gf.generate_code(n_pegs, colour_range)

    print("""
We thought of something!

##########################################################################################
""")

    guess_ints = []
    rounds = 0

    while guess_ints != secret_code:
        rounds += 1
        guess = ask_user_for_guess(n_pegs, colour_range)

        if not guess:
            # user wants to quit
            # returns to the main mastermind program
            gf.goodbye_message()
            return None

        guess_ints = list(map(gf.colour_to_int, guess))

        pin_response = gf.pin_feedback(guess_ints, secret_code)
        print('You guessed {}.\n'
              'We checked your answer.\n'
              'You receive {} red pegs and {} white pegs.\n'.format(gf.format_colours(guess),
                                                                    pin_response[0],
                                                                    pin_response[1]))
    # loop is broken when the user gives the correct combination.
    print('Congratulations!             {} is correct!\n'
          'The secret combination was   {}.\n'
          'It took you {} rounds to guess the secret combination'.format(gf.format_colours(guess),
                                                                         gf.format_colours(secret_code),
                                                                         rounds))
    # asks user if they want to play again or quit.
    if input('1) Play again\n2)Open selection menu') == '1':
        code_creator(n_pegs, colour_range)
