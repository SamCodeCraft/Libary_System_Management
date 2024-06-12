# connection.py
import sqlite3

def get_connection():
    """Establish a connection to the SQLite database"""
    conn = sqlite3.connect('library.db')
    return conn

# Example usage (optional)
if __name__ == "__main__":
    conn = get_connection()
    cursor = conn.cursor()
    
    # Query the database
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    for user in users:
        print(user)
    
    conn.close()
