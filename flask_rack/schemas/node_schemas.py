## Define schemas for Node domain objects in order to perform basic input validation for requests server-side. 
#  to do this, we leverage Marshmallow framework: https://marshmallow.readthedocs.io/en/stable/api_reference.html
from marshmallow import Schema, fields, validate
class NodeSettingsSchema(Schema):
    # the 'required' argument ensures the field exists
    note = fields.Str(required=False)
    node_id = fields.Str(validate=validate.Length(min=1))
    ip = fields.Str(required=True)
    fps = fields.Str(required=True)
    res = fields.Str(required=True)
    location = fields.Str(required=False)
    #time_created = fields.DateTime(required=True)