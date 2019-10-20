import requests
import json
import jsonpath
# API URL
url = "https://reqres.in/api/users"

#Read Input JSON file
file  = open("/home/thileepan/Documents/NewResource.json", 'r')
json_input = file.read()
requests_json = json.loads(json_input)

# Make POST request with Json Input
response = requests.post(url, requests_json)

#Validating response code
assert response.status_code == 201

# Fetch header from response
print(response.headers.get('Content-Length'))

#Parse response to json format
response_json = json.loads(response.text)

#Pick ID from json path
id = jsonpath.jsonpath(response_json, 'id')
print(id[0])