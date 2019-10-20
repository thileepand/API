import requests
import json
import jsonpath

#API URL
url = "https://reqres.in/api/users?page=2"

#Send GET Request
response = requests.get(url)

#Parse response to JSON format
json_response = json.loads(response.text)

#Fetch value using JSON path
for i in range(0,3):
    first_name = jsonpath.jsonpath(json_response, 'data['+str(i)+'].first_name')
    print((first_name[0]))