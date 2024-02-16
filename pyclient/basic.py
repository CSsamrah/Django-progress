import requests
import json

# endpoint="https://httpbin.org/status/200"
# endpoint="https://httpbin.org" # simple http request gives response in HTML form 
endpoint="http://127.0.0.1:8000/api/hello"  
# rest API gives response in JSON 
get_response=requests.get(endpoint)
print(get_response.text)


print(get_response.json()['name'])  
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
# #loads method(used to parse json string)
# parsed_data=json.loads(json_data)
# print(parsed_data) #converts json into python