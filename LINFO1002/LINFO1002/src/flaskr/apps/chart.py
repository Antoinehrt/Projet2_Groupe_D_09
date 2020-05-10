import json
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from ..db import get_db

bp = Blueprint('auth', __name__, url_prefix='/charts')


@bp.route('/', methods=['GET'])
def lepl_1402():
    db = get_db()
    if request.method == 'GET':
        course = request.args.get('course')
        course = course if course else ''
        q = f'SELECT task, course, submitted_on, result from submissions WHERE course="{course}" ORDER BY submitted_on'
        result = db.execute(q).fetchall()
        return render_template('charts/charts.html', title=course, data=json.dumps(result))
    return render_template('charts/charts.html', title="", data=[[]])
