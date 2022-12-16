import marshmallow as ma


class MessageSchemaOK(ma.Schema):
    status = ma.fields.String()
