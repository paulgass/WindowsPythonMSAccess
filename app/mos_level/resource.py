from flask import request
from flask_restplus import Namespace, Resource, fields
from app.mos_level.service import MOSLevelService

api = Namespace('mos_level', description='MOS Level API')
service = MOSLevelService()

model_mos_level = api.model('MOS Level Model', {
    'code': fields.String(required=True, description="code of the MOS Level", help="code cannot be blank."),
    'description': fields.String(required=True, description="description of the MOS Level", help="description cannot be blank.")
    })


@api.route('')
class MOSLevelListResource(Resource):

    @api.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' })
    def get(self):
        try:
            return service.get_all()
        except KeyError as e:
            api.abort(500, e.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as e:
            api.abort(400, e.__doc__, status="Could not retrieve information", statusCode="400")

    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'})
    @api.expect(model_mos_level)
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


@api.route('/<int:mos_level_id>')
class MOSLevelResource(Resource):

    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
                        params={'mos_level_id': 'Specify the dod_id associated with the MOS Level'})
    def get(self, mos_level_id):
        try:
            return service.get_by_id(mos_level_id)
        except KeyError as e:
            api.abort(500, e.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as e:
            api.abort(400, e.__doc__, status="Could not retrieve information", statusCode="400")

    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
                        params={'mos_level_id': 'Specify the dod_id associated with the MOS Level'})
    @api.expect(model_mos_level)
    def put(self, mos_level_id):
        try:
            json_data = request.json
            if not json_data:
                return {'message': 'No input data provided'}, 400

            return service.update(mos_level_id, json_data)
        except KeyError as e:
            api.abort(500, e.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as e:
            api.abort(400, e.__doc__, status="Could not retrieve information", statusCode="400")

    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
                        params={'mos_level_id': 'Specify the dod_id associated with the MOS Level'})
    def delete(self, mos_level_id):
        try:
            return service.delete(mos_level_id)
        except KeyError as e:
            api.abort(500, e.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as e:
            api.abort(400, e.__doc__, status="Could not retrieve information", statusCode="400")
