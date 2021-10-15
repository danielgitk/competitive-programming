#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 22:10:02 2021

@author: daniel
"""

class Solution:
    def reorganizeString(self, S: str) -> str:
        length = len(S)
        counts = [0] * 26
        index = -1
        maxCount= 0
        output = [0]*length
        for char in S:
            toChar = ord(char)-ord('a')
            counts[toChar] += 1
            if maxCount < counts[toChar]:
                maxCount = counts[toChar]
                index = toChar
        if maxCount > (length + 1) // 2: return ""
        ind = 0
        for j in range(counts[index]):
            if ind >= length:
                ind = 1
            output[ind] = chr(index + ord('a'))
            ind += 2
        for i in range(26):
            if i == index:
                continue
            ch = chr(i+ord('a'))
            for j in range(counts[i]):
                if(ind >=length):
                    ind = 1
                output[ind] = ch
                ind += 2
        return "".join(output)