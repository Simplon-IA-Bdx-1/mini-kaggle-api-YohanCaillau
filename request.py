import requests

url = 'http://localhost:5000/submit_api'
r = requests.post(url)

print(r.json())