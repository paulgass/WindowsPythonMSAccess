from app.candidate.models import Candidate
from app.candidate.schemas import CandidateSchema
from app.candidate.repository import CandidateRepository
from flask import abort, make_response

repository_candidate = CandidateRepository()
schema_candidate = CandidateSchema()
many_schema_candidate = CandidateSchema(many=True)


class CandidateService:

    def create(self, candidate_json):

        # Create a candidate instance using the schema and the passed in candidate
        new_candidate = schema_candidate.load(candidate_json)

        # Determine if record with id exists
        existing_candidate = repository_candidate.read_one(dod_id=new_candidate.dod_id, candidate=Candidate)

        # Can we insert this record?
        if existing_candidate is None:

            # Add the object to the database
            repository_candidate.create(new_candidate)

            # Serialize and return the newly created object in the response
            data = schema_candidate.dump(new_candidate)

            return data, 201

        # Otherwise, nope, user exists already
        else:
            abort(409, f'Candidate with DOD ID {new_candidate.dod_id} exists already')

    def update(self, dod_id, candidate_json):

        # Determine if record with id exists
        existing_candidate = repository_candidate.read_one(dod_id=dod_id, candidate=Candidate)

        # Did we find an existing candidate?
        if existing_candidate is not None:

            # Create a candidate instance using the schema and the passed in candidate
            updated_candidate = schema_candidate.load(candidate_json)

            # Update candidate in db
            repository_candidate.update(existing_candidate, updated_candidate)

            # return updated user in the response
            data = schema_candidate.dump(updated_candidate)

            return data, 200

        # Otherwise, nope, didn't find that user
        else:
            abort(404, f"User not found for Id: {dod_id}")

    def delete(self, dod_id):

        # Get the candidate requested
        existing_candidate = Candidate.query.filter(Candidate.dod_id == dod_id).one_or_none()

        # Did we find a candidate?
        if existing_candidate is not None:
            repository_candidate.delete(existing_candidate)
            return make_response(f"User {dod_id} deleted", 200)

        # Otherwise, nope, didn't find that candidate
        else:
            abort(404, f"Candidate not found for Id: {dod_id}")

    def get_by_id(self, dod_id):

        # Determine if a candidate with id exists
        existing_candidate = repository_candidate.read_one(dod_id=dod_id, candidate=Candidate)

        # Did we find a candidate?
        if existing_candidate is not None:

            return  schema_candidate.dump(existing_candidate)

        # Otherwise, nope, didn't find that user
        else:
            abort(404, f"candidate not found for Id: {dod_id}")

    def get_all(self):

        # Get all candidates in db
        candidates = repository_candidate.read_all(Candidate)
        return many_schema_candidate.dump(candidates)
