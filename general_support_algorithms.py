def select_index(datapoint):
    """Takes a list or tuple and an index (int) as input. Selects the value on the index in the list and returns it."""
    return datapoint[0]


def select_column(matrix, index):
    """
    Takes a datamatrix and the name of a column (index) as input. Returns a list with all values inside the data matrix
    on the index.
    """
    result = []
    for row in matrix:
        result.append(row[index])
    return result


def list_mean(a_list):
    """Takes a list with integers as input. Calculated the mean of the list and returns this (float)."""
    return sum(a_list) / len(a_list)
