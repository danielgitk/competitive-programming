#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 22:27:45 2021

@author: daniel
"""

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            try:
                x = int(i)
                stack.append(i)
            except ValueError:                
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                if i == "+":
                    stack.append(num1 + num2)
                elif i == "-":
                    stack.append(num1 - num2)
                elif i == "*":
                    stack.append(num1 * num2)
                elif i == "/":
                    stack.append(int(float(num1) / num2))
        return stack[0]
        