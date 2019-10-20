import requests
import json
import jsonpath

# API URL
url = "https://reqres.in/api/users?page=2"

#Send GET request
response = requests.get(url)

#Parse response to JSON format
json_response = json.loads(response.text)

#Fetch value using json path
page = jsonpath.jsonpath(json_response, "total_pages")
assert page[0] == 4