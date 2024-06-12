# library/transaction_management.py
from datetime import datetime, timedelta
from sqlalchemy.orm.exc import NoResultFound
from database import Session
from library.models import Book, User, Transaction

def borrow_book():
    """Borrow a book"""
    session = Session()
    user_email = input("Enter your email: ")
    book_id = int(input("Enter book ID to borrow: "))

    try:
        user = session.query(User).filter_by(email=user_email).one()
        book = session.query(Book).filter_by(id=book_id).one()

        if book.available_copies > 0:
            borrow_date = datetime.now().date()
            due_date = borrow_date + timedelta(days=14)  # 2 weeks borrowing period
            transaction = Transaction(book=book, user=user, borrow_date=borrow_date, due_date=due_date)
            book.available_copies -= 1

            session.add(transaction)
            session.commit()
            print(f"Book '{book.title}' borrowed successfully. Due date: {due_date}")
        else:
            print("No available copies to borrow.")
    except NoResultFound:
        print("User or book not found.")
    session.close()

def return_book():
    """Return a borrowed book"""
    session = Session()
    transaction_id = int(input("Enter transaction ID: "))

    try:
        transaction = session.query(Transaction).filter_by(id=transaction_id).one()
        if not transaction.return_date:
            transaction.return_date = datetime.now().date()
            days_overdue = (transaction.return_date - transaction.due_date).days
            transaction.fine = days_overdue * 0.5 if days_overdue > 0 else 0  # $0.5 per day fine

            book = transaction.book
            book.available_copies += 1

            session.commit()
            print(f"Book '{book.title}' returned successfully. Fine: ${transaction.fine:.2f}")
        else:
            print("Book already returned.")
    except NoResultFound:
        print("Transaction not found.")
    session.close()

def view_transactions():
    """View all transactions"""
    session = Session()
    transactions = session.query(Transaction).all()
    if transactions:
        for transaction in transactions:
            print(f"ID: {transaction.id}, Book: '{transaction.book.title}', User: {transaction.user.name}, Borrow Date: {transaction.borrow_date}, Due Date: {transaction.due_date}, Return Date: {transaction.return_date}, Fine: ${transaction.fine}")
    else:
        print("No transactions found.")
    session.close()
