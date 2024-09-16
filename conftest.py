import pytest


def pytest_configure():
    pytest.lst1 = [12, 13, 12, 98, 1, 26]


@pytest.fixture()
def append_list():
    list1 = pytest.lst1
    list1.append(56)
    yield list1
    print("Driver syncing")


# fixtures are like before test & after test tests
# like test browsers, db connections - use cases
# fixture is actually passed as argument in a test function - one way to call the fixture
# another is using a marker
@pytest.fixture()
def store_data():
    print("***** Testing fixtures *****")
    data = ["store_id", "store_name", "tags", "products included"]
    return data


# fixtures for request
# fixtures for parameterization
@pytest.fixture()
def data_verify(request):
    print("\nInside module : " + str(request.module.__name__))
    print("inside function : " + str(request.function.__name__))
    print("Scope " + str(request.scope))


# fixtures for factories - result of a fixture is needed multiple time
# the fixture will return the function which in turn will return the data
# task - create a fixture to return the data type
@pytest.fixture()
def data_type_collection():
    def test_data(name):
        if name == "list":
            return [1, 2, 3]
        elif name == "string":
            return ["name", "fame", "came"]
        elif name == "tuple":
            return (2,4,5)

    return test_data


# fixture to be used for parameterization
# providing data using fixture which is actually
# the work of parameterization
@pytest.fixture(params=[("2", "4"), [2, 3, 4]], ids = [tuple, list])
def data_for_fixture(request):
    return request.param


@pytest.fixture(params=["access", "slice", "assign"])
def access_data(request):
    return request.param