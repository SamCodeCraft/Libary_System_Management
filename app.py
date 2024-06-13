import sys
from models.user import User
from models.book import Book
from models.author import Author
from models.transaction import Transaction
from database.setup import setup_database

def main_menu():
    print("\nLibrary Management System")
    print("1. User Management")
    print("2. Book Management")
    print("3. Author Management")
    print("4. Transaction Management")
    print("5. Exit")

def user_menu():
    print("\nUser Management")
    print("1. Create User")
    print("2. View All Users")
    print("3. Find User by ID")
    print("4. Delete User")
    print("5. Back to Main Menu")

def book_menu():
    print("\nBook Management")
    print("1. Create Book")
    print("2. View All Books")
    print("3. Find Book by ID")
    print("4. Delete Book")
    print("5. Back to Main Menu")

def author_menu():
    print("\nAuthor Management")
    print("1. Create Author")
    print("2. View All Authors")
    print("3. Find Author by ID")
    print("4. Delete Author")
    print("5. Back to Main Menu")

def transaction_menu():
    print("\nTransaction Management")
    print("1. Create Transaction")
    print("2. View All Transactions")
    print("3. Find Transaction by ID")
    print("4. Delete Transaction")
    print("5. Back to Main Menu")

def handle_user_menu():
    while True:
        user_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter user name: ")
            email = input("Enter user email: ")
            role = input("Enter user role (admin/patron): ")
            user = User(name=name, email=email, role=role)
            user.create()
            print("User created successfully.")
        elif choice == '2':
            users = User.get_all()
            for user in users:
                print(user)
        elif choice == '3':
            user_id = int(input("Enter user ID: "))
            user = User.find_by_id(user_id)
            if user:
                print(user)
            else:
                print("User not found.")
        elif choice == '4':
            user_id = int(input("Enter user ID to delete: "))
            User.delete(user_id)
            print("User deleted successfully.")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def handle_book_menu():
    while True:
        book_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            title = input("Enter book title: ")
            author_id = int(input("Enter author ID: "))
            category = input("Enter book category: ")
            available_copies = int(input("Enter available copies: "))
            book = Book(title=title, author_id=author_id, category=category, available_copies=available_copies)
            book.create()
            print("Book created successfully.")
        elif choice == '2':
            books = Book.get_all()
            for book in books:
                print(book)
        elif choice == '3':
            book_id = int(input("Enter book ID: "))
            book = Book.find_by_id(book_id)
            if book:
                print(book)
            else:
                print("Book not found.")
        elif choice == '4':
            book_id = int(input("Enter book ID to delete: "))
            Book.delete(book_id)
            print("Book deleted successfully.")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def handle_author_menu():
    while True:
        author_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter author name: ")
            author = Author(name=name)
            author.create()
            print("Author created successfully.")
        elif choice == '2':
            authors = Author.get_all()
            for author in authors:
                print(author)
        elif choice == '3':
            author_id = int(input("Enter author ID: "))
            author = Author.find_by_id(author_id)
            if author:
                print(author)
            else:
                print("Author not found.")
        elif choice == '4':
            author_id = int(input("Enter author ID to delete: "))
            Author.delete(author_id)
            print("Author deleted successfully.")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def handle_transaction_menu():
    while True:
        transaction_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            book_id = int(input("Enter book ID: "))
            user_id = int(input("Enter user ID: "))
            borrow_date = input("Enter borrow date (YYYY-MM-DD): ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            return_date = input("Enter return date (YYYY-MM-DD) (leave blank if not returned): ")
            fine = float(input("Enter fine amount: "))
            transaction = Transaction(
                book_id=book_id,
                user_id=user_id,
                borrow_date=borrow_date,
                due_date=due_date,
                return_date=return_date if return_date else None,
                fine=fine
            )
            transaction.create()
            print("Transaction created successfully.")
        elif choice == '2':
            transactions = Transaction.get_all()
            for transaction in transactions:
                print(transaction)
        elif choice == '3':
            transaction_id = int(input("Enter transaction ID: "))
            transaction = Transaction.find_by_id(transaction_id)
            if transaction:
                print(transaction)
            else:
                print("Transaction not found.")
        elif choice == '4':
            transaction_id = int(input("Enter transaction ID to delete: "))
            Transaction.delete(transaction_id)
            print("Transaction deleted successfully.")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    setup_database()
    while True:
        main_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            handle_user_menu()
        elif choice == '2':
            handle_book_menu()
        elif choice == '3':
            handle_author_menu()
        elif choice == '4':
            handle_transaction_menu()
        elif choice == '5':
            print("Exiting the application.")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()