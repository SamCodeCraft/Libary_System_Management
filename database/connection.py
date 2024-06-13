# database/connection.py

print("Loading connection.py")

import sqlite3

def get_connection():
    print("Creating database connection")
    return sqlite3.connect('library.db')
