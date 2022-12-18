from marshmallow import Schema, fields, validate



class schemaPost(Schema):
    student_id = fields.String(required=True)
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    email = fields.String(required=True)
    gender = fields.String(required=True)
    department = fields.String(required=True)
    title = fields.String(required=True)
    university = fields.String(required=True)

class schemaPut(schemaPost):
    student_id = fields.String(required=True)
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    email = fields.String(required=True)
    gender = fields.String(required=True)
    department = fields.String(required=True)
    title = fields.String(required=True)
    university = fields.String(required=True)