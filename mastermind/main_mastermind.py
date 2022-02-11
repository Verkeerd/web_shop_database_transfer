import guess_the_code
import code_breaker_bot

pegs = 4
colour_amount = 6


def begin_mastermind():
    """"""
    active = True
    while active:
        route = input("""
##########################################################################################
Welcome to mastermind!

Play mastermind against the computer.
Break the code or watch our code-breaker bot crack yours!

1) Break the code
2) Challenge our code-breaker bot
3) Quit

Enter your choice: 
""").strip()
        if route == '1':
            guess_the_code.code_creator(pegs, colour_amount)
        elif route == '2':
            code_breaker_bot.code_breaker()
        else:
            confirm = input('You are quitting the program.\n'
                            'are you sure?\n'
                            'enter "yes" to quit\n').strip()
            if confirm == 'yes':
                # stops the program
                active = False


begin_mastermind()
