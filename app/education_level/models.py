from app.singletons import db


class EducationLevel(db.Model):

    __tablename__ = 'education_level'

    code = db.Column(db.String, primary_key=True)
    description = db.Column(db.String, nullable=False)
