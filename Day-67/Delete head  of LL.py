def deleteHead(head):
    if head is None:
        return None

    temp = head
    head = head.next
    del temp

    return head