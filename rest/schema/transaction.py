import marshmallow as ma
from marshmallow import validate


class TransactionSchema(ma.Schema):
    id = ma.fields.Int(dump_only=True)
    account_from = ma.fields.Int()
    account_to = ma.fields.Int()
    category = ma.fields.Int()
    amount = ma.fields.Float(validate=validate.Range(min=0.0))
