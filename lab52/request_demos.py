import requests

url = "http://127.0.0.1:45047/lab52/mysite.com/main.html"

r = requests.get(url)
if r.ok:
	print(r.text)