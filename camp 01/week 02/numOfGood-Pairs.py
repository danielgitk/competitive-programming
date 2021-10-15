#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 20:43:01 2021

@author: daniel
"""

class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        data = {}
        isGood = 0
        for i in nums:
            if i in data:
                isGood += data[i]
                data[i] += 1                
            else:
                data[i] = 1
        return isGood