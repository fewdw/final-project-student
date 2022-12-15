import pymongo as pymongo
from flask import Flask, request, jsonify, abort
import json
import os
from Schema import schemaPost
app = Flask(__name__)


'''

USE 'flask run' IN TERMNIAL TO START THE API

'''

MONGODB_LINK = os.environ.get("MONGODB_LINK")
MONGODB_USER = os.environ.get("MONGODB_USER")
MONGODB_PASS = os.environ.get("MONGODB_PASS")

client = pymongo.MongoClient(f"mongodb://{MONGODB_USER}:{MONGODB_PASS}@{MONGODB_LINK}/?retryWrites=true&w=majority")
db = client.StudentDB

@app.route('/')
def index():
    return 'Hello, this is the main!'


data = open('MOCK_DATA.json')


@app.route('/student', methods=["POST"])
def add_student():
    read = request.json
    error = schemaPost().validate(read)
    if error:
        return error, 400


    #Writting to the database
    addedId = db.results.insert_one(read).inserted_id
    read["_id"] = str(addedId)

    return jsonify(read)

#Get readings from the database
@app.route('/student/<student_id>', methods=["GET"])
def get_by_id(student_id):
    try:
        cursor = db.results.find({"student_id": student_id})
        read = list(cursor)
        for read in read:
            if "_id" in read:
                read["_id"] = str(read["_id"])

                return jsonify(read)
    except Exception as e:
        print(e)
        return {"error": "some error happened"}, 501


#Put method
@app.route('/student/<student_id>', methods=["PUT"])
def update_student(student_id):
    db.update_one({'student_id': object(id)},{'$set':{
        'id': request.json['id'],
        'first_name': request.json['first_name'],
        'last_name': request.json['last_name'],
        'email': request.json['email'],
        'gender': request.json['gender'],
        'professor_name': request.json['professor_name'],
        'project': request.json['project'],
        'programming_language': request.json['programming_language']

    }} )
    return jsonify({'msg':"User updated succesfully"})


if __name__ == "__main__":
    app.run(debug=True)