from flask import Flask
from flask_smorest import Api
import os

from sqlalchemy.testing.config import db_url

import Resources.config
from APIs.resources.db import db
import APIs.models
from APIs.resources.store import blp as Blue

# This is called factory pattern

develop_store = Flask(__name__)


# db_user = Resources.config.DB_USER
# db_pass = Resources.config.DB_PASS
# db_name = Resources.config.DB_NAME
# db_host = Resources.config.DB_HOST
def create_app(db_url=None):
    develop_store.config["PROPAGATE_EXCEPTIONS"] = True
    develop_store.config["API_TITLE"] = "Stores REST API"
    develop_store.config["API_VERSION"] = "v1"
    develop_store.config["OPENAPI_VERSION"] = "3.0.3"
    develop_store.config["OPENAPI_URL_PREFIX"] = "/"
    develop_store.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    develop_store.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    develop_store.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL", "sqlite:///data.db")
    db.init_app(develop_store)

    api = Api(develop_store)

    with develop_store.app_context():
        db.create_all()

    api.register_blueprint(Blue)

    return develop_store
