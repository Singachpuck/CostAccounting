import marshmallow as ma
from marshmallow import validate


class AccessTokenSchema(ma.Schema):
    access_token = ma.fields.String()
    expires_in = ma.fields.Int()


class UserSchemaLogin(ma.Schema):
    id = ma.fields.Int(dump_only=True)
    name = ma.fields.String(required=True, validate=validate.Length(min=1))
    password = ma.fields.String(required=True, validate=validate.Length(min=4))


class UserSchema(ma.Schema):
    id = ma.fields.Int(dump_only=True)
    name = ma.fields.String(required=True, validate=validate.Length(min=1))
