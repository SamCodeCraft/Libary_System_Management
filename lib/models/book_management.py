# library/book_management.py
from sqlalchemy.orm.exc import NoResultFound
from database import Session
from library.models import Book, Author

def add_book():
    """Add a new book"""
    session = Session()
    title = input("Enter book title: ")
    author_name = input("Enter author name: ")
    category = input("Enter book category: ")
    available_copies = int(input("Enter number of available copies: "))

    # Check if author exists, otherwise add author
    try:
        author = session.query(Author).filter_by(name=author_name).one()
    except NoResultFound:
        author = Author(name=author_name)
        session.add(author)
        session.commit()

    book = Book(title=title, author_id=author.id, category=category, available_copies=available_copies)
    session.add(book)
    session.commit()
    print(f"Book {title} added successfully.")
    session.close()

def edit_book():
    """Edit a book's details"""
    session = Session()
    book_id = int(input("Enter book ID to edit: "))
    try:
        book = session.query(Book).filter_by(id=book_id).one()
        book.title = input(f"Enter new title (current: {book.title}): ") or book.title
        author_name = input(f"Enter new author name (current: {book.author.name}): ") or book.author.name
        book.category = input(f"Enter new category
