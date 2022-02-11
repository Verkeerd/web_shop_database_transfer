import general_functions as gf


def ask_user_for_guess(n, colour_range):
    """"""
    # asks the user for input. strips the input of empty spaces.
    # input is split on spaces. puts these new values in a list.
    # makes sure the values in this list are lowercase.
    guess = list(map(gf.make_lowercase, input('Give your guess:\n').strip().split(sep=' ')))
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
        # checks if the entered values are known colours that are also in use (inside the colour range).
        if not gf.check_colour(colour):
            print('Input was not recognized. {} is not a known colour\n'
                  'Please give your guess by entering the first letter of the colour you want to use\n'
                  '(e.g. "r r b b" (without the quotes) when you want to guess red, red, blue, blue)'.format(colour))
            # returns False if the user wants to quit
            if gf.input_escape_path():
                return False
            return ask_user_for_guess(n, colour_range)

    return guess


def code_creator(n_pegs, colour_range):
    """"""
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
        print('this is guess: "{}"'.format(guess))
        if not guess:
            # user wants to quit
            # returns to the main mastermind program
            gf.goodbye_message()
            return None

        guess_ints = list(map(gf.colour_to_int, guess))

        pin_response = gf.pin_feedback(guess_ints, secret_code)
        print('You guessed {}.\n'
              'We checked your answer.\n'
              'You receive {} red pegs and {} white pegs.\n'.format(gf.print_colour_list(guess),
                                                                    pin_response[0],
                                                                    pin_response[1]))
    # loop is broken when the user gives the correct combination.
    print('Congratulations!             {} is correct!\n'
          'The secret combination was   {}.\n'
          'It took you {} rounds to guess the secret combination'.format(gf.print_colour_list(guess),
                                                                         gf.print_colour_list(secret_code),
                                                                         rounds))
