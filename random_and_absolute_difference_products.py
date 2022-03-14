import load_data_sql as load_sql
import general_support_algorithms as support
import random


def select_random_product(products):
    """Fetches the name and price of a random product in the sql webshop database."""
    random_value = random.randint(0, len(products))
    return products[random_value]


def absolute_biggest_difference():
    """
    Fetches a random product. Calculates which product has the biggest absolute difference in price with this random
    product and returns the name of this other product (str).
    """
    products = load_sql.name_price_products()
    random_product = select_random_product(products)

    # composes a list with all prices.
    prices = support.select_column(products, 0)
    # selects the product tuple with the lowest price
    lowest_price_product = products[prices.index(min(prices))]
    # selects the product tuple with the highest price
    highest_price_product = products[prices.index(max(prices))]

    # calculates mid-value between the highest and lowest price.
    true_median = (lowest_price_product[0] - highest_price_product[0]) / 2
    # returns the products with the highest price when the price of the random product is higher than true median.
    if random_product[0] > true_median:
        return highest_price_product[1]
    # returns the product with the lowest price otherwise.
    return lowest_price_product[1]


if __name__ == '__main__':
    print(absolute_biggest_difference())
