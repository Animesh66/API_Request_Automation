import requests

resp = requests.get("https://reqres.in/api/users?page=2")
print(resp)
print(type(resp))
print(dir(resp))
status_code = resp.status_code
print(status_code)
assert status_code == 200, "Status code is not 200."