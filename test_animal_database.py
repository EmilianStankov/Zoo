import sqlite3

conn = sqlite3.connect("animals.db")
cursor = conn.cursor()

result = cursor.execute("SELECT * FROM animals")

for row in result:
    print(row)
