#!/bin/python3

import sys
import os
from urllib.request import Request
from urllib.request import urlopen
from urllib.error import URLError
import json


import datetime
from urllib import request, parse
# Complete the function below.

def getURL (pageNo):   
    
    while True:
        newUrl = f"https://jsonmock.hackerrank.com/api/stocks/?page={pageNo}"
        yield newUrl
        pageNo +=1
def printWeekDay(data,weekDay, firstDate, lastDate):
    week = {
        "Monday":1,
        "Tuesday":2,
        "Wednesday":3,
        "Thursday":4,
        "Friday":5,
        "Saturday":6,
        "Sunday":7
    }
    
    for item in data:
        dateItem = datetime.datetime.strptime(item['date'],'%d-%B-%Y')
        firstDate_date = datetime.datetime.strptime(firstDate, '%d-%B-%Y')
        lastDate_date = datetime.datetime.strptime(lastDate, '%d-%B-%Y')

        if dateItem >= firstDate_date and dateItem <= lastDate_date:
            weekIndex = dateItem.isoweekday()

            if (weekIndex == week[weekDay]):
                print (item['date'], item['open'], item['close'])


def dataCheck(startDate,endDate,data):
    pageOkay=False
    dataSuffice=False
    startDate_date = datetime.datetime.strptime(startDate,'%d-%B-%Y')
    endDate_date = datetime.datetime.strptime(endDate,'%d-%B-%Y')
    earliestDate = datetime.datetime.strptime(data[0]['date'],'%d-%B-%Y')
    latestDate = datetime.datetime.strptime(data[len(data)-1]['date'], '%d-%B-%Y')
    if (startDate_date>latestDate):
        return (pageOkay,dataSuffice)
    else:
        pageOkay = True
        if (endDate_date < earliestDate):
            #the date does not exist
            dataSuffice = True # end loop
            
        elif(endDate_date>=earliestDate):
            # e.g 2nd and 3rd of same month and year
            
            if (endDate_date<=latestDate):
                #data is complete
                dataSuffice = True
    return (pageOkay,dataSuffice)

def  openAndClosePrices(firstDate, lastDate, weekDay):
    
    dataOkay,dataSuff = False,False
    count = -1
    page = getPage(count)
    while not dataSuff:
        data = next(page)
        dataOkay, dataSuff = dataCheck(firstDate, lastDate, data['data'])
        
        if (dataOkay):
            for day in printWeekDay(data['data'],"Monday",firstDate,lastDate):
                pass

try:
