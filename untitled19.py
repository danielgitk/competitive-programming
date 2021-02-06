#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 01:03:14 2021

@author: daniel
"""

import heapq
heap = []
answer = []
some = input()
arr = list(map( int,input().split()))
for val in arr:
    heapq.heappush(heap,val)
print('[',end="")
counter = 0
while heap:
    if counter == len(arr)-1:
        print(heapq.heappop(heap),end="")
    else:
        print(heapq.heappop(heap),end=",")
    counter += 1

# for i in range(len(answer)):
#     if i == len(answer)-1:
#         print(answer[i], end="")
#     else:
#         print(answer[i],end=",")
print(']')