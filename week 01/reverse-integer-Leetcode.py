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
        y = str(x)
        inte = ''
        if y[0] == '-':
            inte = '-'
            y = y[1:]
        for i in range(len(y)):
            inte = inte+y[-i-1]
        if int(inte) <= pow(-2,31) or int(inte) >= (pow(2,31) -1):
            inte = 0
        return int(inte)
            