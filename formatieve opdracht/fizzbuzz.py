def fizz_buzz():
    """
    prints 1 up until 100, except for every multiple of 3, where 'fizz' is printed and for every multiple of 5, where
    'buzz' is printed. When the number is a multiple of both 3 and 5, 'fizzbuzz' is printed.
    returns:
        :return: doesn't return anything. number and fizzbuzzes are printed
    """
    for i in range(1, 101):
        if i % 3 == 0:
            if i % 5 == 0:
                print('fizzbuzz')
            print('fizz')
        elif i % 5 == 0:
            print('buzz')
        print(i)


fizz_buzz()
