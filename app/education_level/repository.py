from app.singletons import db


class EducationLevelRepository:

    def read_all(self, education_level):
        return education_level.query.all()

    def read_one(self, code, education_level):
        return education_level.query.filter(education_level.code == code).one_or_none()

    def create(self, education_level):

        # Add the user to the database
        db.session.add(education_level)
        db.session.commit()

    def update(self, existing_education_level, updated_education_level):

        # Set the id to the user we want to update
        updated_education_level.code = existing_education_level.code

        # merge the new object into the old and commit it to the db
        db.session.merge(updated_education_level)
        db.session.commit()

    def delete(self, education_level):

        db.session.delete(education_level)
        db.session.commit()
