# Web_shop_database_transfer
A repository dedicated to transfering data supporting a webshop from a mongodb database to an sql database. 
This project is made as an assignment for the course structured programming. 
We are using PostgreSQL and PGAdmin 

# Installation
We assumes you already have access to the mongodb database and have transferred this to a local mongo server.

Clone this repository.
Install pgadmin. Create a local database and run the file make_web_shop_simple.ddl with the query tool in pgadmin.
You are now ready use this project.

# Design
This is the phisical datamodel of the SQL Webshop Database:

![web_shop_physical_datamodel](https://user-images.githubusercontent.com/96492291/158082661-25111f16-acdf-493c-a097-8c7961251d29.png)

We have chosen for this datastructure because we felt that we only needed the product_id, product_name and 
current_price for all products in order to complete all assignments. All other data would have been redundant and 
thus not desired. The product_name and current_price can both be nullable, because this data can be incomplete in 
the original mongoDB database.

# Assignments
The assignments for FA2 are completed in the following files:
- Assingments 2.a is completed in test_read_data_from_mdb.py
- Assignment 2.c.1 is completed in load_data_sql.py
- Assignment 2.c.2 is completed in mean_price_products.py
- Assignment 2.c.3 is completed in random_and_absolute_difference_products.py

# Contributions
This project is made as an assignment and is not open for contribution outside of our project group.
There is no hiarchy in our project group so there are no rules regarding pushing and pulling. 
Please hold yourself to a clean code etiquette when you code for this project.
 
