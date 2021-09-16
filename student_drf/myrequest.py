import requests
import json


def get_req():
    URL ="http://localhost:8000/studentapi/"
    data = {
        "id" : 3
    }
    headers =  { 'content-Type' : 'application/json'}
    json_data= json.dumps(data)
    r = requests.get(url=URL,headers=headers,data=json_data)
    data = r.json()
    print(data)

def post_req():
    URL ="http://localhost:8000/studentapi/"
    data = {
        "name" : "Sonam Ameerpet1",
        "roll" : 106,
        "city" : "Ranchii"
    } 
    headers =  { 'content-Type' : 'application/json'}
    json_data= json.dumps(data)
    r = requests.post(url=URL,headers=headers,data=json_data)
    data = r.json()
    print(data)
    
# post_req()


def put_req():
    URL ="http://localhost:8000/studentapi/"
    data = {
        "id" : 10,
        "name" : "Jasmin",
        "roll" : 106,
        "city" : "Dhanbad"
    } 
    headers =  { 'content-Type' : 'application/json'}
    json_data= json.dumps(data)
    r = requests.put(url=URL,headers=headers,data=json_data)
    data = r.json()
    print(data)
    
# put_req()


def delete_req():
    URL ="http://localhost:8000/studentapi/"
    data = {
        "id" : 10,
        "name" : "Jasmin",
        "roll" : 106,
        "city" : "Dhanbad"
    } 
    headers =  { 'content-Type' : 'application/json'}
    json_data= json.dumps(data)
    r = requests.delete(url=URL,headers=headers,data=json_data)
    data = r.json()
    print(data)
    
delete_req()