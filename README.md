Library Management System
Overview
The Library Management System is a software application designed to manage the day-to-day operations of a library. It facilitates the management of library resources, including books, authors, and users, and streamlines the process of borrowing and returning books. The system aims to provide an efficient way to handle administrative tasks, track book inventories, and manage user transactions, ultimately enhancing the user experience for both library staff and patrons.
Objectives
* Resource Management: Efficiently manage the library's collection of books and authors.
* User Management: Handle user registrations, authentications, and roles (e.g., admin, patron).
* Transaction Tracking: Keep track of book borrowing and returning activities, including due dates and fines.
* Search and Filter: Enable users to search and filter the library's collection.
* Reporting: Generate reports for administrative purposes, such as overdue books and user activity.
Features
1. User Management
* User Registration: Allow new users to register and create accounts.
* User Authentication: Provide login functionality with role-based access (admin/patron).
* Profile Management: Enable users to view and update their profiles.
2. Book Inventory Management
* Add Books: Admins can add new books to the library's collection.
* Edit Books: Update book details like title, author, and category.
* Delete Books: Remove books from the inventory.
* Author Management: Add and manage author information.
3. Borrowing and Returning Books
* Borrow Books: Users can borrow available books.
* Return Books: Record the return of borrowed books.
* Due Dates and Reminders: Calculate due dates for borrowed books and send reminders.
* Fines Management: Calculate and record fines for overdue books.

4. Search and Filter
* Search Books: Search for books by title, author, or category.
* Filter Books: Filter the collection based on availability, category, etc.
5. Reports
* Borrowed Books Report: Generate reports on currently borrowed books.
* Overdue Books Report: Generate reports on overdue books and fines.
* User Activity Report: Track user activities such as borrowing history.
Technologies
* Python: The core programming language for backend development.
* SQLite3: The database for storing library data.
* SQLAlchemy: The ORM (Object-Relational Mapping) tool for database interactions.
Database Entities
* Users
    * id (INTEGER, PRIMARY KEY)
    * name (TEXT, NOT NULL)
    * email (TEXT, UNIQUE, NOT NULL)
    * role (TEXT, NOT NULL)
* Books
    * id (INTEGER, PRIMARY KEY)
    * title (TEXT, NOT NULL)
    * author_id (INTEGER, FOREIGN KEY, NOT NULL)
    * category (TEXT, NOT NULL)
    * available_copies (INTEGER, NOT NULL)
* Authors
    * id (INTEGER, PRIMARY KEY)
    * name (TEXT, NOT NULL)
* Transactions
    * id (INTEGER, PRIMARY KEY)
    * book_id (INTEGER, FOREIGN KEY, NOT NULL)
    * user_id (INTEGER, FOREIGN KEY, NOT NULL)
    * borrow_date (DATE, NOT NULL)
    * due_date (DATE, NOT NULL)
    * return_date (DATE)
    * fine (REAL)
Implementation Steps
1. Database Design
    * Design the database schema and create a database diagram to visualize relationships.
    * Implement the schema using SQLAlchemy.
2. Setup Project Structure
    * Create a structured project layout.
    * Configure SQLAlchemy and SQLite3.
3. Core Features Development
    * Implement user registration, authentication, and profile management.
    * Develop book inventory management functionalities.
    * Implement borrowing and returning of books, including due date calculation and fine management.
4. Search and Reporting
    * Develop search and filter functionalities.
    * Implement reporting features for borrowed books, overdue books, and user activities.
5. Testing and Validation
    * Write unit and integration tests to ensure the system works as expected.
    * Validate the application against various use cases and edge cases.
6. Documentation
    * Document the code, setup instructions, and usage guidelines.
    * Provide a detailed README file.
MVP Deliverables
1. Database Schema: A well-defined database schema with necessary tables and relationships.
2. User Management: Basic user registration, login, and profile management functionalities.
3. Book Management: Ability to add, view, edit, and delete books.
4. Borrowing and Returning: Basic borrowing and returning functionalities with due date tracking.
5. Search Functionality: Simple search feature to find books.
6. Code Documentation: Documentation for the setup, installation, and usage of the system.
7. Basic Interface: A minimal interface to interact with the system (CLI or web).
Installation and Setup
1. Clone the repositoryshCopy codegit clone <repository_url>
2. cd library-management-system
3. 
4. Create a virtual environment and activate itshCopy codepython -m venv venv
5. source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
6. 
7. Install the required dependenciesshCopy codepip install -r requirements.txt
8. 
9. Set up the databaseshCopy codepython setup_db.py
10. 
11. Run the applicationshCopy codepython app.py
12. 
Usage
1. User Registration
    * Access the registration page and fill in the required details to create an account.
2. User Authentication
    * Log in using the registered email and password.
3. Profile Management
    * View and update your profile information.
4. Book Management
    * Admins can add, edit, and delete books.
    * Users can view the list of available books.
5. Borrowing and Returning Books
    * Users can borrow available books and return them before the due date.
6. Search Functionality
    * Use the search feature to find books by title, author, or category.
Testing
* Unit Tests: Run unit tests to ensure individual components work as expected.
* Integration Tests: Run integration tests to ensure different parts of the system work together correctly.
sh
Copy code
python -m unittest discover tests
Contributing
* Fork the repository and create a new branch for your feature or bug fix.
* Submit a pull request with a detailed description of your changes.
License
This project is licensed under the MIT License.
Author
This project was developed by SIYAJARI Samuel.
Acknowledgements
* Thanks to the open-source community for providing the tools and libraries used in this project.
