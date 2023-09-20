from tests.base_test import BaseTest
from models.store import StoreModel
from models.item import ItemModel
from models.user import UserModel


class TestUser(BaseTest):

    def test_create_user(self):
        user = UserModel("plum", "kereate")
        self.assertEqual(user.username, "plum")
        self.assertEqual(user.password, "kereate")

    # def test_json(self):
    #     store = StoreModel("plum")
    #     expected_res = {"name": "plum", "items": []}
    #     self.assertEqual(store.json(), expected_res)
