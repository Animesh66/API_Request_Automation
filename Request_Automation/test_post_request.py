import requests

data = {
    "name": "morpheus",
    "job": "leader"
}
resp = requests.post("https://reqres.in/api/users")