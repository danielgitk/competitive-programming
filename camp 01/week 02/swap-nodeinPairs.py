#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 22:34:20 2021

@author: daniel
"""

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        current = head
        while current and current.next:
            now = current.val 
            current.val = current.next.val
            current.next.val = now
            current = current.next.next
        return head