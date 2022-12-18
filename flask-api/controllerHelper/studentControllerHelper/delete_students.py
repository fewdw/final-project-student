from flask import Flask, request, jsonify, abort
import pymongo as pymongo
from pymongo import MongoClient
import json
import os
from bson import json_util
from bson.objectid import ObjectId

MONGODB_PASS = os.environ.get("MONGODB_PASS")
connection_string = f"mongodb+srv://fewdw:{MONGODB_PASS}@student.kslusvd.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection_string)
database = client.StudentDB
student_collection = database.StudentCollection

# delete by id
def delete_one_student_helper_method(student_id):
    student = student_collection.delete_one({"_id":ObjectId(student_id)})
    return jsonify({"successfully deleted student with id":student_id})