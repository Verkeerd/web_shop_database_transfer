# Web_shop_database_transfer
A repository dedicated to transferring data supporting a web-shop from a mongodb database to a sql database. 
This project is made as an assignment for the course structured programming. 
MongoDB, PostgreSQL and PGAdmin4 are used with this project.

Authors: Kasper Sikkema, Daan Kleijn, Marnix Wesseling, Susan Bruggeling

# Installation
We assume you already have access to the mongodb database and have transferred this to a local mongo server.

Clone this repository.
Install pgadmin. Create a local database and run the file make_web_shop_simple.ddl with the query tool in pgadmin.
You are now ready use this project.

# Design
This is the physical datamodel of the SQL web-shop database:

![web_shop_physical_datamodel](https://user-images.githubusercontent.com/96492291/158082661-25111f16-acdf-493c-a097-8c7961251d29.png)

We have chosen for this datastructure because we felt that we only needed the product_id, product_name and 
selling_price for all products in order to complete all assignments. All other data would have been redundant and 
thus not desired. The product_name and selling_price can both be nullable, because this data can be incomplete in 
the original mongoDB database.

# Assignments
The assignments for FA2 are completed in the following files:
- Assignments 2.a are completed in test_read_data_from_mdb.py
- Assignment 2.c.1 is completed in load_data_sql.py
- Assignment 2.c.2 is completed in mean_price_products.py
- Assignment 2.c.3 is completed in random_and_absolute_difference_products.py

# Contributions
This project is made as an assignment and is not open for contribution outside our project group.
There is no hierarchy in our project group so there are no rules regarding pushing and pulling. 
Please hold yourself to a clean code etiquette when you code for this project.
 
