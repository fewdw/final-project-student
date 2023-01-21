import requests

BASE_URL = "http://127.0.0.1:5001/credentials"

def get_credentials_from_api():
    response = requests.get(BASE_URL)
    return response.json()

def post_credentials_from_api(email, pw_hash, lang, session_type):
    payload = {
        "email": email,
        "hash": pw_hash,
        "lang": lang,
        "type": session_type
    }
    response = requests.post(BASE_URL, json=payload)
    return response.json()

def put_credentials_from_api(_id, email, pw_hash, lang, session_type):
    payload = {
        "id": _id,
        "email": email,
        "hash": pw_hash,
        "lang": lang,
        "type": session_type
    }
    response = requests.put(f"{BASE_URL}/{id}", json=payload)
    return response.json()

def delete_credentials_from_api(id):
    response = requests.delete(f"{BASE_URL}/{id}")
    return response.json()

def get_credentials_by_id_from_api(id):
    response = requests.get(f"{BASE_URL}/{id}")
    return response.json()
