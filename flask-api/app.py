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
def postStudents():   

    id= request.json["id"]
    first_name = request.json["first_name"]
    last_name = request.json["last_name"]
    email = request.json["email"]
    gender = request.json["gender"]
    professor_name = request.json["professor_name"]
    project = request.json["project"]
    programming_language = request.json["programming_language"]
    
    document = {
        "id":id,
        "first_name": first_name,
        "last_name":last_name,
        "email":email,
        "gender":gender,
        "professor_name":professor_name,
        "project": project,
        "programming_language":"python,react"
  

 }
    
    collection.insert_one(document)
    return jsonify(document)



if __name__ == "__main__":
    app.run(debug=True)