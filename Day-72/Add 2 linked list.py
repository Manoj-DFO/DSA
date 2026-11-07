
class Solution:
    def addTwoNumbers(self, l1, l2):

        dummy = ListNode(0)
        current = dummy

        carry = 0

        while l1 or l2 or carry:

            val1 = l1.data if l1 else 0
            val2 = l2.data if l2 else 0

            tot = val1 + val2 + carry

            add = tot % 10
            carry = tot // 10

            current.next = ListNode(add)
            current = current.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return dummy.next