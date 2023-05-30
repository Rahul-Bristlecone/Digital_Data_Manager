""" Create a store - name, items using POST - send store details (name and item[]) in the request body
    and response will be
    1) success code
    2) store created with name and empty list
    3) {name:"OrganicHarvest",
        items:[]} - DONE
"""
""" 
    Create item inside store - (though a store name end-point) - 
    send item details (range & details) in the request body - DONE 
"""
""" Create a store - by clicking the submit button json generated will be the body and 
    concurrently post method will be called """
# Retrieve all stores - DONE
# Retrieve a specific store - DONE
# Retrieve all items of a specific store - DONE
# Retrieve a specific item for a specific store - DONE
# POST request to save the "body data" in database

from flask import Flask, request
import json

app = Flask(__name__)  # Creates a flask app

# list of stores (dictionary)
with open("resources/app_stores.json", 'r') as store_data:
    store_list = []
    store = json.load(store_data)
    store_list.append(store)
    print(type(store_list))


# Retrieve all stores
@app.get("/stores")
def get_stores():
    # return store_list[0] - return first store (which is dictionary in itself)
    # return store_list[0]["name"] - return a name of store
    # return store_list[0]["items"][0]["range"] - return the range of the item accessed
    # print(store_list[0]["products"][0]["details"][0]["category"] + " of " + store_list[0]["products"][0]["range"]
    #       + " range from " + store_list[0]["name"])
    return store_list  # return list of stores


# Retrieve a specific store
@app.get("/store/<string:name>")
def get_store(name):
    for store_name in store_list:
        if store_name["name"] == name:
            return store_name
    return {"message": "Store does not exist"}, 404


# Create a new store
@app.post("/store")  # TODO using query string parameters like ?name=OrganicHarvest
def create_store():
    request_data = request.get_json()
    # new_store = {"name": request_data["name"], "products": request_data["products"]}
    store_list.append(request_data)
    # print(store_list)
    return request_data, 201


# Update an existing store
@app.put("/store/<string:store_name>")
def update_store(store_name):
    request_data = request.get_json()
    for store_name in store_list:
        if store_name["name"] == request_data["name"]:
            store_name |= request_data
            return store_list


# Delete an existing store
@app.delete("/store/<string:store_name>")
def delete_store(store_name):
    request_data = request.get_json()
    for store_name in store_list:
        if store_name["name"] == request_data["name"]:
            store_list.remove(store_name)
            return store_list


# Get all products of a specific store
@app.get("/<string:store_name>/products")
def get_products(store_name):
    for store in store_list:  # store_name is a dictionary
        if store["name"] == store_name:
            return store["products"]  # This will return a list
    return {"message": "Store does not exist"}, 404


# get a specific product (range) from a store
@app.get("/<string:store_name>/<string:product_name>")  # this is better implemented using product_id
def get_product(store_name, product_name):
    for store in store_list:  # store is a dictionary
        if store["name"] == store_name:
            for product in store["products"]:
                if product["range"] == product_name:
                    return product


@app.get("/stores/<string:name>/items/range")
def get_all_ranges(name):
    ranges = []
    for store_name in store_list:
        if store_name["name"] == name:
            for item in store_name["products"]:
                print(item["range"])
                ranges.append(item["range"])
            return ranges
    return {"message": "store does not exist"}, 404


get_all_ranges("MamaEarth")


# Create single/multiple product for a specific store
@app.post("/<string:store_name>/product")  # TODO using query string parameters like ?item name=Vitamin C
def create_product(store_name):
    request_data = request.get_json()
    for store in store_list:
        if store["name"] == store_name and request_data["products"] != []:
            for i in range(len(request_data["products"])):
                new_product = {"range": request_data["products"][i]["range"],
                               "details": request_data["products"][i]["details"]}  # TODO add item with full details
                store["products"].append(new_product)
            return store["products"], 201
    return {"message": "store does not exist"}, 404


# update all products for a specific store
@app.put(
    "/<string:store_name>/product/<string:product_range>")  # TODO using query string parameters like ?item name=Vitamin C
def update_product(store_name, product_range):
    request_data = request.get_json()
    for store in store_list:
        if store["name"] == store_name:
            store["products"] = request_data["products"]
            return store["products"], 201
    return {"message": "store does not exist"}, 404


# delete all products for a store
@app.put("/<string:store_name>/product")
def update_product_only(store_name):
    # request_data = request.get_json()
    for store in store_list:
        if store["name"] == store_name:
            store["products"].clear()
            return store, 201


# delete all products for a store
@app.delete("/<string:store_name>/product")
def delete_products(store_name):
    # request_data = request.get_json()
    for store in store_list:
        if store["name"] == store_name:
            store["products"].clear()
            return store, 201
    return {"message": "store does not exist"}, 404
