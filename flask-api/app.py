from flask import Flask, request, jsonify, abort
import pymongo as pymongo
from pymongo import MongoClient
import json
import os
from Schema import schemaPost
from bson import json_util
from bson.objectid import ObjectId
from controllerHelper.studentControllerHelper.get_students import get_all_students_helper_method, get_one_student_helper_method
from controllerHelper.studentControllerHelper.delete_students import delete_one_student_helper_method
from controllerHelper.studentControllerHelper.put_students import put_an_existing_student_helper_method
from controllerHelper.studentControllerHelper.post_students import post_a_new_student_helper_method
app = Flask(__name__)

'''
USE 'flask run' IN TERMNIAL TO START THE API
'''

#get all students
@app.route('/students/', methods=['GET'])
def get_all_students():
    return get_all_students_helper_method()

#get student by id
@app.route('/students/<id>', methods=['GET'])
def get_one_students(id):
    return get_one_student_helper_method(id)

#delete student by id
@app.route('/students/', methods=['DELETE'])
def delete_one_student():
    return delete_one_student_helper_method(request.json["id"])

#post a new student
@app.route('/students/<id>', methods=['POST'])
def post_new_student():
    return post_a_new_student_helper_method(
        request.json["student_id"],
        request.json["status"],
        request.json["first_name"],
        request.json["last_name"],
        request.json["email"],
        request.json["gender"],
        request.json["professor_name"],
        request.json["year_of_graduation"],
        request.json["degree"],
        request.json["projectId"],
        request.json["programming_language"]
    )

#put a new student
@app.route('/students/', methods=['PUT'])
def put_an_existing_student():
    return put_an_existing_student_helper_method(
        request.json["id"],
        request.json["first_name"],
        request.json["last_name"],
        request.json["email"],
        request.json["gender"],
        request.json["professor_name"],
        request.json["project"],
        request.json["programming_language"]
    )



if __name__ == "__main__":
    app.run(debug=True)