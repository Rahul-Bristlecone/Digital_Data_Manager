import uuid

from flask import Flask, request
from APIs.resources.db_create import stores, product
from flask_smorest import abort

create = Flask(__name__)


# Retrieve all stores
@create.get("/stores")
def get_all_stores():
    return {"stores": list(stores.values())}


# Retrieve a single store
@create.get("/store/<string:store_id>")
def get_store(store_id):
    try:
        return stores[store_id]
    except KeyError:
        # return {"message": "store not found"}, 404
        abort(404, message="store not found")


# Create a new store
@create.post("/store")
def create_store():
    request_data = request.get_json()
    # validate that the name is provided
    if "name" not in request_data:
        abort(400, message="Bad request. Please provide the name of the store")

    # check if the name already exists
    for i in stores.values():
        if request_data["name"] == i["name"]:
            abort(400, message="Bad request. Store already exists")

    store_id = uuid.uuid4().hex  # unique universal id is being generated
    new_store = {**request_data, "store_id": store_id}
    stores[store_id] = new_store
    return stores, 201


# Update an existing store
@create.put("/store/<string:store_id>")
def update_store(store_id):
    request_data = request.get_json()
    if "name" not in request_data:
        abort(400, message="Please provide the name of the store")

    try:
        store = stores[store_id]  # store is a dictionary, store_id is value (not in quotes)
        store |= request_data
        return store
    except KeyError:
        abort(400, message="Bad Request, KeyError")


# Delete an existing store
@create.delete("/store/<string:store_id>")
def delete_store(store_id):
    try:
        del stores[store_id]  # stores is a dictionary of dictionaries, store_id is value (not in quotes)
        return {"message": "store has been deleted"}
    except KeyError:
        abort(400, message="Bad Request, KeyError")


# Retrieve all products
@create.get("/products")
def get_all_products():
    # return "Hello world"
    return {"products": list(product.values())}


# Retrieve an existing product
@create.get("/product/<string:product_id>")
def get_product(product_id):
    return product[product_id]


# create a product
@create.post("/product")
def create_product():
    # validate that the data exists
    # TODO validate the type of data
    product_data = request.get_json()
    if ("Dept" not in product_data
            or "store_id" not in product_data):
        abort(400, message="Bad request. Keys : store_id, Department should be included")

    # Check for Duplicate values
    for i in product.values():  # product.values is a list of dictionary in itself
        if (product_data["store_id"] == i["store_id"] and
                product_data["Dept"] == i["Dept"]):
            abort(400, message="Bad request. Product already exists")  # TODO abort message to be displayed in json

    if product_data["store_id"] in stores:
        product_id = uuid.uuid4().hex
        new_product = {**product_data, "product_id": product_id}
        product[product_id] = new_product
        return product, 201
    else:
        return {"message": "Store not available"}


# update an existing store
@create.put("/product/<string:product_id>")
def update_product(product_id):
    request_data = request.get_json()
    if ("price" not in request_data or
            "store_id" not in request_data or
            "Dept" not in request_data):
        return {"message": "Keys not available"}

    # Validating if a product is part of some store (exists)
    for i in product.values():  # product.values is a list of dictionary in itself
        if (request_data["store_id"] == i["store_id"] and
                request_data["product_id"] == i["product_id"]):
            try:  # How item is a dictionary
                product[product_id] |= request_data
                return product
            except KeyError:
                return {"message": "Key does not exist"}


# Update an existing product
# @create.put("/product/<string:product_id>")
# def update_product(product_id):
#     request_data = request.get_json()
#     if ("price" not in request_data or
#             "store_id" not in request_data or
#             "Dept" not in request_data):
#         return {"message": "Keys not available"}
#
#     # Validating if a product is part of some store (exists)
#     for i in product.values():  # product.values is a list of dictionary in itself
#         if (request_data["store_id"] == i["store_id"] and
#                 request_data["product_id"] == i["product_id"]):
#             return {"message": "Product already exist"}
#             # abort(400, message="Bad request. Product already exists") TODO abort message to be displayed in json
#
#     try:
#         item = product[product_id]  # How item is a dictionary
#         item |= request_data
#         return item
#     except KeyError:
#         return {"message": "Key does not exist"}


# delete an existing product
@create.delete("/product/<string:product_id>")
def delete_product(product_id):
    try:
        del product[product_id]
        return {"message": "product deleted"}
    except KeyError:
        return {"message": "Product not available"}

# TODO Retrieve items of a single store
