#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 22:31:45 2021

@author: daniel
"""

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        n = len(T)
        output, stack = [0]*n,[]
        for i in range(n-1,-1,-1):
            if not stack:
                stack.append(i)
            else:
                while stack and T[stack[-1]] <= T[i]:
                    stack.pop()
                output[i] = stack[-1] - i if  stack else 0
                stack.append(i)
        return output