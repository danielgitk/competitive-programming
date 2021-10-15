#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 18:54:05 2021

@author: daniel
"""

class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        final = [S[0]]
        for x in range(1,len(S)):
            if final and (final[-1] == S[x]) :
                final.pop()
            else:
                final.append(S[x])               
        return "".join(final)
            
            