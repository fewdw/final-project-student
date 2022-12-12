import os
import pymongo as pymongo
from flask import Flask, request, jsonify
from pymongo.server_api import ServerApi
from flask import Flask, request, jsonify, abort
import json
import os
from Schema import schemaPost
app = Flask(__name__)


MONGODB_LINK = os.environ.get("MONGODB_LINK")
MONGODB_USER = os.environ.get("MONGODB_USER")
MONGODB_PASS = os.environ.get("MONGODB_PASS")


client = pymongo.MongoClient(f"mongodb+srv://{MONGODB_USER}:{MONGODB_PASS}@{MONGODB_LINK}/?retryWrites=true&w=majority")
db = client.test



@app.route('/')
def index():
    return "hello world"




data = open('MOCK_DATA.json')

def add_user_to_file(user):
    data.append(user)
    dump_data()


def update_user_to_file(user, idx):
    data[idx] = user
    dump_data()


def dump_data():
    with open('MOCK_DATA.json', 'w') as outfile:
        json.dump(data, outfile)



@app.route('/users/<email>')
def get_users_by_email(email):
    for user in data:
        if user['email'] == email:
            return jsonify(user)
    return {'message': f'{email} not found'}, 404


def sort_users(users, key):
    filtered = sorted(users, key=lambda x: x[key])
    return filtered


@app.route('/users/')
def get_users():
    gender = request.args.get('gender')
    sort = request.args.get('sort')
    if sort not in ['id', 'first_name', 'last_name']:
        sort = None

    if gender is None and sort is None:
        return jsonify(data)
    elif gender is None:
        return jsonify(sort_users(data, sort))

    users = [user for user in data if user['gender'].lower() == gender.lower()]

    if len(users) == 0:
        return jsonify({'message': f'no users found for gender {gender}'}), 404
    if sort is None:
        return jsonify(users)
    else:
        return jsonify(sort_users(users, sort))


@app.route('/users/', methods=['POST'])
def add_user():
    if request.json is None:
        abort(404)

    first_name = request.json.get('first_name')
    last_name = request.json.get('last_name')
    email = request.json.get('email')
    gender = request.json.get('gender')
    department = request.json.get('department')
    title = request.json.get('title')
    university = request.json.get('university')

    for key in [first_name, last_name, gender, department, title, email, university]:
        if key is None:
            abort(404)

    email_found = [user for user in data if user['email'] == email]
    if len(email_found) != 0:
        return {'message': 'email already exist'}, 409

    maxId = max(data, key=lambda x: x['id'])['id']
    user = {"id": maxId + 1, "first_name": first_name, "last_name": last_name,
            "email": email, "gender": gender, "department": department, "title": title, "university": university}
    add_user_to_file(user)
    return jsonify(user)


@app.route('/users/<email>', methods=['PUT'])
def update_user(email):
    if request.json is None:
        abort(404)
    filtered_users = [(data[i], i) for i in range(len(data)) if data[i]['email'] == email]
    if len(filtered_users) == 0:
        return {'message': 'email not found'}, 404

    user, idx = filtered_users[0]

    first_name = request.json.get('first_name', user['first_name'])
    last_name = request.json.get('last_name', user['last_name'])
    gender = request.json.get('gender', user['gender'])
    department = request.json.get('department', user['department'])
    title = request.json.get('title', user['title'])
    university = request.json.get('university', user['university'])

    user['first_name'] = first_name
    user['last_name'] = last_name
    user['gender'] = gender
    user['department'] = department
    user['title'] = title
    user['university'] = university

    dump_data()
    return jsonify(user)




@app.route('/student', methods=["POST"])
def add_student():
    read = request.json



    #Writting to the database
    addedId = db.results.insert_one(read).inserted_id
    read["_id"] = str(addedId)

    return jsonify(read)



if __name__ == '__main__':
    app.run(debug=True)

#activate venv
#mac: source venv/bin/activate
#windows: .\venv\Scripts\activate

# run
# python3 server.py
# or python server.py
