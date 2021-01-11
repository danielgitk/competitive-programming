#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 22:05:56 2021

@author: daniel
"""

class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        newArr = []
        extras = []
        for i in arr2:
            for j in range(len(arr1)):
                if i == arr1[j]:
                    newArr.append(arr1[j])
        for i in arr1:
            if i not in arr2:
                extras.append(i)
        newArr.extend(sorted(extras))
        return newArr
        