import json
import jsonpath
import requests

def test_add_new_student():
    global id
    API_URL = "http://thetestingworldapi.com/api/studentsDetails"
    path = open('/home/thileepan/Documents/API/addstudent.json')
    request_json = json.loads(path.read())
    response = requests.post(API_URL,request_json)
    id = jsonpath.jsonpath(response.json(),'id')
    print(id[0])

def test_get_details():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/"+str(id[0])
    response = requests.get(API_URL)
    print(response.text)

