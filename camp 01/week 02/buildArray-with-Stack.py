#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 18:49:35 2021

@author: daniel
"""

class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        output = []
        n = max(target)
        tracker = [i for i in range(1,n+1)]
        for i in tracker:
            if i not in target:
                output.append("Push")
                output.append("Pop")
            else:
                output.append("Push")
        return output
            
            
                