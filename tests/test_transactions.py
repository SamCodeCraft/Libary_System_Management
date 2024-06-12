# tests/test_transactions.py
import unittest
from library.transaction_management import borrow_book, return_book, view_transactions
from database import Session, engine, Base
from library.models import Book, User, Transaction

class TestTransactionManagement(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up the test database"""
        Base.metadata.create_all(bind=engine)

    def setUp(self):
        """Add sample data to the test database"""
        self.session = Session()

        self.sample_user = User(name="Test User", email="test@example.com", role="patron")
        self.session.add(self.sample_user)

        self.sample_book = Book(title="Test Book", category="Test Category", available_copies=1)
        self.session.add(self.sample_book)

        self.sample_transaction = Transaction(book=self.sample_book, user=self.sample_user)
        self.session.add(self.sample_transaction)

        self.session.commit()

    def tearDown(self):
        """Clean up after each test"""
        self.session.query(Transaction).delete()
        self.session.query(Book).delete()
        self.session.query(User).delete()
        self.session.commit()
        self.session.close()

    def test_borrow_book(self):
        # Add test for borrowing a book
        borrow_book()
        borrowed_book = self.session.query(Transaction).filter_by(book_id=self.sample_book.id).first()
        self.assertIsNotNone(borrowed_book)

    def test_return_book(self):
        # Add test for returning a book
        return_book()
        returned_book = self.session.query(Transaction).filter_by(book_id=self.sample_book.id).first()
        self.assertIsNotNone(returned_book.return_date)

    def test_view_transactions(self):
        # Add test for viewing transactions
        view_transactions()
        transactions = self.session.query(Transaction).all()
        self.assertTrue(len(transactions) > 0)

if __name__ == '__main__':
    unittest.main()
