# print('Hi')

# datatemp = {'coord': {'lon': 37.3517, 'lat': 55.6031}, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'небольшая облачность', 'icon': '02d'}], 'base': 'stations', 'main': {'temp': 11.09, 'feels_like': 10.16, 'temp_min': 8.96, 'temp_max': 13.01, 'pressure': 1019, 'humidity': 73}, 'visibility': 10000, 'wind': {'speed': 6, 'deg': 310}, 'clouds': {'all': 20}, 'dt': 1662386961, 'sys': {'type': 2, 'id': 47653, 'country': 'RU', 'sunrise': 1662345781, 'sunset': 1662394571}, 'timezone': 10800, 'id': 857690, 'name': 'Московский', 'cod': 200}
datatemp = '55.6031,37.3517'
print(datatemp.split(','))
lat, lon = datatemp.split(',')
print(f'lat: {lat}')
print(f'lon: {lon}')

# print(type(datatemp))
# print(datatemp["main"]["temp"])
# print(datatemp["weather"][0]["description"])