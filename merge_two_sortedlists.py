"""
They are linked lists
"""

class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merger(a, b):
    dummy = ListNode()
    tail = dummy

    while a and b:
        if a.val < b.val:
            tail.next = a
            a = a.next
        else:
            tail.next = b
            b = b.next
        tail = tail.next
    if a:
        tail.next = a
    if b:
        tail.next = b

    return dummy.next
