import load_data_sql as load_sql
from random_and_absolute_difference_products import select_random_product
import time


def absolute_biggest_difference_sort():
    """
    Fetches a random product. Calculates which product has the biggest absolute difference in price with this random
    product and returns the name of this other product (str).
    """
    start_time = time.time_ns()
    products = load_sql.name_price_products()
    random_product = select_random_product(products)

    products = support.binary_sort_matrix_lst(products, 0)

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
