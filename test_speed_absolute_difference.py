import load_data_sql as load_sql
from random_and_absolute_difference_products import select_random_product
import time


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


def binary_sort_matrix(matrix, index):
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


def absolute_biggest_difference_sort():
    """
    Fetches a random product. Calculates which product has the biggest absolute difference in price with this random
    product and returns the name of this other product (str).
    """
    start_time = time.time_ns()
    products = load_sql.name_price_products()
    random_product = select_random_product(products)

    products = binary_sort_matrix(products, 0)

    # calculates mid-value between the highest and lowest price.
    true_median = (products[-1][0] - products[0][0]) / 2
    # returns the products with the highest price when the price of the random product is higher than true median.
    if random_product[0] > true_median:
        return products[-1][1], (time.time_ns() - start_time)
    # returns the product with the lowest price otherwise.
    return products[0][1], (time.time_ns() - start_time)


def absolute_biggest_difference_min_max():
    """
    Fetches a random product. Calculates which product has the biggest absolute difference in price with this random
    product and returns the name of this other product (str).
    """
    start_time = time.time_ns()

    products = load_sql.name_price_products()
    random_product = select_random_product(products)

    # composes a list with all prices.
    prices = []
    for row in products:
        prices.append(row[0])

    # selects the product tuple with the lowest price
    lowest_price_product = products[prices.index(min(prices))]
    # selects the product tuple with the highest price
    highest_price_product = products[prices.index(max(prices))]
    print(lowest_price_product, highest_price_product)

    # calculates mid-value between the highest and lowest price.
    true_median = (lowest_price_product[0] - highest_price_product[0]) / 2
    # returns the products with the highest price when the price of the random product is higher than true median.
    if random_product[0] > true_median:
        return highest_price_product[1], (time.time_ns() - start_time)
    # returns the product with the lowest price otherwise.
    return lowest_price_product[1], (time.time_ns() - start_time)


if __name__ == '__main__':
    print('original algorithm with sort:')
    print(absolute_biggest_difference_sort())
    print('\nnew algorithm with min, max')
    print(absolute_biggest_difference_min_max())
