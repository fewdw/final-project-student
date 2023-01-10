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
project_collection = database.ProjectCollection

def put_an_existing_project_helper_method(id, project_id, project_name, project_description):
    filter = {"_id":ObjectId(id)}
    updated_student = {
        "project_id":project_id,
        "project_name":project_name,
        "project_description":project_description,
    }