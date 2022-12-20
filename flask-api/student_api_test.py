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