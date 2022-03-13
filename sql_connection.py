import psycopg2


def connect_sql():
    """Connects to the local PostgreSQL database."""
    connection = None

    try:
        # establishes the  database connection
        connection = psycopg2.connect(host='localhost',
                                      database='postgres',
                                      user='postgres',
                                      password='uhswqf%#BD078')

        # creates cursor
        cursor = connection.cursor()
        return connection, cursor

    # raises exceptions
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def disconnect_sql(connection, cursor):
    """
    Takes an active cursor and connection for a PostgreSQL database as input. closes the cursor and the connection.
    """
    cursor.close()
    connection.close()
