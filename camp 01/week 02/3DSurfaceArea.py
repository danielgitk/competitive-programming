#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 17:03:34 2021

@author: daniel
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the surfaceArea function below.
def bound(x, y ,  mat):
    return 0 <= x < len(mat) and 0<= y < len(mat[0])
    
def surfaceArea(A):
    

    lenofA,lenofB = len(A),len(A[0])
    area = 0
    moves = [[0,1],[1,0],[-1,0],[0,-1]]
    for i in range(lenofA):
        for j in range(lenofB):
            for k,l in moves:
                cArea = A[i][j]
                e,f = k + i,l+ j
                area += max(0,cArea - A[e][f]) if bound(e,f,A) else cArea 
                
    TopandBottom  = lenofA * lenofB * 2
    return  TopandBottom + area
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    HW = input().split()

    H = int(HW[0])

    W = int(HW[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()
