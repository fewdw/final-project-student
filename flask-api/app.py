from flask import Flask, request, jsonify, abort
import pymongo as pymongo
from pymongo import MongoClient
import json
import os
from Schema import schemaPost
from bson import json_util
from bson.objectid import ObjectId

# import from other files
from controllerHelper.studentControllerHelper.get_students import get_all_students_helper_method, get_one_student_helper_method
from controllerHelper.studentControllerHelper.delete_students import delete_one_student_helper_method
from controllerHelper.studentControllerHelper.post_students import post_a_new_student

app = Flask(__name__)

'''
USE 'flask run' IN TERMNIAL TO START THE API
'''

MONGODB_PASS = os.environ.get("MONGODB_PASS")
connection_string = f"mongodb+srv://fewdw:{MONGODB_PASS}@student.kslusvd.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection_string)
database = client.StudentDB
student_collection = database.StudentCollection


# get list of all students
@app.route('/students/', methods=['GET'])
def get_all_students():
    return get_all_students_helper_method()


# get a specific student by id
@app.route('/students/id/<id>', methods=['GET'])
def get_student_by_id(id):
    return get_one_student_helper_method(id)


# delete a specific student
@app.route('/students', methods=['DELETE'])
def delete_specific_student():
    _id = request.json['id']
    return delete_one_student_helper_method(_id)

# post new student data
@app.route('/students', methods=['POST'])
def post_a_new_student():
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    email = request.json['email']
    gender = request.json['gender']
    professor_name = request.json['professor_name']
    project = request.json['project']
    programming_language = request.json['programming_language']


# put/modify data for an existing student using a specific id
@app.route('/students', methods=['PUT'])
def put_an_existing_student():
    pass


if __name__ == "__main__":
    app.run(debug=True)