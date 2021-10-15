#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 22:27:09 2021

@author: daniel
"""

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        current = head
        final = None
        while current:
            next = current.next
            final = self.insert(final,current)
            current = next
        head = final
        return head
    def insert(self,head,new):
        current = None
        if not head or (head.val >= new.val):
            new.next = head
            head = new
        else:
            current = head
            while current.next and current.next.val < new.val:
                current = current.next
            new.next = current.next
            current.next = new
        return head