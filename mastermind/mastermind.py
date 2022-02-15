import guess_the_code
import code_breaker_bot
import heuristic_code_breaker


def begin_mastermind():
    """
    Starts mastermind. Shows information to the user. There are two game-modes. One where you break the code and one
    where you think of a code and our code breaker bot breaks it. Asks for the users choice and starts that game-mode.
    Ends this function if the user quits.
    """
    active = True
    while active:
        route = input("""
##########################################################################################
Welcome to mastermind!

Play mastermind against the computer.
Break the code or watch our code-breaker bot crack yours!

1) Break the Code
2) Challenge Knuth's Code Breaker
3) Challenge My Heuristic Code Breaker
4) Quit

Enter your choice:
""").strip()
        if route == '1':
            guess_the_code.code_creator()
        elif route == '2':
            code_breaker_bot.knuth_code_breaker()
        elif route == '3':
            heuristic_code_breaker.heuristic_code_breaker()
        else:
            confirm = input('\nYou are quitting the program.\n'
                            'are you sure?\n'
                            'enter "quit" to quit:\n').strip().lower()
            if confirm == 'quit':
                # stops the program
                active = False


if __name__ == '__main__':
    begin_mastermind()
