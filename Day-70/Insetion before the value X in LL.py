# Definition of singly linked list:
# class ListNode:
#     def __init__(self, x=0, next=None):
#         self.data = x
#         self.next = next

class Solution:
    def insertBeforeX(self, head, X, val):

        newnode = ListNode(val)

        if head is None:

            return None

        if head.data == X:

            newnode.next = head

            return newnode

        current = head

        while current.next and current.next.data != X:

            current = current.next

        if current.next is None:
            return head

        newnode.next = current.next
        current.next = newnode
    
        return head