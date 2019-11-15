from marshmallow import Schema, fields, post_load
from app.rank_level.models import RankLevel


class RankLevelSchema(Schema):

    code = fields.String()
    description = fields.String()

    @post_load
    def make_rank_level(self, data, **kwargs):
        return RankLevel(**data)

