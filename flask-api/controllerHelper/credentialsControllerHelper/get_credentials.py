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
credential_collection = database.Credentials

def get_all_credentials_from_db():
    all_credentials = credential_collection.find()
    return json.loads(json_util.dumps(all_credentials))

def get_credential_by_id(_id):
    credential = credential_collection.find_one({"_id":ObjectId(_id)})
    return json.loads(json_util.dumps(credential))
