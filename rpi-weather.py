import requests
import matplotlib.pyplot as plt

def getTemp():
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?lat=39.7521448&lon=-105.0233895&APPID=977c4567f54065e97d732e98b76e6180&units=imperial')
    response = r.json()
    print(response)
    temp = response['main']['temp']
    print('the weather is imperial ', temp)
    return temp

# outside_weather.append()