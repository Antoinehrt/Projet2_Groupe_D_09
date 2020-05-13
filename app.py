from flask import Flask, render_template
from SQL import student_task_grade, student_point_for_task, moyenne_grade_task, course_task_submission, rst_or_html, \
    suceeded_task

# Fichier générant les pages HTML

app = Flask(__name__)


@app.route('/')
def Homepage():
    """
    :return: Page d'acceuil du site web
    """
    return render_template('base.html')


@app.route('/course')
def course_graph():
    """
    :return: page de selection de cours du site web
    """
    return render_template('course-selection.html')


@app.route('/student-graph')
def student_graph():
    """
    pre: input venu du code html
    :return: page des graphiques sur les données par étudiants
    """
    # TODO Rajouter les inputs
    return render_template('student-graph.html', name=name_student)


@app.route('/en-savoir-plus')
def en_savoir_plus():
    """
    :return: page contenant des informations sur notre site et sur notre code.
    """
    return render_template('en-savoir-plus.html')


@app.route('/course-LINFO1252')
def LINFO1252_graph():
    """
    pre: appel de fonction provenant du fichier SQL.py. Les données serve de valeur pour les graphiques.
    :return: page du cours contenant 3 graphiques
    """
    values_course = course_task_submission("LSINF1252")[1]
    labels_course = course_task_submission("LSINF1252")[0]
    values2_course = rst_or_html("LSINF1252")
    values3_course = moyenne_grade_task("LSINF1252")[0]
    labels3_course = moyenne_grade_task("LSINF1252")[1]
    return render_template('course/LINFO1252.html', values3=values3_course, labels3=labels3_course,
                           values=values_course, labels=labels_course, values2=values2_course)


@app.route('/course-LINFO1012')
def LINFO1012_graph():
    """
    pre: appel de fonction provenant du fichier SQL.py. Les données serve de valeur pour les graphiques.
    :return: page du cours contenant 3 graphiques
    """
    values_course = course_task_submission("LEPL1402")[1]
    labels_course = course_task_submission("LEPL1402")[0]
    values2_course = rst_or_html("LEPL1402")
    values3_course = moyenne_grade_task("LEPL1402")[0]
    labels3_course = moyenne_grade_task("LEPL1402")[1]
    return render_template('course/LINFO1012.html', values3=values3_course, labels3=labels3_course,
                           values=values_course, labels=labels_course, values2=values2_course)


@app.route('/course-LESPO1412')
def LESPO1412_graph():
    """
    pre: appel de fonction provenant du fichier SQL.py. Les données serve de valeur pour les graphiques.
    :return: page du cours contenant 3 graphiques
    """
    values_course = course_task_submission("LSINF1101-PYTHON")[1]
    labels_course = course_task_submission("LSINF1101-PYTHON")[0]
    values2_course = rst_or_html("LSINF1101-PYTHON")
    values3_course = moyenne_grade_task("LSINF1101-PYTHON")[0]
    labels3_course = moyenne_grade_task("LSINF1101-PYTHON")[1]

    return render_template('course/LEPL1402.html', values3=values3_course, labels3=labels3_course,
                           values=values_course, labels=labels_course, values2=values2_course)


@app.route('/tasks-graph')
def tasks():
    """
   pre: input venant du code html
   :return: page contenant des graphs avec des informations en fonction des tasks
   """
    values4_course = suceeded_task('BinarySearch')  # TODO Rajouter les inputs
    return render_template('tasks.html', values4=values4_course)


if __name__ == '__main__':
    app.run(debug=True)
