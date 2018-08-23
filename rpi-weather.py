import requests
from pymongo import MongoClient
import matplotlib.pyplot as plt
import datetime
import pprint

client = MongoClient('localhost', 27017)
db = client.pymongo_test

r = requests.get('http://api.openweathermap.org/data/2.5/weather?lat=39.7521448&lon=-105.0233895&APPID=977c4567f54065e97d732e98b76e6180&units=imperial')
response = r.json()
pprint.pprint(response)
outside_temp = str(float(response['main']['temp']))
print('the weather is imperial ', outside_temp)

posts = db.posts
weather_data = {
    'title': 'Outside Weather',
    'temp': str(outside_temp),
    'date': datetime.datetime.utcnow()
}
result = posts.insert_one(weather_data)
found_post = posts.find_one({'title': 'Outside Weather'})
print('Here is the data in db:', found_post)

outside_weather = []
for post in posts.find():
    outside_weather.append(post['temp'])
print('here is the collection of temps: ', outside_weather)
plt.plot(outside_weather)

plt.title('Temp In and Out of Place with ' + response['weather'][0]['description'].title() + ' Conditions: ', fontsize=24)
plt.xlabel('Time', fontsize=14)
plt.ylabel('Temp Farenheit', fontsize=14)

# plt.show()

# outside_weather.append()