from flask import request
from flask_restplus import Namespace, Resource, fields
from app.candidate.service import CandidateService
from app.education_level.resource import model_education_level
from app.mos_level.resource import model_mos_level
from app.rank_level.resource import model_rank_level
import os, sys
from datetime import datetime
import pypyodbc

api = Namespace('candidates', description='Candidate API')
service = CandidateService()

model_candidate = api.model('Candidate Model', {
    'dod_id': fields.String(required=True, description="DOD ID of the Candidate", help="dod_id cannot be blank."),
    'last_name': fields.String(required=True, description="Last Name of the Candidate", help="last_name cannot be blank."),
    'first_name': fields.String(required=True, description="First Name of the Candidate", help="first_name cannot be blank."),
    'education_level': fields.Nested(model_education_level, required = True, description="Education Level Nested List for the Candidate.", help="education_level cannot be blank."),
    'mos_level': fields.Nested(model_mos_level, required = True, description="MOS Level Nested List for the Candidate.", help="mos_level cannot be blank."),
    'rank_level': fields.Nested(model_rank_level, required = True, description="Rank Level Nested List for the Candidate.", help="rank_level cannot be blank."),
    'id': fields.String(required=True, description="ID of the Candidate", help="id cannot be blank."),
    'middle_initial': fields.String(required=True, description="Middle Initial of the Candidate", help="middle_initial cannot be blank."),
    'social_security_number': fields.String(required=True, description="Social Security Number of the Candidate", help="social_security_number cannot be blank."),
    'phone_number': fields.String(required=True, description="Phone Number of the Candidate", help="phone_number cannot be blank."),
    'dob': fields.Date(required=True, default='2000-01-31', description="Date Of Birth of the Candidate", help="dob cannot be blank."),
    'sex': fields.String(required=True, description="Sex of the Candidate", help="sex cannot be blank."),
    'active_service_date': fields.Date(required=True, default='2000-01-31', description="Active Service Date of the Candidate", help="active_service_date cannot be blank."),
    'arrival_date': fields.Date(required=True, default='2000-01-31', description="Arrival Date of the Candidate", help="arrival_date cannot be blank."),
    'dmsl': fields.String(required=True, description="DMSL of the Candidate", help="dmsl cannot be blank."),
    'gt_score': fields.String(required=True, description="GT Score of the Candidate", help="gt_score cannot be blank."),
    'contract_acquistion': fields.String(required=True, description="Contract Aquisition of the Candidate", help="contract_acquistion cannot be blank."),
    'emergency_contact_first_name': fields.String(required=True, description="Emergency Contact First Name of the Candidate", help="emergency_contact_first_name cannot be blank."),
    'emergency_contact_last_name': fields.String(required=True, description="Emergency Contact Last Name of the Candidate", help="emergency_contact_last_name cannot be blank."),
    'emergency_contact_phone_number': fields.String(required=True, description="Emergency Contact Phone Number of the Candidate", help="emergency_contact_phone_number cannot be blank."),
    'emergency_contact_relationship': fields.String(required=True, description="Emergency Contact Relationship of the Candidate", help="emergency_contact_relationship cannot be blank."),
    'time_standard': fields.String(required=True, description="Time Standard of the Candidate", help="time_standard cannot be blank."),
    'attended': fields.Boolean(required=True, description="True or False for the Attendance status of the Candidate", help="attended cannot be blank."),
    'failure_code': fields.String(required=True, description="Failure Code of the Candidate", help="failure_code cannot be blank."),
    'failure_comment': fields.String(required=True, description="Failure Comment of the Candidate", help="failure_comment cannot be blank."),
    'home_of_record': fields.String(required=True, description="Home of Record of the Candidate", help="home_of_record cannot be blank."),
    'arrived_from': fields.String(required=True, description="Arrived From of the Candidate", help="arrived_from cannot be blank."),
    'has_dependents': fields.Boolean(required=True, description="True or False for the Dependents status of the Candidate", help="has_dependents cannot be blank."),
    'ranger_regiment_discovered': fields.String(required=True, description="Ranger Regiment Discovered of the Candidate", help="ranger_regiment_discovered cannot be blank."),
    'is_tdy': fields.Boolean(required=True, description="True or False for the TDY status of the Candidate", help="is_tdy cannot be blank."),
    'tdy_unit': fields.String(required=True, description="TDY Unit of the Candidate", help="tdy_unit cannot be blank."),
    'played_sports': fields.Boolean(required=True, description="True or False for the Played Sports status of the Candidate", help="played_sports cannot be blank."),
    'sports_played': fields.String(required=True, description="Sports Played of the Candidate", help="sports_played cannot be blank."),
    'has_hot_weather_injury': fields.Boolean(required=True, description="True or False for the Hot Weather Injury status of the Candidate", help="has_hot_weather_injury cannot be blank."),
    'has_cold_weather_injury': fields.Boolean(required=True, description="True or False for the Cold Weather Injury status of the Candidate", help="has_cold_weather_injury cannot be blank."),
    'has_physical': fields.Boolean(required=True, description="True or False for the Physical status of the Candidate", help="has_physical cannot be blank."),
    'has_airborne': fields.Boolean(required=True, description="True or False for the Airborne status of the Candidate", help="has_airborne cannot be blank."),
    'has_ranger_sof_affiliations': fields.Boolean(required=True, description="True or False for the Ranger SOF Affiliations status of the Candidate", help="has_ranger_sof_affiliations cannot be blank."),
    'has_glasses': fields.Boolean(required=True, description="True or False for the Glasses status of the Candidate", help="has_glasses cannot be blank."),
    'success_factors': fields.String(required=True, description="Success Factors of the Candidate", help="success_factors cannot be blank."),
    'success_motivators': fields.String(required=True, description="Success Motivators of the Candidate", help="success_motivators cannot be blank."),
    'bad_habits': fields.String(required=True, description="Bad Habits of the Candidate", help="bad_habits cannot be blank.")
})

