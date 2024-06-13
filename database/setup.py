import sqlite3
from database.connection import get_connection

def setup_database():
    """
    Sets up the database by creating the necessary tables.
    """
    connection = get_connection()
    cursor = connection.cursor()

    # Create Users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            role TEXT NOT NULL
        )
    ''')

    # Create Authors table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Authors (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        )
    ''')

    # Create Books table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Books (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            author_id INTEGER NOT NULL,
            category TEXT NOT NULL,
            available_copies INTEGER NOT NULL,
            FOREIGN KEY (author_id) REFERENCES Authors(id)
        )
    ''')

    # Create Transactions table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Transactions (
            id INTEGER PRIMARY KEY,
            book_id INTEGER NOT NULL,
            user_id INTEGER NOT NULL,
            borrow_date DATE NOT NULL,
            due_date DATE NOT NULL,
            return_date DATE,
            fine REAL,
            FOREIGN KEY (book_id) REFERENCES Books(id),
            FOREIGN KEY (user_id) REFERENCES Users(id)
        )
    ''')

    connection.commit()
    connection.close()

if __name__ == '__main__':
    setup_database()
    print("Database setup complete.")
