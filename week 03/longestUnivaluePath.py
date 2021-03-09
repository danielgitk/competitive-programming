# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.longer = 0
        def recursive(node):
            if not node: return 0,0
            left = max(recursive(node.left))
            right = max(recursive(node.right))
        
            left = 1 + left if node.left and node.left.val == node.val else 0
            right  = 1 + right if node.right and node.right.val == node.val else 0
        
            self.longer  = max(self.longer, left + right)
        
            return left,right
        recursive(root)
        return self.longer