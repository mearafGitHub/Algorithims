def rev(head):
    # pointers to nodes in the linked list
    curr, prev = None, None

    while curr:
        nxt_node = curr.next
        curr.next = prev
        prev = curr
        curr = nxt_node
    # the new head of the linked list is stored in prev at the last iteration
    return prev
