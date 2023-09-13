from unittest import TestCase
from APIs.experian_poc import experian_poc


# superclass
class BaseTest(TestCase):
    def SetUP(self):
        experian_poc.testing = True
        self.experian_poc = experian_poc.test_client
