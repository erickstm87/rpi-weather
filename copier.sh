#!/bin/bash

python3 rpi-weather.py
aws s3 cp weather.svg s3://data-visual/
