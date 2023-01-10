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

# get all
def get_all_students_helper_method():
    all_students = student_collection.find()
    return json.loads(json_util.dumps(all_students))

# get by id
def get_one_student_helper_method(student_id):
    student = student_collection.find_one({"_id":ObjectId(student_id)})
    return json.loads(json_util.dumps(student))
