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
degree_collection = database.DegreeCollection

def put_an_existing_degree_helper_method(id, degree_id, name_degree, description):
    filter = {"_id":ObjectId(id)}
    updated_student = {
        "degree_Id":degree_id,
        "name_degree":name_degree,
        "description":description
    }
    if degree_collection.replace_one(filter,updated_student):
        return "Updated successfully"
    else:
        return {"error": "resource not found"}, 404