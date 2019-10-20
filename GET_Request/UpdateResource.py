import json
import jsonpath
import requests

# API URL
url = "https://reqres.in/api/users/2"

#Read Input JSON file
file = open("/home/thileepan/Documents/NewResource.json", 'r')
json_input = file.read()
request_json = json.loads(json_input)

# Make PUT request in JSON input
response  = requests.put(url, request_json)

#Validating response code
assert response.status_code == 200

#Parse response content
response_json = json.loads(response.text)

#Pick ID from JSON path
updated_li = jsonpath.jsonpath(response_json, "updatedAt")
print(updated_li[0])