import requests
import json
import public_ip as ip
import getipinfo
from config import KEY_WEATHER

result = getipinfo.get_info(ip.get())[1]
lat = result.split(',')[0]
lon = result.split(',')[1]

# print(result.split(','))
# print(f'lat: {lat}')
# print(f'lon: {lon}')

url = "https://api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s&lang=%s&appid=%s&units=metric" % (lat, lon, 'ru', KEY_WEATHER)
response = requests.get(url)
data = json.loads(response.text)
# print(data)
print(data["main"]["temp"])
print(data["weather"][0]["description"])