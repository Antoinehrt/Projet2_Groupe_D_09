import sqlite3

conn = sqlite3.connect('inginious.sqlite')

cursor = conn.cursor()

for row in cursor.execute("SELECT * from CLASSE"):
    print(row)