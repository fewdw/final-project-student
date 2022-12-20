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