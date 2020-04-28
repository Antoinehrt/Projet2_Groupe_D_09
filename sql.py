import sqlite3

conn = sqlite3.connect('SQL\inginious.sqlite')

cursor = conn.cursor()

Abcisse = []
Ordonnées = []
for row in cursor.execute("SELECT DISTINCT(task) from user_tasks WHERE course LIKE 'LSINF1252'"):
    Abcisse.append(row[0])

for i in Abcisse:
    select = "SELECT COUNT(submission) from user_tasks WHERE task LIKE '{}'".format(i)
    for row2 in cursor.execute(select):
        Ordonnées.append(row2[0])
if len(Abcisse) == len(Ordonnées):
    print(Abcisse)
    print(Ordonnées)
