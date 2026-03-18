class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        l3 = ListNode()
        n1 = l3
        carry = 0
        while l1 or l2 or carry:
            digit = 0
            tot = carry
            if l1 is not None:
                tot += l1.val
                l1 = l1.next

            if l2 is not None:
                tot += l2.val
                l2 = l2.next

            digit = tot % 10
            carry = tot // 10

            newNode = ListNode(digit)
            n1.next = newNode
            n1 = n1.next
        
        l3 = l3.next
        return l3