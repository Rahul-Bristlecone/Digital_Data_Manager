from models.item import ItemModel
from models.store import StoreModel
from tests.base_test import BaseTest


class TestItem(BaseTest):
    def test_crud(self):
        with self.app_context():  # to access the app and the db associated
            store = StoreModel("plum")  # these are needed when store is created for the item to be added
            store.save_to_db()
            item = ItemModel("Harley", "2.5", 1)
            # before save to db
            self.assertIsNone(ItemModel.find_by_name("Harley"))
            # adding to db
            item.save_to_db()
            # after save to db
            self.assertIsNotNone(ItemModel.find_by_name("Harley"))
            # deleting from db
            item.delete_from_db()
            # after delete from db
            self.assertIsNone(ItemModel.find_by_name("Harley"))

    def test_store_relationship(self):
        with self.app_context():
            store = StoreModel("test_store")
            item = ItemModel("test_item", 19.99, 1)

            store.save_to_db()
            item.save_to_db()

            self.assertEqual(item.store.name, "test store")  # check "store" as foreign key of item
