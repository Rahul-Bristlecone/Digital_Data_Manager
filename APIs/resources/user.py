from flask_smorest import Blueprint, abort
from flask.views import MethodView
from passlib.hash import pbkdf2_sha256
from flask_jwt_extended import create_access_token
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from APIs.resources.db import db
from APIs.models.user_db import UserModel
from APIs.schemas import UserSchema

blp = Blueprint("Users", __name__, description="operations on user")


@blp.route("/register")
class UserRegister(MethodView):
    @blp.arguments(UserSchema)
    def post(self, user_data):
        if UserModel.query.filter(UserModel.username == user_data["username"]).first():
            abort(409, message="already exist")

        user = UserModel(username=user_data["username"],
                         password=pbkdf2_sha256.hash(user_data["password"]), )

        db.session.add(user)
        db.session.commit()

        return {"message": "All good"}, 201


@blp.route("/login")
class UserAuth(MethodView):
    @blp.arguments(UserSchema)
    def post(self, user_data):
        # checking if the user exists
        user = UserModel.query.filter(UserModel.username == user_data["username"]).first()
        # verifying if the password provided matches with the password saved in db
        if user and pbkdf2_sha256.verify(user_data["password"], user.password):
            # generated token will be used for the specific end-points
            access_token = create_access_token(identity=user.user_id)
            return {"Token": access_token}
        return {"message": "Invalid credentials"}
