#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def getScores(scores,alices):
    localScore = scores
    for score in alices:
        if (localScore.index(score)==-1):
            localScore.append(score)
            localScore.sort(reverse=True)
        yield localScore

def climbingLeaderboard(scores, alice):
    finalArray = []
    localScore = getScores(scores,alice)
    for score in alice:
        print(next(localScore).index(score))
        
    return finalArray

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
