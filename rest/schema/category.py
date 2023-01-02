import marshmallow as ma
from marshmallow import validate

class CategoryQuerySchema(ma.Schema):
    category = ma.fields.String(required=False)


class CategorySchema(ma.Schema):
    id = ma.fields.Int(dump_only=True)
    name = ma.fields.String(required=True, validate=validate.Length(min=1))
