from Testcases.system.base_test import BaseTest
from APIs.experian_poc import experian_poc  # experian_poc is a flask app
#  when we are importing it, server will run in the background but that should not happen
#  but having __name__ == __main__ is helping it not to run
import json


class TestExperianHome(BaseTest):
    def test_home(self):
        # flask gives a test client that allow us to make requests
        # without running the complete app in background
        with experian_poc.test_client() as home:
            # with self.experian_poc() as home:
            resp = home.get('/home')  # context manager

            self.assertEqual(resp.status_code, 200)
            # resp.get_data() will return a string - json.loads to make it a valid json)
            self.assertEqual(json.loads(resp.get_data()), ({"Message": "Welcome to the Experian world"}))
