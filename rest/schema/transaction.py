import marshmallow as ma
from marshmallow import validate


class TransactionSchema(ma.Schema):
    id = ma.fields.Int(dump_only=True)
    account_from = ma.fields.Int(required=True)
    account_to = ma.fields.Int(required=True)
    category = ma.fields.Int(required=True)
    amount = ma.fields.Float(required=True, validate=validate.Range(min=0.0))
