# Definition of singly linked list:
# class ListNode:
#     def __init__(self, x=0, next=None):
#         self.data = x
#         self.next = next

class Solution:
    def insertAtKthPosition(self, head, X, k):

        newnode = ListNode(X)
        if k == 1:

            newnode.next = head

            return newnode

        current = head

        for _ in range(k - 2):

            current = current.next

        newnode.next = current.next
        current.next = newnode

        return head