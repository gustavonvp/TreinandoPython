import requests
import json

payload = {'name': 'Gustavo Nunes', 'job': 'developer'}

response = requests.post('https://www.reqres.in/api/users',data = json.dumps(payload))

print(response.request.body)

print(response.status_code)

print(response.text)
