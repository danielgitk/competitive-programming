# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        queue = deque()
        if not root:return
        queue.append(root)
        while queue:            
                c = queue.pop() 
                if c.right is not None: queue.appendleft(c.right)
                if c.left is not None: queue.appendleft(c.left)
        return c.val