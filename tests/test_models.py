import unittest
import sqlite3
import os
from datetime import datetime, timedelta

# Import the CRUD functions
from models.book_management import add_book, get_book, get_all_books, update_book, delete_book
from models.user_management import add_user, get_user, get_all_users, update_user, delete_user
from models.transaction_management import add_transaction, get_transaction, get_all_transactions, update_transaction, delete_transaction

DATABASE = 'test_library.db'

def setup_test_db():
    """Set up a test database with the required tables"""
    conn = sqlite3.connect(DATABASE)
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

    # Add some initial data
    cursor.execute('INSERT INTO authors (name) VALUES (?)', ("Test Author",))
    cursor.execute('INSERT INTO books (title, author_id, category, available_copies) VALUES (?, ?, ?, ?)',
                   ("Test Book", 1, "Fiction", 5))
    conn.commit()
    conn.close()

class TestLibraryManagement(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up the test database before running tests"""
        if os.path.exists(DATABASE):
            os.remove(DATABASE)
        setup_test_db()

    @classmethod
    def tearDownClass(cls):
        """Clean up the test database after running tests"""
        if os.path.exists(DATABASE):
            os.remove(DATABASE)

    def setUp(self):
        """Set the test database connection"""
        self.conn = sqlite3.connect(DATABASE)
        self.cursor = self.conn.cursor()

    def tearDown(self):
        """Close the test database connection"""
        self.conn.close()

    # Book Management Tests
    def test_add_book(self):
        add_book("New Book", 1, "Non-Fiction", 3)
        book = get_book(2)
        self.assertEqual(book[1], "New Book")
        self.assertEqual(book[3], "Non-Fiction")

    def test_get_all_books(self):
        books = get_all_books()
        self.assertEqual(len(books), 2)

    def test_update_book(self):
        update_book(1, title="Updated Book")
        book = get_book(1)
        self.assertEqual(book[1], "Updated Book")

    def test_delete_book(self):
        delete_book(1)
        book = get_book(1)
        self.assertIsNone(book)

    # User Management Tests
    def test_add_user(self):
        add_user("Test User", "testuser@example.com", "patron")
        user = get_user(1)
        self.assertEqual(user[1], "Test User")
        self.assertEqual(user[2], "testuser@example.com")

    def test_get_all_users(self):
        add_user("Another User", "anotheruser@example.com", "patron")
        users = get_all_users()
        self.assertEqual(len(users), 2)

    def test_update_user(self):
        add_user("Update User", "updateuser@example.com", "patron")
        update_user(1, name="Updated User")
        user = get_user(1)
        self.assertEqual(user[1], "Updated User")

    def test_delete_user(self):
        add_user("Delete User", "deleteuser@example.com", "patron")
        delete_user(1)
        user = get_user(1)
        self.assertIsNone(user)

    # Transaction Management Tests
    def test_add_transaction(self):
        borrow_date = datetime.now().date()
        due_date = borrow_date + timedelta(days=14)
        add_transaction(1, 1, borrow_date, due_date)
        transaction = get_transaction(1)
        self.assertEqual(transaction[1], 1)
        self.assertEqual(transaction[2], 1)

    def test_get_all_transactions(self):
        borrow_date = datetime.now().date()
        due_date = borrow_date + timedelta(days=14)
        add_transaction(1, 1, borrow_date, due_date)
        transactions = get_all_transactions()
        self.assertEqual(len(transactions), 1)

    def test_update_transaction(self):
        borrow_date = datetime.now().date()
        due_date = borrow_date + timedelta(days=14)
        add_transaction(1, 1, borrow_date, due_date)
        return_date = borrow_date + timedelta(days=7)
        update_transaction(1, return_date=return_date, fine=0.0)
        transaction = get_transaction(1)
        self.assertEqual(transaction[5], str(return_date))
        self.assertEqual(transaction[6], 0.0)

    def test_delete_transaction(self):
        borrow_date = datetime.now().date()
        due_date = borrow_date + timedelta(days=14)
        add_transaction(1, 1, borrow_date, due_date)
        delete_transaction(1)
        transaction = get_transaction(1)
        self.assertIsNone(transaction)

if __name__ == "__main__":
    unittest.main()
