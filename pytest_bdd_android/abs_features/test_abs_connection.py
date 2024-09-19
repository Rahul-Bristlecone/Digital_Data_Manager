from pytest_bdd import scenario, scenarios, given, when, then
from pathlib import Path

from pytest_bdd.types import GIVEN

scenario_file = "connection.feature"
directory_path = "abs_features"

parent_path = Path(__file__).resolve().parent
FILE_PATH = parent_path.joinpath(scenario_file)


# load the .feature file
# in case of pytest-fixture, Scenario will be the fixture

@scenario(FILE_PATH, "set up and verify connection")
def test_connection():
    print(FILE_PATH)


@given("the URL 102.34.32 & port number")
def test_url_port():
    print("port and url")


@when("I send a request to URL with port number")
def test_request():
    print("Test request")


@then("connection response should be 200 (successful)")
def test_response():
    print("Verify resposnse code")
