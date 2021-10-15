#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 17:50:34 2021

@author: daniel
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        arr = []        
        self.recursive(root,arr)
        return min(arr[i]-arr[i-1] for i in range(1,len(arr)))     
        
    def recursive(self,root, arr):
        if not root:
            return
        self.recursive(root.left,arr)
        arr.append(root.val)
        self.recursive(root.right,arr)
        
        
        
        
        
        
        
        