import requests
import json
import jsonpath
import pytest

# API URL
url = "https://reqres.in/api/users"

a = 100

@pytest.fixture()
def start_json_path():
    global file
    file = open("/home/thileepan/Documents/NewResource.json", 'r')

@pytest.mark.Sanity
#@pytest.mark.skipif(a>100, reason="Condition is not satisfied")
def test_create_new_user(start_json_path):
    json_input = file.read()
    requests_json = json.loads(json_input)

    # Make POST request with Json Input
    response = requests.post(url, requests_json)

    #Validating response code
    assert response.status_code == 201

@pytest.mark.Smoke
def test_create_other_user(start_json_path):
    json_input = file.read()
    requests_json = json.loads(json_input)
    # Make POST request with Json Input
    response = requests.post(url, requests_json)
    # Parse response to json format
    response_json = json.loads(response.text)
    # Pick ID from json path
    id = jsonpath.jsonpath(response_json, 'id')
    print(id[0])
