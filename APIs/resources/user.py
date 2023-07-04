from flask_smorest import Blueprint, abort
from flask.views import MethodView
# from passlib import pbkdf2_sha256
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from APIs.resources.db import db
from APIs.models.user_db import UserModel
from APIs.schemas import UserSchema

blp = Blueprint("Users", __name__, description="operations on user")


class UserRegister(MethodView):
    def post(self, user_data):
        if UserModel.query.filter(UserModel.username == user_data["username"]).first():
            abort(409, message="already exist")

            user = UserModel(usename=user_data["username"],
                             password=user_data["password"])

            db.session.add(user)
            db.session.commit(user)

            return {"message":"All good"}
