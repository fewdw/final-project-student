from flask import Flask, request, jsonify, abort
import pymongo as pymongo
from pymongo import MongoClient
import json
import os
from bson import json_util
from bson.objectid import ObjectId
import certifi
ca = certifi.where()

MONGODB_PASS = os.environ.get("MONGODB_PASS")
connection_string = f"mongodb+srv://fewdw:{MONGODB_PASS}@student.kslusvd.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection_string, tlsCAFile=ca)
database = client.StudentDB
student_collection = database.StudentCollection

def post_a_new_student_helper_method(student_Id, status, first_name, last_name, email, gender, professor_name, year_of_graduation, degree, projectId, programming_language,resume):
    new_student = {
        "student_id": student_Id,
        "status": status,
        "first_name":first_name,
        "last_name":last_name,
        "email":email,
        "gender":gender,
        "professor_name":professor_name,
        "year_of_graduation": year_of_graduation,
        "degree":degree,
        "projectId":projectId,
        "programming_language":programming_language,
        "resume":resume
    }
    _id = student_collection.insert_one(new_student).inserted_id
    return jsonify({"added":str(_id)})