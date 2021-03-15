#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gridlandMetro function below.
def gridlandMetro(n, m, k, track):
    free = n * m
    extras = 0
    dicti  = {}    
    for row, start,finish in track:
        start,finish = (start,finish) if start <= finish else (finish,start)
        if row not in dicti:
            dicti[row] = [[start,finish]]
        else :
            found = 0
            for i in range(len(dicti[row])):
                rows = dicti[row]
                print(rows)
                start1,finish1 = dicti[row][i]
                if start > finish1 or finish < start1:
                    continue
                else:
                    start1 = start if start <= start1 else start1
                    finish1 = finish if finish >= finish1 else finish1
                    dicti[row][i] = [start1,finish1] 
                    found = 1
            if not found:
                dicti[row].append([start,finish])
                print(dicti)
                   
    for row in dicti.values():
        for start, finish in row:
            free -= (finish - start + 1)       
    return free
            
            
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nmk = input().split()

    n = int(nmk[0])

    m = int(nmk[1])

    k = int(nmk[2])

    track = []

    for _ in range(k):
        track.append(list(map(int, input().rstrip().split())))

    result = gridlandMetro(n, m, k, track)

    fptr.write(str(result) + '\n')

    fptr.close()
