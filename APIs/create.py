from flask import Flask
from Digital_Manager import glambook

create = Flask(__name__)

store_list = [
    {
        "name": "MamaEarth",
        "products":
        [
            {
                "range": "Aloe vera",
                "details":
                [
                    {
                        "category": "face",
                        "Description":
                        {
                            "gender": "men",
                            "product_type": "Moisturiser",
                            "price": 256.80,
                            "quantity": 80
                        }
                    },
                    {
                        "category": "Body",
                        "Description":
                        {
                            "gender": "men",
                            "product_type": "Body Lotion",
                            "price": 199,
                            "quantity": 200
                        }
                    }
                ]
            },
            {
                "range": "Vitamin C",
                "Details":
                [
                    {
                        "category": "Serum",
                        "Description":
                        {
                            "gender": "women",
                            "type": "face",
                            "price": 459.80,
                            "quantity": 100
                        }
                    }
                ]
            }
        ]
    }
]


@create.post("/store")
def create():
    store_instance = glambook.GlamBookFrame()
    request_data = store_instance.submit_details()
    new_store = {"name": request_data["name"], "items": []}
    store_list.append(new_store)
    print(store_list)
    return store_list, 201
    pass


create()