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
db = client.test

@app.route('/')
def index():
    return 'Hello, Flask!'


data = open('MOCK_DATA.json')

# GET


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


if __name__ == "__main__":
    app.run(debug=True)