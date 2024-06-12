# main.py
from library import user_management, book_management, transaction_management

def main_menu():
    """Main menu for the Library Management System"""
    while True:
        print("\nLibrary Management System")
        print("1. User Management")
        print("2. Book Management")
        print("3. Transactions")
        print("4. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            user_menu()
        elif choice == '2':
            book_menu()
        elif choice == '3':
            transaction_menu()
        elif choice == '4':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice, please try again.")

def user_menu():
    """Menu for user management"""
    while True:
        print("\nUser Management")
        print("1. Register User")
        print("2. Login User")
        print("3. View Profile")
        print("4. Back to Main Menu")

        choice = input("Select an option: ")

        if choice == '1':
            user_management.register_user()
        elif choice == '2':
            user_management.login_user()
        elif choice == '3':
            user_management.view_profile()
        elif choice == '4':
            break
        else:
            print("Invalid choice, please try again.")

def book_menu():
    """Menu for book management"""
    while True:
        print("\nBook Management")
        print("1. Add Book")
        print("2. Edit Book")
        print("3. Delete Book")
        print("4. View Books")
        print("5. Back to Main Menu")

        choice = input("Select an option: ")

        if choice == '1':
            book_management.add_book()
        elif choice == '2':
            book_management.edit_book()
        elif choice == '3':
            book_management.delete_book()
        elif choice == '4':
            book_management.view_books()
        elif choice == '5':
            break
        else:
            print("Invalid choice, please try again.")

def transaction_menu():
    """Menu for transaction management"""
    while True:
        print("\nTransaction Management")
        print("1. Borrow Book")
        print("2. Return Book")
        print("3. View Transactions")
        print("4. Back to Main Menu")

        choice = input("Select an option: ")

        if choice == '1':
            transaction_management.borrow_book()
        elif choice == '2':
            transaction_management.return_book()
        elif choice == '3':
            transaction_management.view_transactions()
        elif choice == '4':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main_menu()
