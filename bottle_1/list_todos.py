import sqlite3

connection = sqlite3.connect("todo.db")
cursor = connection.cursor()
cursor.execute("select * from todo1")
result = cursor.fetchall()
print(result)