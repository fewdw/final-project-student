from flask import Flask, request, jsonify, abort
import pymongo as pymongo
from pymongo import MongoClient
import json
import os
from Schema import schemaPost
from bson import json_util

# import for other files


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
    pass


# get a specific student by id
@app.route('/students/id/<id>', methods=['GET'])
def get_student_by_id(id):
    pass


# delete a specific student
@app.route('/students', methods=['DELETE'])
def delete_specific_student():
    pass

# post new student data
@app.route('/students', methods=['POST'])
def post_a_new_student():
    pass


# put/modify data for an existing student using a specific id
@app.route('/students', methods=['PUT'])
def put_an_existing_student():
    pass


if __name__ == "__main__":
    app.run(debug=True)