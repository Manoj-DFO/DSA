class Solution(object):
    def detectCycle(self, head):

        slow = head
        fast = head

        # Find meeting point
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        else:
            return None

        # Find cycle starting point
        slow = head

        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow