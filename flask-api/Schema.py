from marshmallow import Schema, fields, validate


class schemaPost(Schema):
    student_id = fields.Int(required=True)
    status = fields.Bool(required=True)
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    email = fields.String(required=True)
    gender = fields.String(required=True)
    professor_name = fields.String(required=True)
    year_of_graduation = fields.Int(required=True)
    degree = fields.String(required=True)
    projectId = fields.String(required=True)
    programming_language = fields.String(required=True)
    
