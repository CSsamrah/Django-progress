import requests
import json

# simple http request gives response in HTML form 
# endpoint="http://127.0.0.1:8000/api/studinfo/2"  
# rest API gives response in JSON 
# get_response=requests.get(endpoint)
# print(get_response.text)

URL="http://127.0.0.1:8000/api/studcreate/"

data={
    'name':'daniya',
    'roll':17,
    'city':'faisalabad',
}

json_data=json.dumps(data)
print(json_data)
r=requests.post(url=URL, data=json_data)
data=r.json()
print(data)


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