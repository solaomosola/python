#!/bin/python3

import sys
import os
from urllib.request import Request
from urllib.request import urlopen
from urllib.error import URLError
import json


from datetime import datetime
from urllib import request, parse
import json
# Complete the function below.
week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
dateformat = '%d-%B-%Y'
def getURL (pageNo):   
    while True:
        newUrl = 'https://jsonmock.hackerrank.com/api/stocks/?page={}'.format(pageNo)
        yield newUrl
        pageNo +=1
def getPage(URL,from_,to_,weekDay):
    req = request.urlopen(URL)
    data = req.read()
    jsonData = json.loads(data)['data']
    
    from_date = datetime.strptime(from_,dateformat)
    to_date = datetime.strptime(to_,dateformat)
    dateAtBegin = datetime.strptime(jsonData[0]['date'],dateformat)
    dateAtEnd = datetime.strptime(jsonData[len(jsonData)-1]['date'], dateformat)
    if (from_date<=dateAtEnd):
        if (to_date<=dateAtEnd):
            needsNextPage  = False
        else:
            needsNextPage= True
    else:
        needsNextPage = True
    return (needsNextPage,jsonData)
            
            

    
def  openAndClosePrices(firstDate, lastDate, weekDay):
    url = getURL(1)
    needsNextPage = True
    
    while needsNextPage:
        needsNextPage,jsonData = getPage(next(url), firstDate, lastDate, weekDay)
        for item in jsonData:
            currentDate = datetime.strptime(item['date'], dateformat)
            from_date = datetime.strptime(firstDate, dateformat)
            to_date = datetime.strptime(lastDate, dateformat)
            if (currentDate>=from_date and currentDate<=to_date and week[currentDate.weekday()]==weekDay):
                print(item['date'], item['open'],item['close'])



    

    
    

try:
