import requests

payload = {
    "name": "Animesh",
    "job": "QA Engineer"
}

resp = requests.post("https://reqres.in/api/users", data=payload)
status_code = resp.status_code
resp_json = resp.json()
print(status_code)
print(resp_json)
assert resp_json['job'] == 'QA Engineer', "Job title is not matching with the expected job title"
