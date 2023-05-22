import uuid

from flask import Flask, request
from APIs.resources.stores_data import stores, product
from flask_smorest import abort

create = Flask(__name__)


# Retrieve all stores
@create.get("/stores")
def get_all_stores():
    return {"stores": list(stores.values())}


# Retrieve a single store
@create.get("/stores/<string:store_id>")
def get_store(store_id):
    try:
        return stores[store_id]
    except KeyError:
        # return {"message": "store not found"}, 404
        abort(404, message="store not found")


# Retrieve all items
@create.get("/products")
def get_all_item():
    # return "Hello world"
    return {"products": list(product.values())}


# Create a store
@create.post("/store")
def create_store():
    request_data = request.get_json()
    # validate that the name is provided
    if "name" not in request_data:
        abort(400, "Bad request. Please provide the name of the store")

    # check if the name already exists
    for i in stores.values():
        if request_data["name"] == i["name"]:
            abort(400, message="Bad request. Duplicate store name")

    store_id = uuid.uuid4().hex  # unique universal id is being generated
    new_store = {**request_data, "store_id": store_id}
    stores[store_id] = new_store
    return stores, 201


@create.delete("/store/<string:store_id>")
def delete_store(store_id):
    try:
        del stores[store_id]
        return {"message": "store deleted"}
    except KeyError:
        return {"message": "store not found"}


# Update a store
@create.put("/store/<string:store_id>")
def update_store(store_id):
    request_data = request.get_json()
    if "name" not in request_data:
        abort(400, message="store name not available")

    try:
        store = stores[store_id]
        print(type(store))
        store |= request_data
        return store
    except KeyError:
        return {"message": "India"}


# create an item
@create.post("/product")
def create_item():
    # validate that the data exists
    # TODO validate the type of data
    product_data = request.get_json()
    if ("range" not in product_data
            or "store_id" not in product_data):
        abort(400, message="Bad request. store_id, range should be included")

    # Check for Duplicate values
    for i in product.values():  # product.values is a list of dictionary in itself
        if (product_data["store_id"] == i["store_id"] and
                product_data["range"] == i["range"]):
            abort(400, message="Bad request. Product already exists")  # TODO abort message to be displayed in json

    if product_data["store_id"] in stores:
        product_id = uuid.uuid4().hex
        new_product = {**product_data, "product_id": product_id}
        product[product_id] = new_product
        return product, 201
    else:
        return {"message": "Store not available"}


# Retrieve an item
@create.get("/product/<string:product_id>")
def get_product(product_id):
    return product[product_id]


# delete an product
@create.delete("/products/<string:product_id>")
def delete_product(product_id):
    try:
        del product[product_id]
        return {"message": "product deleted"}
    except KeyError:
        return {"message": "Product not available"}


@create.put("/product/<string:product_id>")
def update_product(product_id):
    request_data = request.get_json()
    if ("price" not in request_data or
            "store_id" not in request_data or
            "range" not in request_data):
        return {"message": "Keys not available"}

    # Validating if a product is part of some store (exists)
    for i in product.values():  # product.values is a list of dictionary in itself
        if (request_data["store_id"] == i["store_id"] and
                request_data["range"] == i["range"]):
            return {"message": "Product already exist"}
            # abort(400, message="Bad request. Product already exists") TODO abort message to be displayed in json

    try:
        item = product[product_id]  # How item is a dictionary
        item |= request_data
        return item
    except KeyError:
        return {"message": "Key does not exist"}

# TODO Retrieve items of a single store
