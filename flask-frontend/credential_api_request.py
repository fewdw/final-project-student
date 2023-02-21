import requests
import requests, json
import os

auth = requests.auth.HTTPBasicAuth(os.environ.get("api_user"), os.environ.get("api_pass"))
URL= os.environ.get("url")
BASE_URL = f"{URL}/credentials"

def get_credentials_from_api():
    response = requests.get(BASE_URL, auth=auth)
    creds = json.loads(response.text)
    return creds

def post_credentials_from_api(email, pw_hash, lang, session_type):
    payload = {
        "email": email,
        "hash": pw_hash,
        "lang": lang,
        "type": session_type
    }
    response = requests.post(BASE_URL, json=payload, auth=auth)

def put_credentials_from_api(_id, email, pw_hash, lang, session_type):
    payload = {
        "id": _id,
        "email": email,
        "hash": pw_hash,
        "lang": lang,
        "type": session_type
    }
    response = requests.put(BASE_URL, json=payload, auth=auth)

def delete_credentials_from_api(_id):
    payload = {"id":_id}
    requests.delete(BASE_URL, json=payload, auth=auth)

def get_credentials_by_id_from_api(id):
    response = requests.get(f"{BASE_URL}/{id}", auth=auth)
    creds = json.loads(response.text)
    return creds
