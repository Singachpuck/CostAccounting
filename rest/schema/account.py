import marshmallow as ma
from marshmallow import validate


class AccountSchema(ma.Schema):
    id = ma.fields.Int(dump_only=True)
    user = ma.fields.Int(required=True)
    amount = ma.fields.Float(required=True, validate=validate.Range(min=0.0))
