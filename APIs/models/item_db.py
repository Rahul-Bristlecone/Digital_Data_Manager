from APIs.resources.db import db


class ItemModel(db.Model):  # Mapping the class to the rows of the table
    __tablename__ = "items"  # Telling the name of the table i.e. items to SqlAlchemy

    item_id = db.Column(db.Integer, primary_key=True)  # need not be passed
    name = db.Column(db.String(40), unique=True, nullable=False)
    # category = db.Column(db.String(40), unique=True, nullable=False)  # unique to Range->category
    price = db.Column(db.Integer, unique=False, nullable=False)  # foreign key
    store_id = db.Column(db.Integer, db.ForeignKey("stores.store_id"), unique=False, nullable=False)

    store = db.relationship("StoreModel")
    tags = db.relationship("TagsModel", secondary="item_tags_db")
