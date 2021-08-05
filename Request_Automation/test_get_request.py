import requests

parameters = {'page': 2}
resp = requests.get("https://reqres.in/api/users", params=parameters)
print(resp.url)
print(resp)
print(type(resp))
print(dir(resp))
status_code = resp.status_code
print(status_code)
assert status_code == 200, "Status code is not 200."
print(resp.text)  # Content of the response, in unicode.
print(resp.content)  # Content of the response, in bytes.
resp_json = resp.json()
resp_header = resp.headers
resp_cookies = resp.cookies
resp_encoding = resp.encoding
print(resp_header)  # returns all the headers
print(resp_json)  # Returns the json-encoded content of a response, if any
# Navigate to http://jsonviewer.stack.hu/ to view the json format data
print(resp_cookies)

#   *** Verify responses ***

print(resp_json['total_pages'])
assert resp_json['total_pages'] == 2, "Total pages count does not match"
print(resp_json['data'][0]['email'])
assert resp_json['data'][0]['email'] == 'michael.lawson@reqres.in', "Email id is not matching"
assert (resp_json['data'][0]['email']).endswith('@reqres.in'), "Email format not matching"
