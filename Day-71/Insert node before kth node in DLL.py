"""
# Definition for a Node.
class ListNode:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
"""

class Solution:
    def insertBeforeKthPosition(self, head: ListNode, X: int, K: int) -> ListNode:

        newnode = ListNode(X)

        if head is None:
            return None

        if K == 1:
            head.prev = newnode
            newnode.next =  head
            return newnode
        
        current = head
        count = 1

        while current.next and count < K:
            current = current.next
            count += 1

        newnode.prev = current.prev
        newnode.next = current

        current.prev.next = newnode
        current.prev = newnode

        return head