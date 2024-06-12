import sqlite3
from connection import DATABASE

class Author:
    def __init__(self, id, name):
        self._id = id
        self._name = name

    # Create a new author in the database
    def add_author(self, name):
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO authors (name) VALUES (?)", (name,))
        conn.commit()
        conn.close()

    # Retrieve an author by their ID
    def get_author(self, author_id):
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM authors WHERE id = ?", (author_id,))
        author = cursor.fetchone()
        conn.close()
        return author

    # Retrieve all authors from the database
    def get_all_authors(self):
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM authors")
        authors = cursor.fetchall()
        conn.close()
        return authors

    # Update author information
    def update_author(self, author_id, name):
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("UPDATE authors SET name = ? WHERE id = ?", (name, author_id))
        conn.commit()
        conn.close()

    # Delete an author from the database
    def delete_author(self, author_id):
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM authors WHERE id = ?", (author_id,))
        conn.commit()
        conn.close()
