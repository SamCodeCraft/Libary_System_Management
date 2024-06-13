import sqlite3
from database.connection import get_connection

class User:
    def __init__(self, id=None, name=None, email=None, role=None):
        self.id = id
        self.name = name
        self.email = email
        self.role = role

    @classmethod
    def create_table(cls):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                role TEXT NOT NULL
            )
        ''')
        connection.commit()
        connection.close()

    def create(self):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute('''
            INSERT INTO users (name, email, role) VALUES (?, ?, ?)
        ''', (self.name, self.email, self.role))
        connection.commit()
        connection.close()

    @classmethod
    def get_all(cls):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM users')
        users = cursor.fetchall()
        connection.close()
        return [cls(*user) for user in users]

    @classmethod
    def find_by_id(cls, id):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM users WHERE id = ?', (id,))
        user = cursor.fetchone()
        connection.close()
        if user:
            return cls(*user)
        return None

    @classmethod
    def delete(cls, id):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute('DELETE FROM users WHERE id = ?', (id,))
        connection.commit()
        connection.close()
