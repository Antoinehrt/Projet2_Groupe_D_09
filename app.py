from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def Homepage():
    return render_template('base.html')


@app.route('/course-graph')
def course_graph():
    return render_template('course_graph.html')


@app.route('/student-graph')
def student_graph():
    return render_template('student_graph.html')


if __name__ == '__main__':
    app.run(debug=True)
