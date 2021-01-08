#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 11:04:04 2021

@author: daniel
"""
def insertionSort(array):
    for i in range(1, len(array)):
        value = array[i]
        tracker = i
        while tracker > 0 and array[tracker - 1] > value:
            array[tracker] = array[tracker -1]
            print(tracker)
            tracker = tracker - 1
            

        array[tracker] = value
    return array
                

if __name__ == "__main__":
    arr = [1,5,9,3,4,6,7]
    print(insertionSort(arr))

        