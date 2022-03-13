import load_data_sql as load_sql
import general_support_algorithms as support
import random


def select_random_product():
    """Fetches the name and price of a random product in the sql webshop database."""
    products = load_sql.name_price_products()
    random_value = random.randint(0, len(products))
    return products[random_value]


def absolute_biggest_difference():
    """
    Fetches a random product. Returns the name of this product.
    """
    products = load_sql.name_price_products()
    random_product = select_random_product()

    products = support.binary_sort_matrix_lst(products, 0)
    # TODO: Test if calculating the highest and lowest products would be quicker than sorting
    # calculates mid-value between the highest and lowest price.
    true_median = (products[-1][0] - products[0][0]) / 2
    # returns the products with the highest price when the price of the random product is higher than true median.
    if random_product[0] > true_median:
        return products[-1][1]
    # returns the product with the lowest price otherwise.
    return products[0][1]


if __name__ == '__main__':
    print(absolute_biggest_difference())
