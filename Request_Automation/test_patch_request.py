import requests

payload = {
    "name": "Suresh"
}

resp = requests.patch('https://reqres.in/api/users/2', data=payload)
print(resp.status_code)
print(resp.json())
