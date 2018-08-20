import requests
import matplotlib.pyplot as plt

outside_weather, inside_weather = [], []
r = requests.get('http://api.openweathermap.org/data/2.5/weather?lat=39.7521448&lon=-105.0233895&APPID=977c4567f54065e97d732e98b76e6180&units=imperial')
response = r.json()
print(response)
temp = float(response['main']['temp'])
print('the weather is imperial ', temp)

for i in range(11):
    temp += 1
    outside_weather.append(temp)

print(outside_weather)
plt.plot(outside_weather)

plt.title('Temp In and Out of Place: ', fontsize=24)
plt.xlabel('Time', fontsize=14)
plt.ylabel('Temp Farenheit', fontsize=14)

plt.show()

# outside_weather.append()