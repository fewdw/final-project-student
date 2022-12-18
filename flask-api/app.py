from flask import Flask, request, jsonify, abort
import pymongo as pymongo
from pymongo import MongoClient
import json
import os
from Schema import schemaPost
app = Flask(__name__)

from controllerHelper.studentControllerHelper.get_students import get_all_students_helper_method, get_one_student_helper_method
from controllerHelper.studentControllerHelper.delete_students import delete_one_student_helper_method
from controllerHelper.studentControllerHelper.put_students import put_an_existing_student_helper_method
from controllerHelper.studentControllerHelper.post_students import post_a_new_student_helper_method


'''
USE 'flask run' IN TERMNIAL TO START THE API
'''

#get all students
@app.route('/students/', methods=['GET'])
def get_all_students():
    return get_all_students_helper_method()

client = pymongo.MongoClient(f"mongodb://{MONGODB_USER}:{MONGODB_PASS}@{MONGODB_LINK}/?retryWrites=true&w=majority")
db = client.StudentDB

#delete student by id
@app.route('/students/', methods=['DELETE'])
def delete_one_student():
    return delete_one_student_helper_method(request.json["id"])

#put student by id 
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
        request.json["programming_language"],
        request.json["degree"],
        request.json["projectId"],
        request.json["year_of_graduation"]
    )



data = open('MOCK_DATA.json')






if __name__ == "__main__":
    app.run(debug=True)