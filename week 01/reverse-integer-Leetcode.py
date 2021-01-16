#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 08:42:48 2021

@author: daniel
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        number = str(x)
        reversed = ''
        if number[0] == '-':
            reversed = '-'
            number = number[1:]
        for i in range(len(number)):
            reversed = reversed+number[-i-1]
        if int(reversed) <= pow(-2,31) or int(reversed) >= (pow(2,31) -1):
            reversed = 0
        return int(reversed)
            