class Solution:
    def deleteKthElement(self, head: ListNode, k: int) -> ListNode:

        if head == None:
            return None

        current = head
        count = 1

        while current.next and count < k:
            current = current.next
            count += 1

        if current.prev:
            current.prev.next = current.next

        else:
            head = current.next

        if current.next:
            current.next.prev = current.prev

        return head 