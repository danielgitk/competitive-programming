#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 18:24:03 2021

@author: daniel
"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dicti = {}        
        for i in s:
            if i in dicti:
                dicti[i] += 1
            else:
                dicti[i] = 1
        for j in t:
            if j not in dicti:
                return False
            else:
                if dicti[j] != 0:
                    dicti[j] -= 1
                else:
                    return False                
        for i,j in dicti.items():
            if j != 0:
                return False
        return True