from marshmallow import Schema, fields


# TODO Nested data validations using Marshmallow
# TODO Duplicate data validations

# This is for validation of incoming request data

class PlainStoreSchema(Schema):
    store_id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    # product = fields.List(fields.Str())


class PlainItemSchema(Schema):
    # store_id = fields.Str(dump_only=True)
    product_id = fields.Str(required=True)
    range = fields.List(fields.Str())


class UpdateStoreSchema(Schema):
    store_id = fields.Str(required=True)
    name = fields.Str(required=True)
    product = fields.List(fields.Str())


class ItemSchema(PlainStoreSchema):
    store_id = fields.Str(load_only=True)  # store_id will automatically load up when use ItemSchema
    store = fields.Nested(PlainStoreSchema(), dump_only=True)


class StoreSchema(PlainItemSchema):
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only= True)
