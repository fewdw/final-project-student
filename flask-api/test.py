from app import app
import unittest
import json

class TestDefaultRoute(unittest.TestCase):
    def test_default_route_status_code(self):
        # Send a request to the '/' route and store the response
        response = app.test_client().get('/')

        # Assert that the status code of the response is 200
        self.assertEqual(response.status_code, 200)


class TestStudentsRoute(unittest.TestCase):
    def test_students_route_returns_json(self):
        # Send a request to the '/students/' route and store the response
        response = app.test_client().get('/students/')

        # Assert that the response content type is 'application/json'
        self.assertEqual(response.headers['Content-Type'], 'application/json')

        # Try to parse the response body as JSON
        try:
            json.loads(response.data)
        except ValueError:
            self.fail('Response is not valid JSON')

if __name__ == '__main__':
    unittest.main()

if __name__ == '__main__':
    unittest.main()
