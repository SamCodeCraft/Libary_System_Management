import unittest
from models.author import Author
from models.book import Book
from models.transaction import Transaction
from models.user import User

class TestLibraryManagementSystem(unittest.TestCase):

    def test_author_crud_operations(self):
        author = Author()
        author.add_author("Jane Austen")
        result = author.get_all_authors()
        self.assertIn(("Jane Austen",), result)
        author_info = author.get_author(result[0][0])
        self.assertEqual(author_info[1], "Jane Austen")
        author.update_author(result[0][0], "Jane A.")
        self.assertEqual(author.get_author(result[0][0])[1], "Jane A.")
        author.delete_author(result[0][0])
        self.assertEqual(author.get_all_authors(), [])

    def test_book_crud_operations(self):
        book = Book()
        book.add_book("Pride and Prejudice", 1, "Fiction", 5)
        result = book.get_all_books()
        self.assertIn(("Pride and Prejudice", 1, "Fiction", 5), result)
        book_info = book.get_book(result[0][0])
        self.assertEqual(book_info[1], "Pride and Prejudice")
        book.update_book(result[0][0], "Pride & Prejudice")
        self.assertEqual(book.get_book(result[0][0])[1], "Pride & Prejudice")
        book.delete_book(result[0][0])
        self.assertEqual(book.get_all_books(), [])

    def test_transaction_crud_operations(self):
        transaction = Transaction()
        transaction.add_transaction(1, 1, "2024-01-01", "2024-02-01")
        result = transaction.get_all_transactions()
        self.assertIn((1, 1, "2024-01-01", "2024-02-01", None, 0.0), result)
        transaction_info = transaction.get_transaction(result[0][0])
        self.assertEqual(transaction_info[1], 1)
        transaction.update_transaction(result[0][0], return_date="2024-01-15", fine=10.0)
        self.assertEqual(transaction.get_transaction(result[0][0])[4], "2024-01-15")
        transaction.delete_transaction(result[0][0])
        self.assertEqual(transaction.get_all_transactions(), [])

    def test_user_crud_operations(self):
        user = User()
        user.add_user("John Doe", "john@example.com", "member")
        result = user.get_all_users()
        self.assertIn(("John Doe", "john@example.com", "member"), result)
        user_info = user.get_user(result[0][0])
        self.assertEqual(user_info[1], "John Doe")
        user.update_user(result[0][0], email="john.doe@example.com")
        self.assertEqual(user.get_user(result[0][0])[2], "john.doe@example.com")
        user.delete_user(result[0][0])
        self.assertEqual(user.get_all_users(), [])

    def test_relationship_methods(self):
        author = Author()
        author.add_author("George Orwell")
        author_id = author.get_all_authors()[0][0]

        book = Book()
        book.add_book("1984", author_id, "Dystopian", 10)
        book_id = book.get_all_books()[0][0]

        user = User()
        user.add_user("Alice", "alice@example.com", "member")
        user_id = user.get_all_users()[0][0]

        transaction = Transaction()
        transaction.add_transaction(book_id, user_id, "2024-01-01", "2024-02-01")
        transaction_id = transaction.get_all_transactions()[0][0]

        books_by_author = author.get_books_by_author(author_id)
        self.assertEqual(books_by_author[0][1], "1984")

        author_by_book = book.get_author_by_book(book_id)
        self.assertEqual(author_by_book[1], "George Orwell")

        user_by_transaction = transaction.get_user_by_transaction(transaction_id)
        self.assertEqual(user_by_transaction[1], "Alice")

        book_by_transaction = transaction.get_book_by_transaction(transaction_id)
        self.assertEqual(book_by_transaction[1], "1984")

        transactions_by_user = user.get_transactions_by_user(user_id)
        self.assertEqual(transactions_by_user[0][1], book_id)

if __name__ == '__main__':
    unittest.main()
