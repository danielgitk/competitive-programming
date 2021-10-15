# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k < 2:return head
        current = head
        for _ in range(k):
            if not current:
                return head
            current = current.next
        
        prev = self.reverseKGroup(current,k)
        for _ in range(k):
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev