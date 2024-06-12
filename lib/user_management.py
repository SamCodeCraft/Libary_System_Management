# library/user_management.py
from sqlalchemy.orm.exc import NoResultFound
from database import Session
from library.models import User

def register_user():
    """Register a new user"""
    session = Session()
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    role = input("Enter your role (admin/patron): ")

    user = User(name=name, email=email, role=role)
    session.add(user)
    session.commit()
    print(f"User {name} registered successfully.")
    session.close()

def login_user():
    """Login a user"""
    session = Session()
    email = input("Enter your email: ")
    try:
        user = session.query(User).filter_by(email=email).one()
        print(f"Welcome, {user.name}!")
    except NoResultFound:
        print("User not found.")
    session.close()

def view_profile():
    """View user profile"""
    session = Session()
    email = input("Enter your email: ")
    try:
        user = session.query(User).filter_by(email=email).one()
        print(f"Name: {user.name}\nEmail: {user.email}\nRole: {user.role}")
    except NoResultFound:
        print("User not found.")
    session.close()
