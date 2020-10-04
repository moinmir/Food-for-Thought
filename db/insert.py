#!/usr/bin/env python
# insert.py

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

def create_user_account(params):
    connection, cursor = _connect()
    
    statement = "INSERT INTO users (username, password, email) \
        VALUES (%s, %s, %s)"
    values = (params['username'], params['password'], params['email'])
    cursor.execute(statement, values)
    connection.commit()

    cursor.close()
    connection.close()

#-----------------------------------------------------------------------

def create_restaurant_account(params):
    connection, cursor = _connect()

    statement = "INSERT INTO restaurants (username, password, email) \
        VALUES (%s, %s, %s)"
    values = (params['username'], params['password'], params['email'])
    cursor.execute(statement, values)
    connection.commit()

    cursor.close()
    connection.close()

#-----------------------------------------------------------------------

def create_restaurant_profile(username, params):
    connection, cursor = _connect()

    statement = "INSERT INTO profiles (restaurant_id, name, description, icon_url, meal_cost, street, \
        city, state, zip, lat, long) \
        VALUES ((SELECT id FROM restaurants WHERE username=%s), %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (username, params['name'], params['description'], params['icon_url'], params['meal_cost'], 
        params['street'], params['city'], params['state'], params['zip'], params['lat'], params['long'])
    cursor.execute(statement, values)
    connection.commit()

    cursor.close()
    connection.close()

#-----------------------------------------------------------------------

def create_transaction(donor_username, restaurant_username, params):
    connection, cursor = _connect()

    statement = "INSERT INTO transactions (user_id, restaurant_id, num_meals, amount) \
        VALUES ((SELECT id FROM users WHERE username=%s), \
        (SELECT id FROM restaurants WHERE username=%s), %s, %s)"
    values = (donor_username, restaurant_username, params['num_meals'], params['amount'])
    cursor.execute(statement, values)
    connection.commit()

    cursor.close()
    connection.close()

#-----------------------------------------------------------------------------------------------------------------

# testing
if __name__ == '__main__':
    create_user_account({'username':'jdoe', 'password':'passwd', 'email':'jdoe@gmail.com'})
    create_restaurant_account({'username':'titosPizz', 'password':'pizza', 'email':'titos@aol.com'})
    create_restaurant_profile('titosPizz', {'name':'Tito\'s Pizza', 'description': 'Seeking donations to deliver \
    pizzas to NYU Medical Center', 'icon_url':'pic.com', 'meal_cost':5.25, 'street':'5th Ave', 'city':'New York', 
    'state':'NY', 'zip':'10001', 'lat':123.2, 'long':15.15})
    create_transaction('jdoe', 'titosPizz', {'num_meals':3, 'amount':15.75})
