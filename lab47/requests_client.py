import requests

# ---------------------------- Simple GET request ---------------------------- #
url = 'http://127.0.0.1:8000'

headers = {
	'User-Agent': 'Iva',
}

r = requests.get(url,headers=headers)
q = {

}

request = r.request

print(request.headers)
print('~'*30)
print(r.headers)
print('~'*30)
if r.ok:
	print(r.text)
else:
	print(f'status_code: {r.status_code}')

# ---------------------------- Simple POST Request --------------------------- #
# base url
url = 'http://127.0.0.1:9999'

# prepare headers
headers = {
  'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
}

data = {
  'username':'python_course_test',
  'password':'python_course_test123'
}

# send request
response = requests.post(url, headers=headers, data=data)

if response.ok:
    print(response.text)
else:
	print(response.status_code)
