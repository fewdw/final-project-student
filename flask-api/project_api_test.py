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

    #get all students
    def test_students_api(self):
        response = requests.get('http://127.0.0.1:5001/project')
        self.assertEqual(response.status_code, 200)
    
    #check if nu
    def test_students_api_5_objects(self):
        response = requests.get('http://127.0.0.1:5001/project/')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertGreater(len(data), 5)

    #post student project, should return 200
    def test_post_project_api(self):
        url = "http://127.0.0.1:5001/projects/"
        payload = {
            "project_id": "1",
            "project_name": "test_project_name",
            "project_description": "test_project_description"
        }
        headers = {'content-type': 'application/json'}
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        _id = response.json()['added']
        self.assertEqual(response.status_code, 200)

        url = "http://127.0.0.1:5001/projects/"
        payload = {
            "id": _id,
            "project_id": "1",
            "project_name": "test_project_name",
            "project_description": "test_project_description"
        }
        headers = {'content-type': 'application/json'}
        response = requests.put(url, data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(str(response.content),"b'Updated successfully'")

        url = "http://127.0.0.1:5001/projects/"
        payload = {
            "id": _id
        }
        headers = {'content-type': 'application/json'}
        response = requests.delete(url, json=payload, headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["msg"], "project successfully deleted")


if __name__ == '__main__':
    unittest.main()