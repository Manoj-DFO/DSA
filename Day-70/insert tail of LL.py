class Solution:
    def insertAtTail(self, head, X):
        newNode = ListNode(X)

        if head is None:
            return newNode

        current = head

        while current.next is not None:
            current = current.next

        current.next = newNode

        return head