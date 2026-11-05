# Definition of singly linked list:
# class ListNode:
#     def __init__(self, x=0, next=None):
#         self.data = x
#         self.next = next

class Solution:
    def insertAtHead(self, head, X):
      newNode = ListNode(X)

      newNode.next = head

      return newNode
    