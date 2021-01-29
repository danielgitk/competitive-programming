#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 17:59:31 2021

@author: daniel
"""

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        nums1 = set(nums1)    
        nums2 = set(nums2)
   
        return nums1.intersection(nums2)