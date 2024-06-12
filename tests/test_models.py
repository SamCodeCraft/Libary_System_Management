import unittest
from models.User import User
from models.Book import Book
from models.Author import Author
from models.Transaction import Transaction

class TestModels(unittest.TestCase):
    def test_user_operations(self):
        # Test User CRUD operations
        # Add a user
        User().add_user("John Doe", "john@example.com", "patron")
        user = User().get_user(1)
        self.assertIsNotNone(user)
        self.assertEqual(user[1], "John Doe")
        self.assertEqual(user[2], "john@example.com")
        self.assertEqual(user[3], "patron")

        # Update user information
        User().update_user(1, name="Jane Doe", role="admin")
        user = User().get_user(1)
        self.assertIsNotNone(user)
        self.assertEqual(user[1], "Jane Doe")
        self.assertEqual(user[3], "admin")

        # Delete a user
        User().delete_user(1)
        user = User().get_user(1)
        self.assertIsNone(user)

    def test_book_operations(self):
        # Test Book CRUD operations
        # Add a book
        Book().add_book("Python Programming", 1, "Programming", 10)
        book = Book().get_book(1)
        self.assertIsNotNone(book)
        self.assertEqual(book[1], "Python Programming")
        self.assertEqual(book[2], 1)
        self.assertEqual(book[3], "Programming")
        self.assertEqual(book[4], 10)

        # Update book information
        Book().update_book(1, title="Python Programming 101")
        book = Book().get_book(1)
        self.assertIsNotNone(book)
        self.assertEqual(book[1], "Python Programming 101")

        # Delete a book
        Book().delete_book(1)
        book = Book().get_book(1)
        self.assertIsNone(book)

    def test_author_operations(self):
        # Test Author CRUD operations
        # Add an author
        Author().add_author("John Smith")
        author = Author().get_author(1)
        self.assertIsNotNone(author)
        self.assertEqual(author[1], "John Smith")

        # Update author information
        Author().update_author(1, "Jane Smith")
        author = Author().get_author(1)
        self.assertIsNotNone(author)
        self.assertEqual(author[1], "Jane Smith")

        # Delete an author
        Author().delete_author(1)
        author = Author().get_author(1)
        self.assertIsNone(author)

    def test_transaction_operations(self):
        # Test Transaction CRUD operations
        # Add a transaction
        Transaction().add_transaction(1, 1, "2024-06-12", "2024-07-12")
        transaction = Transaction().get_transaction(1)
        self.assertIsNotNone(transaction)
        self.assertEqual(transaction[1], 1)
        self.assertEqual(transaction[2], 1)
        self.assertEqual(transaction[3], "2024-06-12")
        self.assertEqual(transaction[4], "2024-07-12")

        # Update transaction information
        Transaction().update_transaction(1, due_date="2024-07-15")
        transaction = Transaction().get_transaction(1)
        self.assertIsNotNone(transaction)
        self.assertEqual(transaction[4], "2024-07-15")

        # Delete a transaction
        Transaction().delete_transaction(1)
        transaction = Transaction().get_transaction(1)
        self.assertIsNone(transaction)

if __name__ == '__main__':
    unittest.main()
