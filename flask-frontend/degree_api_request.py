import requests, json
from bson.objectid import ObjectId
import os

auth = requests.auth.HTTPBasicAuth(os.environ.get("api_user"), os.environ.get("api_pass"))

URL= os.environ.get("url")
BASE_URL = f"{URL}/degrees"

# get all degrees
def get_all_degrees_from_api():
    all_dgrees_api_link = BASE_URL
    response = requests.get(all_dgrees_api_link, auth=auth)
    degrees = json.loads(response.text)
    return degrees

def delete_degree_from_api(id):
    _id = id[10:34]
    url = BASE_URL
    payload = {"id":_id}
    requests.delete(url, json=payload, auth=auth)

def post_a_degree_to_api(d_id,name,desc):
        url = BASE_URL
        payload = {
            "degree_id":d_id,
            "name_degree":name,
            "description":desc
        }
        requests.post(url, json=payload, auth=auth)
    
def put_a_degree_to_api(_id,d_id,name,desc):
    url = BASE_URL
    payload= {
        "id":_id,
        "degree_id":d_id,
        "name_degree":name,
        "description":desc
    }
    requests.put(url,json=payload, auth=auth)