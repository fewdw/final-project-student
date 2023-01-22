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
credential_collection = database.Credentials

def post_a_new_credential_to_db(email,pw_hash,lang,session_type):
     new_cred={
        "email": email,
        "hash": pw_hash,
        "lang": lang,
        "type": session_type
    }
     _id = credential_collection.insert_one(new_cred).inserted_id
     return jsonify({"added credential with id": str(_id)})