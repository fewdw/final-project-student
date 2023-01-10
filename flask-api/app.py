from flask import Flask, request, jsonify, abort
import pymongo as pymongo
from pymongo import MongoClient
import json
import os
from bson import json_util
from bson.objectid import ObjectId

app = Flask(__name__)
#Student
from controllerHelper.studentControllerHelper.get_students import get_all_students_helper_method, get_one_student_helper_method
from controllerHelper.studentControllerHelper.delete_students import delete_one_student_helper_method
from controllerHelper.studentControllerHelper.put_students import put_an_existing_student_helper_method
from controllerHelper.studentControllerHelper.post_students import post_a_new_student_helper_method
#Degrees
from controllerHelper.degreeControllerHelper.get_degrees import get_all_degrees_helper_method
from controllerHelper.degreeControllerHelper.get_degrees import get_degree_by_id
from controllerHelper.degreeControllerHelper.delete_degrees import delete_one_degree_helper_method
from controllerHelper.degreeControllerHelper.update_degrees import put_an_existing_degree_helper_method
from controllerHelper.degreeControllerHelper.post_degrees import post_new_degree_helper_method 
#projects
from controllerHelper.projectControllerHelper.delete_project import delete_one_project_helper_method
from controllerHelper.projectControllerHelper.get_project import get_project_by_id, get_all_projects_helper_method
from controllerHelper.projectControllerHelper.update_project import put_an_existing_project_helper_method




'''
USE 'flask run' IN TERMNIAL TO START THE API
'''

@app.route('/')
def default_route():
    return {"json":"type"}

#get all students
@app.route('/students/', methods=['GET'])
def get_all_students():
    return jsonify(get_all_students_helper_method())

#get all degrees
@app.route('/degrees/', methods=['GET'])
def get_all_degrees():
    return jsonify(get_all_degrees_helper_method())



#get student by id
@app.route('/students/<id>', methods=['GET'])
def get_one_students(id):
    return get_one_student_helper_method(id)


#get project by id
@app.route('/project/<id>', methods=['GET'])
def get_one_project(id):
    return get_project_by_id(id)

#get all projects
@app.route('/project/', methods=['GET'])
def get_all_project():
    return jsonify(get_all_projects_helper_method())


# get degree by id
@app.route('/degrees/<id>', methods=['GET'])
def get_one_degree(id):
    return jsonify(get_degree_by_id(id))


#delete student by id
@app.route('/students/', methods=['DELETE'])
def delete_one_student():
    return delete_one_student_helper_method(request.json["id"])

#delete degree by id
@app.route('/degrees/', methods=['DELETE'])
def delete_one_degree():
    return delete_one_degree_helper_method(request.json["id"])


#delete project by id
@app.route('/projects/', methods=['DELETE'])
def delete_one_project():
    return delete_one_project_helper_method(request.json["id"])

#post a new student
@app.route('/students/', methods=['POST'])
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

# post a new degree
@app.route('/degrees/', methods=['POST'])
def post_new_degree():
    return post_new_degree_helper_method(
        request.json["degree_id"],
        request.json["name_degree"],
        request.json["description"],

    )


@app.route('/students/', methods=['PUT'])
def put_a_student_to_mongodb():
        return put_an_existing_student_helper_method(
            request.json['id'],
            request.json['student_id'],
            request.json['status'],
            request.json['first_name'],
            request.json['last_name'],
            request.json['email'],
            request.json['gender'],
            request.json['professor_name'],
            request.json['year_of_graduation'],
            request.json['degree'],
            request.json['projectId'],
            request.json['programming_language']
        )

@app.route('/degrees/', methods=['PUT'])
def put_a_degree():
    return put_an_existing_degree_helper_method(
        request.json['id'],
        request.json['degree_id'],
        request.json['name_degree'],
        request.json['description']
    )
@app.route('/projects/', methods=['PUT'])
def put_a_project():
    return put_an_existing_project_helper_method(
        request.json['id'],
        request.json['project_id'],
        request.json['project_name'],
        request.json['project_description'],
    )

if __name__ == "__main__":
    app.run(debug=True)