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

#new project
def post_new_project_helper_method(project_Id, project_name, project_description):
     new_project={

        "project_id": project_Id,
        "project_name": project_name,
        "project_description": project_description
    }

     _id = project_collection.insert_one(new_project).inserted_id
     return jsonify({"added":str(_id)})