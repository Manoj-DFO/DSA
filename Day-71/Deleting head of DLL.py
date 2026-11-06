"""
# Definition for a Node.
class ListNode:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
"""

class Solution:
    def deleteHead(self, head: ListNode) -> ListNode:
        
        if head is None:
            return None

        head = head.next

        if head:
            head.prev = None
        
        return head