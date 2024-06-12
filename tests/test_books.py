# tests/test_books.py
import unittest
from library.book_management import add_book, edit_book, delete_book, view_books
from database import Session, engine, Base
from library.models import Book, Author

class TestBookManagement(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up the test database"""
        Base.metadata.create_all(bind=engine)

    def setUp(self):
        """Add sample book to the test database"""
        self.session = Session()
        self.sample_author = Author(name="Test Author")
        self.session.add(self.sample_author)
        self.session.commit()

        self.sample_book = Book(title="Test Book", author=self.sample_author, category="Test Category", available_copies=1)
        self.session.add(self.sample_book)
        self.session.commit()

    def tearDown(self):
        """Clean up after each test"""
        self.session.query(Book).delete()
        self.session.query(Author).delete()
        self.session.commit()
        self.session.close()

    def test_add_book(self):
        # Add test for adding a book
        add_book()
        new_book = self.session.query(Book).filter_by(title="New Test Book").first()
        self.assertIsNotNone(new_book)

    def test_edit_book(self):
        # Add test for editing a book
        edit_book()
        edited_book = self.session.query(Book).filter_by(title="Edited Test Book").first()
        self.assertIsNotNone(edited_book)

    def test_delete_book(self):
        # Add test for deleting a book
        delete_book()
        deleted_book = self.session.query(Book).filter_by(title="Test Book").first()
        self.assertIsNone(deleted_book)

    def test_view_books(self):
        # Add test for viewing books
        view_books()
        books = self.session.query(Book).all()
        self.assertTrue(len(books) > 0)

if __name__ == '__main__':
    unittest.main()
