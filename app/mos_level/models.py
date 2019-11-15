from app.singletons import db


class MOSLevel(db.Model):

    __tablename__ = 'mos_level'

    code = db.Column(db.String, primary_key=True)
    description = db.Column(db.String, nullable=False)
