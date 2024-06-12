# models/book_management.py
import sqlite3
from datetime import datetime

DATABASE = 'library.db'

def get_connection():
    """Establish a connection to the SQLite database"""
    conn = sqlite3.connect(DATABASE)
    return conn

# Create
def add_book(title, author_id, category, available_copies):
    """Add a new book to the database"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO books (title, author_id, category, available_copies)
        VALUES (?, ?, ?, ?)
    ''', (title, author_id, category, available_copies))
    conn.commit()
    conn.close()

# Read
def get_book(book_id):
    """Retrieve a book from the database by its ID"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM books WHERE id = ?', (book_id,))
    book = cursor.fetchone()
    conn.close()
    return book

def get_all_books():
    """Retrieve all books from the database"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM books')
    books = cursor.fetchall()
    conn.close()
    return books

# Update
def update_book(book_id, title=None, author_id=None, category=None, available_copies=None):
    """Update the details of a book"""
    conn = get_connection()
    cursor = conn.cursor()
    query = 'UPDATE books SET '
    params = []

    if title is not None:
        query += 'title = ?, '
        params.append(title)
    if author_id is not None:
        query += 'author_id = ?, '
        params.append(author_id)
    if category is not None:
        query += 'category = ?, '
        params.append(category)
    if available_copies is not None:
        query += 'available_copies = ?, '
        params.append(available_copies)

    query = query.rstrip(', ')
    query += ' WHERE id = ?'
    params.append(book_id)

    cursor.execute(query, tuple(params))
    conn.commit()
    conn.close()

# Delete
def delete_book(book_id):
    """Delete a book from the database by its ID"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM books WHERE id = ?', (book_id,))
    conn.commit()
    conn.close()
