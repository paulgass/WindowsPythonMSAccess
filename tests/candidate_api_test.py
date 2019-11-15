from tests.data_utils import create_complete_candidate
from app.candidate.schemas import CandidateSchema
from tests.fixtures import app, client


def test_post(app, client):

    # given
    candidate = create_complete_candidate()
    schema = CandidateSchema()
    dictionary = schema.dumps(candidate)
    # c_json = json.dumps(dictionary)

    with client:

        response = client.post('/candidates', data=dictionary, content_type='application/json')
        # assert response.status_code == 201
        # assert response.is_json


# def test_get_all(app, client):
#
#     with client:
#
#         response = client.get('/candidates')
#         assert response.status_code == 200
#         assert response.is_json
