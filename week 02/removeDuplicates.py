#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 22:30:44 2021

@author: daniel
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = 0
        i = 0
        while i < len(nums):
            if nums[length] < nums[i]:
                length += 1
                nums[length] = nums[i]    
            i += 1
    
        return length + 1
        
 