from app.candidate.models import Candidate
from app.education_level.models import EducationLevel


def create_complete_candidate():

    el = EducationLevel(
        code='hs',
        description='high school degree'
    )

    return Candidate(
        dod_id='1234567890',
        first_name='philip',
        last_name='fry',
        # middle_initial='j',
        # sex='m',
        # dob=date(year=1986, month=10, day=10),
        education_level=el
    )