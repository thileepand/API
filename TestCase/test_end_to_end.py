import requests
import json
import jsonpath

def test_add_new_student():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails"
    path = open('/home/thileepan/Documents/API/studentdetails.json','r')
    request_json = json.loads(path.read())
    response = requests.post(API_URL,request_json)
    id  = jsonpath.jsonpath(response.json(),'id')
    print(id[0])

    tech_api_url = "http://thetestingworldapi.com/api/technicalskills"
    path = open('/home/thileepan/Documents/API/technicalskills.json','r')
    request_json = json.loads(path.read())
    request_json['id'] = int(id[0])
    request_json['st_id'] = id[0]
    response = requests.post(tech_api_url,request_json,'id')
    print(response.text)

    add_api_url = "http://thetestingworldapi.com/api/addresses"
    path = open('/home/thileepan/Documents/API/address.json','r')
    request_json = json.loads(path.read())
    request_json['stId'] = id[0]
    response = requests.post(add_api_url,request_json)

    final_api_url = "http://thetestingworldapi.com/api/FinalStudentDetails/"+str(id[0])
    response = requests.get(final_api_url)
    print(response.text)