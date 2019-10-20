import requests
import json
from requests.auth import HTTPBasicAuth

def test_basic_auth():
    headers = {'content-type': 'application/json'}
    url = 'https://qa-product.ivycpg.com/webapi/api/usermaster/authenticateuser'
    data = {'LoginId':'thileep.dse','Password':'2'}
    response =  requests.post(url,  data=json.dumps(data), headers=headers)
    print(response.text)
    assert response.status_code == 200









