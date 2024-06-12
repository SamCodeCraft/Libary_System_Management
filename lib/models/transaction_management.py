# models/transaction_management.py
import sqlite3
from datetime import datetime, timedelta

DATABASE = 'library.db'

def get_connection():
    """Establish a connection to the SQLite database"""
    conn = sqlite3.connect(DATABASE)
    return conn

# Create
def add_transaction(book_id, user_id, borrow_date, due_date):
    """Add a new transaction to the database"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO transactions (book_id, user_id, borrow_date, due_date)
        VALUES (?, ?, ?, ?)
    ''', (book_id, user_id, borrow_date, due_date))
    conn.commit()
    conn.close()

# Read
def get_transaction(transaction_id):
    """Retrieve a transaction from the database by its ID"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM transactions WHERE id = ?', (transaction_id,))
    transaction = cursor.fetchone()
    conn.close()
    return transaction

def get_all_transactions():
    """Retrieve all transactions from the database"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM transactions')
    transactions = cursor.fetchall()
    conn.close()
    return transactions

# Update
def update_transaction(transaction_id, return_date=None, fine=None):
    """Update the details of a transaction"""
    conn = get_connection()
    cursor = conn.cursor()
    query = 'UPDATE transactions SET '
    params = []

    if return_date is not None:
        query += 'return_date = ?, '
        params.append(return_date)
    if fine is not None:
        query += 'fine = ?, '
        params.append(fine)

    query = query.rstrip(', ')
    query += ' WHERE id = ?'
    params.append(transaction_id)

    cursor.execute(query, tuple(params))
    conn.commit()
    conn.close()

# Delete
def delete_transaction(transaction_id):
    """Delete a transaction from the database by its ID"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM transactions WHERE id = ?', (transaction_id,))
    conn.commit()
    conn.close()
