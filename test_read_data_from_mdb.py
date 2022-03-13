import mongo_connection as mdb_c
import pprint

database = mdb_c.connect_mdb()

session_collection = database.sessions
product_collection = database.products
profile_collection = database.profiles

product_list = [product for product in product_collection.find()]

first_product = product_list[0]

pprint.pprint(first_product)

print(type(first_product))

print('The first product\'s name is: {}'.format(first_product['name']))

for product in product_list:
    if product['name'][0] == 'R':

        print('The first product\'s name beginning with the "R" is: {}'.format(product['name']))
        break

total_all_prices = 0

for product in product_list:
    price = product['price']['selling_price']
    print(price)
    total_all_prices += price

average_price = total_all_prices / len(product_list)

print('The average price of all products in the database is: {}'.format(average_price))
