#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 17:25:56 2021

@author: daniel
"""

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        dicti = {}
        for i in nums:
            dicti[i] = dicti.get(i,0) + 1
        return sorted(nums, key=lambda x: (dicti[x], -x))