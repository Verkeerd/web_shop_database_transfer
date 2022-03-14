import mongo_connection as mdb_c
import sql_connection as sql_c


def create_product_query(product):
    """
    Takes information about a product (dict) as input. Constructs a sql query to insert this product with name, id and
    price into a sql database. Returns the constructed sql query (str).
    """
    sql_query_tp = 'INSERT INTO products (product__id, product_name, selling_price) VALUES (%s, %s, %s)'

    values = (product['_id'], product['name'], product['price']['selling_price'])

    return sql_query_tp, values


def upload_product(product):
    """
    Takes information about a product (dict) as input. Uploads the product to the local sql database. Uploads the
    product id, the name and the price.
    """
    connection, cursor = sql_c.connect_sql()
    sql_query = create_product_query(product)
    cursor.execute(sql_query)
    connection.commit()
    sql_c.disconnect_sql(connection, cursor)


def upload_all_products():
    """Loads all products from the local mongodb database."""
    database = mdb_c.connect_mdb()
    products_collection = database.products
    sql_connection, sql_cursor = sql_c.connect_sql()

    for product in list(products_collection.find()):
        sql_query, format_values = create_product_query(product)

        sql_cursor.execute(sql_query, format_values)
        print(sql_query, format_values)
    sql_connection.commit()
    sql_c.disconnect_sql(sql_connection, sql_cursor)


if __name__ == '__main__':
    upload_all_products()
