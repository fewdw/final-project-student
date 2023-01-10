from flask import Flask, request, jsonify, abort
import pymongo as pymongo
from pymongo import MongoClient
import json
import os
from bson import json_util
from bson.objectid import ObjectId
import certifi
ca = certifi.where()



#Connection string 
MONGODB_PASS = os.environ.get("MONGODB_PASS")
connection_string = f"mongodb+srv://fewdw:{MONGODB_PASS}@student.kslusvd.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection_string, tlsCAFile=ca)
database = client.StudentDB
project_collection = database.ProjectCollection

# get all 
def get_all_projects_helper_method():
    all_projects = project_collection.find()
    return json.loads(json_util.dumps(all_projects))

def get_project_by_id(project_id):
    degree = project_collection.find_one({"_id":ObjectId(degree_id)})
    return json.loads(json_util.dumps(degree))