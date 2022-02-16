import random
import itertools

colours_in_program = ['r', 'b', 'g', 'y', 'p', 'o', 'w', 't']


########################################################################################################################
# pins
def calc_black_pins(guess, code):
    """
    Takes a secret code (list) [int] and a guess (list) [int] as input.
    Calculates the amount of pegs that are the correct color on the correct spot and deletes these pegs from both lists.
    Returns the amount of pegs that were found (int).
    """
    amount = 0
    # cycles through the two lists in reversed order
    for i in range((len(guess) - 1), -1, -1):
        if guess[i] == code[i]:
            amount += 1
            del guess[i]
            del code[i]

    return amount


def calc_white_pins(guess, code):
    """
    Takes a secret code (list) [int] and a guess (list) [int] as input.
    Calculates the amount of pegs that are the correct color, but on the wrong spot.
    Returns the amount of pegs that were found (int).
    """
    amount = 0
    for item in guess:
        if item in code:
            amount += 1
            # removes the used peg from the secret code.
            code.remove(item)
    return amount


def calc_pin_feedback(guess, code):
    """
    Takes a secret code (list) [int] and a guess (list) [int] as input.
    Calculates the amount of black pegs (correct colour on correct spot) and white pegs (correct colour on wrong spot).
    Returns black and white pegs in a tuple (int, int).
    """
    guess_copy = guess.copy()
    code_copy = code.copy()
    black_pins = calc_black_pins(guess_copy, code_copy)
    white_pins = calc_white_pins(guess_copy, code_copy)

    return black_pins, white_pins


def all_possible_pins(slots):
    """Takes slots (int) as input. Returns possible pin outcomes based on the amount of slots (list) [(int, int)]."""
    if slots == 2:
        return [(0, 0), (0, 1), (0, 2), (1, 0)]
    if slots == 3:
        return [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (2, 0), (1, 1), (1, 2), (2, 1)]
    if slots == 4:
        return [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (3, 0)]
    return None


########################################################################################################################
# input
def input_pin_feedback(slots):
    """
    Takes slots (int) as input. Asks user for feedback when the bot tries to guess their secret code. Asks for the
    amount of black and white pins. Returns this information in a tuple (int, int).
    Returns false if the user doesn't enter valid input and quits.
    """
    black_pins = safe_int_input('how many red pins?:\n', max_amount=slots)
    if black_pins == -1:
        return False
    if black_pins in (slots-1, slots):
        return black_pins, 0

    white_pins = safe_int_input('how many white pins?:\n', max_amount=slots)
    if white_pins == -1:
        return False

    return black_pins, white_pins


def input_escape_path():
    """
    Gives the user the option to escape from an input field. Use when the user gave the wrong input.
    Returns True (bool) if the user quits. Returns false otherwise.
    """
    if input('Enter "end" to stop\n'
             'Enter anything else to try again:\n').strip().lower() == 'end':
        return True
    # returns False if the user wants to continue
    return False


def safe_int_input(message, max_amount=4):
    """
    Takes a message (str); max_amount as input.
    The message is shown to the user. Asks user for an integer input. If the input does not meet the requirements,
    shows the user an error message and gives them the option of quitting or trying again.
    requirements:
        - must be an integer
        - must be a number up until max_amount
    If the input meets requirements, returns the input (int).
    If user quits before giving correct input, returns -1 (int).
    """
    try:
        wanted_integer = int(input(message).strip())
        if wanted_integer > max_amount:
            print('The maximum amount allowed is {}.\n'.format(max_amount))
            raise ValueError
        return wanted_integer
    # if user doesn't enter an integer
    except ValueError:
        print('Input was not recognised. Please enter a number up until {}.\n'.format(max_amount))
        # returns false if the user wants to quit
        if input_escape_path():
            return -1
        # calls this function again if the user wants to try again.
        return safe_int_input(message)


def set_slots_and_colours(max_slots=6, max_colours=8):
    """
    Takes the max amount of slots (int); max amount of colours (int) as input. Asks the user with how many slots and
    colours they want to play. Checks if the input is below the respective maximum.
    If the input does not meet the requirements, asks user if they want to try again or quit.
    If the input does meet the requirement, returns the given amount of slots and colours (tuple) (int, int).
    Returns None when the user quits.
    """
    print('You can choose with how many slots and colours you want to play! ')
    slots = safe_int_input('With how many slots do you want to play? (max {})\n'.format(max_slots),
                           max_amount=max_slots)
    colour_range = safe_int_input('With how many colours do you want to play? (max {})\n'.format(max_colours),
                                  max_amount=max_colours)
    if slots <= 1:
        print('You have to use at least 2 slots!')
        if input_escape_path():
            return -1
        return set_slots_and_colours(max_slots, max_colours)

    if colour_range <= 3:
        print('You have to use at least 4 colours!')
        if input_escape_path():
            return -1
        return set_slots_and_colours(max_slots, max_colours)
    return slots, colour_range


