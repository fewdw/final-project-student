import requests, json
from bson.objectid import ObjectId
import os

auth = requests.auth.HTTPBasicAuth(os.environ.get("api_user"), os.environ.get("api_pass"))

# get all degrees
def get_all_degrees_from_api():
    all_dgrees_api_link = "http://127.0.0.1:5001/degrees/"
    response = requests.get(all_dgrees_api_link, auth=auth)
    degrees = json.loads(response.text)
    return degrees

def delete_degree_from_api(id):
    _id = id[10:34]
    url = "http://127.0.0.1:5001/degrees/"
    payload = {"id":_id}
    requests.delete(url, json=payload, auth=auth)

def post_a_degree_to_api(d_id,name,desc):
        url = "http://127.0.0.1:5001/degrees"
        payload = {
            "degree_id":d_id,
            "name_degree":name,
            "description":desc
        }
        requests.post(url, json=payload, auth=auth)
    
def put_a_degree_to_api(_id,d_id,name,desc):
    url = "http://127.0.0.1:5001/degrees"
    payload= {
        "id":_id,
        "degree_id":d_id,
        "name_degree":name,
        "description":desc
    }
    requests.put(url,json=payload, auth=auth)