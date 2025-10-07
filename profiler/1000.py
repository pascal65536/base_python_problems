import sqlite3
import random

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Создание таблицы
cursor.execute("""
CREATE TABLE IF NOT EXISTS your_table (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data TEXT
)
""")

# Вставка 1000 записей
for i in range(1000):
    cursor.execute("INSERT INTO your_table (data) VALUES (?)", (f"Data {random.randint(0, 10)}",))

conn.commit()

print("Добавлено 1000 записей в таблицу your_table")

conn.close()
