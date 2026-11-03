# Definition of singly linked list:
# class ListNode:
#     def __init__(self, x=0, next=None):
#         self.data = x
#         self.next = next

class Solution:
    def deleteNodeWithValueX(self, head, X):

        current = head

        if head is None:
            return None

        if head.data == X:
            return head.next

        while current.next and current.next.data != X:

            current = current.next

        if current.next:
            
            current.next = current.next.next

        return head