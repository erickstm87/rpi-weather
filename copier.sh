#!/bin/bash

python3 /home/pi/rpi-weather/rpi-weather.py
/usr/local/bin/aws s3 cp weather.svg s3://data-visual/
python3 /home/pi/rpi-weather/api-calls/api-calls.py
/usr/local/bin/aws s3 cp /home/pi/rpi-weather/api-calls/python_repos.svg s3://data-visual/
python3 /home/pi/rpi-weather/api-calls/javascript-calls.py
/usr/local/bin/aws s3 cp /home/pi/rpi-weather/api-calls/javascript_repos.svg s3://data-visual/
python3 /home/pi/rpi-weather/api-calls/scala-calls.py
/usr/local/bin/aws s3 cp /home/pi/rpi-weather/api-calls/scala_repos.svg s3://data-visual/
