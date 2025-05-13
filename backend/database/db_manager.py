import sqlite3

def connect_db():
    return sqlite3.connect('db.db')

def create_user(email, username, password):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO users (email, username, password)
            VALUES (?, ?, ?)
        ''', (email, username, password))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False  # Пользователь с такой почтой уже существует
    finally:
        conn.close()
        
def check_user(email, password):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM users WHERE email = ? AND password = ?
    ''', (email, password))
    user = cursor.fetchone()
    conn.close()
    return user is not None
