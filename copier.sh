#!/bin/bash

python3 /Users/terickson/rpi-weather/rpi-weather.py
aws s3 cp weather.svg s3://data-visual/
