import requests

# API URL
url = "https://reqres.in/api/users?page=2"

response = requests.get(url)
print(response)
print("**********************************************")
print(response.content)
print("**********************************************")
print(response.headers)