#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 12:56:53 2021

@author: daniel
"""

class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        l= max(weights)
        r= sum(weights)
        while l<r:
            mid = l + (r-l)//2
            val = self.possibleCapacity(weights, mid)
            if val > D:
                l = mid + 1
            else:
                r = mid
        return l       
    def possibleCapacity(self,arr, k):
        counter = 1
        sum = 0
        for i in arr:
            if sum + i <= k:
                sum += i
            else:
                counter += 1
                sum = i
        return counter 