########################################################################################################################
# output
def goodbye_message():
    """Prints a message for the user when they quit a sub-part of the system."""
    print("""
You have chosen to stop.
Goodbye!
Returning to the main program...
""")


def format_colours(colour_list):
    """
    Takes a list with colours [int] as input. Looks up the full name of the colour and places those colours in a string
    with the following format: {colour1}, {colour2}, {colour3}.
    Returns this formatted string with colours (str).
    """
    result = readable_colour(colour_list[0])
    for i in range(1, len(colour_list)):
        colour = readable_colour(colour_list[i])
        result += ', {}'.format(colour)
    return result


########################################################################################################################
# colours
def check_colour(colour, colour_range):
    """
    Takes a colour (str); colour_range (int) as input. checks if this colour is allowed by the game.
    Returns True (bool) if the colour is allowed, returns False otherwise.
    """
    return colour in colours_in_program[:colour_range]


def colour_to_int(colour):
    """Takes the first letter of a colour (str) as input. Returns the number used for this colour (int)."""
    return colours_in_program.index(colour)


def readable_colour(colour):
    """
    Takes a symbolic form (first letter or int in use for this colour) of a colour as input.
    Returns the full name of the colour (str).
    """
    full_names = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'white', 'teal']
    for index_item in list(enumerate(colours_in_program)):
        if colour in index_item:
            return full_names[index_item[0]]
    return ''


########################################################################################################################
# codes
def generate_code(slots, colour_range):
    """
    Takes slots (int) and colour_range (int) as input. Generates a list. The list is slots (from input) items long.
    Every item is a random generated number between 0 and colour_range.
    Returns the generated code (list) [int].
    """
    result = []
    while slots >= 1:
        result.append(random.randrange(0, colour_range))
        slots -= 1
    return result


def all_possible_codes(slots, colour_range):
    """
    Takes the amount of pegs (int) and colour_range (int) as input.
    Creates a list that contains tuples.
    The tuples have slots amount of elements, where every element can be 0 to colour_range. No two tuples are identical.
    The place of the elements matters. Elements can repeat.
    The list contains all possible tuples.
    Returns the list with all possible codes (list) [(int)].
    """
    # source: MutantOctopus, (2016, 6 maart). Combinations with repetition in python, where order MATTERS.
    # stackoverflow. Geraadpleegd op 11-2-2022, van
    # https://stackoverflow.com/questions/35822627/combinations-with-repetition-in-python-where-order-matters

    iter_colours = [i for i in range(colour_range)]

    return list(itertools.product(iter_colours, repeat=slots))

def get_starters(slots):
    """Takes slots (int) as input. Returns possible starters based on the amount of slots (tuple)."""
    if slots == 2:
        return [(0,0), (0,1)]
    if slots == 3:
        return [(0,0,0), (0,0,1), (0,1,2)]
    if slots == 4:
        return [(0,0,0,0), (0,0,0,1), (0,0,1,1), (0,0,1,2), (0,1,2,3)]
    return None


def eliminate_codes(guess, all_codes, feedback_pins):
    """
    Takes all codes left over before the most recent guess (list) [(int)]; a guess (list) [int]; feedback_pins (tuple)
    (int, int) as input.
    Checks for all codes what feedback they would give when you guess the guess code. If the generated feedback is
    the same as feedback_pins, the code is added to a new list.
    Returns the list with all possible codes left after the feedback (list) [(int)].
    """
    # asks for the peg response the guess attempt for every code.
    # if the code responds with different pegs to the guess attempt, the code cannot be the secret code.

    possible_codes = []
    for code in all_codes:
        # When black and white pins are calculated, a list containing integers is needed, so the code have to be
        # converted before feedback can be collected.
        code = list(code)

        peg_response = calc_pin_feedback(guess=guess, code=code)

        # when the generated peg response is the same as the user gave us, adds the code to the list
        if peg_response == feedback_pins:
            possible_codes.append(code)

    return possible_codes


########################################################################################################################
# other
def make_lowercase(string):
    """Takes a string as input. Returns a copy of that string with all lowercase characters (str)."""
    return string.lower()
