from app.rank_level.models import RankLevel
from app.rank_level.schemas import RankLevelSchema
from app.rank_level.repository import RankLevelRepository
from flask import abort, make_response

repository = RankLevelRepository()
rank_level_schema = RankLevelSchema()
many_rank_level_schema = RankLevelSchema(many=True)


class RankLevelService:

    def create(self, rank_level):

        # Create a rank level instance using the schema and the passed in json
        new_rank_level = rank_level_schema.load(rank_level)

        # Determine if record with id exists
        existing_rank_level = repository.read_one(code=new_rank_level.code, rank_level=RankLevel)

        # Can we insert this record?
        if existing_rank_level is None:

            # Add the object to the database
            repository.create(new_rank_level)

            # Serialize and return the newly created object in the response
            data = rank_level_schema.dump(new_rank_level)

            return data, 201

        # Otherwise, nope, user exists already
        else:
            abort(409, f'rank level with code {new_rank_level.code} exists already')

    def update(self, code, rank_level):

        # Determine if record with id exists
        existing_rank_level = repository.read_one(code=code, rank_level=RankLevel)

        # Did we find an existing rank level?
        if existing_rank_level is not None:

            # Create an rank level instance using the schema and the passed in rank level
            updated_rank_level = rank_level_schema.load(rank_level)

            # Update rank_level in db
            repository.update(existing_rank_level, updated_rank_level)

            # return updated user in the response
            data = rank_level_schema.dump(updated_rank_level)

            return data, 200

        # Otherwise, nope, didn't find that user
        else:
            abort(404, f"User not found for Id: {code}")

    def delete(self, code):

        # Get the rank level requested
        existing_rank_level = repository.read_one(code, RankLevel)

        # Did we find a rank level?
        if existing_rank_level is not None:
            repository.delete(existing_rank_level)
            return make_response(f"User {code} deleted", 200)

        # Otherwise, nope, didn't find that rank level
        else:
            abort(404, f"rank level not found for Id: {code}")

    def get_by_id(self, code):

        # Determine if a rank level with code exists
        existing_rank_level = repository.read_one(code=code, rank_level=RankLevel)

        # Did we find a rank level?
        if existing_rank_level is not None:

            return rank_level_schema.dump(existing_rank_level)

        # Otherwise, nope, didn't find that user
        else:
            abort(404, f"rank level not found for Id: {code}")

    def get_all(self):

        # Get all rank level in db
        rank_levels = repository.read_all(RankLevel)
        return many_rank_level_schema.dump(rank_levels)
