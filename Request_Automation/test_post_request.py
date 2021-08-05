import json
import requests

json_data = open("data.json", "r").read()
resp = requests.post("https://reqres.in/api/users", data=json.loads(json_data))
status_code = resp.status_code
resp_json = resp.json()
print(status_code)
print(resp_json)
print(resp.headers.get("Content-Type"))  # this is to get the content type filed from header
assert resp_json['job'] == 'QA Engineer', "Job title is not matching with the expected job title"
