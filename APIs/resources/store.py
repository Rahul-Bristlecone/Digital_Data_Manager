import uuid
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from APIs.resources.db import db
from APIs.models import StoreModel
from APIs.schemas import StoreSchema, UpdateStoreSchema

# created a blueprint "stores" with description and Dunder method (__name__)
# Dunder are usually used for operator overloading
blp = Blueprint("stores", __name__, description="Operations on stores")


# create a class from MethodView whose methods will route to specific end-points because the blue-print is--
# --prepared for that particular class
# This blueprint method will route all the methods of this class to this particular end-point
@blp.route("/store/<string:store_id>")
class Store(MethodView):
    @blp.response(200, StoreSchema)
    def get(self, store_id):
        store = StoreModel.get_or_404(store_id)
        return store

    # except KeyError:
    #     # return {"message": "store not found"}, 404
    #     abort(404, message="store not found")

    def delete(self, store_id):
        try:
            store = StoreModel.query.get_or_404(store_id)
            db.db.session.delete(store)
            db.db.session.commit()
            return {"message": "store deleted"}
        except KeyError:
            # return {"message": "store not found"}, 404
            abort(404, message="store not found")


@blp.route("/store")
class StoreList(MethodView):
    @blp.response(200, StoreSchema(many=True))
    def get(self):
        return stores.values()
        # store = StoreModel.query.get_or_404(store_id)

    # TODO if incoming data for a store has some blank values apart from the name of the store, not to be updated
    @blp.arguments(UpdateStoreSchema)  # Validation of request data (i.e. store_data) for updating a store
    def put(self, store_data, store_id):
        # request_data = request.get_json()
        try:
            store = StoreModel.query.get_or_404(store_id)
            store |= store_data
            db.db.session.commit()
            return store
        except KeyError:
            abort(400, message="Store not available")

    @blp.arguments(StoreSchema)  # Validation of request data for creating a store (Marshmallow)
    @blp.response(201, StoreSchema)  # Decorating the response
    def post(self, store_data):
        # check if the name already exists, this can also be done using Marshmallow
        store = StoreModel(**store_data)
        try:
            db.session.add(store)
            db.session.commit()
        except IntegrityError:
            abort(400, message = "Store already exists")
        except SQLAlchemyError:
            abort(500, message="Store not available while creating")

        return store

        # store_id = uuid.uuid4().hex  # unique universal id is being generated
        # new_store = {**store_data, "store_id": store_id}
        # stores_data.stores[store_id] = new_store
        # return stores_data.stores, 201
