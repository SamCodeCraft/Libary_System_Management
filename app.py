# app.py

from models.author import Author
from models.book import Book
from models.transaction import Transaction
from models.user import User

def main():
    while True:
        print("\nLibrary Management System")
        print("1. Manage Authors")
        print("2. Manage Books")
        print("3. Manage Transactions")
        print("4. Manage Users")
        print("5. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == '1':
            manage_authors()
        elif choice == '2':
            manage_books()
        elif choice == '3':
            manage_transactions()
        elif choice == '4':
            manage_users()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def manage_authors():
    author = Author()
    
    while True:
        print("\nManage Authors")
        print("1. Add Author")
        print("2. View All Authors")
        print("3. Update Author")
        print("4. Delete Author")
        print("5. View Books by Author")
        print("6. Back")
        
        choice = input("Enter choice: ")
        
        if choice == '1':
            name = input("Enter author name: ")
            author.add_author(name)
            print("Author added successfully.")
        elif choice == '2':
            authors = author.get_all_authors()
            for a in authors:
                print(f"ID: {a[0]}, Name: {a[1]}")
        elif choice == '3':
            author_id = input("Enter author ID: ")
            name = input("Enter new name: ")
            author.update_author(author_id, name)
            print("Author updated successfully.")
        elif choice == '4':
            author_id = input("Enter author ID: ")
            author.delete_author(author_id)
            print("Author deleted successfully.")
        elif choice == '5':
            author_id = input("Enter author ID: ")
            books = author.get_books_by_author(author_id)
            for b in books:
                print(f"ID: {b[0]}, Title: {b[1]}, Category: {b[2]}, Available Copies: {b[3]}")
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

def manage_books():
    book = Book()
    
    while True:
        print("\nManage Books")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Update Book")
        print("4. Delete Book")
        print("5. View Author by Book")
        print("6. Back")
        
        choice = input("Enter choice: ")
        
        if choice == '1':
            title = input("Enter book title: ")
            author_id = input("Enter author ID: ")
            category = input("Enter book category: ")
            available_copies = int(input("Enter available copies: "))
            book.add_book(title, author_id, category, available_copies)
            print("Book added successfully.")
        elif choice == '2':
            books = book.get_all_books()
            for b in books:
                print(f"ID: {b[0]}, Title: {b[1]}, Author ID: {b[2]}, Category: {b[3]}, Available Copies: {b[4]}")
        elif choice == '3':
            book_id = input("Enter book ID: ")
            title = input("Enter new title: ")
            author_id = input("Enter new author ID: ")
            category = input("Enter new category: ")
            available_copies = int(input("Enter new available copies: "))
            book.update_book(book_id, title, author_id, category, available_copies)
            print("Book updated successfully.")
        elif choice == '4':
            book_id = input("Enter book ID: ")
            book.delete_book(book_id)
            print("Book deleted successfully.")
        elif choice == '5':
            book_id = input("Enter book ID: ")
            author = book.get_author_by_book(book_id)
            print(f"ID: {author[0]}, Name: {author[1]}")
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

def manage_transactions():
    transaction = Transaction()
    
    while True:
        print("\nManage Transactions")
        print("1. Add Transaction")
        print("2. View All Transactions")
        print("3. Update Transaction")
        print("4. Delete Transaction")
        print("5. View User by Transaction")
        print("6. View Book by Transaction")
        print("7. Back")
        
        choice = input("Enter choice: ")
        
        if choice == '1':
            book_id = input("Enter book ID: ")
            user_id = input("Enter user ID: ")
            borrow_date = input("Enter borrow date (YYYY-MM-DD): ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            transaction.add_transaction(book_id, user_id, borrow_date, due_date)
            print("Transaction added successfully.")
        elif choice == '2':
            transactions = transaction.get_all_transactions()
            for t in transactions:
                print(f"ID: {t[0]}, Book ID: {t[1]}, User ID: {t[2]}, Borrow Date: {t[3]}, Due Date: {t[4]}, Return Date: {t[5]}, Fine: {t[6]}")
        elif choice == '3':
            transaction_id = input("Enter transaction ID: ")
            return_date = input("Enter return date (YYYY-MM-DD): ")
            fine = float(input("Enter fine amount: "))
            transaction.update_transaction(transaction_id, return_date=return_date, fine=fine)
            print("Transaction updated successfully.")
        elif choice == '4':
            transaction_id = input("Enter transaction ID: ")
            transaction.delete_transaction(transaction_id)
            print("Transaction deleted successfully.")
        elif choice == '5':
            transaction_id = input("Enter transaction ID: ")
            user = transaction.get_user_by_transaction(transaction_id)
            print(f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}, Role: {user[3]}")
        elif choice == '6':
            transaction_id = input("Enter transaction ID: ")
            book = transaction.get_book_by_transaction(transaction_id)
            print(f"ID: {book[0]}, Title: {book[1]}, Author ID: {book[2]}, Category: {book[3]}, Available Copies: {book[4]}")
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")

def manage_users():
    user = User()
    
    while True:
        print("\nManage Users")
        print("1. Add User")
        print("2. View All Users")
        print("3. Update User")
        print("4. Delete User")
        print("5. View Transactions by User")
        print("6. Back")
        
        choice = input("Enter choice: ")
        
        if choice == '1':
            name = input("Enter user name: ")
            email = input("Enter user email: ")
            role = input("Enter user role: ")
            user.add_user(name, email, role)
            print("User added successfully.")
        elif choice == '2':
            users = user.get_all_users()
            for u in users:
                print(f"ID: {u[0]}, Name: {u[1]}, Email: {u[2]}, Role: {u[3]}")
        elif choice == '3':
            user_id = input("Enter user ID: ")
            name = input("Enter new name: ")
            email = input("Enter new email: ")
            role = input("Enter new role: ")
            user.update_user(user_id, name, email, role)
            print("User updated successfully.")
        elif choice == '4':
            user_id = input("Enter user ID: ")
            user.delete_user(user_id)
            print("User deleted successfully.")
        elif choice == '5':
            user_id = input("Enter user ID: ")
            transactions = user.get_transactions_by_user(user_id)
            for t in transactions:
                print(f"ID: {t[0]}, Book ID: {t[1]}, Borrow Date: {t[2]}, Due Date: {t[3]}, Return Date: {t[4]}, Fine: {t[5]}")
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
