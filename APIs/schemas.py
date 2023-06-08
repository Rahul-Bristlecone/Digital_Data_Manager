from marshmallow import Schema, fields


# TODO Nested data validations using Marshmallow
# TODO Duplicate data validations

# This is for validation of incoming request data

class PlainItemSchema(Schema):
    # store_id = fields.Str(dump_only=True) # commented because dealt in another class below
    product_id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Int(required=True)


class PlainStoreSchema(Schema):
    store_id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    # product = fields.List(fields.Str())


class PlainTagsSchema(Schema):
    tag_id = fields.Int(dump_only=True)
    name = fields.Str()


class UpdateStoreSchema(Schema):
    store_id = fields.Str(required=True)
    name = fields.Str(required=True)
    product = fields.List(fields.Str())


class UpdateItemSchema(Schema):
    name = fields.Str()
    price = fields.Int()
    store_id = fields.Int()


class ItemSchema(PlainItemSchema):
    store_id = fields.Int(required=True, load_only=True)  # store_id will automatically load up when use ItemSchema
    store = fields.Nested(PlainStoreSchema(), dump_only=True)
    tag = fields.List(fields.Nested(PlainTagsSchema()), dump_only=True)


class StoreSchema(PlainStoreSchema):
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)
    tags = fields.List(fields.Nested(PlainTagsSchema(), dump_only=True))


class TagsSchema(PlainTagsSchema):
    tag_id = fields.Int(load_only=True)  # store_id will automatically load up when use ItemSchema
    store = fields.Nested(PlainStoreSchema(), dump_only=True)
    tag = fields.List(fields.Nested(PlainItemSchema(), dump_only=True))


class TagAndItemSchema(Schema):
    message = fields.Str()
    item = fields.Nested(ItemSchema)
    tag = fields.Nested(TagsSchema)
