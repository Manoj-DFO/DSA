"""
# Definition for a Node.
class ListNode:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
"""

class Solution:
    def insertBeforeTail(self, head: ListNode, X: int) -> ListNode:
        
        newnode = ListNode(X)

        if head.next is None:
            head.prev = newnode
            newnode.next = head
            return newnode

        current = head

        while current.next.next:
            current = current.next

        newnode.next = current.next
        newnode.prev = current
    
        current.next.prev = newnode
        current.next = newnode

        return head