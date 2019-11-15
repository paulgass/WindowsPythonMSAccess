from app.education_level.models import EducationLevel
from app.education_level.schemas import EducationLevelSchema
from app.education_level.repository import EducationLevelRepository
from flask import abort, make_response

repository = EducationLevelRepository()
education_level_schema = EducationLevelSchema()
many_education_level_schema = EducationLevelSchema(many=True)


class EducationLevelService:

    def create(self, education_level):

        # Create a education level instance using the schema and the passed in json
        new_education_level = education_level_schema.load(education_level)

        # Determine if record with id exists
        existing_education_level = repository.read_one(code=new_education_level.code, education_level=EducationLevel)

        # Can we insert this record?
        if existing_education_level is None:

            # Add the object to the database
            repository.create(new_education_level)

            # Serialize and return the newly created object in the response
            data = education_level_schema.dump(new_education_level)

            return data, 201

        # Otherwise, nope, user exists already
        else:
            abort(409, f'education level with code {new_education_level.code} exists already')

    def update(self, code, education_level):

        # Determine if record with id exists
        existing_education_level = repository.read_one(code=code, education_level=EducationLevel)

        # Did we find an existing education level?
        if existing_education_level is not None:

            # Create an education level instance using the schema and the passed in education level
            updated_education_level = education_level_schema.load(education_level)

            # Update education_level in db
            repository.update(existing_education_level, updated_education_level)

            # return updated user in the response
            data = education_level_schema.dump(updated_education_level)

            return data, 200

        # Otherwise, nope, didn't find that user
        else:
            abort(404, f"User not found for Id: {code}")

    def delete(self, code):

        # Get the education level requested
        existing_education_level = repository.read_one(code, EducationLevel)

        # Did we find a education level?
        if existing_education_level is not None:
            repository.delete(existing_education_level)
            return make_response(f"User {code} deleted", 200)

        # Otherwise, nope, didn't find that education level
        else:
            abort(404, f"education level not found for Id: {code}")

    def get_by_id(self, code):

        # Determine if a education level with code exists
        existing_education_level = repository.read_one(code=code, education_level=EducationLevel)

        # Did we find a education level?
        if existing_education_level is not None:

            return education_level_schema.dump(existing_education_level)

        # Otherwise, nope, didn't find that user
        else:
            abort(404, f"education level not found for Id: {code}")

    def get_all(self):

        # Get all education level in db
        education_levels = repository.read_all(EducationLevel)
        return many_education_level_schema.dump(education_levels)
