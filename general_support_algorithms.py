def select_index(datapoint):
    """Takes a list or tuple and an index (int) as input. Selects the value on the index in the list and returns it."""
    return datapoint[0]


def select_column(matrix, index):
    result = []
    for row in matrix:
        result.append(row[index])
    return result


def binary_search_index_matrix(matrix, target, index, low, high):
    """
    searches for the index of the target in the column {index} of the data matrix.
    args:
        :param matrix: a matrix of data.
        :param target: the element being sought
        :param index: the column of the data matrix being sought.
        :param low: the minimum index of the list that can contain the target.
        :param high: the maximum index of the list that can contain the target.
    returns:
        :return int: returns the index the target was found at.
                     returns the index the target would fit sorted when the index isn't found
    """
    if low > high:
        return high + 1

    mid_index = low + (high - low) // 2
    try:
        if target < matrix[mid_index][index]:
            return binary_search_index_matrix(matrix, target, index=index, low=low, high=mid_index - 1)
        elif target > matrix[mid_index][index]:
            return binary_search_index_matrix(matrix, target, index=index, low=mid_index + 1, high=high)
        elif matrix[mid_index][index] == target:
            return mid_index
    except TypeError:
        return 0


def binary_sort_matrix_lst(matrix, index):
    """
    sorts a data matrix based upon the data in the index column of the matrix.
    args:
        :param matrix: a matrix of data.
        :param index: the name of a column in the data matrix
    returns:
        :return: a copy of the matrix, sorted on the column {index}.
    """
    lst_sorted = [matrix[0]]
    for i in range(1, len(matrix)):
        lst_sorted.insert(binary_search_index_matrix(lst_sorted, matrix[i][index], index, 0, i - 1), matrix[i])
    return lst_sorted


def list_mean(a_list):
    """takes a list with integers as input. Calculated the mean of the list and returns this (float)."""
    return sum(a_list) / len(a_list)
