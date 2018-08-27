import requests
from pymongo import MongoClient
import matplotlib.pyplot as plt
import pygal
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
outside_temp = float(response['main']['temp'])
# print('the weather is imperial ', outside_temp)
hourly = datetime.now().hour
minutely = datetime.now().minute
current_time = str(hourly) + ':' + str(minutely)

posts = db.posts
weather_data = {
    'title': 'Outside Weather',
    'temp': outside_temp,
    'date': current_time
}
result = posts.insert_one(weather_data)
found_post = posts.find_one({'title': 'Outside Weather'})

outside_weather, the_time = [], []
for post in posts.find():
    outside_weather.append(post['temp'])
    the_time.append(post['date'])

print(outside_weather)
print(the_time)

line_chart = pygal.Line()
line_chart.title = ('Temp In and Out of Place with ' + response['weather'][0]['description'].title() + ' Conditions: ')
line_chart.x_labels = map(str, the_time)
line_chart.add('Outside', outside_weather)
line_chart.render_to_file('weather.svg')

# for post in posts.find():
#     posts.remove()
def remove_entries():
    for post in posts.find():
        posts.remove()