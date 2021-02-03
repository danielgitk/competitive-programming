#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 17:30:07 2021

@author: daniel
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if not root:
            return 0        
        else:
            if low <= root.val <= high:
                return root.val + self.rangeSumBST(root.left,low,high) + self.rangeSumBST(root.right,low,high)
            else:
                return 0 + self.rangeSumBST(root.left,low,high) + self.rangeSumBST(root.right,low,high)
        