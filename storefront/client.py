import requests
import json

URL="http://127.0.0.1:8000/playground/student-create/"

# get_response=requests.get(url=URL)
# r=get_response.json()
# print(r)


data={
    'name':'samrah',
    'roll':17,
    'city':'lahore',
}

json_data=json.dumps(data)
print(json_data)
r=requests.post(url=URL, data=json_data)
# print(r.headers)
data=r.json()
print(data)