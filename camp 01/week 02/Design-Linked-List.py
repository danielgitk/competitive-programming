#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 16:26:48 2021

@author: daniel
"""

class Node():
    def __init__(self,val=None):
        self.val = val


class MyLinkedList(object):

    def __init__(self,head=None):
        """
        Initialize your data structure here.
        """
        self.head = head
        self.size = 0
        
        

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index <0 or index>=self.size:
            return -1
        current = self.head
        i = 0
        while current:
            if i == index:
                return current.val
            current = current.next
            i += 1
        
            
        

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        current = self.head
        newNode = Node(val)
        newNode.next = current
        self.head = newNode
        self.size += 1

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        newNode = Node(val)
        newNode.next = None
        if not self.head:
            self.head = newNode
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
        self.size += 1
        

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        if index > self.size:return
        newNode = Node(val)
        current = self.head

        i = 0
        if index == 0:
            newNode.next = current
            self.head = newNode
        else:
            while i<index-1:
                current = current.next
                i+= 1
            newNode.next = current.next
            current.next = newNode
        self.size += 1
            
                
        

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        if index <0 or index>=self.size:
            return
          
        current = self.head
        if index == 0:
            self.head = self.head.next
        else:
            for i in range(index-1):
                current = current.next
            new = current.next.next
            current.next = None
            current.next = new
        self.size -= 1
            
                
            

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)