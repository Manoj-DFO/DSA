class Solution:
    def rotateRight(self, head, k):

        if not head or not head.next or k == 0:
            return head

        l = 1
        tail = head

        while tail.next:
            tail = tail.next
            l += 1

        k = k % l

        if k == 0:
            return head

        step = l - k - 1
        newtail = head

        for _ in range(step):
            newtail = newtail.next

        newhead = newtail.next
        newtail.next = None
        tail.next = head

        return newhead