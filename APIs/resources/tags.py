from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from APIs.models import ItemModel
from APIs.models.store_db import StoreModel
from APIs.models.tags_db import TagsModel
from APIs.resources.db import db
from APIs.schemas import TagsSchema

blp = Blueprint("tags", __name__, description="Operations on tags")


@blp.route("/store/<string:store_id>/tag")
class TagsList(MethodView):
    # number of tags applicable for a store
    @blp.response(200, TagsSchema(many=True))
    def get(self, store_id):
        store = StoreModel.query.get_or_404(store_id)
        return store.tags.all()

    # creating tags but inside a store
    @blp.arguments(TagsSchema)
    @blp.response(201, TagsSchema)
    def post(self, tag_data, store_id):

        tag = TagsModel(**tag_data, store_id=store_id)

        try:
            db.session.add(tag)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(500, message="details incomplete")

        return tag


# Create an endpoint to link/unlink item with already created tags
# should exist & item should exist
@blp.route("/item/<string:item_id>/tag/<string:tag_id>")
class ItemTagLink(MethodView):
    @blp.response(201, TagsSchema)
    def post(self, tag_id, product_id):
        item = ItemModel.query.get_or_404(product_id)
        tag = TagsModel.query.get_or_404(tag_id)

        item.tags.append(tag)
        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the tag.")

        return tag


@blp.route("/tag/<string:tag_id>")
class Tag(MethodView):
    @blp.response(200, TagsSchema)
    def get(self, tag_id):
        tag = TagsModel.query.get_or_404(tag_id)
        return tag
