#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 17:37:47 2021

@author: daniel
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,root,val):       
        if val < root.val and not root.left:
            root.left = TreeNode(val)
            return root
        if val > root.val and not root.right:
            root.right = TreeNode(val)
            return root
        if val < root.val:
            return self.helper(root.left, val)
        if val > root.val:
            return self.helper(root.right,val)
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        self.helper(root,val)
        return root