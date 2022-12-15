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
student_collection = db.StudentCollection

@app.route('/')
def index():
    return 'Hello, this is the main!'

#Put method
@app.route('/students/', methods=["PUT"])
def update_student():
    
    _id = ObjectId(request.json['id'])
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    email = request.json['email']
    gender = request.json['gender']
    professor_name = request.json['professor_name']
    project = request.json['project']
    programming_language = request.json['programming_language']

    new_student ={
        'id': 7,
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'gender': gender,
        'professor_name': professor_name,
        'project': project,
        'programming_language': programming_language
        
    }
    student_collection.replace_one({"_id": _id}, new_student)

    return {str(_id): "was updated"}
    


if __name__ == "__main__":
    app.run(debug=True)