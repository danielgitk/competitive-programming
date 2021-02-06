#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 12:55:30 2021

@author: daniel
"""

class Solution:
    # from bisect import bisect_left,bisect_right
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def searchBinary(nums, left, right, target, start):
            while left<=right:
                mid = left + (right-left)//2
                if nums[mid]==target:
                    if start:
                        right = mid - 1
                    else:
                        left = mid + 1
                elif nums[mid]<target:
                    left = mid + 1
                else:
                    right = mid - 1
            if start:
                return left
            return right
        res = [-1,-1]
        if len(nums)==0:
            return res
        left, right = 0, len(nums) - 1
        start = searchBinary(nums, left, right, target, True)
        if start>=len(nums) or nums[start]!=target:
            return res
        res[0] = start    
        res[1] = searchBinary(nums, start, right, target, False)
        return res
        # l=bisect.bisect_left(nums,target)
        # r=bisect.bisect_right(nums,target)
        # return (l,r-1) if l<r else (-1,-1)