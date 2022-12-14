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

def put_an_existing_student_helper_method(id,student_id, status, first_name, last_name, email, gender, professor_name, year_of_graduation, degree, projectId, programming_language):
    filter = {"_id":ObjectId(id)}
    updated_student = {
        'student_id':student_id,
        'status':status,
        'first_name':first_name,
        'last_name':last_name,
        'email':email,
        'gender':gender,
        'professor_name':professor_name,
        'year_of_graduation':year_of_graduation,
        'degree':degree,
        'projectId':projectId,
        'programming_language':programming_language
    }
    if student_collection.replace_one(filter,updated_student):
        return "Updated successfully"
    else:
        return {"error": "resource not found"}, 404
