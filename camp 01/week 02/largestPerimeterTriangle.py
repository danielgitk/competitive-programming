#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 18:11:30 2021

@author: daniel
"""

class Solution(object):
    def isPossible(self,side1,side2,side3):
        if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
            return True
        else:
            return False
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A = sorted(A,reverse=True)
        for i in range(len(A)-2):
            if self.isPossible(A[i],A[i+1],A[i+2]):
                return A[i]+A[i+1]+A[i+2]
        return 0
        
        
    
    
        