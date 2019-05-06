from flask import render_template
import sqlite3 as db

from app.blueprints import increase


@increase.route('/', methods=['GET'])
def increase():
    print("increasing")
    with db.connect('database.db') as conn:
        count = conn.execute('SELECT count(*) FROM counts').fetchone()[0]
        conn.execute('insert into counts (id) VALUES (?)', (count + 1,))
        conn.commit()
    return render_template('increase.html', counter=count + 1)
