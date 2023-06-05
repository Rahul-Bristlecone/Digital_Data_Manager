from APIs.resources.db import db


class StoreModel(db.Model):  # Mapping the class to the rows of the table
    __tablename__ = "stores"  # Telling the name of the table i.e. items to SqlAlchemy

    store_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=True, nullable=False)
    items = db.relationship("ItemModel", lazy="dynamic")

