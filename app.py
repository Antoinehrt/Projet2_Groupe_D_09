from flask import Flask, render_template, jsonify
from SQL import student_task_grade, student_point_for_task, moyenne_grade_task

app = Flask(__name__)

name_student = "anon_1317"

sql = student_task_grade(name_student)


studentgraph1 = student_point_for_task(name_student)

X = studentgraph1[0]
y = studentgraph1[1]
@app.route('/')
def Homepage():
    return render_template('base.html')


@app.route('/course')
def course_graph():
    return render_template('course-selection.html')


@app.route('/student-graph')
def student_graph():
    return render_template('student-graph.html', name=name_student)


@app.route('/course-LINFO1252')
def LINFO1252_graph():
    values_course=moyenne_grade_task("LINFO1252")[0]
    labels_course=moyenne_grade_task("LINFO1252")[1]
    return render_template('course/LINFO1252.html',values=values_course,labels=labels_course)


@app.route('/course-LINFO1012')
def LINFO1012_graph():
    values_course=moyenne_grade_task("LSINF1101-PYTHON")[0]
    labels_course=moyenne_grade_task("LSINF1101-PYTHON")[1]
    return render_template('course/LINFO1012.html',values=values_course,labels=labels_course)


@app.route('/course-LESPO1412')
def LESPO1412_graph():
    values_course=moyenne_grade_task("LEPL1402")[0]
    labels_course=moyenne_grade_task("LEPL1402")[1]
    return render_template('course/LESPO1412.html',values=values_course,labels=labels_course)


@app.route('/data')
def data():
    return jsonify({'results': sql},{'X': X})


if __name__ == '__main__':
    app.run(debug=True)

