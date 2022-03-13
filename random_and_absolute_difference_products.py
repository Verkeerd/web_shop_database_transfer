import load_data_sql as load_sql
import general_support_algorithms as support
import random


def select_random_product():
    """Fetches the name and price of a random product in the sql webshop database."""
    products = load_sql.load_products_sql()
    random_value = random.randint(0, len(products))
    return products[random_value]


def absolute_biggest_difference():
    """"""
    products = load_sql.load_products_sql()
    random_product = select_random_product()

    products = support.binary_sort_matrix_lst(products, 0)
    # TODO: Test if calculating the highest and lowest products would be quicker than sorting
    true_median = products[-1][0] / 2

    if random_product[0] > true_median:
        return products[-1][1]

    return products[0][1]


if __name__ == '__main__':
    print(absolute_biggest_difference())
