from APIs.resources.db import db


class TagsModel(db.Model):  # Mapping the class to the rows of the table
    __tablename__ = "tags"  # Telling the name of the table i.e. items to SqlAlchemy

    tag_id = db.Column(db.Integer, primary_key=True)  # need not be passed
    name = db.Column(db.String(40), unique=True, nullable=False)
    # category = db.Column(db.String(40), unique=True, nullable=False)  # unique to Range->category
    store_id = db.Column(db.Integer, db.ForeignKey("stores.store_id"), unique=False, nullable=False)
    store = db.relationship("StoreModel")

    items = db.relationship("ItemModel", secondary="item_tags_db")
