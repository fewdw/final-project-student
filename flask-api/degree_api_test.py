from app import app
import unittest
import json
from flask import Flask, jsonify
import requests

class TestDefaultRoute(unittest.TestCase):

    #app setup test!
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    # return 200 test!
    def test_default_route_200(self):
        response = app.test_client().get('/')
        self.assertEqual(response.status_code, 200)

    def test_degrees_api(self):
        response = requests.get('http://127.0.0.1:5001/degrees/')
        self.assertEqual(response.status_code, 200)
    
    def test_degrees_api_5_objects(self):
        response = requests.get('http://127.0.0.1:5001/degrees/')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertGreater(len(data), 5)

    def test_post_degrees_api(self):
        url = "http://127.0.0.1:5001/degrees/"
        payload = {
            "degree_id": "1",
            "description": "building engineering, building, engineering, engineer, certificate Graduate Certificate Certificate engineering & computer science graduate course-based sgw Graduate",
            "name_degree": "Building Engineering (Grad. Cert.)"
        }
        headers = {'content-type': 'application/json'}
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        _id = response.json()['added']
        self.assertEqual(response.status_code, 200)

        url = "http://127.0.0.1:5001/degrees/"
        payload = {
            "id": _id,
            "degree_id": "1",
            "name_degree": "test_project_name",
            "description": "test_project_description"
        }
        headers = {'content-type': 'application/json'}
        response = requests.put(url, data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(str(response.content),"b'Updated successfully'")

        url = "http://127.0.0.1:5001/degrees/"
        payload = {
            "id": _id
        }
        headers = {'content-type': 'application/json'}
        response = requests.delete(url, json=payload, headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["msg"], "degree successfully deleted")


if __name__ == '__main__':
    unittest.main()