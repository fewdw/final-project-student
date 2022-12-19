import requests, json
from bson.objectid import ObjectId

# get all students
def get_all_students_from_api():
    all_students_api_link = "http://127.0.0.1:5001/students/"
    response = requests.get(all_students_api_link)
    students = json.loads(response.text)
    return students

# get one student
def get_one_student_from_api(id):
    _id = id[10:34]
    all_students_api_link = f"http://127.0.0.1:5001/students/{_id}"
    response = requests.get(all_students_api_link)
    student = json.loads(response.text)
    return student

# delete one student
def delete_student_from_api(id):
    _id = id[10:34]
    url = "http://127.0.0.1:5001/students/"
    payload = {"id":_id}
    requests.delete(url, json=payload)
