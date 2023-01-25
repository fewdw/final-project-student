import requests
import requests, json

BASE_URL = "http://127.0.0.1:5001/credentials"

def get_credentials_from_api():
    response = requests.get(BASE_URL)
    creds = json.loads(response.text)
    return creds

def post_credentials_from_api(email, pw_hash, lang, session_type):
    payload = {
        "email": email,
        "hash": pw_hash,
        "lang": lang,
        "type": session_type
    }
    response = requests.post(BASE_URL, json=payload)

def put_credentials_from_api(_id, email, pw_hash, lang, session_type):
    payload = {
        "id": _id,
        "email": email,
        "hash": pw_hash,
        "lang": lang,
        "type": session_type
    }
    response = requests.put(BASE_URL, json=payload)

def delete_credentials_from_api(_id):
    payload = {"id":_id}
    requests.delete(BASE_URL, json=payload)

def get_credentials_by_id_from_api(id):
    response = requests.get(f"{BASE_URL}/{id}")
    creds = json.loads(response.text)
    return creds
