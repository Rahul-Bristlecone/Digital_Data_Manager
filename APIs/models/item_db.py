from APIs.resources.db import db


class ItemModel(db.Model):  # Mapping the class to the rows of the table
    __tablename__ = "items"  # Telling the name of the table i.e. items to SqlAlchemy

    product_id = db.Column(db.Integer, primary_key=True, nullable=False)
    range = db.Column(db.String(40), unique=True, nullable=False)
    # category = db.Column(db.String(40), unique=True, nullable=False)  # unique to Range->category
    store_id = db.Column(db.Integer, db.ForeignKey("stores.store_id"), unique=False, nullable=False)  # foreign key
    store = db.relationship("StoreModel")
