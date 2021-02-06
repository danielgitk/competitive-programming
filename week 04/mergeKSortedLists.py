#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 12:51:48 2021

@author: daniel
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = ListNode()
        current = head
        heap = []
        for i,node in enumerate(lists):
            if node:
                heapq.heappush(heap,(node.val,i))
        while heap:
            val,index = heapq.heappop(heap)
            current.next = ListNode(val)
            current = current.next
            if lists[index]:
                lists[index] = lists[index].next
                if lists[index]:
                    heapq.heappush(heap,(lists[index].val, index))
        return head.next
            