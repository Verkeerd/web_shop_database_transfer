import general_functions as gf
import itertools

peg_amount = 4
colour_amount = 6

possible_pegs = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1),
                 (2, 2), (3, 0)]


def all_possible_codes(slots, colour_range):
    """
    Takes the amount of pegs (int) and colour_range (int) as input.
    Creates a list that contains strings. The strings contain every combination of n * pegs where n represents
    every number from 0 up until colour_range. No two lists are identical.
    Returns the list (list) [str].
    """
    # source: MutantOctopus
    # https://stackoverflow.com/questions/35822627/combinations-with-repetition-in-python-where-order-matters
    # creates a list that contains tuples.
    # The tuples contain every combination of [n * p] where n is 0 to c where p = pegs; c = colour_range.
    # No two lists are identical.

    # a string with all possible colours represented by integers
    # (if there are 6 colours, iter_colours will be '012345')
    iter_colours = ''
    for i in range(0, colour_range):
        iter_colours += str(i)
    return list(itertools.product(iter_colours, repeat=slots))


def eliminate_codes(guess, all_codes, feedback_pins):
    """
    Takes all codes left over before the most recent guess (list) [str]; a guess (list) [int]; feedback_pins (tuple)
    (int, int) as input.
    Checks for all codes what feedback they would give when you guess the guess code. If the generated feedback is
    the same as feedback_pins, the code is added to a new list.
    Returns the new list.
    """
    # asks for the peg response the guess attempt for every code.
    possible_combos = []
    for code in all_codes:
        # if the code responds with different pegs to the guess attempt
        # the code cannot be the secret code.
        list_guess = guess
        list_combination = gf.str_to_integer_list(code)

        peg_response = gf.pin_feedback(guess=list_guess, code=list_combination)

        # when the generated peg response is the same as the user gave us, adds the code to the list
        if peg_response == feedback_pins:
            possible_combos.append(code)

    return possible_combos


def next_guess(codes_to_check, all_codes):
    """
    Takes all codes to consider as guess (list) [str]; all potential codes (list) [str] as input (same list except first
    guess). Calculates the amount of codes left after all possible feedback (combination of white and black pins) that
    can be received. Keeps track of the worst case scenario for every considered guess
    (worst case scenario = the highest amount of codes left over).
    Returns the code (list) [int] with the lowest worst case scenario.
    """
    print('I\'m thinking about my next move...')
    best_code = []
    least_combinations_left = len(all_codes)

    for code in codes_to_check:
        worst_case = 0
        for peg_outcome in possible_pegs:
            codes_left_over = len(eliminate_codes(gf.str_to_integer_list(code), all_codes, peg_outcome))

            if codes_left_over > worst_case:
                worst_case = codes_left_over
        if worst_case < least_combinations_left:
            best_code = code

    return gf.str_to_integer_list(best_code)


def first_guess(all_codes):
    """
    Takes all potential codes (list) [str] as input.
    Calculates the best first guess. All colours can be treated as the same in the first guess, as there is no
    statistical difference between      blue    blue    blue    red
    and                                 yellow  yellow  yellow  red
    Returns the best first guess.
    """

    starters = ['0000', '0001', '0011', '0122', '0123']

    return next_guess(starters, all_codes)


def get_feedback():
    """
    Asks user for feedback when the bot tries to guess their secret code. Asks for the amount of black and white pins.
    Returns this information in a tuple (int, int).
    Returns false if the user doesn't enter valid input and choses to quit.
    """
    black_pins = gf.safe_int_input('how many red pins?:\n')
    if black_pins == -1:
        return False
    if black_pins == 4:
        return 4, 0

    white_pins = gf.safe_int_input('how many white pins?:\n')
    if white_pins == -1:
        return False

    return black_pins, white_pins


def code_breaker(slots, colour_range):
    """
    Takes slots (int) and colour_range (int) as input. Prints information, generates all possible codes slots long with
    all entries a number between 0 and colour_range. Plays mastermind with the user by guessing the code and asking for
    feedback. Does this until the bot breaks the code.
    Finally, gives the user the option to play again or quit.
    """
    # prints information and waits for the user
    input("""
##########################################################################################
Hello!
I am the Code Breaker. I am excited to be playing against you today!

First I'll explain the rules:

You have pegs in multiple colours and spots to place them on.
You can use the same colour on multiple spots, and the order matters!
You can choose from the following colours:
    - red (r)
    - blue (b)
    - green (g)
    - yellow (y)
    - purple (p)
    - orange (o)

When you have created the combination, I will attempt to guess it.
After I guess, please provide me with feedback!

Give me a red pin for every peg that is the correct colour and in the correct spot.
Give a white pin for every peg that is the the correct colour, but not in the correct spot.

Every peg in your code can only award one pin. Red feedback_pins have priority over white feedback_pins.
(e.g. if your code is:   Blue,   Blue,   Green,  Green
and I guess:             Blue,   Green,  Green,  Green,
I will receive two red feedback_pins and no white ones.
The second peg in my guess (green) will not receive a white peg, because both green pegs
in your code already awarded a pin.)


Those are the rules!
If you are confused about anything, please look up the official mastermind rules at
https://www.ultraboardgames.com/mastermind/game-rules.php


Please create a secret code!
Remember it well, or write it down somewhere.

Press Enter to continue
""")
    possible_codes = all_possible_codes(slots=slots, colour_range=colour_range)

    rounds = 1

    guess = first_guess(possible_codes)
    # prints the guess in a user-friendly format
    readable_guess = gf.format_colours(guess)
    print("""
##########################################################################################    

Let's begin!

My first guess is {}
""".format(readable_guess))

    # asks user for feedback.
    feedback_pins = get_feedback()

    if not feedback_pins:
        gf.goodbye_message()
        return None

    while feedback_pins != (4, 0):
        rounds += 1
        # eliminates all combination no longer possible with the provided feedback
        possible_codes = eliminate_codes(guess=guess, all_codes=possible_codes, feedback_pins=feedback_pins)

        # calculates the next best guess (based on the best worst-case scenario)
        guess = next_guess(possible_codes, possible_codes)

        print("My {}nd guess is {}\n".format(rounds, gf.format_colours(guess)))

        # get new feedback
        feedback_pins = get_feedback()
        if not feedback_pins:
            gf.goodbye_message()
            return None

    # program quits automatically if user doesn't want to continue
    if input("""
Yay! I guessed the code.
It was {}
It took me {} rounds to guess it.

##########################################################################################
1) Play again
2) Open selection menu
""".format(readable_guess, rounds)).strip() == '1':
        code_breaker(slots, colour_range)
