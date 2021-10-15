#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 15:17:46 2021

@author: daniel
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    sum = 0
    true_split = 0
    for i in range(len(bill)):
        if i != k:
            sum = sum + bill[i]

    true_split = int(sum/2)

    if true_split == b:
        print("Bon Appetit")
    else:
        print(abs(true_split - b))
    
        
        
    

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
