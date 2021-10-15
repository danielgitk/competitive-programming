#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 14:21:15 2021

@author: daniel
"""

def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums)//2 
        L = nums[:mid] 
        R = nums[mid:] 

        merge_sort(L) 
        merge_sort(R)
        
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                nums[k] = L[i]
                i += 1
                k += 1
            else:
                nums[k] = R[j]
                j += 1
                k += 1

        while i < len(L):
            nums[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            nums[k] = R[j]
            j += 1
            k += 1
    return nums
if __name__ == "__main__":
    print(merge_sort([8,5,3,2,3,1,4,6]))