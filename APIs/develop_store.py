from flask import Flask
from flask_smorest import Api

from APIs.resources.store import blp as Blue

develop_store = Flask(__name__)

develop_store.config["PROPAGATE_EXCEPTIONS"] = True
develop_store.config["API_TITLE"] = "Stores REST API"
develop_store.config["API_VERSION"] = "v1"
develop_store.config["OPENAPI_VERSION"] = "3.0.3"
develop_store.config["OPENAPI_URL_PREFIX"] = "/"
develop_store.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
develop_store.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(develop_store)

api.register_blueprint(Blue)
