from flask import Flask
from importlib import import_module
from app.blueprints import all_blueprints
import sqlite3 as db

import app as app_root
import os

APP_ROOT_FOLDER = os.path.abspath(os.path.dirname(app_root.__file__))
TEMPLATE_FOLDER = os.path.join(APP_ROOT_FOLDER, 'templates')
STATIC_FOLDER = os.path.join(APP_ROOT_FOLDER, 'static')


def create_app():
    """
    Flask application factory. Initializes and returns the Flask application.
    Blueprints are registered in here.
    Modeled after: http://flask.pocoo.org/docs/patterns/appfactories/

    :return The initialized Flask application.
    """
    # Initialize app.
    flask_app = Flask(__name__, template_folder=TEMPLATE_FOLDER, static_folder=STATIC_FOLDER)

    # Setup redirects and register blueprints.
    # app.add_url_rule('/favicon.ico', 'favicon', lambda: app.send_static_file('favicon.ico'))
    for bp in all_blueprints:
        import_module(bp.import_name)
        flask_app.register_blueprint(bp)

    # Initialize extensions/add-ons/plugins.
    with db.connect('database.db') as conn:
        conn.execute('drop table if exists counts;')
        conn.execute('create table counts (id integer primary key not null)')
        conn.execute('insert into counts (id) VALUES (1)')
        conn.commit()
        print('Successfully created database')

    return flask_app
