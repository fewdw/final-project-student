import unittest
from flask import Flask
from flask.testing import FlaskClient

def test_post_method(app: Flask, client: FlaskClient):
    data = {

    "student_id": "1111",
    "status": True,
    "first_name": "test",
    "last_name": "test",
    "email": "test@example.com",
    "gender": "male",
    "professor_name": "test",
    "year_of_graduation": "2022",
    "degree": "test",
    "projectId": 1,
    "programming_language": ["test"]
 

    }

    response = client.post('/admin/list', json=data)
    assert response.status_code == 201
    assert response.get_json()=={'success': True}


if __name__ == '__main__':
    unittest.main()