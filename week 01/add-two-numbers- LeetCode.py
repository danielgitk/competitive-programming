#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 17:16:36 2020

@author: daniel
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        final = result
        carry = 0
        while l1 or l2:  
            x = (l1.val if l1 else 0)
            y = (l2.val if l2 else 0)
            sum1 = x + y + carry  
            carry = sum1 // 10
            rem = sum1 % 10               
            somenode = ListNode(rem) 
            final.next = somenode
            final = final.next     
            if (l1 != None): l1 = l1.next
            if (l2 != None): l2 = l2.next
            
        if carry:
            final.next = ListNode(carry)
        return result.next
            
            