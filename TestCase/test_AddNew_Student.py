import requests
import json
import jsonpath

def test_Add_Student_Data():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails"
    path = open("/home/thileepan/Documents/API/studentdetails.json",'r')
    json_request = json.loads(path.read())
    response = requests.post(API_URL,json_request)
    print(response.text)

def test_Update_Student_Data():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/139739"
    path = open("/home/thileepan/Documents/API/studentdetails.json",'r')
    json_request = json.loads(path.read())
    response = requests.put(API_URL,json_request)
    print(response.text)

def test_Delete_Student_Data():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/139739"
    response = requests.delete(API_URL)
    print(response.text)

def test_Get_Student_Data():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/139739"
    response = requests.get(API_URL)
    json_path = json.loads(response.text)
    id = jsonpath.jsonpath(json_path, 'data.id')
    assert id[0] == 139739