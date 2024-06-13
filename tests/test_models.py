import unittest
import sqlite3
from models.user import User
from models.book import Book
from models.transaction import Transaction
from models.author import Author
from database.connection import get_connection
from database.setup import setup_database

class TestModels(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Create tables for testing
        setup_database()

    def setUp(self):
        # Clear the database before each test
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute('DELETE FROM transactions')
        cursor.execute('DELETE FROM users')
        cursor.execute('DELETE FROM books')
        cursor.execute('DELETE FROM authors')
        connection.commit()
        connection.close()

    def test_user_crud(self):
        # Create User
        user = User(name='John Doe', email='john@example.com', role='admin')
        user.create()
        users = User.get_all()
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].name, 'John Doe')

        # Find User by ID
        user_id = users[0].id
        user = User.find_by_id(user_id)
        self.assertIsNotNone(user)
        self.assertEqual(user.name, 'John Doe')

        # Delete User
        User.delete(user_id)
        users = User.get_all()
        self.assertEqual(len(users), 0)

    def test_book_crud(self):
        # Create Book
        book = Book(title='1984', author='George Orwell', category='Dystopian')
        book.create()
        books = Book.get_all()
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0].title, '1984')

        # Find Book by ID
        book_id = books[0].id
        book = Book.find_by_id(book_id)
        self.assertIsNotNone(book)
        self.assertEqual(book.title, '1984')

        # Delete Book
        Book.delete(book_id)
        books = Book.get_all()
        self.assertEqual(len(books), 0)

    def test_author_crud(self):
        # Create Author
        author = Author(name='George Orwell')
        author.create()
        authors = Author.get_all()
        self.assertEqual(len(authors), 1)
        self.assertEqual(authors[0].name, 'George Orwell')

        # Find Author by ID
        author_id = authors[0].id
        author = Author.find_by_id(author_id)
        self.assertIsNotNone(author)
        self.assertEqual(author.name, 'George Orwell')

        # Delete Author
        Author.delete(author_id)
        authors = Author.get_all()
        self.assertEqual(len(authors), 0)

    def test_transaction_crud(self):
        # Create User and Book
        user = User(name='John Doe', email='john@example.com', role='admin')
        user.create()
        author = Author(name='George Orwell')
        author.create()
        book = Book(title='1984', author_id=author.id, category='Dystopian', available_copies=5)
        book.create()

        # Create Transaction
        users = User.get_all()
        books = Book.get_all()
        transaction = Transaction(
            book_id=books[0].id,
            user_id=users[0].id,
            borrow_date='2023-01-01',
            due_date='2023-01-15',
            return_date='2023-01-10',
            fine=0.0
        )
        transaction.create()
        transactions = Transaction.get_all()
        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0].book_id, books[0].id)

        # Find Transaction by ID
        transaction_id = transactions[0].id
        transaction = Transaction.find_by_id(transaction_id)
        self.assertIsNotNone(transaction)
        self.assertEqual(transaction.book_id, books[0].id)

        # Delete Transaction
        Transaction.delete(transaction_id)
        transactions = Transaction.get_all()
        self.assertEqual(len(transactions), 0)

if __name__ == '__main__':
    unittest.main()
