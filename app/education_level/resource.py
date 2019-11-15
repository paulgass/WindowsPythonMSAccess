from flask import request
from flask_restplus import Namespace, Resource, fields
from app.education_level.service import EducationLevelService

api = Namespace('education_level', description='Education Level API')
service = EducationLevelService()

model_education_level = api.model('Education Level Model', {
    'code': fields.String(required=True, description="code of the Education Level", help="code cannot be blank."),
    'description': fields.String(required=True, description="description of the Education Level", help="description cannot be blank.")
    })


@api.route('')
class EducationLevelListResource(Resource):

    @api.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' })
    def get(self):
        try:
            return service.get_all()
        except KeyError as e:
            api.abort(500, e.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as e:
            api.abort(400, e.__doc__, status="Could not retrieve information", statusCode="400")

    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'})
    @api.expect(model_education_level)
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


@api.route('/<int:education_level_id>')
class EducationLevelResource(Resource):

    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
                        params={'education_level_id': 'Specify the dod_id associated with the Education Level'})
    def get(self, education_level_id):
        try:
            return service.get_by_id(education_level_id)
        except KeyError as e:
            api.abort(500, e.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as e:
            api.abort(400, e.__doc__, status="Could not retrieve information", statusCode="400")

    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
                        params={'education_level_id': 'Specify the dod_id associated with the Education Level'})
    @api.expect(model_education_level)
    def put(self, education_level_id):
        try:
            json_data = request.json
            if not json_data:
                return {'message': 'No input data provided'}, 400

            return service.update(education_level_id, json_data)
        except KeyError as e:
            api.abort(500, e.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as e:
            api.abort(400, e.__doc__, status="Could not retrieve information", statusCode="400")

    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
                        params={'education_level_id': 'Specify the dod_id associated with the Education Level'})
    def delete(self, education_level_id):
        try:
            return service.delete(education_level_id)
        except KeyError as e:
            api.abort(500, e.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as e:
            api.abort(400, e.__doc__, status="Could not retrieve information", statusCode="400")
