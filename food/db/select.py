#!/usr/bin/env python
# select.py

#-----------------------------------------------------------------------

from psycopg2 import connect

#-----------------------------------------------------------------------

def _connect():
    connection = connect(
        host='localhost',
        port=5432,
        password='ivyhacks',
        database='foodforthought'
    )

    cursor = connection.cursor()
    return connection, cursor

#-----------------------------------------------------------------------

def get_transactions_by_user(username):
    connection, cursor = _connect()

    statement = "SELECT profiles.name, transactions.num_meals, transactions.amount, \
        transactions.created_at FROM users, transactions, profiles \
        WHERE transactions.user_id = users.id AND transactions.restaurant_id = profiles.restaurant_id \
        AND users.username = %s"
    values = (username,)
    cursor.execute(statement, values)
    connection.commit()

    return cursor.fetchall()

    cursor.close()
    connection.close()

#-----------------------------------------------------------------------

def get_transactions_by_restaurant(username):
    connection, cursor = _connect()

    statement = "SELECT transactions.num_meals, transactions.amount, transactions.created_at \
        FROM restaurants, transactions \
        WHERE transactions.restaurant_id = restaurants.id AND restaurants.username = %s"
    values = (username,)
    cursor.execute(statement, values)
    connection.commit()

    return cursor.fetchall()

    cursor.close()
    connection.close()

#-----------------------------------------------------------------------

def user_login(username, password):
    connection, cursor = _connect()

    statement = "SELECT email FROM users WHERE username=%s AND password=%s"
    values = (username, password)
    cursor.execute(statement, values)
    connection.commit()

    return cursor.fetchall()

    cursor.close()
    connection.close()

#-----------------------------------------------------------------------

def restaurant_login(username, password):
    connection, cursor = _connect()

    statement = "SELECT email FROM restaurants WHERE username=%s AND password=%s"
    values = (username, password)
    cursor.execute(statement, values)
    connection.commit()

    return cursor.fetchall()

    cursor.close()
    connection.close()

#-----------------------------------------------------------------------

def get_profile(username):
    connection, cursor = _connect()

    statement = "SELECT name, description, icon_url, meal_cost, street, city, \
        state, zip, lat, long FROM profiles, restaurants \
        WHERE profiles.restaurant_id=restaurants.id AND restaurants.username=%s"
    values = (username,)
    cursor.execute(statement, values)
    connection.commit()

    return cursor.fetchall()

    cursor.close()
    connection.close()

#-----------------------------------------------------------------------

if __name__ == '__main__':
    transactions = get_transactions_by_user('jdoe')
    transactions = get_transactions_by_restaurant('titosPizz')
    email = user_login('jdoe', 'passwd')
    email = restaurant_login('titosPizz', 'pizza')
    profile = get_profile('titosPizz')
    print(profile)