#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 15:37:59 2021

@author: daniel
"""

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if citations == []:
            return 0
        citations = sorted(citations,reverse =True)
        i = 0
        while i < len(citations):
            if i+1 > citations[i]: break
            i+= 1                
        return i