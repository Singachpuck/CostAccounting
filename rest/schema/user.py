import marshmallow as ma
from marshmallow import validate


class UserPathVariableSchema(ma.Schema):
    user_id = ma.fields.Int()


class UserSchema(ma.Schema):
    id = ma.fields.Int(dump_only=True)
    name = ma.fields.String(validate=validate.Length(min=1))
