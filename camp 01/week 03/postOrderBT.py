#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 17:39:46 2021

@author: daniel
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        arr = []
        self.recursive(root,arr)
        return arr
        

        
    def recursive(self, root:TreeNode, arr):
        if not root:
            return        
        self.recursive(root.left,arr)
        self.recursive(root.right,arr)
        arr.append(root.val)