import sqlite3

conn = sqlite3.connect('SQL\inginious.sqlite')

cursor = conn.cursor()

Abcisse = []
Ordonnées = []
for row in cursor.execute("SELECT DISTINCT(task) from user_tasks WHERE course LIKE 'LSINF1252'"):
    Abcisse.append(row[0])


for row2 in cursor.execute("SELECT COUNT(submission) from user_tasks WHERE task "):
    Ordonnées.append(row2[0])
print(Abcisse)
print(len(Ordonnées))