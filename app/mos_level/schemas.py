from marshmallow import Schema, fields, post_load
from app.mos_level.models import MOSLevel


class MOSLevelSchema(Schema):

    code = fields.String()
    description = fields.String()

    @post_load
    def make_mos_level(self, data, **kwargs):
        return MOSLevel(**data)