# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):

        def merge(a, b):

            dummy = ListNode(0)
            current = dummy

            while a and b:

                if a.val < b.val:
                    current.next = a
                    a = a.next

                else:
                    current.next = b
                    b = b.next

                current = current.next

            if a:
                current.next = a

            if b:
                current.next = b

                #current.next = list1 if list1 else list2

            return dummy.next

        
        if not lists:
            return None

        interval = 1
        
        while interval < len(lists):

            for i in range(0,len(lists) - interval,2*interval):

                lists[i] = merge(lists[i], lists[i + interval])
 
            interval *= 2

        return lists[0]