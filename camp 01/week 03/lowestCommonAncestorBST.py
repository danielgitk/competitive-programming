#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 17:49:30 2021

@author: daniel
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode': 
        if p.val < q.val:
            return self.recursive(root,p,q)
        else:
            return self.recursive(root,q,p) 
    
    def recursive(self, root, p , q):
        if not root:
            return            
        if p.val <= root.val and q.val>= root.val:
            return root
        if p.val>= root.val and q.val >= root.val:
            return self.recursive(root.right,p,q)
        if p.val<= root.val and q.val <= root.val:
            return self.recursive(root.left,p,q)
        
        
        
        
        
        