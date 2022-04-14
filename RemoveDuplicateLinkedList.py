class Node:
    def __init__(self, val, ):
        self.val = val
        self.next = None


class Solution:
    def noDuplicate(self, head):
        if not head:
            return None

        def removeDup(head):
            cur = head
            while cur:
                nxtNode = cur.next
                if nxtNode.next:
                    if cur.val == nxtNode.val:
                        cur.next = nxtNode.next.next
                    cur = nxtNode
                else:
                    break
            data = []
            nxt = head
            while nxt:
                data.append(nxt.val)
                nxt = nxt.next
            return (data, head)

        return removeDup(head)


head = Node(3)
head.next = Node(4)
head.next.next = Node(1)
head.next.next.next = Node(2)
head.next.next.next.next = Node(15)
head.next.next.next.next.next = Node(-5)
head.next.next.next.next.next.next = Node(-5)
head.next.next.next.next.next.next.next = Node(-5)
dup = Solution()

print('Updated Linked List and a list and Head:  \n', dup.noDuplicate(head))
