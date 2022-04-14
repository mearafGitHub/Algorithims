class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, one: Optional[ListNode], two: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        head = dummy
        carry = 0
        while one or two:
            p = one.val if one else 0
            q = two.val if two else 0
            res = p + q + carry
            carry = res // 10
            res = res % 10
            head.next = ListNode(res)

            head = head.next
            one = one.next if one else None
            two = two.next if two else None

        while carry > 0:
            head.next = ListNode(carry % 10)
            head.next
            carry = carry // 10

        return dummy.next
