from app import app
import unittest
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
          # get all
    def test_students_route_get_all(self):
        response = requests.get('http://127.0.0.1:5000/students')
        self.assertGreater(len(response.json()),1,"test")