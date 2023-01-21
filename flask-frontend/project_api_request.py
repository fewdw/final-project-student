import requests, json
from bson.objectid import ObjectId

# get all projects by id 
def get_all_projects_from_api():
    all_projects_api_link = "http://127.0.0.1:5001/project/"
    response = requests.get(all_projects_api_link)
    projects = json.loads(response.text)
    return projects


def delete_project_from_api(p_id):
    print(p_id)
    url = "http://127.0.0.1:5001/projects"
    payload = {"id":p_id}
    requests.delete(url, json=payload)

def post_a_project_to_api(d_id,name,desc):
        url = "http://127.0.0.1:5001/projects"
        payload = {
            "project_id":d_id,
            "project_name":name,
            "project_description":desc
        }
        requests.post(url, json=payload)

def put_a_project_to_api(_id,d_id,name,desc):
    url = "http://127.0.0.1:5001/projects"
    payload= {
        "id":_id,
        "degree_id":d_id,
        "name_degree":name,
        "description":desc
    }
    requests.put(url,json=payload)