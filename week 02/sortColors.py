#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 18:21:56 2021

@author: daniel
"""

class Solution(object):
    def sortColors(self, array):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for j in range(len(array)):
            for i in range(len(array)-1):
                if array[i] > array[i + 1]:
                    array[i],array[i+1] = array[i+1],array[i]
        return array
        