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


# Retrieve all stores only - not a specific store
@app.get("/stores")
def get_stores():
    # return store_list[0] - return first store (which is dictionary in itself)
    # return store_list[0]["name"] - return a name of store
    # return store_list[0]["items"][0]["range"] - return the range of the item accessed
    # print(store_list[0]["products"][0]["details"][0]["category"] + " of " + store_list[0]["products"][0]["range"]
    #       + " range from " + store_list[0]["name"])
    return store_list  # return list of stores


get_stores()


# Retrieve a specific store
@app.get("/stores/<string:name>")
def get_store(name):
    for store_name in store_list:
        if store_name["name"] == name:
            return store_name
    return {"message": "Store does not exist"}, 404


# Get all items of a specific store
@app.get("/stores/<string:name>/items")
def get_items(name):
    for store_name in store_list:  # store_name is a dictionary
        if store_name["name"] == name:
            return store_name["products"]  # This will return a list
    return {"message": "Store does not exist"}, 404


# Retrieve all the product ranges, for which items are available in a specific store
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


# Create a new store
@app.post("/store")  # TODO using query string parameters like ?name=OrganicHarvest
def create_store():
    request_data = request.get_json()
    new_store = {"name": request_data["name"], "products": request_data["products"]}
    store_list.append(new_store)
    # print(store_list)
    return new_store, 201


# Create a product inside a specific store
@app.post("/store/<string:name>/item")  # TODO using query string parameters like ?item name=Vitamin C
def create_product(name):
    request_data = request.get_json()
    for store_name in store_list:
        if store_name["name"] == name:
            new_item_details = {"range": request_data['range'],
                                "details": request_data['details']}  # TODO add item with full details
            store_name["products"].append(new_item_details)
            return new_item_details, 201
    return {"message": "store does not exist"}, 404
