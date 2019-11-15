from app.mos_level.models import MOSLevel
from app.mos_level.schemas import MOSLevelSchema
from app.mos_level.repository import MOSLevelRepository
from flask import abort, make_response

repository = MOSLevelRepository()
mos_level_schema = MOSLevelSchema()
many_mos_level_schema = MOSLevelSchema(many=True)


class MOSLevelService:

    def create(self, mos_level):

        # Create a mos level instance using the schema and the passed in json
        new_mos_level = mos_level_schema.load(mos_level)

        # Determine if record with id exists
        existing_mos_level = repository.read_one(code=new_mos_level.code, mos_level=MOSLevel)

        # Can we insert this record?
        if existing_mos_level is None:

            # Add the object to the database
            repository.create(new_mos_level)

            # Serialize and return the newly created object in the response
            data = mos_level_schema.dump(new_mos_level)

            return data, 201

        # Otherwise, nope, user exists already
        else:
            abort(409, f'mos level with code {new_mos_level.code} exists already')

    def update(self, code, mos_level):

        # Determine if record with id exists
        existing_mos_level = repository.read_one(code=code, mos_level=MOSLevel)

        # Did we find an existing mos level?
        if existing_mos_level is not None:

            # Create an mos level instance using the schema and the passed in mos level
            updated_mos_level = mos_level_schema.load(mos_level)

            # Update mos_level in db
            repository.update(existing_mos_level, updated_mos_level)

            # return updated user in the response
            data = mos_level_schema.dump(updated_mos_level)

            return data, 200

        # Otherwise, nope, didn't find that user
        else:
            abort(404, f"User not found for Id: {code}")

    def delete(self, code):

        # Get the mos level requested
        existing_mos_level = repository.read_one(code, MOSLevel)

        # Did we find a mos level?
        if existing_mos_level is not None:
            repository.delete(existing_mos_level)
            return make_response(f"User {code} deleted", 200)

        # Otherwise, nope, didn't find that mos level
        else:
            abort(404, f"mos level not found for Id: {code}")

    def get_by_id(self, code):

        # Determine if a mos level with code exists
        existing_mos_level = repository.read_one(code=code, mos_level=MOSLevel)

        # Did we find a mos level?
        if existing_mos_level is not None:

            return mos_level_schema.dump(existing_mos_level)

        # Otherwise, nope, didn't find that user
        else:
            abort(404, f"mos level not found for Id: {code}")

    def get_all(self):

        # Get all mos level in db
        mos_levels = repository.read_all(MOSLevel)
        return many_mos_level_schema.dump(mos_levels)
