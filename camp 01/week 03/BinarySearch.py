#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 22:11:43 2021

@author: daniel
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] <target:
                l = m + 1
            else:
                r = m - 1
        return -1
#         length = len(nums)+1
#         mid = length//2
#         if nums[mid-1] == target:
#             return mid - 1
#         else:
#             if target > mid:
#                 return mid + 1 + self.search(nums[mid+1:],target)
#             elif target < mid:
#                 return self.search(nums[0:mid],target)
#             else:
#                 return -1