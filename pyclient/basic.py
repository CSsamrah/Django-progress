import requests
import json

# simple http request gives response in HTML form 
# endpoint="http://127.0.0.1:8000/api/studinfo/2"  
# rest API gives response in JSON 
# get_response=requests.get(endpoint)
# print(get_response.text)

URL="http://127.0.0.1:8000/api/student-api/"

def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id}
    json_data=json.dumps(data)
    headers={'content-type':'application/json'}
    r=requests.get(url=URL,headers=headers,data=json_data)
    data=r.json()
    print(data)
get_data(15)

def create_data():
    data={
        'name':'sajjad',
        'roll':45,
        'city':'karachi'
    }
    json_data=json.dumps(data)
    headers={'content-type':'application/json'}
    r=requests.post(url=URL,headers=headers,data=json_data)
    data=r.json()
    print(data)
# create_data()


def update_data():
    data={
    'id':21,
    'name':'samrah',
    'roll':56,
    'city':'karachi',
    }

    json_data=json.dumps(data)
    headers={'content-Type':'application/json'}

    r=requests.put(url=URL,headers=headers, data=json_data)

    data=r.json()
    print(data)
# update_data()

def delete_data():
    data={
        'id':19
    }
    json_data=json.dumps(data)
    headers={'content-type':'application/json'}
    r=requests.delete(url=URL,headers=headers, data=json_data)
    data=r.json()
    print(data)
delete_data()
    




# print(get_response.json())  
# converted into python dictionary
# print("\n") 
# print(get_response.status_code)
# print("\n") 
# print(get_response)
 
# convert python dictionary into json
# dumps method (to convert python obj into json string)
# python_data={'name':'Samrah', 'roll_no':'SE-22-01'}
# json_data=json.dumps(python_data)
# print(json_data)
# # #loads method(used to parse json string)
# parsed_data=json.loads(json_data)
# print(parsed_data) #converts json into python