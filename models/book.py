import sqlite3
from connection import DATABASE

class Book:
    def __init__(self, id=None, title=None, author_id=None, category=None, available_copies=None):
        self._id = id
        self._title = title
        self._author_id = author_id
        self._category = category
        self._available_copies = available_copies

    # Create a new book in the database
    def add_book(self, title, author_id, category, available_copies):
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO books (title, author_id, category, available_copies) VALUES (?, ?, ?, ?)",
                       (title, author_id, category, available_copies))
        conn.commit()
        conn.close()

    # Retrieve a book by its ID
    def get_book(self, book_id):
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books WHERE id = ?", (book_id,))
        book = cursor.fetchone()
        conn.close()
        return book

    # Retrieve all books from the database
    def get_all_books(self):
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books")
        books = cursor.fetchall()
        conn.close()
        return books

    # Update book information
    def update_book(self, book_id, title=None, author_id=None, category=None, available_copies=None):
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        if title:
            cursor.execute("UPDATE books SET title = ? WHERE id = ?", (title, book_id))
        if author_id:
            cursor.execute("UPDATE books SET author_id = ? WHERE id = ?", (author_id, book_id))
        if category:
            cursor.execute("UPDATE books SET category = ? WHERE id = ?", (category, book_id))
        if available_copies:
            cursor.execute("UPDATE books SET available_copies = ? WHERE id = ?", (available_copies, book_id))
        conn.commit()
        conn.close()

    # Delete a book from the database
    def delete_book(self, book_id):
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
        conn.commit()
        conn.close()

    # Retrieve author by book
    def get_author_by_book(self, book_id):
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT authors.id, authors.name
            FROM authors
            JOIN books ON authors.id = books.author_id
            WHERE books.id = ?
        """, (book_id,))
        author = cursor.fetchone()
        conn.close()
        return author
