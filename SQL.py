import sqlite3



def course_task_submission(course):
    conn = sqlite3.connect('SQL\inginious.sqlite')

    cursor = conn.cursor()
    abscissa = []
    ordinate = []
    select = "SELECT DISTINCT(task) from user_tasks WHERE course LIKE '{}'".format(course)

    for row in cursor.execute(select):
        abscissa.append(row[0])

    for i in abscissa:
        select2 = "SELECT COUNT(submission) from user_tasks WHERE task LIKE '{}'".format(i)
        for row2 in cursor.execute(select2):
            ordinate.append(row2[0])
    cursor.close()

    return abscissa, ordinate


def student_task_grade(student):
    conn = sqlite3.connect('SQL\inginious.sqlite')

    cursor = conn.cursor()
    result = []
    x = 0
    y = 0
    select3 = "SELECT grade from user_tasks WHERE username like '{}'".format(student)
    for row3 in cursor.execute(select3):
        if row3 == (100.0,):
            x += 1
        else:
            y += 1
    result.append(x)
    result.append(y)
    cursor.close()

    return result


def moyenne_grade_task(x):  # Bastien
    conn = sqlite3.connect('SQL\inginious.sqlite')

    cursor = conn.cursor()
    liste = []
    liste_task = []
    liste_moyenne = []
    select = "SELECT task, grade from submissions WHERE course LIKE '{}'".format(x)
    for row in cursor.execute(select):

        if row[0] not in (i[0] for i in liste):
            liste.append([row[0], row[1], 1])
        else:
            count = -1
            for z in (i[0] for i in liste):
                count += 1
                if z == row[0]:
                    liste[count][1] = float(liste[count][1]) + float(row[1])
                    liste[count][2] = float(liste[count][2]) + 1.0

    for y in liste:
        liste_moyenne.append(y[1] / y[2])
        liste_task.append(y[0])
    del liste
    if len(liste_moyenne) == len(liste_task):
        cursor.close()
        return liste_moyenne, liste_task


def rst_or_html(
        course):  # graphique circulaire qui permet de voir si les cours en question a des soumissions html ou rst
    conn = sqlite3.connect('SQL\inginious.sqlite')

    cursor = conn.cursor()
    result = []
    x = 0
    y = 0
    select3 = "SELECT response_type FROM submissions WHERE course LIKE'{}'".format(course)
    for row3 in cursor.execute(select3):
        if row3[0] == 'rst':
            x += 1
        else:
            y += 1
    result.append(x)
    result.append(y)
    cursor.close()

    return result


def student_point_for_task(
        student):  # graphique qui montre les points d'un etudiant pour chaque task (le cours etant implicite)
    conn = sqlite3.connect('SQL\inginious.sqlite')

    cursor = conn.cursor()
    task = []
    point = []

    select = "SELECT DISTINCT(task) from user_tasks WHERE username LIKE '{}'".format(student)

    for row in cursor.execute(select):
        task.append(row[0])

    for i in task:
        select2 = "SELECT MAX(grade) from user_tasks WHERE task LIKE '{}' AND username LIKE '{}'".format(i, student)
        for row2 in cursor.execute(select2):
            point.append(row2[0])
    cursor.close()

    return task, point


def student_tries_for_task(
        student):  # graphique qui montre le nombre de tentative d'un etudiant pour chaque task (le cours etant implicite)
    conn = sqlite3.connect('SQL\inginious.sqlite')

    cursor = conn.cursor()
    task = []
    tries = []

    select = "SELECT DISTINCT(task) from user_tasks WHERE username LIKE '{}'".format(student)

    for row in cursor.execute(select):
        task.append(row[0])

    for i in task:
        select2 = "SELECT tried from user_tasks WHERE task LIKE '{}' AND username LIKE '{}'".format(i, student)
        for row2 in cursor.execute(select2):
            tries.append(row2[0])
    cursor.close()

    return task, tries


def suceeded_task(
        task):  # graphique circulaire qui permet de voir le pourcentage de bonnes reponses sur le cours en question
    conn = sqlite3.connect('SQL\inginious.sqlite')

    cursor = conn.cursor()
    result = []
    x = 0
    y = 0
    select3 = "SELECT succeeded FROM user_tasks WHERE task LIKE'{}'".format(task)
    for row3 in cursor.execute(select3):
        if row3[0] == True:
            x += 1
        else:
            y += 1
    result.append(x)
    result.append(y)
    cursor.close()

    return result


