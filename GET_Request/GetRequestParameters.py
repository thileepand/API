import requests
param = {'name':'Thileepan','email':'thileepan.r@ivymobility.com', 'number':'7305-673-661'}
response  = requests.get('https://httpbin.org/get', params=param)
print(response.text)