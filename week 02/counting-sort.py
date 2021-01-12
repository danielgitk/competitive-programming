#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 09:28:16 2021

@author: daniel
"""
def countingSort(arr):
    arr = [1,3,4,5,5,2,9]
    maxi = max(arr) + 1
    counter_arr = [0]*maxi
    n = len(arr)
    new_arr = [0]*n
    
    for i in range(len(arr)):
        counter_arr[arr[i]] += 1
    for i in range(1,maxi):
        counter_arr[i]+= counter_arr[i-1]
    
    i = n - 1
    while i >= 0:
        new_arr[counter_arr[arr[i]] - 1] = arr[i]
        counter_arr[arr[i]] -= 1
        i -= 1
    return new_arr

if __name__ == "__main__":
    print(countingSort([3,6,7,2,0,1,3]))


    

