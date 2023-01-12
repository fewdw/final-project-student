import requests, json
from bson.objectid import ObjectId

# get all degrees
def get_all_degrees_from_api():
    all_dgrees_api_link = "http://127.0.0.1:5001/degrees/"
    response = requests.get(all_dgrees_api_link)
    degrees = json.loads(response.text)
    return degrees