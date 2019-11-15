from flask_restplus import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

api = Api(
    title='Candidate API',
    version='1.0',
    description='Candidate API'
)

db = SQLAlchemy()
ma = Marshmallow()