import sqlite3
from pyinstrument import Profiler
import random


conn = sqlite3.connect('example.db')
cursor = conn.cursor()

profiler = Profiler()
profiler.start()

query_count = 0

for i in range(10):  # Выполняем 10 SQL-запросов в цикле
    name = f"Data {random.randint(0, 10)}"
    # cursor.execute("SELECT * FROM your_table WHERE id = ?", (i,))
    cursor.execute("SELECT * FROM your_table WHERE data = ?", (name,))
    query_count += 1
    rows = cursor.fetchall()
    print(name, len(rows), sep='\t')

profiler.stop()

print(f"Всего выполнено запросов: {query_count}")
print(profiler.output_text(unicode=True, color=True))

conn.close()
