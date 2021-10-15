#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 09:02:00 2021

@author: daniel
"""
import math
import os
import random
import re
import sys#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    sea_level = 0
    valley_nums = 0
    for x in path:
        if x == "U" and sea_level == -1:
            sea_level = sea_level + 1
            valley_nums = valley_nums + 1
            
        elif x == "D":
            sea_level = sea_level - 1
        else:
            sea_level = sea_level + 1
        
    return valley_nums
               

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
