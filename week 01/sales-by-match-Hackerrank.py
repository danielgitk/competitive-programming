#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 08:43:21 2021

@author: daniel
"""
import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    dicti = {}   
    for i in ar:
        if i not in dicti:
            dicti[i] = 1
        elif i in dicti:
            dicti[i] += 1
    matching_socks = 0
    for x in dicti:
        matching_socks += dicti[x]//2
    return matching_socks
   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()