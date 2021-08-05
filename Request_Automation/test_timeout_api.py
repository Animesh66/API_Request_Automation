import requests

resp = requests.get("https://httpbin.org/delay/10", timeout=5)  # delay API with 10 second request
print(resp.status_code)  # will throw an error due to timeout requests.exceptions.ReadTimeout