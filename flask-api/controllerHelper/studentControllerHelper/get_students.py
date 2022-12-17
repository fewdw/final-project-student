from flask import Flask, request, jsonify, abort
import pymongo as pymongo
from pymongo import MongoClient
import json
import os
from Schema import schemaPost
from bson import json_util

MONGODB_PASS = os.environ.get("MONGODB_PASS")
connection_string = f"mongodb+srv://fewdw:{MONGODB_PASS}@student.kslusvd.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection_string)
database = client.StudentDB
student_collection = database.StudentCollection

def get_all_students_helper_method():
    all_students = student_collection.find()
    return json.loads(json_util.dumps(all_students))