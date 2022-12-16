import pymongo as pymongo
from flask import Flask, request, jsonify, abort
import json
import os
from Schema import schemaPost
import requests
import pymongo as pymongo
from bson import ObjectId
from flask import Flask, request, jsonify
# from flask_objectid_converter import ObjectIDConverter
from pymongo import ReturnDocument
from pymongo.server_api import ServerApi

import os




'''

USE 'flask run' IN TERMNIAL TO START THE API

'''

MONGODB_USER = os.environ.get("fewdw")
MONGODB_PASS = os.environ.get("fewdw")

client = pymongo.MongoClient("mongodb+srv://fewdw:fewdw@student.kslusvd.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))
db = client.StudentDB
app = Flask(__name__)

db = client['StudentDB']
collection = db['StudentCollection']


@app.route('/')
def index():
    return 'Hello, this is the main!'


data = open('MOCK_DATA.json')

@app.route('/students', methods=["POST"])
def students():   

    document = {
        "id":1,
        "first_name": "Francis",
        "last_name":"Shehata",
        "email":"francis_2002@icloud.com",
        "gender":"male",
        "professor_name":"Christine Gerard",
        "project": "ISRS",
        "programming_language":"python,react"
  

 }
    
    collection.insert_one(document)



if __name__ == "__main__":
    app.run(debug=True)