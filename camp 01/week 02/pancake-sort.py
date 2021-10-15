#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 00:08:15 2021

@author: daniel
"""
class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        flips = []
        i = len(arr)
        while i > 1:
            if i == arr[i-1]:
                i -= 1
            else:
                ind = self.getIndex(arr,i)
                self.flip(arr,ind)
                flips.append(ind+1)
                self.flip(arr,i-1)
                flips.append(i)
        return flips                       
    def getIndex(self,arr,num):
        for i in range(len(arr)):
            if arr[i] == num:
                return i
        
    def flip(self,arr,i):
        leng = len(arr[:i+1])
        const = leng//2
        i = 0
        while i < const:
            arr[i],arr[leng-i-1] = arr[leng-i-1],arr[i]
            i += 1
        return arr
            
        
        
        
        
        
        
        