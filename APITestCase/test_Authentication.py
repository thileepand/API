import json
import jsonpath
import requests
import openpyxl
import logging


def test_user_master():
    global token_value
    headers = {'content-type': 'application/json;charset=utf-8'}
    url = 'https://qa-product.ivycpg.com/webapi/api/usermaster/authenticateuser'
    data = {'grant_type':'Password','LoginId':'thileep.dse','Password':'1'}
    response = requests.post(url,headers=headers,data=json.dumps(data))
    h = response.headers
    token_value = json.loads(json.dumps(dict(h)))['SECURITY_TOKEN_KEY']
    assert response.status_code == 200
    #print(response.status_code)

def test_retailer_master():
    global headers,data
    API_URL = 'https://qa-product.ivycpg.com/webapi/api/V14/RetailerMaster/Masters'
    headers = {"content-type": "application/json", "SECURITY_TOKEN_KEY":  token_value }
    data = {"UserId":"552", "VersionCode":"1430"}
    response = requests.post(API_URL,headers=headers,data=json.dumps(data))
    #print(response.text)
    assert response.status_code==200
    try:
        if  response.status_code ==200:
            print(response.status_code)
    except:
            print("Can not hit retailer master api")

def test_product_master():
    pm = 'https://qa-product.ivycpg.com/webapi/api/Product/Masters'
    response = requests.post(pm,headers=headers,data=json.dumps(data))
    #print(response.text)
    assert response.status_code == 200
    try:
        if  response.status_code ==200:
            print(response.status_code)
    except:
            print("Can not hit product master api")

def test_add_route():
    API_URL = "https://qa-product.ivycpg.com/webapi/api/V2/BeatMaster/Masters"
    path = open("/home/thileepan/Documents/API/beatmaster.json",'r')
    json_request = json.loads(path.read())
    response = requests.post(API_URL,headers=headers,data=json.dumps(dict(data),json_request))
    print(response.text)



def test_route_master():
    rm = 'https://qa-product.ivycpg.com/webapi/api/V2/BeatMaster/Masters'
    response = requests.post(rm,headers=headers,data=json.dumps(data))
    assert response.status_code == 200
    print(response.text)
    try:
        if response.status_code == 200:
            print(response.status_code)
    except:
        print("Can not hit route master api")


