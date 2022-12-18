from flask import Flask, request, jsonify, abort
import pymongo as pymongo
from pymongo import MongoClient
import json
import os
from Schema import schemaPost
from bson import json_util
from bson.objectid import ObjectId

MONGODB_PASS = os.environ.get("MONGODB_PASS")
connection_string = f"mongodb+srv://fewdw:{MONGODB_PASS}@student.kslusvd.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection_string)
database = client.StudentDB
student_collection = database.studentCollection

def put_an_existing_student_helper_method(id,first_name, last_name, email, gender, professor_name, project, programming_language,year_of_graduation,projectId):
 replace_student = {
    "first_name": first_name,
    "last_name":last_name,
    "email":email,
    "gender": gender,
    "professor_name": professor_name,
    "project": project,
    "programming_language":programming_language,
    "year_of_graduation": year_of_graduation,
    "projectId": projectId
 }

 _id = student_collection.replace_one({"_id":ObjectId(id)},replace_student)

 return {"student is successfully updated": str(_id)}