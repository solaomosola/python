#!/bin/python3

import sys
import os
from urllib.request import Request
from urllib.request import urlopen
from urllib.error import URLError
import json


import requests
from datetime import datetime
from dateutil.parser import parse
# Complete the function below.

def  openAndClosePrices(firstDate, lastDate, weekDay):
    URL = "https://jsonmock.hackerrank.com/api/stocks"
    PARAMS = {"page":1}
    
    response = requests.get(url=URL, params = PARAMS)
    data = response.json()
    items = data['data']
    startPage,endPage = data["page"],data["total_pages"]
    week = {
        "Monday":1,
        "Tuesday":2,
        "Wednesday":3,
        "Thursday":4,
        "Friday":5,
        "Saturday":6,
        "Sunday":7
    }
    
    for item in items:
        
        dateItem = datetime.strptime(item['date'],'%d-%B-%Y')
        firstDate_date = datetime.strptime(firstDate,'%d-%B-%Y')
        lastDate_date = datetime.strptime(lastDate,'%d-%B-%Y')
        
        if dateItem>=firstDate_date and dateItem<=lastDate_date:
            weekIndex = dateItem.isoweekday()
            
            if (weekIndex == week[weekDay]):
                print(item['date'],item['open'],item['close'])
    
    
try: