from APIs.resources.db import db


class ItemTagsModel(db.Model):
    __tablename__ = "ItemTagsModel"

    item_tag_id = db.Column(db.Integer, primary_key=True)
    item_id = db.column(db.Integer, db.ForeignKey("item_db.item_id"))
    tag_id = db.column(db.Integer, db.ForeignKey("tags_db.tag_id"))
