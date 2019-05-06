from flask import render_template
import sqlite3 as db

from app.blueprints import index


@index.route('/', methods=['GET'])
def index():
    print("index")
    with db.connect('database.db') as conn:
        count = conn.execute('SELECT count(*) FROM counts').fetchone()[0]
    return render_template('index.html', counter=count)
