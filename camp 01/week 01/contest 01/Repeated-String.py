#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 15:20:16 2021

@author: daniel
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    d = len(s)
    sum = 0
    div = n//d
    rem = n%d  
    if div:
        for i in s:
            if i == 'a':
                sum = sum + 1
    sum = sum * div
        
    if rem:
        for i in s[:rem]:
            if i == 'a':
                sum = sum + 1
   
  
    return sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
