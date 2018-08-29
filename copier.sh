#!/bin/bash

python3 /Users/terickson/rpi-weather/rpi-weather.py
aws s3 cp weather.svg s3://data-visual/
python3 ./api-calls/api-calls.py
aws s3 cp ./api-calls/python_repos.svg s3://data-visual/
python3 ./api-calls/javascript-calls.py
aws s3 cp ./api-calls/javascript_repos.svg s3://data-visual/
python3 ./api-calls/scala-calls.py
aws s3 cp ./api-calls/scala_repos.svg s3://data-visual/