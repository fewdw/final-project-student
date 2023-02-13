from flask import Flask, request, jsonify, abort
import pymongo as pymongo
from pymongo import MongoClient
import json
import os
from bson import json_util
from bson.objectid import ObjectId
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

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
from controllerHelper.projectControllerHelper.update_project import put_an_existing_project_helper_method
from controllerHelper.projectControllerHelper.get_project import get_project_by_id, get_all_projects_helper_method
from controllerHelper.projectControllerHelper.post_project import post_new_project_helper_method
#credentials
from controllerHelper.credentialsControllerHelper.delete_credentials import delete_one_credential_to_db
from controllerHelper.credentialsControllerHelper.put_credentials import update_an_existing_credential_to_db
from controllerHelper.credentialsControllerHelper.get_credentials import get_all_credentials_from_db, get_credential_by_id
from controllerHelper.credentialsControllerHelper.post_credentials import post_a_new_credential_to_db



'''
USE 'flask run' IN TERMNIAL TO START THE API
'''

@auth.verify_password
def verify_password(username, password):
    return username == os.environ.get("api_user") and password == os.environ.get("api_pass")

@app.route('/')
@auth.login_required
def default_route():
    return {"json":"type"}

#get all students
@app.route('/students/', methods=['GET'])
@auth.login_required
def get_all_students():
    return jsonify(get_all_students_helper_method())

#get all degrees
@app.route('/degrees/', methods=['GET'])
@auth.login_required
def get_all_degrees():
    return jsonify(get_all_degrees_helper_method())



#get student by id
@app.route('/students/<id>', methods=['GET'])
@auth.login_required
def get_one_students(id):
    return get_one_student_helper_method(id)


#get project by id
@app.route('/project/<id>', methods=['GET'])
@auth.login_required
def get_one_project(id):
    return get_project_by_id(id)

#get all projects
@app.route('/project/', methods=['GET'])
@auth.login_required
def get_all_project():
    return jsonify(get_all_projects_helper_method())


# get degree by id
@app.route('/degrees/<id>', methods=['GET'])
@auth.login_required
def get_one_degree(id):
    return jsonify(get_degree_by_id(id))


#delete student by id
@app.route('/students/', methods=['DELETE'])
@auth.login_required
def delete_one_student():
    return delete_one_student_helper_method(request.json["id"])

#delete degree by id
@app.route('/degrees/', methods=['DELETE'])
@auth.login_required
def delete_one_degree():
    return delete_one_degree_helper_method(request.json["id"])


#delete project by id
@app.route('/projects/', methods=['DELETE'])
@auth.login_required
def delete_one_project():
    return delete_one_project_helper_method(request.json["id"])

#post a new student
@app.route('/students/', methods=['POST'])
@auth.login_required
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
        request.json["programming_language"],
        request.json["resume"]
    )

# post a new degree
@app.route('/degrees/', methods=['POST'])
@auth.login_required
def post_new_degree():
    return post_new_degree_helper_method(
        request.json["degree_id"],
        request.json["name_degree"],
        request.json["description"],

    )

#post a new project
@app.route('/projects/', methods=['POST'])
@auth.login_required
def post_new_project():
    return post_new_project_helper_method(
        request.json["project_id"],
        request.json["project_name"],
        request.json["project_description"],

    ) 


@app.route('/students/', methods=['PUT'])
@auth.login_required
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
@auth.login_required
def put_a_degree():
    return put_an_existing_degree_helper_method(
        request.json['id'],
        request.json['degree_id'],
        request.json['name_degree'],
        request.json['description']
    )

@app.route('/projects/', methods=['PUT'])
@auth.login_required
def put_a_project():
    return put_an_existing_project_helper_method(
        request.json['id'],
        request.json['project_id'],
        request.json['project_name'],
        request.json['project_description'],
    )


@app.route("/credentials", methods=['GET', 'POST', 'DELETE', 'PUT'])
@auth.login_required
def credentials_url():
    if request.method == 'GET':
        return jsonify(get_all_credentials_from_db())

    if request.method == 'POST':
        return post_a_new_credential_to_db(
            request.json['email'],
            request.json['hash'],
            request.json['lang'],
            request.json['type']
        )

    if request.method == 'DELETE':
        return delete_one_credential_to_db(request.json['id'])

    if request.method == 'PUT':
        return update_an_existing_credential_to_db(
            request.json['id'],
            request.json['email'],
            request.json['hash'],
            request.json['lang'],
            request.json['type']
        ) 

@app.route("/credentials/<cred_id>", methods=["GET"])
@auth.login_required
def credential_by_id_route(cred_id):
    return get_credential_by_id(cred_id)

if __name__ == "__main__":
    app.run(debug=True)
    