# models/user_management.py
import sqlite3

DATABASE = 'library.db'

def get_connection():
    """Establish a connection to the SQLite database"""
    conn = sqlite3.connect(DATABASE)
    return conn

# Create
def add_user(name, email, role):
    """Add a new user to the database"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO users (name, email, role)
        VALUES (?, ?, ?)
    ''', (name, email, role))
    conn.commit()
    conn.close()

# Read
def get_user(user_id):
    """Retrieve a user from the database by their ID"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
    user = cursor.fetchone()
    conn.close()
    return user

def get_all_users():
    """Retrieve all users from the database"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    conn.close()
    return users

# Update
def update_user(user_id, name=None, email=None, role=None):
    """Update the details of a user"""
    conn = get_connection()
    cursor = conn.cursor()
    query = 'UPDATE users SET '
    params = []

    if name is not None:
        query += 'name = ?, '
        params.append(name)
    if email is not None:
        query += 'email = ?, '
        params.append(email)
    if role is not None:
        query += 'role = ?, '
        params.append(role)

    query = query.rstrip(', ')
    query += ' WHERE id = ?'
    params.append(user_id)

    cursor.execute(query, tuple(params))
    conn.commit()
    conn.close()

# Delete
def delete_user(user_id):
    """Delete a user from the database by their ID"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()
    conn.close()
