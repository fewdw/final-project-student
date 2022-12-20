from app import app
import unittest
import json
from flask import Flask, jsonify
import requests

class TestDefaultRoute(unittest.TestCase):

    #app setup test!
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    # return 200 test!
    def test_default_route_200(self):
        response = app.test_client().get('/')
        self.assertEqual(response.status_code, 200)

    # get by id
    def test_students_route_get_by_id(self):
        response = requests.get('http://127.0.0.1:5000/students/63a1453dd4c253b8774b74b4')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['first_name'],'Agnes')

    # get all
    def test_students_route_get_all(self):
        response = requests.get('http://127.0.0.1:5000/students')
        self.assertGreater(len(response.json()),1,"test")

    # post should return 400
    def test_students_route_get_all_should_return_400(self):
        response = requests.post('http://127.0.0.1:5000/students',data={"not":"valid"})
        self.assertEqual(response.status_code, 400)

    # post and delete should work
    def test_students_route_get_all_should_work(self):
        url = "http://127.0.0.1:5000/students"
        payload = {
        "student_id":"student_Id",
        "status":True,
        "first_name":"first_name",
        "last_name":"last_name",
        "email":"email", 
        "gender":"gender",
        "professor_name":"professor_name", 
        "year_of_graduation": "year_of_graduation", 
        "degree":"degree",
        "projectId":"projectId",
        "programming_language":"programming_language"}
        response = requests.post(url, json=payload)
        j = response.json()
        _id_to_delete = j['added']
        self.assertEqual(response.status_code, 200)
        
        self.assertIsNotNone(response.json()['added'])

        url = "http://127.0.0.1:5000/students/"
        payload = {"id":_id_to_delete}
        del_response = requests.delete(url, json=payload)
        self.assertEqual(del_response.json(),{'successfully deleted student with id': _id_to_delete})

    # put test
    def test_put_should_work(self):
        url = "http://127.0.0.1:5000/students/"
        payload = {
            "id": "63a13a5da4acd21e65360820",
            "student_id":"UPDATEDupdated-student_id",
            "status" : "UPDATEDstatus",
            "first_name" : "UPDATEDfirst_name",
            "last_name" : "UPDATEDlast_name",
            "email" : "UPDATEDemail",
            "gender" :  "UPDATEDgender",
            "professor_name" : "UPDATEDprofessor_name",
            "year_of_graduation" : "UPDATEDyear_of_graduation",
            "degree" : "degree",
            "projectId" : "projectId",
            "programming_language" : "UPDATEDprogramming_language"    
        }
        put_response = requests.put(url, json=payload) 
        self.assertEqual(put_response.json()['updated student with id'],"63a13a5da4acd21e65360820")



if __name__ == '__main__':
    unittest.main()
