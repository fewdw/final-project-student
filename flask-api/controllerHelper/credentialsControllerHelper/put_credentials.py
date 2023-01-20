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

def update_an_existing_credential_to_db(id, email, pw_hash, lang, session_type):
    filter = {"_id":ObjectId(id)}
    new_cred={
        "email": email,
        "hash": pw_hash,
        "lang": lang,
        "type": session_type
    }
    if credential_collection.replace_one(filter,new_cred):
        return "Updated successfully"
    else:
        return {"error": "resource not found"}, 404