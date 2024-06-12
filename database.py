# database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import Config

# Create the engine and session
engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)
Base = declarative_base()

def create_database():
    """Create database tables"""
    from library.models import User, Book, Author, Transaction
    Base.metadata.create_all(engine)
