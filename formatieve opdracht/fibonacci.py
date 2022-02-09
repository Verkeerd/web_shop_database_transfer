def fibonacci(n):
    """
    Takes a number (n) as input. Calculates the nth number of the fibonacci sequence and returns this.
    args:
        :param n: (int) index of the fibonacci sequence
    returns:
        :return: (int) number on the nth index of the fibonacci sequence
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


for i in range(20):
    print(fibonacci(i))
