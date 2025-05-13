import sqlite3

# Создание подключения к базе данных (создаст файл, если его не существует)
conn = sqlite3.connect('db.db')

# Создание курсора
cursor = conn.cursor()

# Создание таблицы пользователей
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL UNIQUE,
    username TEXT NOT NULL,
    password TEXT NOT NULL
)
''')

# Сохраняем изменения
conn.commit()

# Закрываем соединение
conn.close()
