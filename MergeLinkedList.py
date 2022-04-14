# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, headA: ListNode, headB: ListNode) -> ListNode:
        if (headA == None) | (headB == None):
            if (headA == None):
                return headB
            else:
                return headA

        if headA.val > headB.val:  # headA points to the smaller one
            temp = headA
            headA = headB
            headB = temp
        head = headA
        curA = headA.next  # curA one step ahead
        curB = headB
        while (curA != None) & (curB != None):
            if (curA.val >= curB.val):
                headB = headB.next
                curB.next = curA
                headA.next = curB
                headA = curA
                curA = curA.next
                curB = headB
            else:
                headA = curA
                curA = curA.next
        if curA == None:
            headA.next = headB
        return head


s = Solution()
l1 = ListNode(val=2)
l1.next = ListNode(val=3)

l2 = ListNode(val=4)
l2.next = ListNode(val=2)
n = s.mergeTwoLists(l1, l2)

def testMerge(node):
    expected = []
    while node:
        expected.append(node.val)
        node = node.next
    print(expected)

testMerge(n)



