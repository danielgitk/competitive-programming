#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    # Write your code here
    d = []
    scores  = getArray(ranked)
    n = len(scores)
    i = 0
    for x in player:
        while i<n and scores[n-i-1] <= x:
            i+= 1
        d.append(n-i+1)      
    return d
        
    
def getArray(arr):
    y = len(arr)
    res = []
    i = 0
    while i < y:
        someval = arr[i]
        res.append(someval)
        while i < y and someval == arr[i]:
            i += 1   
    return res
    
        
        
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
