from flask import Flask, request, jsonify, abort
import pymongo as pymongo
from pymongo import MongoClient
import json
import os
from Schema import schemaPost
from bson import json_util
from bson.objectid import ObjectId
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


#get student by id
@app.route('/students/<id>', methods=['GET'])
def get_all_students(id):
    return get_one_student_helper_method(id)

#delete student by id
@app.route('/students/', methods=['DELETE'])
def delete_one_student():
    return delete_one_student_helper_method(request.json["id"])

#post a new student
#@app.route('/students/', methods=['POST'])


#put a new student




if __name__ == "__main__":
    app.run(debug=True)