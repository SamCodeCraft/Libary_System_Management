import sqlite3
from connection import get_db_connection

class Transaction:
    def __init__(self, id=None, book_id=None, user_id=None, borrow_date=None, due_date=None, return_date=None, fine=None):
        self.id = id
        self.book_id = book_id
        self.user_id = user_id
        self.borrow_date = borrow_date
        self.due_date = due_date
        self.return_date = return_date
        self.fine = fine

    @classmethod
    def create_table(cls):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY,
                book_id INTEGER,
                user_id INTEGER,
                borrow_date DATE,
                due_date DATE,
                return_date DATE,
                fine REAL,
                FOREIGN KEY (book_id) REFERENCES books(id),
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
        ''')
        connection.commit()
        connection.close()

    def create(self):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute('''
            INSERT INTO transactions (book_id, user_id, borrow_date, due_date, return_date, fine) VALUES (?, ?, ?, ?, ?, ?)
        ''', (self.book_id, self.user_id, self.borrow_date, self.due_date, self.return_date, self.fine))
        connection.commit()
        connection.close()

    @classmethod
    def get_all(cls):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM transactions')
        transactions = cursor.fetchall()
        connection.close()
        return [cls(*transaction) for transaction in transactions]

    @classmethod
    def find_by_id(cls, id):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM transactions WHERE id = ?', (id,))
        transaction = cursor.fetchone()
        connection.close()
        if transaction:
            return cls(*transaction)
        return None

    @classmethod
    def delete(cls, id):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute('DELETE FROM transactions WHERE id = ?', (id,))
        connection.commit()
        connection.close()
