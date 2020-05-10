from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from ..db import get_db
bp = Blueprint('home', __name__, url_prefix='/')


@bp.route('/')
def index():
    db = get_db()
    valided_all = db.execute("SELECT count() FROM submissions WHERE result='success'").fetchone()[0]
    failed_all = db.execute("SELECT count() FROM submissions WHERE result='failed'").fetchone()[0]
    valided_lepl1402 = db.execute("SELECT count() FROM submissions WHERE result='success' "
                                  "AND course='LEPL1402'").fetchone()[0]
    valided_lsinf1101 = db.execute("SELECT count() FROM submissions WHERE result='success' "
                                   "AND course='LSINF1101-PYTHON'").fetchone()[0]
    valided_lsinf1252 = db.execute("SELECT count() FROM submissions WHERE result='success' "
                                   "AND course='LSINF1252'").fetchone()[0]
    failed_lepl1402 = db.execute("SELECT count() FROM submissions WHERE result='failed' "
                                 "AND course='LEPL1402'").fetchone()[0]
    failed_lsinf1101 = db.execute("SELECT count() FROM submissions WHERE result='failed' "
                                  "AND course='LSINF1101-PYTHON'").fetchone()[0]
    failed_lsinf1252 = db.execute("SELECT count() FROM submissions WHERE result='failed' "
                                  "AND course='LSINF1252'").fetchone()[0]
    return render_template('home/home.html', valided_all=valided_all, failed_all=failed_all,
                           valided_lepl1402=valided_lepl1402, valided_lsinf1101=valided_lsinf1101,
                           valided_lsinf1252=valided_lsinf1252, failed_lepl1402=failed_lepl1402,
                           failed_lsinf1101=failed_lsinf1101, failed_lsinf1252=failed_lsinf1252)
