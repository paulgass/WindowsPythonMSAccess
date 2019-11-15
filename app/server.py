import os
import sys
from flask import Flask
from app.candidate.resource import api as candidate_api
from app.education_level.resource import api as education_level_api
from app.mos_level.resource import api as mos_level_api
from app.rank_level.resource import api as rank_level_api
from app.singletons import db, api, ma
from healthcheck import HealthCheck

DB_NAME = 'app.db'


def config():

    # Get Service Name from the environment variable
    service_name = os.getenv('DATABASE_SERVICE_NAME', '').upper().replace('-', '_')

    engine = os.getenv('DATABASE_ENGINE', 'sqlite')

    if engine == 'postgresql':

        print('using postgresql configuration...')
        engine = os.getenv('DATABASE_ENGINE').lower()
        name = os.getenv('DATABASE_NAME')
        user = os.getenv('DATABASE_USER')
        password = os.getenv('DATABASE_PASSWORD')
        host = os.getenv('{}_SERVICE_HOST'.format(service_name))
        port = os.getenv('{}_SERVICE_PORT_POSTGRESQL'.format(service_name))

        connection_string = f'{engine}://{user}:{password}@{host}:{port}/{name}'
        print(f'connecting to db using {connection_string}')

        return connection_string

    else:

        print('using sqlite configuration...')
        basedir = os.path.abspath(os.path.dirname(__file__))

        # if 'win32' (Windows) or 'cygwin' (Windows) then 3 slashes
        if sys.platform == 'win32' or sys.platform == 'cygwin':
            return f'{engine}:///{os.path.join(basedir, DB_NAME)}'
        # else 'linux' (Linux) or 'darwin' (Mac OS) then 4 slashes
        else:
            return f'{engine}:////{os.path.join(basedir, DB_NAME)}'


def create_app(env=None):

    # initialize app
    app = Flask(__name__)

    # Configure the SqlAlchemy part of the app instance
    app.config["SQLALCHEMY_ECHO"] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = config()
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # set app for db
    db.init_app(app)

    # Delete database file if it exists currently
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)

    # Create the database
    with app.app_context():
        db.create_all()

    # set app for api
    api.init_app(app)
    api.add_namespace(candidate_api)
    api.add_namespace(education_level_api)
    api.add_namespace(mos_level_api)
    api.add_namespace(rank_level_api)
    # set app for marshmallow
    ma.init_app(app)

    # Initialize Health Check
    health = HealthCheck(app, "/health")

    return app