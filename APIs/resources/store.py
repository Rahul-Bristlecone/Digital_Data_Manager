import uuid
from flask_smorest import Blueprint, abort
from flask.views import MethodView
# from flask import request

from APIs.resources import stores_data
from APIs.schemas import StoreSchema, UpdateStoreSchema

# created a blueprint with description and Dunder method (__name__)
# Dunder are usually used for operator overloading
blp = Blueprint("stores", __name__, description="Operations on stores")


# create a class from MethodView whose methods will route to specific end-points because the blue-print is
# prepared for that particular class

# This blueprint method will route all the methods of this class to this particular end-point
@blp.route("/store/<string:store_id>")
class Stores(MethodView):
    def get(self, store_id):
        try:
            return stores_data.stores[store_id]
        except KeyError:
            # return {"message": "store not found"}, 404
            abort(404, message="store not found")

    def delete(self, store_id):
        try:
            del stores_data.stores[store_id]
            return stores_data.stores[store_id]
        except KeyError:
            # return {"message": "store not found"}, 404
            abort(404, message="store not found")

    # TODO if incoming data for a store has some blank values apart from the name of the store, not to be updated
    @blp.arguments(UpdateStoreSchema)  # Validation of request data (i.e. store_data) for updating a store
    def put(self, store_data, store_id):
        # request_data = request.get_json()
        try:
            store = stores_data.stores[store_id]
            store |= store_data
            return store
        except KeyError:
            abort(400, message="Store not available")


@blp.route("/store")
class StoreList(MethodView):
    @blp.response(200)
    def get(self):
        return {"stores": list(stores_data.stores.values())}

    @blp.arguments(StoreSchema)  # Validation of request data for creating a store (Marshmallow)
    @blp.response(201, StoreSchema)  # Decorating the response
    def post(self, store_data):
        # check if the name already exists, this can also be done using Marshmallow
        for i in stores_data.stores.values():
            if store_data["name"] == i["name"]:
                abort(400, message="Bad request. Duplicate store name")

        store_id = uuid.uuid4().hex  # unique universal id is being generated
        new_store = {**store_data, "store_id": store_id}
        stores_data.stores[store_id] = new_store
        return stores_data.stores, 201
