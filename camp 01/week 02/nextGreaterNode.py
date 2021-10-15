#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 22:31:22 2021

@author: daniel
"""

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        current = head
        array = []
        while current:
            array.append(current.val)
            current = current.next
        print(array)
        output = [0]*len(array)
        stack = []
        for i in range(len(array)):
            while stack and array[stack[-1]] < array[i]:
                output[stack.pop()] = array[i]
            stack.append(i)
        return output