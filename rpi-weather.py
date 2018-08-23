import requests
from pymongo import MongoClient
import sqlite3
import matplotlib.pyplot as plt

client = MongoClient()
# conn = sqlite3.connect('temps.db')

client = MongoClient('localhost', 27017)
db = client.pymongo_test
posts = db.posts
post_data = {
    'title': 'Python and MongoDB',
    'content': 'PyMongo is fun, you guys',
    'author': 'Scott'
}
result = posts.insert_one(post_data)
print('One post: {0}'.format(result.inserted_id))


r = requests.get('http://api.openweathermap.org/data/2.5/weather?lat=39.7521448&lon=-105.0233895&APPID=977c4567f54065e97d732e98b76e6180&units=imperial')
response = r.json()
print(response)
temp = float(response['main']['temp'])
print('the weather is imperial ', temp)

# c = conn.cursor()
# c.execute('''CREATE TABLE weather(outside_weather, inside_weather, time)''')
# c.execute("Insert weather (25,28,7)")
# conn.commit()
# conn.close()

# print(outside_weather)
# plt.plot(outside_weather)

# plt.title('Temp In and Out of Place: ', fontsize=24)
# plt.xlabel('Time', fontsize=14)
# plt.ylabel('Temp Farenheit', fontsize=14)

# plt.show()

# outside_weather.append()