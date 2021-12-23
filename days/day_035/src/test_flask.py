
import unittest
from flask_run import web_app

class Test(unittest.TestCase):

    def test_get(self):
        client = web_app.test_client()
        response = client.get("/")
        self.assertEqual(200, response.status_code)

