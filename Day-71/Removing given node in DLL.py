"""
# Definition for a Node.
class ListNode:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
"""

class Solution:
    def deleteGivenNode(self, node: ListNode) -> None:
        
        if node.prev:
            node.prev.next = node.next
            
        if node.next:
            node.next.prev = node.prev