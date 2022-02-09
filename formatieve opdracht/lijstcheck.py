def count(x, lst):
    """
    Takes a number and a list as input. Counts how often x is an item of the list and returns this count.
    args:
        :param x: (int) a number
        :param lst: (list) a list
    returns:
        :return: (int) amount of times x is contained in a_list
    """
    result = 0
    for item in lst:
        if item == x:
            result += 1
    return result


def biggest_step(lst):
    """
    Takes a list as input. Measures the difference between the items on each consecutive index of the list.
    Returns the biggest difference.
    args:
        :param lst: (list) a list
    returns:
        :return: the biggest difference between the items on two consecutive indexes of the list.
    """
    biggest_diff = 0
    for i in range(0, (len(lst) - 1)):
        # calculates the difference between the two indexes
        diff = abs(lst[i] - lst[i + 1])
        # remembers the difference when it is the highest recorded yet.
        if diff > biggest_diff:
            biggest_diff = diff
    return biggest_diff


def zeros_and_ones(lst_01):
    """
    Takes a list of which all items are either a 0 or a 1. Checks if the list meets the following requirements:
    - There are more 1's than there are 0's.
    - There are no more than twelve 0's
    Returns True if the requirements are met. Returns False otherwise.
    args:
        :param lst_01: a list with items that are either a 0 or a 1.
    returns:
        :return: (bool) True if the list meets the requirements, otherwise False.
    """
    amount_0 = count(0, lst_01)
    if amount_0 >= 13:
        return False
    amount_1 = count(1, lst_01)
    if amount_1 > amount_0:
        return True
    # only option left is:  amount_1 <= amount_0
    return False


print(count(2, [1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 2, 2, 1]))
print(biggest_step([1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 5, 7, 9]))
print(zeros_and_ones([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
print(zeros_and_ones([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
print(zeros_and_ones([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]))
