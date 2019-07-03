#!/bin/python3

import sys
import os
from urllib.request import Request
from urllib.request import urlopen
from urllib.error import URLError
import json


import requests
# Complete the function below.

def  openAndClosePrices(firstDate, lastDate, weekDay):
    URL = "https://jsonmock.hackerrank.com/api/stocks"
    PARAMS = {}
    
    response = requests.get(url=URL, params = PARAMS)
    data = response.json()
    print(data['data'])

try:
    _firstDate = str(input())
except:
    _firstDate = None


try:
    _lastDate = str(input())
except:
    _lastDate = None


try:
    _weekDay = str(input())
except:
    _weekDay = None

openAndClosePrices(_firstDate, _lastDate, _weekDay)

