# Definition of singly linked list:
# class ListNode:
#     def __init__(self, x=0, next=None):
#         self.data = x
#         self.next = next

class Solution:
    def deleteKthNode(self, head, k):

        current = head

        if head is None:

            return None

        if k == 1:

            return head.next

        for i in range(k - 2):

            current = current.next

        current.next = current.next.next

        return head