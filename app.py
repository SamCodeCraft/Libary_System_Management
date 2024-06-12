from models.User import User
from models.Book import Book
from models.Author import Author
from models.Transaction import Transaction

def print_users():
    users = User().get_all_users()
    print("Users:")
    for user in users:
        print(user)

def print_books():
    books = Book().get_all_books()
    print("Books:")
    for book in books:
        print(book)

def print_authors():
    authors = Author().get_all_authors()
    print("Authors:")
    for author in authors:
        print(author)

def print_transactions():
    transactions = Transaction().get_all_transactions()
    print("Transactions:")
    for transaction in transactions:
        print(transaction)

def main():
    print("Welcome to Library Management System")

    while True:
        print("\nMenu:")
        print("1. Print Users")
        print("2. Print Books")
        print("3. Print Authors")
        print("4. Print Transactions")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print_users()
        elif choice == "2":
            print_books()
        elif choice == "3":
            print_authors()
        elif choice == "4":
            print_transactions()
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
