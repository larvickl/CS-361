import requests

url = 'http://localhost:5000/observations'

params = {'park_name': 'yellowstone-national-park'}

response = requests.get(url, params=params)

data = response.json()
print(data) 
