import requests
import json

API_key = 'c6fb64fec365de60c2e15986a29b3a1c'
url = f"https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid={API_key}"

response = requests.get(url)

data = response.json()

print(json.dumps(data,indent=5))
