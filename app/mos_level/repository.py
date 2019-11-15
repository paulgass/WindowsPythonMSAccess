from app.singletons import db


class MOSLevelRepository:

    def read_all(self, mos_level):
        return mos_level.query.all()

    def read_one(self, code, mos_level):
        return mos_level.query.filter(mos_level.code == code).one_or_none()

    def create(self, mos_level):

        # Add the user to the database
        db.session.add(mos_level)
        db.session.commit()

    def update(self, existing_mos_level, updated_mos_level):

        # Set the id to the user we want to update
        updated_mos_level.code = existing_mos_level.code

        # merge the new object into the old and commit it to the db
        db.session.merge(updated_mos_level)
        db.session.commit()

    def delete(self, mos_level):

        db.session.delete(mos_level)
        db.session.commit()
