#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'chooseFlask' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY requirements
#  2. INTEGER m
#  3. 2D_INTEGER_ARRAY markings
#
def filterFlasks(orders,flasks):
    rem_flasks=[]
    

    for flask in flasks:
        add = True
        if (type(flask)=="str"):
            biggest_flask = int(max(flask.split(" ")))
        else:
            biggest_flask = int(max(flask))

        for order in orders:
            if order>biggest_flask:
                add = False
        if (add):
            rem_flasks.append(flask)    

    return rem_flasks
def getLossOfOrder(orders,flasks):
    if (type(flasks)=="str"):
        flasks = flasks.split(" ")
    
    loss = 0
    for order in orders:
        for flask in flasks:
            flask = int(flask)
            if (flask < order): continue
            loss += flask - order
            #print(flask,order,loss)
            break

    return loss
def chooseFlask(requirements, m, markings):
    # Write your code here
    orders,flasks = requirements,markings
    print(orders,flasks)
    right_Flasks = filterFlasks(orders,flasks)

    index,correct_Index = -1,-1
    loss = None

    for flask in flasks:
    
        index +=1
        
        if flask in right_Flasks:
            newLoss = getLossOfOrder(orders,flask)
            
            if loss is None:
                loss = newLoss
                correct_Index = index
            else:
                if newLoss<loss:
                    loss = newLoss
                    correct_Index = index
    return correct_Index
if __name__ == '__main__':
