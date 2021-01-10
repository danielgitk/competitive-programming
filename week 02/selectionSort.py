#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 18:18:06 2021

@author: daniel
"""
def selectionSort(arr):
    
    tracker = 0
    while True:
        if tracker == len(arr):
            return arr
        mini = tracker              
        for i in range(tracker,len(arr)):
            
            if arr[i] < arr[mini]:
                mini = i
        
        arr[tracker],arr[mini] = arr[mini],arr[tracker] 
        tracker += 1
        
if __name__ == "__main__":
    arr  = [1,4,2,9,3,5]
    selectionSort(arr)
    
    