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


def archive_student():
    student_id = request.form["student_id"]
    student_collection.update_one({"_id": student_id}, {"$set": {"archived": True}})
    return "Student archived successfully"