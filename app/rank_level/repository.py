from app.singletons import db


class RankLevelRepository:

    def read_all(self, rank_level):
        return rank_level.query.all()

    def read_one(self, code, rank_level):
        return rank_level.query.filter(rank_level.code == code).one_or_none()

    def create(self, rank_level):

        # Add the user to the database
        db.session.add(rank_level)
        db.session.commit()

    def update(self, existing_rank_level, updated_rank_level):

        # Set the id to the user we want to update
        updated_rank_level.code = existing_rank_level.code

        # merge the new object into the old and commit it to the db
        db.session.merge(updated_rank_level)
        db.session.commit()

    def delete(self, rank_level):

        db.session.delete(rank_level)
        db.session.commit()
