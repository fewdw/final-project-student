import pymongo as pymongo
from flask import Flask, request, jsonify, abort
import json
import os
from Schema import schemaPost
from bson.objectid import ObjectId
app = Flask(__name__)


'''

USE 'flask run' IN TERMNIAL TO START THE API

'''

MONGODB_LINK = os.environ.get("MONGODB_LINK")
MONGODB_USER = os.environ.get("MONGODB_USER")
MONGODB_PASS = os.environ.get("MONGODB_PASS")

client = pymongo.MongoClient(f"mongodb://{MONGODB_USER}:{MONGODB_PASS}@{MONGODB_LINK}/?retryWrites=true&w=majority")
db = client.StudentDB

@app.route('/')
def index():
    return 'Hello, this is the main!'





#Put method
@app.route('/students/', methods=["PUT"])
def update_student(_id):
    
        _id = ObjectId(request.json['id'])
        
        '_id': ObjectId(request.json['id']),
        'first_name': request.json['first_name'],
        'last_name': request.json['last_name'],
        'email': request.json['email'],
        'gender': request.json['gender'],
        'professor_name': request.json['professor_name'],
        'project': request.json['project'],
        'programming_language': request.json['programming_language'],

    }} )
    return jsonify({'msg':"User updated succesfully"})
    


if __name__ == "__main__":
    app.run(debug=True)