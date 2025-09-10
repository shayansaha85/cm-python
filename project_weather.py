import requests

cityName = input('Enter your city name : ')

URL = f'http://api.openweathermap.org/geo/1.0/direct?q={cityName}&limit=5&appid=*********'

response = requests.get(URL)
output = response.json()

lat = output[0]['lat']
lon = output[0]['lon']

lat = round(lat, 2)
lon = round(lon, 2)

weatherURL = f'http://api.weatherapi.com/v1/current.json?q={lat},{lon}&key=**********'

weatherResponse = requests.get(weatherURL)
outputWeather = weatherResponse.json()

temperature = outputWeather['current']['temp_c']
print(f'Temperature of {cityName} : {temperature}°C')