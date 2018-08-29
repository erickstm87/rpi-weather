import boto3

s3 = boto3.resource('s3')
bucket = s3.Bucket('data-visual')
#s3.upload_file('weather.svg', 'data-visual', 'weather_one.svg')
#s3.Bucket('data-visual').upload_file('weather.svg', 'weather-copied.svg')
with open('weather.svg', 'rb') as data:
    bucket.upload_fileobj(data, 'weathercopy.svg')
