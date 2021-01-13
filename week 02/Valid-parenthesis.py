#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 23:03:19 2021

@author: daniel
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            elif i == ')' or i == '}' or i == ']' :
                if not stack:
                    return False
                last = stack[-1]
                if (last == '{' and i=='}') or (last == '(' and i==')') or (last == '[' and i==']'):
                    stack.pop(-1)
                else:
                    return False
        if stack:
            return False
            
        return True
            
        