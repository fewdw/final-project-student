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

    #add student 
    def add_student_to_list(student_Id,status,first_name,last_name,email,gender, professor_name, year_of_graduation, degree, projectId, programming_language):
        url = "http://127.0.0.1:5001/admin/list"
        payload = {"studentId":student_Id,"status":status,"firstName":first_name, "last_name":last_name,
