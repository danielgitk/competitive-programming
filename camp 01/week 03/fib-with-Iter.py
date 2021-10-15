#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 17:49:44 2021

@author: daniel
"""
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        f0 = 0
        f1 = 1
        if n == 0:
            return 0
        for i in range(n-1):
            f = f0 + f1
            f0 = f1
            f1 = f        
        return f1
            