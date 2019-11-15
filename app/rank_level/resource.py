from flask import request
from flask_restplus import Namespace, Resource, fields
from app.rank_level.service import RankLevelService

api = Namespace('rank_level', description='Rank Level API')
service = RankLevelService()

model_rank_level = api.model('Rank Level Model', {
    'code': fields.String(required=True, description="code of the Rank Level", help="code cannot be blank."),
    'description': fields.String(required=True, description="description of the Rank Level", help="description cannot be blank.")
    })


@api.route('')
class RankLevelListResource(Resource):

    @api.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' })
    def get(self):
        try:
            return service.get_all()
        except KeyError as e:
            api.abort(500, e.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as e:
            api.abort(400, e.__doc__, status="Could not retrieve information", statusCode="400")

    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'})
    @api.expect(model_rank_level)
    def post(self):
        try:

            json_string = request.json
            if not json_string:
                return {'message': 'No input data provided'}, 400

            return service.create(json_string)
        except KeyError as e:
            api.abort(500, e.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as e:
            api.abort(400, e.__doc__, status="Could not retrieve information", statusCode="400")


@api.route('/<int:rank_level_id>')
class RankLevelResource(Resource):

    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
                        params={'rank_level_id': 'Specify the dod_id associated with the Rank Level'})
    def get(self, rank_level_id):
        try:
            return service.get_by_id(rank_level_id)
        except KeyError as e:
            api.abort(500, e.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as e:
            api.abort(400, e.__doc__, status="Could not retrieve information", statusCode="400")

    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
                        params={'rank_level_id': 'Specify the dod_id associated with the Rank Level'})
    @api.expect(model_rank_level)
    def put(self, rank_level_id):
        try:
            json_data = request.json
            if not json_data:
                return {'message': 'No input data provided'}, 400

            return service.update(rank_level_id, json_data)
        except KeyError as e:
            api.abort(500, e.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as e:
            api.abort(400, e.__doc__, status="Could not retrieve information", statusCode="400")

    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
                        params={'rank_level_id': 'Specify the dod_id associated with the Rank Level'})
    def delete(self, rank_level_id):
        try:
            return service.delete(rank_level_id)
        except KeyError as e:
            api.abort(500, e.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as e:
            api.abort(400, e.__doc__, status="Could not retrieve information", statusCode="400")
