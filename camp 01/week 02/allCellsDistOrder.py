#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 10:50:31 2021

@author: daniel
"""

class Solution(object):
    def allCellsDistOrder(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        dicti = {}
        answer = []
        for i in range(R):
            for j in range(C):
                lend = abs(r0-i)+abs(c0-j)        
                dicti[(i,j)] = lend
        sorted_x = sorted(dicti.items(), key=lambda kv: kv[1])

        for x in sorted_x:
            answer.append(list(x[0]))
        return answer
        
        