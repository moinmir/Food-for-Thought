#!/usr/bin/env python
# create.py

#-----------------------------------------------------------------------

from os import path
from sys import argv, stderr, exit
from psycopg2 import connect

#-----------------------------------------------------------------------

def main(argv):

    if len(argv) != 1:
        print("Usage: python create.py", file=stderr)
        exit(1)

    connection = connect(
        host='localhost',
        port=5432,
        password='ivyhacks',
        database='foodforthought'
    )

    cursor = connection.cursor()

    #-------------------------------------------------------------------

    # users table
    cursor.execute("DROP TABLE IF EXISTS users")
    cursor.execute("CREATE TABLE users ( \
        id serial PRIMARY KEY, \
        username TEXT UNIQUE NOT NULL, \
        password TEXT UNIQUE NOT NULL, \
        email TEXT NOT NULL, \
        created_at TIMESTAMP DEFAULT NOW())")

    #-------------------------------------------------------------------

    # restaurants table
    cursor.execute("DROP TABLE IF EXISTS restaurants")
    cursor.execute("CREATE TABLE restaurants ( \
        id serial PRIMARY KEY, \
        username TEXT UNIQUE NOT NULL, \
        password TEXT UNIQUE NOT NULL, \
        email TEXT NOT NULL, \
        created_at TIMESTAMP DEFAULT NOW())")

    #-------------------------------------------------------------------

    # profiles table
    cursor.execute("DROP TABLE IF EXISTS profiles")
    cursor.execute("CREATE TABLE profiles ( \
        restaurant_id INTEGER PRIMARY KEY, \
        name TEXT, \
        description TEXT, \
        icon_url TEXT, \
        meal_cost REAL, \
        street TEXT, \
        city TEXT, \
        state TEXT, \
        zip TEXT, \
        lat REAL, \
        long REAL)")

    #-------------------------------------------------------------------

    # transactions table
    cursor.execute("DROP TABLE IF EXISTS transactions")
    cursor.execute("CREATE TABLE transactions ( \
        id serial PRIMARY KEY, \
        user_id INTEGER NOT NULL, \
        restaurant_id INTEGER NOT NULL, \
        num_meals INTEGER, \
        amount REAL, \
        created_at TIMESTAMP DEFAULT NOW())")

    #-------------------------------------------------------------------

    connection.commit()

    cursor.close()
    connection.close()

#-----------------------------------------------------------------------

if __name__ == '__main__':
    main(argv)