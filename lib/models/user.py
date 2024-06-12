import sqlite3
from connection import DATABASE

class User:
    def __init__(self, id, name, email, role):
        self._id = id
        self._name = name
        self._email = email
        self._role = role

    # Create a new user in the database
    def add_user(self, name, email, role):
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, email, role) VALUES (?, ?, ?)", (name, email, role))
        conn.commit()
        conn.close()

    # Retrieve a user by their ID
    def get_user(self, user_id):
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        user = cursor.fetchone()
        conn.close()
        return user

    # Retrieve all users from the database
    def get_all_users(self):
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        conn.close()
        return users

    # Update user information
    def update_user(self, user_id, name=None, email=None, role=None):
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        if name:
            cursor.execute("UPDATE users SET name = ? WHERE id = ?", (name, user_id))
        if email:
            cursor.execute("UPDATE users SET email = ? WHERE id = ?", (email, user_id))
        if role:
            cursor.execute("UPDATE users SET role = ? WHERE id = ?", (role, user_id))
        conn.commit()
        conn.close()

    # Delete a user from the database
    def delete_user(self, user_id):
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        conn.commit()
        conn.close()
