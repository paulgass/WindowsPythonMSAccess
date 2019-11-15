from app.singletons import db


class CandidateRepository:

    def read_all(self, candidate):
        return candidate.query.all()

    def read_one(self, dod_id, candidate):
        return candidate.query.filter(candidate.dod_id == dod_id).one_or_none()

    def create(self, candidate):

        # Add the user to the database
        db.session.add(candidate)
        db.session.commit()

    def update(self, existing_candidate, updated_candidate):

        # Set the id to the user we want to update
        updated_candidate.dod_id = existing_candidate.dod_id

        # merge the new object into the old and commit it to the db
        db.session.merge(updated_candidate)
        db.session.commit()

    def delete(self, candidate):

        db.session.delete(candidate)
        db.session.commit()
