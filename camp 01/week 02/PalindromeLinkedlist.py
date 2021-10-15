#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 18:44:00 2021

@author: daniel
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # newHead = ListNode(head.val, None )
        # new = newHead
        array = []
        current = head
        if not current or not current.next:
            return True
        while current:
            array.append(current.val)
            current = current.next
        return array == array[::-1]