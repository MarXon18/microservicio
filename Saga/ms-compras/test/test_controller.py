import unittest
from flask import current_app
import requests
from app import create_app

class ControllerTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_app(self):
        self.assertIsNotNone(current_app)
    
    def test_index(self):
        r = requests.get('http://localhost:5002/api/v1/')
        self.assertEqual(r.status_code, 200)
        self.assertEqual('2', r.json()['microservicio'])
        self.assertEqual('ok', r.json()['status'])

if __name__ == '__main__':
    unittest.main()