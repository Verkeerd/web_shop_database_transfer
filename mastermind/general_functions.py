import random

colours_in_program = ['r', 'b', 'g', 'y', 'p', 'o']


########################################################################################################################
# pins
def calc_black_pins(guess, code):
    """
    Takes a secret code (list) [int] and a guess (list) [int] as input.
    Calculates the amount of pegs that are the correct color on the correct spot and deletes these pegs from both lists.
    Returns the amount of pegs found.
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
    Calculates the amount of pegs that are the correct color, but on the wrong spot. Returns the amount of pegs found.
    """
    amount = 0
    for item in guess:
        if item in code:
            amount += 1
            # removes the used peg from the secret code.
            code.remove(item)
    return amount


def pin_feedback(guess, code):
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


########################################################################################################################
# input
def input_escape_path():
    """
    Gives the user the option to escape from an input field. Use when the user gave the wrong input.
    Returns True if the user wants to quit. Returns false otherwise.
    """
    if input('Enter "end" to stop\n'
             'Enter anything else to try again:\n').strip() == 'end':
        return True
    # returns False if the user wants to continue
    return False


def safe_int_input(message):
    """
    Takes a message (str) as input.
    The message is shown to the user. Asks user for an integer input. If the input does not meet the requirements,
    shows the user an error message and gives them the option of quitting or trying again.
    If the input meets requirements, returns the input as integer.
    If user quits before giving correct input, returns -1.
    """
    try:
        return int(input(message).strip())
    # if user doesn't enter an integer
    except ValueError:
        print('Input was not recognised. Please enter an integer.\n(e.g. "4")')
        # returns false if the user wants to quit
        if input_escape_path():
            return -1
        # calls this function again if the user wants to try again.
        return safe_int_input(message)


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
    Takes a list with colours (c_list) [int] as input. Looks up the full name of the colour and places those colours in
    a string with the following format: {colour1}, {colour2}, {colour3}. Returns this string.
    """
    result = readable_colour(colour_list[0])
    for i in range(1, len(colour_list)):
        colour = readable_colour(colour_list[i])
        result += ', {}'.format(colour)
    return result


########################################################################################################################
# colours
def check_colour(colour):
    """
    Takes a colour (str) as input. checks if this colour is allowed by the game. Returns True if this is case, returns
    False otherwise.
    """
    return colour in colours_in_program


def colour_to_int(colour):
    """Takes the first letter of a colour (str) as input. Returns the number used for this colour (in the game)."""
    return colours_in_program.index(colour)


def readable_colour(colour):
    """
    Takes the representation of a colour (first letter or int in use for this colour) as input. Returns the full name of
    the colour.
    """
    int_str_colors = list(enumerate(colours_in_program))
    if colour in int_str_colors[0]:
        return 'red'
    if colour in int_str_colors[1]:
        return 'blue'
    if colour in int_str_colors[2]:
        return 'green'
    if colour in int_str_colors[3]:
        return 'yellow'
    if colour in int_str_colors[4]:
        return 'purple'
    if colour in int_str_colors[5]:
        return 'orange'


def generate_code(slots, colour_range):
    """
    Generates a string. The string is n characters long. Every character is a random generated number between 0 and r.
    """
    result = []
    for i in range(slots):
        result.append(random.randrange(0, colour_range))
    return result


########################################################################################################################
# other
def make_lowercase(string):
    """Takes a string as input. Returns a copy of that string with all lowercase characters."""
    return string.lower()


def str_to_integer_list(code):
    """Takes a string containing only numbers (e.g. '0011') as input. Turns it into a list with integers."""
    return list(map(int, list(code)))
