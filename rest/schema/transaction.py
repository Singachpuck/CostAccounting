import marshmallow as ma
from marshmallow import validate


class TransactionSchema(ma.Schema):
    id = ma.fields.Int(dump_only=True)
    accountFrom = ma.fields.Int()
    accountTo = ma.fields.Int()
    categoryId = ma.fields.Int()
    amount = ma.fields.Float(validate=validate.Range(min=0.0))
