import json
import jsonpath
import requests
import openpyxl


def test_user_master():
    headers = {'content-type': 'application/json;charset=utf-8'}
    url = 'https://qa-product.ivycpg.com/webapi/api/usermaster/authenticateuser'
    data = {'grant_type':'Password','LoginId':'thileep.dse','Password':'2'}
    response = requests.post(url,headers=headers,data=json.dumps(data))
    h = response.headers
    token_value = json.loads(json.dumps(dict(h)))['SECURITY_TOKEN_KEY']

    API_URL = 'https://qa-product.ivycpg.com/webapi/api/V14/RetailerMaster/Masters'
    #API_URL = 'http://192.168.56.1/app2/api/V14/RetailerMaster/Master'
    headers1 = {"content-type": "application/json;charset=utf-8",
               "SECURITY_TOKEN_KEY":  token_value }

    data1 = {"UserId":"552", "VersionCode":"1430"}
    response = requests.post(API_URL,headers=headers1,data=json.dumps(data1))
    print(response.text)

    pm = 'https://qa-product.ivycpg.com/webapi/api/Product/Masters'
    h2 = {"content-type": "application/json;charset=utf-8",
               "SECURITY_TOKEN_KEY":  token_value }
    d2 =  {"UserId":"552", "VersionCode":"1430"}
    response = requests.post(pm,headers=h2,data=json.dumps(d2))
    print(response.text)


