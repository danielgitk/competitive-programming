#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 17:47:04 2021

@author: daniel
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        ind = nums.index(max(nums))
        val = TreeNode(nums[ind])
        left = nums[:ind]
        right = nums[ind+1:]
        val.left = self.constructMaximumBinaryTree(left)
        val.right = self.constructMaximumBinaryTree(right)
        return val
        
        