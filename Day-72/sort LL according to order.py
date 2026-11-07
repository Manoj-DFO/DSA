class Solution:
    def sortList(self, head):

        count0 = count1 = count2 = 0
        current = head

        while current:

            if current.data == 0:
                count0 += 1

            if current.data == 1:
                count1 += 1

            if current.data == 2:
                count2 += 1

            current = current.next

        current = head

        while current:

            if count0 > 0:
                current.data = 0
                count0 -= 1

            elif count1 > 0:
                current.data = 1
                count1 -= 1

            elif count2 > 0:
                current.data = 2
                count2 -=1 
            
            current = current.next

        return head