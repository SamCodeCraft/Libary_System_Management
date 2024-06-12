import sqlite3
from connection import DATABASE

class Transaction:
    def __init__(self, id, book_id, user_id, borrow_date, due_date, return_date=None, fine=0.0):
        self._id = id
        self._book_id = book_id
        self._user_id = user_id
        self._borrow_date = borrow_date
        self._due_date = due_date
        self._return_date = return_date
        self._fine = fine

    # Create a new transaction in the database
    def add_transaction(self, book_id, user_id, borrow_date, due_date, return_date=None, fine=0.0):
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO transactions (book_id, user_id, borrow_date, due_date, return_date, fine) VALUES (?, ?, ?, ?, ?, ?)",
                       (book_id, user_id, borrow_date, due_date, return_date, fine))
        conn.commit()
        conn.close()

    # Retrieve a transaction by its ID
    def get_transaction(self, transaction_id):
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM transactions WHERE id = ?", (transaction_id,))
        transaction = cursor.fetchone()
        conn.close()
        return transaction

    # Retrieve all transactions from the database
    def get_all_transactions(self):
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM transactions")
        transactions = cursor.fetchall()
        conn.close()
        return transactions

    # Update transaction information
    def update_transaction(self, transaction_id, book_id=None, user_id=None, borrow_date=None, due_date=None, return_date=None, fine=None):
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        if book_id:
            cursor.execute("UPDATE transactions SET book_id = ? WHERE id = ?", (book_id, transaction_id))
        if user_id:
            cursor.execute("UPDATE transactions SET user_id = ? WHERE id = ?", (user_id, transaction_id))
        if borrow_date:
            cursor.execute("UPDATE transactions SET borrow_date = ? WHERE id = ?", (borrow_date, transaction_id))
        if due_date:
            cursor.execute("UPDATE transactions SET due_date = ? WHERE id = ?", (due_date, transaction_id))
        if return_date:
            cursor.execute("UPDATE transactions SET return_date = ? WHERE id = ?", (return_date, transaction_id))
        if fine:
            cursor.execute("UPDATE transactions SET fine = ? WHERE id = ?", (fine, transaction_id))
        conn.commit()
        conn.close()

    # Delete a transaction from the database
    def delete_transaction(self, transaction_id):
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM transactions WHERE id = ?", (transaction_id,))
        conn.commit()
        conn.close()
