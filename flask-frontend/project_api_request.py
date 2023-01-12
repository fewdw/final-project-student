import requests, json
from bson.objectid import ObjectId

# get all projects by id 
def get_all_projects_from_api():
    all_projects_api_link = "http://127.0.0.1:5001/project/"
    response = requests.get(all_projects_api_link)
    projects = json.loads(response.text)
    return projects