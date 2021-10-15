#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 14:29:35 2021

@author: daniel
"""

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.toSaveOn = []
        self.toHelp = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.toSaveOn.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        while self.toSaveOn:
            self.toHelp.append(self.toSaveOn.pop())
        answer = self.toHelp.pop()
        while self.toHelp:
            self.toSaveOn.append(self.toHelp.pop())
        return answer
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        while self.toSaveOn:
            self.toHelp.append(self.toSaveOn.pop())
        answer = self.toHelp[-1]
        while self.toHelp:
            self.toSaveOn.append(self.toHelp.pop())
        return answer
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.toSaveOn
        