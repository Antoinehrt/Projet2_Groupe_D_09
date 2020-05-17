import sqlite3


# Fichier contenant des fonctions permettant d'extraites les données nécessaire à la créations de nos graphs

def course_task_submission(course):
    """
    :graph type: line
    :param course: Le nom d'un cours compris dans la db
    :return: une liste d'abscisse (nom d'une task) et d'ordonnée (nombre de soumission)
    """
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
    """
    :graph type: pie
    :param student: nom d'un étudiant compris dans la db
    :return: une liste result (nombre de personne ayant réussie ayant 100%, n'ayant pas encore réussi)
    """
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


def moyenne_grade_task(course):
    """
    :graph type: line
    :param course: nom d'un cours compris dans la db
    :return: une liste d'abscisse (nom d'une task) et d'ordonnée (moyenne des notes)
    """
    conn = sqlite3.connect('SQL\inginious.sqlite')

    cursor = conn.cursor()
    liste = []
    abscisse = []
    ordonnée = []
    select = "SELECT task, grade from submissions WHERE course LIKE '{}'".format(course)
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
        ordonnée.append(y[1] / y[2])
        abscisse.append(y[0])
    del liste
    if len(ordonnée) == len(abscisse):
        cursor.close()
        return ordonnée, abscisse
    cursor.close()


def rst_or_html(course):
    """
    :graph type: pie
    :param course: nom d'un cours compris dans la db
    :return: une liste result (nombre de soumissions en rst ou html)
    """
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


def student_point_for_task(student):
    """
    :graph type: line
    :param student: nom d'un étudiant compris dans la db
    :return: une liste d'abscisse (nom d'une task) et d'ordonnée (note de l'étudiant)
    """
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


def student_tries_for_task(student):
    """
    :graph type: line
    :param student: nom d'un étudiant compris dans la db
    :return: une liste d'abscisse (nom d'une task) et d'ordonnée (nombre d'essais de l'étudiant)
    """
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

def student_task(task) :
    conn = sqlite3.connect('SQL\inginious.sqlite')

    cursor = conn.cursor()
    select3 = "SELECT grade FROM user_tasks WHERE task LIKE'{}'".format(task)
    value=[]
    label=[]
    for row in cursor.execute(select3):
        count=-1
        if row[0] not in label :
            if label==[] :
                label.append(row[0])
                value.append(1)
            else :
                for x in label :
                    count+=1
                    if row[0] < x :
                        label.insert(count,row[0])
                        value.insert(count,1)
                        break

                    
        else :
            for x in label :
                count+=1
                if str(x) == str(row[0]) :
                    value[count] = value[count]+1
                    break
                    
    cursor.close()
    return value,label

def suceeded_task(task):
    """
    :graph type: pie
    :param task: nom d'un task compris dans la db
    :return: une liste result (nombre de bonne et de mauvaise réponse)
    """
    conn = sqlite3.connect('SQL\inginious.sqlite')

    cursor = conn.cursor()
    result = []
    x = 0
    y = 0
    select3 = "SELECT succeeded FROM user_tasks WHERE task LIKE'{}'".format(task)
    for row3 in cursor.execute(select3):
        if row3[0] == 'true':
            x += 1
        else:
            y += 1
    result.append(x)
    result.append(y)
    cursor.close()

    return result

