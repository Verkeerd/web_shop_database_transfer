def calculate_average_lst(lst):
    """
    Takes a list of numbers as input. Calculates the average and returns it.
    args:
        :param lst: (list) [int] a list of numbers
    returns:
        :return: (int) the average of the numbers in the list.
    """
    # returns the sum of all the items in the list, divided by the amount of items
    return sum(lst) / len(lst)


def calculate_average_matrix(matrix):
    """
    Takes a list containing lists with numbers as input. Calculates the average for each list item of the matrix.
    Returns all averages in a new list.
    args:
        :param matrix: (list) [[int]] a list with items that are lists containing numbers.
    returns:
        :return: (list) [int] a list with averages (of the list items of the input matrix)
    """
    list_of_averages = []
    for lst in matrix:
        list_of_averages.append(calculate_average_lst(lst))
    return list_of_averages


lst_0 = [1, 2, 2, 3]
lst_1 = [5, 6, 6, 7, 7, 8, 9, 9]
lst_2 = [5, 7, 9, 5, 6, 8, 5, 4, 7, 8, 9]

data_matrix = [lst_0, lst_1, lst_2]

print(calculate_average_matrix(data_matrix))
