#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 18:24:53 2021

@author: daniel
"""

class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxi = 0
        count = 0
        for x in s:
            if x == '(':
                count += 1
            if count >= maxi:
                maxi = count
            if x == ')':
                count -= 1
        return maxi
        