sql_brandi_create = """CREATE TABLE candidate (dod_id VARCHAR(255) PRIMARY KEY, first_name VARCHAR(255), last_name VARCHAR(255), education_level_code VARCHAR(255), education_level_description VARCHAR(255), mos_level_code VARCHAR(255), mos_level_description VARCHAR(255), rank_level_code VARCHAR(255), rank_level_description VARCHAR(255), id VARCHAR(255), middle_initial VARCHAR(255), social_security_number VARCHAR(255), phone_number VARCHAR(255), dob DATE, sex VARCHAR(255), active_service_date DATE, arrival_date DATE, dmsl VARCHAR(255), gt_score VARCHAR(255), contract_acquistion VARCHAR(255), emergency_contact_first_name VARCHAR(255), emergency_contact_last_name VARCHAR(255), emergency_contact_phone_number VARCHAR(255), emergency_contact_relationship VARCHAR(255), time_standard VARCHAR(255), attended BIT, failure_code VARCHAR(255), failure_comment VARCHAR(255), home_of_record VARCHAR(255), arrived_from VARCHAR(255), has_dependents BIT, ranger_regiment_discovered VARCHAR(255), is_tdy BIT, tdy_unit VARCHAR(255), played_sports BIT, sports_played VARCHAR(255), has_hot_weather_injury BIT, has_cold_weather_injury BIT, has_physical BIT, has_airborne BIT, has_ranger_sof_affiliations BIT, has_glasses BIT, success_factors VARCHAR(255), success_motivators VARCHAR(255), bad_habits VARCHAR(255));"""
sql_brandi_insert = """INSERT INTO [candidate] ([dod_id], [first_name], [last_name], [education_level_code], [education_level_description], [mos_level_code], [mos_level_description], [rank_level_code], [rank_level_description], [id], [middle_initial], [social_security_number], [phone_number], [dob], [sex], [active_service_date], [arrival_date], [dmsl], [gt_score], [contract_acquistion], [emergency_contact_first_name], [emergency_contact_last_name], [emergency_contact_phone_number], [emergency_contact_relationship], [time_standard], [attended], [failure_code], [failure_comment], [home_of_record], [arrived_from], [has_dependents], [ranger_regiment_discovered], [is_tdy], [tdy_unit], [played_sports], [sports_played], [has_hot_weather_injury], [has_cold_weather_injury], [has_physical], [has_airborne], [has_ranger_sof_affiliations], [has_glasses], [success_factors], [success_motivators], [bad_habits]) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""

@api.route('')
class CandidateListResource(Resource):

    @api.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' })
    def get(self):
        try:
            return service.get_all()
        except KeyError as e:
            api.abort(500, e.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as e:
            api.abort(400, e.__doc__, status="Could not retrieve information", statusCode="400")

    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'})
    @api.expect(model_candidate)
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


@api.route('/<int:candidate_id>')
class CandidateResource(Resource):

    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
                        params={'candidate_id': 'Specify the dod_id associated with the candidate'})
    def get(self, candidate_id):
        try:
            return service.get_by_id(candidate_id)
        except KeyError as e:
            api.abort(500, e.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as e:
            api.abort(400, e.__doc__, status="Could not retrieve information", statusCode="400")

    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
                        params={'candidate_id': 'Specify the dod_id associated with the candidate'})
    @api.expect(model_candidate)
    def put(self, candidate_id):
        try:
            json_data = request.json
            if not json_data:
                return {'message': 'No input data provided'}, 400

            return service.update(candidate_id, json_data)
        except KeyError as e:
            api.abort(500, e.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as e:
            api.abort(400, e.__doc__, status="Could not retrieve information", statusCode="400")

    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
                        params={'candidate_id': 'Specify the dod_id associated with the candidate'})
    def delete(self, candidate_id):
        try:
            return service.delete(candidate_id)
        except KeyError as e:
            api.abort(500, e.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as e:
            api.abort(400, e.__doc__, status="Could not retrieve information", statusCode="400")

@api.route('msaccess/')
class CandidateMSAccessListResource(Resource):

    @api.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' })
    def post(self):
        try:
            json_string_array = service.get_all()

            if not json_string_array:
                return {'message': 'No input data provided'}, 400

            brandi_project_directory = str(os.getcwd())
            brandi_database_currenttime = datetime.now().strftime("%Y%m%d%H%M%S")

            # if 'win32' (Windows) or 'cygwin' (Windows) then \ backslash
            if sys.platform == 'win32' or sys.platform == 'cygwin':
                mdbfilepath = '%s\%s_%s' % (brandi_project_directory, "brandi", brandi_database_currenttime)
            # else 'linux' (Linux) or 'darwin' (Mac OS) then / forwardslash
            else:
                mdbfilepath = '%s/%s_%s' % (brandi_project_directory, "brandi", brandi_database_currenttime)

            connection = pypyodbc.win_create_mdb('%s.mdb' % (mdbfilepath))
            connection.cursor().execute(sql_brandi_create).commit()

            for json_string in json_string_array:
                param_dod_id = json_string['dod_id']
                param_first_name = json_string['first_name']
                param_last_name = json_string['last_name']
                param_education_level_code = json_string['education_level']['code']
                param_education_level_description = json_string['education_level']['description']
                param_mos_level_code = json_string['mos_level']['code']
                param_mos_level_description = json_string['mos_level']['description']
                param_rank_level_code = json_string['rank_level']['code']
                param_rank_level_description = json_string['rank_level']['description']
                param_id = json_string['id']
                param_middle_initial = json_string['middle_initial']
                param_social_security_number = json_string['social_security_number']
                param_phone_number = json_string['phone_number']
                param_dob = json_string['dob']
                param_sex = json_string['sex']
                param_active_service_date = json_string['active_service_date']
                param_arrival_date = json_string['arrival_date']
                param_dmsl = json_string['dmsl']
                param_gt_score = json_string['gt_score']
                param_contract_acquistion = json_string['contract_acquistion']
                param_emergency_contact_first_name = json_string['emergency_contact_first_name']
                param_emergency_contact_last_name = json_string['emergency_contact_last_name']
                param_emergency_contact_phone_number = json_string['emergency_contact_phone_number']
                param_emergency_contact_relationship = json_string['emergency_contact_relationship']
                param_time_standard = json_string['time_standard']
                param_attended = json_string['attended']
                param_failure_code = json_string['failure_code']
                param_failure_comment = json_string['failure_comment']
                #param_datetime_creation = json_string['datetime_creation']
                #param_datetime_update = json_string['datetime_update']
                param_home_of_record = json_string['home_of_record']
                param_arrived_from = json_string['arrived_from']
                param_has_dependents = json_string['has_dependents']
                param_ranger_regiment_discovered = json_string['ranger_regiment_discovered']
                param_is_tdy = json_string['is_tdy']
                param_tdy_unit = json_string['tdy_unit']
                param_played_sports = json_string['played_sports']
                param_sports_played = json_string['sports_played']
                param_has_hot_weather_injury = json_string['has_hot_weather_injury']
                param_has_cold_weather_injury = json_string['has_cold_weather_injury']
                param_has_physical = json_string['has_physical']
                param_has_airborne = json_string['has_airborne']
                param_has_ranger_sof_affiliations = json_string['has_ranger_sof_affiliations']
                param_has_glasses = json_string['has_glasses']
                param_success_factors = json_string['success_factors']
                param_success_motivators = json_string['success_motivators']
                param_bad_habits = json_string['bad_habits']

                params = (param_dod_id, param_first_name, param_last_name, param_education_level_code, param_education_level_description, param_mos_level_code, param_mos_level_description, param_rank_level_code, param_rank_level_description, param_id, param_middle_initial, param_social_security_number, param_phone_number, param_dob, param_sex, param_active_service_date, param_arrival_date, param_dmsl, param_gt_score, param_contract_acquistion, param_emergency_contact_first_name, param_emergency_contact_last_name, param_emergency_contact_phone_number, param_emergency_contact_relationship, param_time_standard, param_attended, param_failure_code, param_failure_comment, param_home_of_record, param_arrived_from, param_has_dependents, param_ranger_regiment_discovered, param_is_tdy, param_tdy_unit, param_played_sports, param_sports_played, param_has_hot_weather_injury, param_has_cold_weather_injury, param_has_physical, param_has_airborne, param_has_ranger_sof_affiliations, param_has_glasses, param_success_factors, param_success_motivators, param_bad_habits)
                connection.cursor().execute(sql_brandi_insert, params)
                connection.cursor().close()
                connection.commit()

            connection.close()
            return("MS Access TABLE rows INSERT Succeeded.")
        except KeyError as e:
            api.abort(500, e.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as e:
            api.abort(400, e.__doc__, status="Could not retrieve information", statusCode="400")


@api.route('msaccess/<int:candidate_id>')
class CandidateMSAccessResource(Resource):

    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
                        params={'candidate_id': 'Specify the dod_id associated with the candidate'})
    def post(self, candidate_id):
        try:
            json_string = service.get_by_id(candidate_id)

            if not json_string:
                return {'message': 'No input data provided'}, 400

            brandi_project_directory = str(os.getcwd())
            brandi_database_currenttime = datetime.now().strftime("%Y%m%d%H%M%S")

            # if 'win32' (Windows) or 'cygwin' (Windows) then \ backslash
            if sys.platform == 'win32' or sys.platform == 'cygwin':
                mdbfilepath = '%s\%s_%s' % (brandi_project_directory, "brandi", brandi_database_currenttime)
            # else 'linux' (Linux) or 'darwin' (Mac OS) then / forwardslash
            else:
                mdbfilepath = '%s/%s_%s' % (brandi_project_directory, "brandi", brandi_database_currenttime)

            connection = pypyodbc.win_create_mdb('%s.mdb' % (mdbfilepath))
            connection.cursor().execute(sql_brandi_create).commit()

            param_dod_id = json_string['dod_id']
            param_first_name = json_string['first_name']
            param_last_name = json_string['last_name']
            param_education_level_code = json_string['education_level']['code']
            param_education_level_description = json_string['education_level']['description']
            param_mos_level_code = json_string['mos_level']['code']
            param_mos_level_description = json_string['mos_level']['description']
            param_rank_level_code = json_string['rank_level']['code']
            param_rank_level_description = json_string['rank_level']['description']
            param_id = json_string['id']
            param_middle_initial = json_string['middle_initial']
            param_social_security_number = json_string['social_security_number']
            param_phone_number = json_string['phone_number']
            param_dob = json_string['dob']
            param_sex = json_string['sex']
            param_active_service_date = json_string['active_service_date']
            param_arrival_date = json_string['arrival_date']
            param_dmsl = json_string['dmsl']
            param_gt_score = json_string['gt_score']
            param_contract_acquistion = json_string['contract_acquistion']
            param_emergency_contact_first_name = json_string['emergency_contact_first_name']
            param_emergency_contact_last_name = json_string['emergency_contact_last_name']
            param_emergency_contact_phone_number = json_string['emergency_contact_phone_number']
            param_emergency_contact_relationship = json_string['emergency_contact_relationship']
            param_time_standard = json_string['time_standard']
            param_attended = json_string['attended']
            param_failure_code = json_string['failure_code']
            param_failure_comment = json_string['failure_comment']
            #param_datetime_creation = json_string['datetime_creation']
            #param_datetime_update = json_string['datetime_update']
            param_home_of_record = json_string['home_of_record']
            param_arrived_from = json_string['arrived_from']
            param_has_dependents = json_string['has_dependents']
            param_ranger_regiment_discovered = json_string['ranger_regiment_discovered']
            param_is_tdy = json_string['is_tdy']
            param_tdy_unit = json_string['tdy_unit']
            param_played_sports = json_string['played_sports']
            param_sports_played = json_string['sports_played']
            param_has_hot_weather_injury = json_string['has_hot_weather_injury']
            param_has_cold_weather_injury = json_string['has_cold_weather_injury']
            param_has_physical = json_string['has_physical']
            param_has_airborne = json_string['has_airborne']
            param_has_ranger_sof_affiliations = json_string['has_ranger_sof_affiliations']
            param_has_glasses = json_string['has_glasses']
            param_success_factors = json_string['success_factors']
            param_success_motivators = json_string['success_motivators']
            param_bad_habits = json_string['bad_habits']

            params = (param_dod_id, param_first_name, param_last_name, param_education_level_code, param_education_level_description, param_mos_level_code, param_mos_level_description, param_rank_level_code, param_rank_level_description, param_id, param_middle_initial, param_social_security_number, param_phone_number, param_dob, param_sex, param_active_service_date, param_arrival_date, param_dmsl, param_gt_score, param_contract_acquistion, param_emergency_contact_first_name, param_emergency_contact_last_name, param_emergency_contact_phone_number, param_emergency_contact_relationship, param_time_standard, param_attended, param_failure_code, param_failure_comment, param_home_of_record, param_arrived_from, param_has_dependents, param_ranger_regiment_discovered, param_is_tdy, param_tdy_unit, param_played_sports, param_sports_played, param_has_hot_weather_injury, param_has_cold_weather_injury, param_has_physical, param_has_airborne, param_has_ranger_sof_affiliations, param_has_glasses, param_success_factors, param_success_motivators, param_bad_habits)
            connection.cursor().execute(sql_brandi_insert, params)
            connection.cursor().close()
            connection.commit()
            connection.close()
            return("MS Access TABLE row INSERT Succeeded.")
        except KeyError as e:
            api.abort(500, e.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as e:
            api.abort(400, e.__doc__, status="Could not retrieve information", statusCode="400")
            

@api.route('msaccesscreateblank/')
class CandidateMSAccessBlankListResource(Resource):

    @api.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' })
    def post(self):
        try:
            brandi_project_directory = str(os.getcwd())
            brandi_database_currenttime = datetime.now().strftime("%Y%m%d%H%M%S")

            # if 'win32' (Windows) or 'cygwin' (Windows) then \ backslash
            if sys.platform == 'win32' or sys.platform == 'cygwin':
                mdbfilepath = '%s\%s_%s' % (brandi_project_directory, "brandi", brandi_database_currenttime)
            # else 'linux' (Linux) or 'darwin' (Mac OS) then / forwardslash
            else:
                mdbfilepath = '%s/%s_%s' % (brandi_project_directory, "brandi", brandi_database_currenttime)

            connection = pypyodbc.win_create_mdb('%s.mdb' % (mdbfilepath))
            #connection.cursor().execute('CREATE TABLE candidate (id VARCHAR(255) PRIMARY KEY, name VARCHAR(25));').commit()
            connection.cursor().execute(sql_brandi_create).commit()
            response_text = ".mdb File Created @ %s" % (mdbfilepath)
            return response_text
        except KeyError as e:
            api.abort(500, e.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as e:
            api.abort(400, e.__doc__, status="Could not retrieve information", statusCode="400")