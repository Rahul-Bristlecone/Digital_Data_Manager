from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from APIs.models import ItemModel
from APIs.models.store_db import StoreModel
from APIs.models.tags_db import TagsModel
from APIs.models.item_db import ItemModel

from APIs.resources.db import db
from APIs.schemas import TagsSchema, TagAndItemSchema

blp = Blueprint("tags", __name__, description="Operations on tags")


# Tags related to a store (create and retrieve)
@blp.route("/store/<int:store_id>/tag")
class TagsInStore(MethodView):
    # get the list of tags registered under a store
    @blp.response(200, TagsSchema(many=True))
    def get(self, store_id):
        if store_id:
            store = StoreModel.query.get_or_404(store_id)
            return store.tags()
        # store = StoreModel.query.get_or_404(store_id)  # to check if store_id exists
        # return store.query.all()

    # creating/Register a tag for a store
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


@blp.route("/tag/<int:tag_id>")
class Tag(MethodView):
    @blp.response(200, TagsSchema)
    def get(self, tag_id):
        tag = TagsModel.query.get_or_404(tag_id)
        return tag

    @blp.response(200, TagsSchema)
    def delete(self, tag_id):
        tag = TagsModel.query.get_or_404(tag_id)
        if not tag.items:
            db.session.delete(tag)
            db.session.commit()
            return {"message": "Tag deleted"}
        abort(400, message="Tag is not free, associated with one or more items")


# class for linking/unlinking tag with item
@blp.route("/item/<int:item_id>/tag/<int:tag_id>")
class ItemTagsLink(MethodView):
    # To link tag and item, add a row in the ItemTags table
    @blp.response(201, TagsSchema)
    def post(self, tag_id, item_id):
        tag = TagsModel.query.get_or_404(tag_id)
        item = ItemModel.query.get_or_404(item_id)

        item.tags.append(tag)

        try:
            db.session.commit(item)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, "error")

        return tag

    @blp.response(201, TagAndItemSchema)
    def delete(self, tag_id, item_id):
        tag = TagsModel.query.get_or_404(tag_id)
        item = ItemModel.query.get_or_404(item_id)

        item.tags.remove(tag)

        try:
            db.session.commit(item)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="error")

        return {"message": "removed", "item": item, "tag": tag}
