# Definition of singly linked list:
# class ListNode:
#     def __init__(self, x=0, next=None):
#         self.data = x
#         self.next = next

class Solution:
    def deleteTail(self, head):

        current = head

        if current is None or current.next is None:

            return None

        while current.next.next:

            current = current.next

        current.next = None

        return head

            