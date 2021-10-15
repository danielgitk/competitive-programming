#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 23:04:10 2021

@author: daniel
"""

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = []

    def push(self, x):
        self.stack.append(x)
        if x <= self.getMin():
            self.min.append(x)
        return x

    def pop(self):
        if self.stack.pop() == self.getMin():
            self.min.pop()

    def top(self):
        return self.stack[-1]


    def getMin(self):
        try:
            return self.min[-1]
        except IndexError:
            return self.top()

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()