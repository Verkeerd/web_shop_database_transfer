import general_functions as gf
import itertools

peg_amount = 4
colour_amount = 6

possible_pegs = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1),
                 (2, 2), (3, 0)]


def all_possible_combinations(pegs, colour_range):
    """
    Takes pegs (int) and colour_range (int) as input. Creates a list that contains tuples. The tuples contain every
    combination of [n * pegs] where n represents every number from 0 up until colour_range. No two lists are identical.
    """
    # source: MutantOctopus
    # https://stackoverflow.com/questions/35822627/combinations-with-repetition-in-python-where-order-matters
    # creates a list that contains tuples.
    # The tuples contain every combination of [n * p] where n is 0 to c where p = pegs; c = colour_range.
    # No two lists are identical.

    # a string with all possible integers representing numbers
    # (if there are 6 colours, iter_colours will be '012345')
    iter_colours = ''
    for i in range(0, colour_range):
        iter_colours += str(i)
    return list(itertools.product(iter_colours, repeat=4))


def eliminate_combinations(guess, all_combinations, pegs):
    """"""
    # asks for the peg response the guess attempt for every combination.
    possible_combos = []
    for combination in all_combinations:
        # if the combination responds with different pegs to the guess attempt
        # the combination cannot be the secret code.
        peg_response = gf.pin_feedback(guess=list(guess), code=list(combination))

        # when the generated peg response is the same as the user gave us, adds the combination to the list
        if peg_response == pegs:
            possible_combos.append(combination)

    return possible_combos


def next_guess(combinations, all_combinations):
    """"""
    # print('I\'m thinking about my next move...')
    best_combination = []
    least_combinations_left = len(all_combinations)

    for combo in combinations:
        worst_case = 0
        for peg_outcome in possible_pegs:
            combinations_left_over = len(eliminate_combinations(combo, all_combinations, peg_outcome))

            if combinations_left_over > worst_case:
                worst_case = combinations_left_over
        if worst_case < least_combinations_left:
            best_combination = combo

    return best_combination


def first_guess(all_combinations):
    """"""
    starters = ['0000', '0001', '0011', '0122', '0123']

    return next_guess(starters, all_combinations)


def get_feedback():
    """"""
    black_pins = gf.safe_int_input('how many red pins?:\n')
    if black_pins == -1:
        return False
    if black_pins == 4:
        return 4, 0

    white_pins = gf.safe_int_input('how many white pins?:\n')
    if white_pins == -1:
        return False

    return black_pins, white_pins


def code_breaker():
    """"""
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

Every peg in your code can only award one pin. Red pins have priority over white pins. 
(e.g. if your code is:   Blue,   Blue,   Green,  Green 
and I guess:             Blue,   Green,  Green,  Green, 
I will receive two red pins and no white ones. 
The second peg in my guess (green) will not receive a white peg, because both green pegs 
in your code already awarded a pin.) 


Those are the rules! 
If you are confused about anything, please look up the official mastermind rules at 
https://www.ultraboardgames.com/mastermind/game-rules.php


Please create a combination! 
Remember it well, or write it down somewhere.

Press Enter to continue
""")
    combination_list = all_possible_combinations(pegs=peg_amount, colour_range=colour_amount)

    rounds = 1

    guess = first_guess(combination_list)

    # prints the guess in a user friendly format
    readable_guess = gf.print_colour_list(list(map(int, list(guess))))
    print("""
##########################################################################################    

Let's begin!

My first guess is {}
""".format(readable_guess))

    # asks user for feedback on the pins.
    pins = get_feedback()

    if not pins:
        gf.goodbye_message()
        return None

    while pins != (4, 0):
        rounds += 1
        # eliminates all combination no longer possible with provided feedback
        combination_list = eliminate_combinations(guess, combination_list, pins)

        # comes up with a new guess
        guess = next_guess(combination_list, combination_list)

        readable_guess = gf.print_colour_list(list(map(int, list(guess))))
        print("My {}nd guess is {}\n".format(rounds, readable_guess))

        # get new feedback from
        pins = get_feedback()
        if not pins:
            gf.goodbye_message()
            return None

    # program quits automatically if user doesn't want to continue
    if input("""
Yay! I guessed the code.
It was {}
It took me {} rounds to guess it.

##########################################################################################

1) play again
2) return to main_frame
""".format(readable_guess, rounds)).strip() == '1':
        code_breaker()


def test_the_bot():
    """"""
    initial_combination_list = all_possible_combinations(4, 6)
    for i in range(100):
        combination_list = initial_combination_list.copy()
        rounds = 1
        secret_code = gf.generate_code(slot_amount=4,
                                       colour_amount=6)
        print('The secret code is: {}'.format(secret_code))
        guess = first_guess(combination_list)

        pins = gf.pin_feedback(list(map(int, guess)),
                               code=secret_code)

        while pins != (4, 0):
            rounds += 1

            combination_list = eliminate_combinations(guess, combination_list, pins)

            # prints an error message if there are no possible combinations
            if not combination_list:
                print('something went wrong')
                break
            guess = next_guess(combination_list, combination_list)

            pins = gf.pin_feedback(list(map(int, guess)), secret_code)

        print('the computer played against itself and guessed {} in {} rounds\n'.format(guess, rounds))


if __name__ == '__main__':
    test_the_bot()
