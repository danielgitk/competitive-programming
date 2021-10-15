#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 18:39:33 2021

@author: daniel
"""

class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        t0 = 0
        t1 = 1
        t2 = 1
        if n == 0: return 0
        if n == 1 or n == 2: return 1
        
        for i in range(n-2):
            trib = t0
            t0 = t1
            t1 = t2
            t2 = t1 + t0 + trib
        return t2
            