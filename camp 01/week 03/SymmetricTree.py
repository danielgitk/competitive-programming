#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 17:41:59 2021

@author: daniel
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        q = [root]
        while q:
            vals = []
            for i in range(len(q)):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                    vals.append(node.left.val)  
                else:
                    vals.append(-1)
                if node.right:
                    q.append(node.right)
                    vals.append(node.right.val)
                else:
                    vals.append(-1)
            if vals != list(reversed(vals)):
                return False
                
        return True
        