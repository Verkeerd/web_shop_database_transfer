import random

colour_list = ['r', 'b', 'g', 'y', 'p', 'o']


########################################################################################################################
# pegs
def calc_black_pegs(guess, code):
    """"""
    result = 0
    # cycles through the two lists in reversed order
    for i in range((len(guess) - 1), -1, -1):
        if guess[i] == code[i]:
            result += 1
            del guess[i]
            del code[i]

    return result


def calc_white_pegs(guess, code):
    """"""
    result = 0
    for item in guess:
        if item in code:
            result += 1
            code.remove(item)
    return result


def pin_feedback(guess, code):
    guess_copy = guess.copy()
    code_copy = code.copy()
    black_pins = calc_black_pegs(guess_copy, code_copy)
    white_pins = calc_white_pegs(guess_copy, code_copy)
    return black_pins, white_pins


########################################################################################################################
# input
def input_escape_path():
    """"""
    if input('Enter "end" to stop\n'
             'Enter anything else to try again:\n').strip() == 'end':
        return True
    # returns False if the user wants to continue
    return False


def safe_int_input(message):
    """"""
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
    print("""
You have chosen to stop.
Goodbye!
Returning to the main program...
""")


def print_colour_list(c_list):
    result = symbol_to_colour(c_list[0])
    for i in range(1, len(c_list)):
        colour = symbol_to_colour(c_list[i])
        result += ', {}'.format(colour)
    return result


########################################################################################################################
# colours
def check_colour(colour):
    return colour in colour_list


def colour_to_int(colour):
    return colour_list.index(colour)


def symbol_to_colour(colour):
    """"""
    int_str_colors = list(enumerate(colour_list))
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


def generate_code(slot_amount, colour_amount):
    """
    Generates a string. The string is n characters long. Every character is a random generated number between 0 and r
    """
    result = []
    for i in range(slot_amount):
        result.append(random.randrange(0, colour_amount))
    return result


########################################################################################################################
# other
def make_lowercase(string):
    return string.lower()
