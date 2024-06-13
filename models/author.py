import sqlite3
from connection import get_db_connection

class Author:
    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name

    # Create a new author in the database
    def create(self):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute(
            'INSERT INTO authors (name) VALUES (?)',
            (self.name,)
        )
        connection.commit()
        self.id = cursor.lastrowid
        connection.close()

    # Get all authors from the database
    @classmethod
    def get_all(cls):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT id, name FROM authors')
        rows = cursor.fetchall()
        connection.close()
        return [cls(id=row[0], name=row[1]) for row in rows]

    # Find an author by ID
    @classmethod
    def find_by_id(cls, author_id):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT id, name FROM authors WHERE id = ?', (author_id,))
        row = cursor.fetchone()
        connection.close()
        if row:
            return cls(id=row[0], name=row[1])
        return None

    # Delete an author from the database
    @classmethod
    def delete(cls, author_id):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute('DELETE FROM authors WHERE id = ?', (author_id,))
        connection.commit()
        connection.close()

    def __str__(self):
        return f'Author(id={self.id}, name={self.name})'
