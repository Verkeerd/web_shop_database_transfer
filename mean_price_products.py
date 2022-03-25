import load_data_sql as load_sql


def mean_price_products():
    """Calculates the mean price of all the products in the web-shop database. Returns the price (float)."""
    product_prizes = load_sql.all_product_prices()
    return sum(product_prizes) / len(product_prizes)


def mean_price_products_formatted():
    """
    Calculates the mean price of all the products in the web-shop database. Returns the price (str) in a nice format,
    rounded to two point behind the decimal.
    """
    return '{:.2f} euro'.format(mean_price_products())


if __name__ == '__main__':
    print(mean_price_products_formatted())
