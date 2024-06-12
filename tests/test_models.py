# tests/test_models.py
import unittest
from datetime import datetime, timedelta
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from library.models import Base, User, Book, Author, Transaction

# Create an in-memory SQLite database for testing
engine = create_engine('sqlite:///:memory:')
Session = sessionmaker(bind=engine)

class TestLibraryModels(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up the test database schema"""
        Base.metadata.create_all(engine)

    def setUp(self):
        """Create a new session for each test"""
        self.session = Session()

        # Add sample data for testing
        self.author = Author(name="Sample Author")
        self.session.add(self.author)
        self.session.commit()

        self.book = Book(title="Sample Book", author_id=self.author.id, category="Fiction", available_copies=3)
        self.session.add(self.book)
        self.session.commit()

        self.user = User(name="Sample User", email="user@example.com", role="patron")
        self.session.add(self.user)
        self.session.commit()

    def tearDown(self):
        """Clean up after each test"""
        self.session.query(Transaction).delete()
        self.session.query(Book).delete()
        self.session.query(Author).delete()
        self.session.query(User).delete()
        self.session.commit()
        self.session.close()

    def test_user_creation(self):
        """Test creating a user"""
        user = User(name="Test User", email="testuser@example.com", role="patron")
        self.session.add(user)
        self.session.commit()

        found_user = self.session.query(User).filter_by(email="testuser@example.com").one()
        self.assertEqual(found_user.name, "Test User")
        self.assertEqual(found_user.role, "patron")

    def test_book_creation(self):
        """Test creating a book"""
        book = Book(title="New Book", author_id=self.author.id, category="Non-Fiction", available_copies=5)
        self.session.add(book)
        self.session.commit()

        found_book = self.session.query(Book).filter_by(title="New Book").one()
        self.assertEqual(found_book.category, "Non-Fiction")
        self.assertEqual(found_book.available_copies, 5)

    def test_author_creation(self):
        """Test creating an author"""
        author = Author(name="New Author")
        self.session.add(author)
        self.session.commit()

        found_author = self.session.query(Author).filter_by(name="New Author").one()
        self.assertEqual(found_author.name, "New Author")

    def test_transaction_creation(self):
        """Test creating a transaction"""
        transaction = Transaction(book_id=self.book.id, user_id=self.user.id, borrow_date=datetime.now(), due_date=datetime.now() + timedelta(days=14))
        self.session.add(transaction)
        self.session.commit()

        found_transaction = self.session.query(Transaction).filter_by(user_id=self.user.id).one()
        self.assertEqual(found_transaction.book_id, self.book.id)
        self.assertEqual(found_transaction.user_id, self.user.id)

    def test_book_borrow(self):
        """Test borrowing a book"""
        initial_copies = self.book.available_copies

        transaction = Transaction(book_id=self.book.id, user_id=self.user.id, borrow_date=datetime.now(), due_date=datetime.now() + timedelta(days=14))
        self.book.available_copies -= 1
        self.session.add(transaction)
        self.session.commit()

        found_book = self.session.query(Book).filter_by(id=self.book.id).one()
        self.assertEqual(found_book.available_copies, initial_copies - 1)

    def test_book_return(self):
        """Test returning a book"""
        transaction = Transaction(book_id=self.book.id, user_id=self.user.id, borrow_date=datetime.now(), due_date=datetime.now() + timedelta(days=14))
        self.session.add(transaction)
        self.session.commit()

        initial_copies = self.book.available_copies

        # Simulate returning the book
        transaction.return_date = datetime.now()
        self.book.available_copies += 1
        self.session.commit()

        found_book = self.session.query(Book).filter_by(id=self.book.id).one()
        self.assertEqual(found_book.available_copies, initial_copies + 1)

    def test_overdue_fine(self):
        """Test calculating fines for overdue books"""
        borrow_date = datetime.now() - timedelta(days=20)
        due_date = borrow_date + timedelta(days=14)
        transaction = Transaction(book_id=self.book.id, user_id=self.user.id, borrow_date=borrow_date, due_date=due_date)
        self.session.add(transaction)
        self.session.commit()

        # Simulate returning the book late
        transaction.return_date = datetime.now()
        days_overdue = (transaction.return_date - transaction.due_date).days
        transaction.fine = days_overdue * 0.5  # $0.5 per day fine
        self.session.commit()

        found_transaction = self.session.query(Transaction).filter_by(id=transaction.id).one()
        self.assertEqual(found_transaction.fine, days_overdue * 0.5)

if __name__ == '__main__':
    unittest.main()
