#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 22:18:42 2021

@author: daniel
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superDigit function below.
def superDigit(n, k):
    sum = 0
    for i in n:
        sum += int(i)
    sum = sum * k
    return super_digit(sum)
def super_digit(p):
    if len(str(p)) == 1:
        return p
    else:
        return super_digit(sum([int(x) for x in str(p)]))
        
        
        
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
