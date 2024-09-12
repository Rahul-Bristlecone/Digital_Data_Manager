from flask import json

from models.user import UserModel
from tests.base_test import BaseTest


class TestUser(BaseTest):
    def test_user_register(self):
        with self.app() as client:  # it acts as a user needed for request-response
            with self.app_context():  # needed for database initialisation
                request = client.post("/register", data={"username": "Hulk", "password": 12345})
                self.assertEqual(request.status_code, 201)

                self.assertIsNotNone(UserModel.find_by_username("Hulk"))
                self.assertDictEqual({"message": "User created successfully"},
                                     json.loads(request.data))

    def test_user_duplicate(self):
        with self.app() as client:  # it acts as a user needed for request-response
            with self.app_context():  # needed for database initialisation
                client.post("/register", data={"username": "Hulk", "password": 12345})
                request = client.post("/register", data=json.dump({"username": "Hulk", "password": 12345}))
                self.assertEqual(request.status_code, 400)
                self.assertDictEqual({"message": "A user with that username already exists"},
                                     json.loads(request.data))

    def test_user_login(self):
        with self.app() as client:  # it acts as a user needed for request-response
            with self.app_context():  # needed for database initialisation
                client.post("/register", data={"username": "Hulk", "password": 12345})
                auth_request = client.post("/auth", data=json.dump({"username": "Hulk", "password": 12345}),
                                           headers={"content-type": "application/json"})
                self.assertIn("access_token", json.loads(auth_request.data).keys())
