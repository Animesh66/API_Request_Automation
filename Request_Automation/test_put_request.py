import requests

payload = {
    "name": "Nitai",
    "job": "Melbourne"
}

resp = requests.put('https://reqres.in/api/users/2', data=payload)
print(resp.status_code)
print(resp.json())