#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 17:54:48 2021

@author: daniel
"""

class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        dicti = {}
        answer = []
        for x,y in points:
            dicti[x,y] = x**2 + y**2       
        c = sorted(dicti.items(), key=lambda kv: kv[1])
        j = 1
        for i in c:
            answer.append(list(i[0]))
            if j>= K:
                break
            j+=1

            
        return answer
        
            
        