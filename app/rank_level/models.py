from app.singletons import db


class RankLevel(db.Model):

    __tablename__ = 'rank_level'

    code = db.Column(db.String, primary_key=True)
    description = db.Column(db.String, nullable=False)
