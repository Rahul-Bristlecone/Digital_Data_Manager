from marshmallow import Schema, fields


# TODO Nested data validations using Marshmallow
# TODO Duplicate data validations

# This is for validation of incoming request data
class StoreSchema(Schema):
    store_id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    product = fields.List(fields.Str())


class UpdateStoreSchema(Schema):
    store_id = fields.Str(required=True)
    name = fields.Str(required=True)
    product = fields.List(fields.Str())
