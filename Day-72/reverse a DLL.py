# class ListNode:
#     def __init__(self, data):
#         self.data = data
#         self.prev = None
#         self.next = None

class Solution:
    def reverseDLL(self, head):

        current = head
        
        while current:
            current.prev, current.next = current.next, current.prev

            head = current
            current = current.prev

        return head