import sqlite3
from datetime import datetime, timedelta
from models.book_management import add_book, get_book, get_all_books, update_book, delete_book
from models.user_management import add_user, get_user, get_all_users, update_user, delete_user
from models.transaction_management import add_transaction, get_transaction, get_all_transactions, update_transaction, delete_transaction

DATABASE = 'library.db'

def initialize_db():
    """Initialize the database with required tables"""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # Create Authors table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS authors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')

    # Create Books table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author_id INTEGER NOT NULL,
            category TEXT NOT NULL,
            available_copies INTEGER NOT NULL,
            FOREIGN KEY (author_id) REFERENCES authors(id)
        )
    ''')

    # Create Users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            role TEXT NOT NULL
        )
    ''')

    # Create Transactions table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            book_id INTEGER NOT NULL,
            user_id INTEGER NOT NULL,
            borrow_date DATE NOT NULL,
            due_date DATE NOT NULL,
            return_date DATE,
            fine REAL,
            FOREIGN KEY (book_id) REFERENCES books(id),
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    ''')

    conn.commit()
    conn.close()

def main_menu():
    """Display the main menu"""
    print("Library Management System")
    print("=========================")
    print("1. User Management")
    print("2. Book Management")
    print("3. Borrow/Return Books")
    print("4. Exit")
    choice = input("Enter choice: ")
    return choice

def user_management_menu():
    """Display the user management menu"""
    print("\nUser Management")
    print("1. Add User")
    print("2. View User")
    print("3. View All Users")
    print("4. Update User")
    print("5. Delete User")
    print("6. Back to Main Menu")
    choice = input("Enter choice: ")
    return choice

def book_management_menu():
    """Display the book management menu"""
    print("\nBook Management")
    print("1. Add Book")
    print("2. View Book")
    print("3. View All Books")
    print("4. Update Book")
    print("5. Delete Book")
    print("6. Back to Main Menu")
    choice = input("Enter choice: ")
    return choice

def borrow_return_menu():
    """Display the borrow/return menu"""
    print("\nBorrow/Return Books")
    print("1. Borrow Book")
    print("2. Return Book")
    print("3. View Transactions")
    print("4. Back to Main Menu")
    choice = input("Enter choice: ")
    return choice

def main():
    """Main function to run the CLI"""
    initialize_db()

    while True:
        choice = main_menu()

        if choice == '1':
            while True:
                user_choice = user_management_menu()
                if user_choice == '1':
                    name = input("Enter name: ")
                    email = input("Enter email: ")
                    role = input("Enter role (admin/patron): ")
                    add_user(name, email, role)
                    print("User added successfully.")
                elif user_choice == '2':
                    user_id = int(input("Enter user ID: "))
                    user = get_user(user_id)
                    if user:
                        print(f"User ID: {user[0]}, Name: {user[1]}, Email: {user[2]}, Role: {user[3]}")
                    else:
                        print("User not found.")
                elif user_choice == '3':
                    users = get_all_users()
                    for user in users:
                        print(f"User ID: {user[0]}, Name: {user[1]}, Email: {user[2]}, Role: {user[3]}")
                elif user_choice == '4':
                    user_id = int(input("Enter user ID: "))
                    name = input("Enter new name (leave blank to keep current): ")
                    email = input("Enter new email (leave blank to keep current): ")
                    role = input("Enter new role (admin/patron, leave blank to keep current): ")
                    update_user(user_id, name=name if name else None, email=email if email else None, role=role if role else None)
                    print("User updated successfully.")
                elif user_choice == '5':
                    user_id = int(input("Enter user ID: "))
                    delete_user(user_id)
                    print("User deleted successfully.")
                elif user_choice == '6':
                    break

        elif choice == '2':
            while True:
                book_choice = book_management_menu()
                if book_choice == '1':
                    title = input("Enter title: ")
                    author_id = int(input("Enter author ID: "))
                    category = input("Enter category: ")
                    available_copies = int(input("Enter number of available copies: "))
                    add_book(title, author_id, category, available_copies)
                    print("Book added successfully.")
                elif book_choice == '2':
                    book_id = int(input("Enter book ID: "))
                    book = get_book(book_id)
                    if book:
                        print(f"Book ID: {book[0]}, Title: {book[1]}, Author ID: {book[2]}, Category: {book[3]}, Available Copies: {book[4]}")
                    else:
                        print("Book not found.")
                elif book_choice == '3':
                    books = get_all_books()
                    for book in books:
                        print(f"Book ID: {book[0]}, Title: {book[1]}, Author ID: {book[2]}, Category: {book[3]}, Available Copies: {book[4]}")
                elif book_choice == '4':
                    book_id = int(input("Enter book ID: "))
                    title = input("Enter new title (leave blank to keep current): ")
                    author_id = input("Enter new author ID (leave blank to keep current): ")
                    category = input("Enter new category (leave blank to keep current): ")
                    available_copies = input("Enter new number of available copies (leave blank to keep current): ")
                    update_book(book_id, title=title if title else None, author_id=int(author_id) if author_id else None, category=category if category else None, available_copies=int(available_copies) if available_copies else None)
                    print("Book updated successfully.")
                elif book_choice == '5':
                    book_id = int(input("Enter book ID: "))
                    delete_book(book_id)
                    print("Book deleted successfully.")
                elif book_choice == '6':
                    break

        elif choice == '3':
            while True:
                borrow_choice = borrow_return_menu()
                if borrow_choice == '1':
                    book_id = int(input("Enter book ID: "))
                    user_id = int(input("Enter user ID: "))
                    borrow_date = datetime.now().date()
                    due_date = borrow_date + timedelta(days=14)
                    add_transaction(book_id, user_id, borrow_date, due_date)
                    print("Book borrowed successfully.")
                elif borrow_choice == '2':
                    transaction_id = int(input("Enter transaction ID: "))
                    return_date = datetime.now().date()
                    transaction = get_transaction(transaction_id)
                    if transaction:
                        due_date = datetime.strptime(transaction[4], '%Y-%m-%d').date()
                        fine = max((return_date - due_date).days * 0.5, 0)  # Calculate fine (e.g., $0.5 per day)
                        update_transaction(transaction_id, return_date=return_date, fine=fine)
                        print(f"Book returned successfully. Fine: ${fine:.2f}")
                    else:
                        print("Transaction not found.")
                elif borrow_choice == '3':
                    transactions = get_all_transactions()
                    for transaction in transactions:
                        print(f"Transaction ID: {transaction[0]}, Book ID: {transaction[1]}, User ID: {transaction[2]}, Borrow Date: {transaction[3]}, Due Date: {transaction[4]}, Return Date: {transaction[5]}, Fine: {transaction[6]}")
                elif borrow_choice == '4':
                    break

        elif choice == '4':
            break

if __name__ == "__main__":
    main()
