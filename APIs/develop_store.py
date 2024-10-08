from flask import Flask, jsonify
from flask_smorest import Api
import os

from flask_jwt_extended import JWTManager

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.testing.config import db_url

from APIs.resources.db import db
from blocklist import BLOCKLIST
import APIs.models  # SQLAlchemy knows tables to be created through Models

from APIs.resources.store import blp as StoreBp
from APIs.resources.product import blp as ItemBp
from APIs.resources.tags import blp as TagsBp
from APIs.resources.user import blp as UserBp


# This is called factory pattern

# db_user = Resources.config.DB_USER
# db_pass = Resources.config.DB_PASS
# db_name = Resources.config.DB_NAME
# db_host = Resources.config.DB_HOST
def create_app(db_url=None):
    develop_store = Flask(__name__)
    develop_store.config["PROPAGATE_EXCEPTIONS"] = True
    develop_store.config["API_TITLE"] = "Stores REST API"
    develop_store.config["API_VERSION"] = "v1"
    develop_store.config["OPENAPI_VERSION"] = "3.0.3"
    develop_store.config["OPENAPI_URL_PREFIX"] = "/"
    develop_store.config['TESTING'] = True
    develop_store.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    develop_store.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    develop_store.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL", "sqlite:///store_data.db")
    db.init_app(develop_store)  # db is SQLAlchemy extension

    api = Api(develop_store)
    # assign a secret key to JWT to verify that the key is generated by application
    # configuring this application to use JWTs for authentication
    develop_store.config["JWT_SECRET_KEY"] = "hello"
    jwt = JWTManager(develop_store)

    @jwt.token_in_blocklist_loader
    def verify_token_exist(jwt_header, jwt_payload):
        return jwt_payload["jti"] in BLOCKLIST

    @jwt.expired_token_loader
    def missing_token(error):
        return jsonify({"message": "Token missing"}), 401

    @jwt.expired_token_loader
    def invalid_token(error):
        return jsonify({"message": "Signature verification failed, invalid token"}), 401

    @jwt.expired_token_loader
    def expired_token(jwt_header, jwt_payload):
        return jsonify({"message": "Expired token"}), 401

    @develop_store.before_request
    def create_tables():
        db.create_all()

    # with develop_store.app_context():
    #     # db = SQLAlchemy(develop_store)
    #     db.create_all()

    api.register_blueprint(StoreBp)
    api.register_blueprint(ItemBp)
    api.register_blueprint(TagsBp)
    api.register_blueprint(UserBp)

    return develop_store
