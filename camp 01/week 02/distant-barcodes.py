#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 17:40:06 2021

@author: daniel
"""

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:  
        dicti = {}   
        for i in barcodes:
            if i not in dicti:
                dicti[i] = 1
            else:
                dicti[i]+=1
        temp = []
        for a,b in dicti.items():
            temp.append([a,b])
        i = 0
        result = [0]*len(barcodes)
        temp = sorted(temp,key=lambda v:v[1])
        while i <len(result):
            result[i] = temp[-1][0]
            temp[-1][1]-=1
            if temp[-1][1]==0:
                temp.pop()
            i+=2
        i=1
        while i <len(result):
            result[i] = temp[-1][0]
            temp[-1][1]-=1
            if temp[-1][1]==0:
                temp.pop()
            i+=2
        return result
        