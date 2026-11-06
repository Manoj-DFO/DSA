class Solution:
    def deleteTail(self, head):

        if head is None:
            return None

        if head.next is None:
            return None

        current = head

        while current.next:
            current = current.next

        current.prev.next = None

        return head