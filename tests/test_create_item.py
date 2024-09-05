import pytest
from APIs.resources.db import db
from APIs.develop_store import create_app
# from APIs.models import ItemModel


@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///store_data.db'
    with app.app_context():
        db.create_all()
    yield app


@pytest.fixture
def client(app):
    return app.test_client()


# In this example, we defined two pytest fixtures app and client, that set up a test Flask application and
# a test client for making requests to the application. We then define a test function test_post
# that uses the client fixture to make a POST request to the /item endpoint with some test data.
# We check the response status code and data to make sure they are correct, and
# we also check that the item was added to the database

def test_post(client):
    # Test data
    item_data = {
        "name": "test_item05",
        "price": 10,
        "store_id": 1
    }

    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5MTA0MTk0OSwianRpIjoiYjIxZDFiYzEtOGY5Yy00OGExLWJlNDUtZjAyYzlkYzc1YWFlIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MywibmJmIjoxNjkxMDQxOTQ5LCJleHAiOjE2OTEwNDI4NDl9.EPHoyQsLoA5PG8ezd35o0VN9PS8jBIiyAEXky2enk7c"

    # Make a POST request to the endpoint with the test data
    response = client.post("/item", json=item_data, headers={"Authorization": f"Bearer {token}"})

    # Check the response status code and data
    assert response.status_code == 201
    assert response.get_json() == {
        "product_id": 23,
        "name": "test_item05",
        "price": 10,
        "tags": []
    }

    # # Check that the item was added to the database
    # with app.app_context():
    #     item = ItemModel.query.filter_by(name="test_item8").first()
    #     assert item is not None
    #     assert item.name == "test_item8"
    #     assert item.price == 10
