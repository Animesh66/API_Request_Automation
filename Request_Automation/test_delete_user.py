import requests

resp = requests.delete("https://reqres.in/api/users/200")
print(resp.status_code)
assert resp.status_code == 204, "Response code should be 204 but not matching"
