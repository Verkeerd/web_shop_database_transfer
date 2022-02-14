import general_functions as gf
import code_breaker_bot as bot

slot_amount = 4
colour_amount = 6


def test_code_breaker(repeat=100):
    """
    Takes the amount of loops (repeat) (int) as input. Generates a random secret code and prints it. Runs the code
    breaker bot by generating guesses and feedback until the code is guessed or the bot is out of guesses.
    Prints a message about the outcome after every match. Keeps count of every time bot didn't guess the code and prints
    this after the game.
    """
    initial_combination_list = gf.all_possible_codes(4, 6)
    error_runs = 0
    while repeat >= 1:
        # copies original list so entries can be deleted (and I don't have to generate the list again every loop)
        combination_list = initial_combination_list.copy()
        rounds = 1
        # generates a secret code
        secret_code = gf.generate_code(slots=slot_amount,
                                       colour_range=colour_amount)
        print('The secret code is: {}'.format(secret_code))

        # breaks the secret code with the code-breaker bot
        guess = bot.first_guess(combination_list, slot_amount)
        pins = gf.calc_pin_feedback(guess=guess, code=secret_code)

        while pins != (4, 0):
            rounds += 1

            combination_list = gf.eliminate_codes(guess, combination_list, pins)

            # prints an error message if there are no possible combinations
            if not combination_list:
                error_runs += 1
                print('something went wrong')
                break
            guess = bot.next_guess(combination_list, combination_list)
            pins = gf.calc_pin_feedback(guess, secret_code)

        repeat -= 1
        print('the computer played against itself and guessed {} in {} rounds\n'.format(guess, rounds))
    # When the code is broken, we break out of the loop
    print('The code-breaker bot broke itself {} times'.format(error_runs))


test_code_breaker()
