import uuid
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from sqlalchemy.exc import SQLAlchemyError

from APIs.resources.db import db
from APIs.models import ItemModel
from APIs.schemas import StoreSchema, UpdateStoreSchema, ItemSchema

# created a blueprint "stores" with description and Dunder method (__name__)
# Dunder are usually used for operator overloading
blp = Blueprint("Items", __name__, description="Operations on Items")


# create a class from MethodView whose methods will route to specific end-points because the blue-print is--
# --prepared for that particular class
# This blueprint method will route all the methods of this class to this particular end-point
@blp.route("/item/<string:item_id>")
class Item(MethodView):
    @blp.response(200, ItemSchema)
    def get(self, item_id):
        try:
            item = ItemModel.query.get_or_404(item_id)
            return item
        except KeyError:
            # return {"message": "store not found"}, 404
            abort(404, message="item not found")

    def delete(self, item_id):
        try:
            item = ItemModel.query.get_or_404(item_id)
            db.db.session.delete(item)
            db.db.session.commit()
            return {"message": "item deleted"}
        except KeyError:
            # return {"message": "store not found"}, 404
            abort(404, message="item not found")


@blp.route("/item")
class ItemList(MethodView):
    @blp.response(200, ItemSchema(many=True))
    def get(self):
        return items.values()
        # store = StoreModel.query.get_or_404(store_id)

    # TODO if incoming data for a store has some blank values apart from the name of the store, not to be updated
    # @blp.arguments(UpdateStoreSchema)  # Validation of request data (i.e. store_data) for updating a store
    # def put(self, store_data, store_id):
    #     # request_data = request.get_json()
    #     try:
    #         store = StoreModel.query.get_or_404(store_id)
    #         store |= store_data
    #         db.db.session.commit()
    #         return store
    #     except KeyError:
    #         abort(400, message="Store not available")

    @blp.arguments(ItemSchema)  # Validation of request data for creating a store (Marshmallow)
    @blp.response(201, ItemSchema)  # Decorating the response
    def post(self, item_data):
        # check if the name already exists, this can also be done using Marshmallow
        item = ItemModel(**item_data)

        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="Store not available while inserting item")

        return item

        # store_id = uuid.uuid4().hex  # unique universal id is being generated
        # new_store = {**store_data, "store_id": store_id}
        # stores_data.stores[store_id] = new_store
        # return stores_data.stores, 201
