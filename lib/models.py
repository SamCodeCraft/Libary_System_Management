# library/models.py
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Float
from sqlalchemy.orm import relationship, backref
from database import Base

class User(Base):
    """User model"""
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    role = Column(String(20), nullable=False)

    transactions = relationship("Transaction", backref="user")

class Book(Base):
    """Book model"""
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'), nullable=False)
    category = Column(String(100), nullable=False)
    available_copies = Column(Integer, nullable=False)

    author = relationship("Author", backref=backref("books", lazy='dynamic'))
    transactions = relationship("Transaction", backref="book")

class Author(Base):
    """Author model"""
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)

class Transaction(Base):
    """Transaction model"""
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey('books.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    borrow_date = Column(Date, nullable=False)
    due_date = Column(Date, nullable=False)
    return_date = Column(Date)
    fine = Column(Float)
