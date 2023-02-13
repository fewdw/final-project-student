import requests, json
from bson.objectid import ObjectId
import os

auth = requests.auth.HTTPBasicAuth(os.environ.get("api_user"), os.environ.get("api_pass"))

# get all projects by id 
def get_all_projects_from_api():
    all_projects_api_link = "http://127.0.0.1:5001/project/"
    response = requests.get(all_projects_api_link, auth=auth)
    projects = json.loads(response.text)
    return projects


def delete_project_from_api(p_id):
    print(p_id)
    url = "http://127.0.0.1:5001/projects"
    payload = {"id":p_id}
    requests.delete(url, json=payload, auth=auth)

def post_a_project_to_api(p_id,name,desc):
        url = "http://127.0.0.1:5001/projects"
        payload = {
            "project_id":p_id,
            "project_name":name,
            "project_description":desc
        }
        requests.post(url, json=payload, auth=auth)

def put_a_project_to_api(_id,p_id,name,desc):
    url = "http://127.0.0.1:5001/projects"
    payload= {
        "id":_id,
        "project_id":p_id,
        "project_name":name,
        "project_description":desc
    }
    requests.put(url,json=payload, auth=auth)