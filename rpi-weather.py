import requests
from pymongo import MongoClient
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import pprint
from pytz import timezone
import pytz

client = MongoClient('localhost', 27017)
db = client.pymongo_test

utc = pytz.utc

print('here is the time: ', datetime.now())

r = requests.get('http://api.openweathermap.org/data/2.5/weather?lat=39.7521448&lon=-105.0233895&APPID=977c4567f54065e97d732e98b76e6180&units=imperial')
response = r.json()
pprint.pprint(response)
outside_temp = str(float(response['main']['temp']))
print('the weather is imperial ', outside_temp)
hourly = datetime.now().hour
minutely = datetime.now().minute
current_time = str(hourly) + ':' + str(minutely)

posts = db.posts
weather_data = {
    'title': 'Outside Weather',
    'temp': str(outside_temp),
    'date': current_time
}
result = posts.insert_one(weather_data)
found_post = posts.find_one({'title': 'Outside Weather'})

outside_weather, the_time = [], []
for post in posts.find():
    outside_weather.append(post['temp'])
    #the_time.append(post['date'])

plt.plot(the_time, outside_weather)

plt.title('Temp In and Out of Place with ' + response['weather'][0]['description'].title() + ' Conditions: ', fontsize=24)
plt.xlabel('Time', fontsize=14)
plt.ylabel('Temp Farenheit', fontsize=14)

plt.show()

# outside_weather.append()
