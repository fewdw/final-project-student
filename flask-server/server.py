import os
import pymongo as pymongo
from flask import Flask, request, jsonify
from pymongo.server_api import ServerApi

import os

app = Flask(__name__)


MONGODB_LINK = os.environ.get("MONGODB_LINK")
MONGODB_USER = os.environ.get("MONGODB_USER")
MONGODB_PASS = os.environ.get("MONGODB_PASS")


client = pymongo.MongoClient(f"mongodb+srv://{MONGODB_USER}:{MONGODB_PASS}@{MONGODB_LINK}/?retryWrites=true&w=majority")
db = client.test



@app.route('/')
def index():
    return "hello world"


if __name__ == '__main__':
    app.run(debug=True)

#activate venv
#mac: source venv/bin/activate
#windows: .\venv\Scripts\activate

# run
# python3 server.py
# or python server.py
