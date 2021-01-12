#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 08:19:07 2021

@author: daniel
"""

class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        isCool = 0
        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                if i==1 or nums[i-2] <= nums[i]:
                    nums[i-1] = nums[i]
                    isCool += 1
                else:
                    nums[i] = nums[i-1]
                    isCool += 1
            if isCool > 1:
                return False
                
                     
        return True
        
        