from models.store import StoreModel
from tests.base_test import BaseTest
from models.item import ItemModel


class TestStore(BaseTest):
    # def test_create_store(self):
    #     store = StoreModel("plum")
    #     self.assertEqual(store.items.all(), [], "store already exists")

    def test_crud(self):
        with self.app_context():
            store = StoreModel('plum')
            # store should be empty before creation of store
            self.assertIsNone(StoreModel.find_by_name('plum'), "Found an store with name 'test' before save_to_db")
            # store create
            store.save_to_db()
            # verify if store creation was successful
            self.assertIsNotNone(StoreModel.find_by_name('plum'),
                                 "Did not find an store with name 'test' after save_to_db")
            # delete store
            store.delete_from_db()
            # verify if deletion was successful
            self.assertIsNone(StoreModel.find_by_name('plum'), "Found an store with name 'test' after delete_from_db")

    def test_store_relationship(self):
        with self.app_context():
            store = StoreModel("plum")
            item = ItemModel("test_item", 19.99, 1)

            store.save_to_db()
            item.save_to_db()

            self.assertEqual(store.items.first().name, "test_item")  # check "store" as foreign key of item
