# setup.py
import sqlite3

def setup_database():
    """Create the database and tables using sqlite3"""
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    # Create Authors table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS authors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')

    # Create Books table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author_id INTEGER NOT NULL,
            category TEXT NOT NULL,
            available_copies INTEGER NOT NULL,
            FOREIGN KEY (author_id) REFERENCES authors(id)
        )
    ''')

    # Create Users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            role TEXT NOT NULL
        )
    ''')

    # Create Transactions table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            book_id INTEGER NOT NULL,
            user_id INTEGER NOT NULL,
            borrow_date DATE NOT NULL,
            due_date DATE NOT NULL,
            return_date DATE,
            fine REAL,
            FOREIGN KEY (book_id) REFERENCES books(id),
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    ''')

    # Optionally, add some initial data
    cursor.execute('INSERT INTO authors (name) VALUES (?)', ("Initial Author",))
    cursor.execute('INSERT INTO books (title, author_id, category, available_copies) VALUES (?, ?, ?, ?)', 
                   ("Initial Book", 1, "Fiction", 10))
    cursor.execute('INSERT INTO users (name, email, role) VALUES (?, ?, ?)', 
                   ("Admin User", "admin@example.com", "admin"))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup_database()
