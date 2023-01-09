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

# delete by id
def delete_one_degree_helper_method(degree_id):
    degree = degree_collection.delete_one({"_id":ObjectId(degree_id)})
    return jsonify({"msg":"degree successfully deleted"})