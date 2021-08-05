import requests
payload = {
    "name": "morpheus",
    "job": "zion resident"
}
resp = requests.put('https://reqres.in/api/users/2', data=payload)