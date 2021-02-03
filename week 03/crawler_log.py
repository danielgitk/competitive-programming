#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 17:12:11 2021

@author: daniel
"""
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ans = 0
        for i in logs:
            if i == "./": continue
            elif i == "../":
                ans -= 1
            else:
                ans += 1
            if ans < 0:
                ans = 0
        return ans
        

