from marshmallow import Schema, fields, post_load
from app.education_level.models import EducationLevel


class EducationLevelSchema(Schema):

    code = fields.String()
    description = fields.String()

    @post_load
    def make_education_level(self, data, **kwargs):
        return EducationLevel(**data)

