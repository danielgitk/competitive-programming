#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 17:24:04 2021

@author: daniel
"""

def bubbleSort(array):
    for j in range(len(array)):
        for i in range(len(array)-1):
            if array[i] > array[i + 1]:
                array[i],array[i+1] = array[i+1],array[i]
    return array


if __name__ == "__main__":
    ar = [1,4,4,5,8,12,23,2,6,9]
    print(bubbleSort(ar))