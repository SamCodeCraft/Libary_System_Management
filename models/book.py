import sqlite3
from database.connection import get_connection

class Book:
    def __init__(self, id=None, title=None, author=None, category=None):
        self.id = id
        self.title = title
        self.author = author
        self.category = category

    @classmethod
    def create_table(cls):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                category TEXT NOT NULL
            )
        ''')
        connection.commit()
        connection.close()

    def create(self):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute('''
            INSERT INTO books (title, author, category) VALUES (?, ?, ?)
        ''', (self.title, self.author, self.category))
        connection.commit()
        connection.close()

    @classmethod
    def get_all(cls):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM books')
        books = cursor.fetchall()
        connection.close()
        return [cls(*book) for book in books]

    @classmethod
    def find_by_id(cls, id):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM books WHERE id = ?', (id,))
        book = cursor.fetchone()
        connection.close()
        if book:
            return cls(*book)
        return None

    @classmethod
    def delete(cls, id):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute('DELETE FROM books WHERE id = ?', (id,))
        connection.commit()
        connection.close()
