#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 17:41:13 2021

@author: daniel
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if p and q:
            if p.val != q.val:
                return False                
            else:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right,q.right)
                
        else:
            return False
        