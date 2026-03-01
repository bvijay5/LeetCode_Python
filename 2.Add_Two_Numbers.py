class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0
        n1 = l1
        n2 = l2

        newNode = ListNode()
        n3 = newNode
        
        while n1 or n2 or carry:
            tot = 0
            if n1 is not None:
                tot += n1.val
                n1 = n1.next

            if n2 is not None:
                tot += n2.val
                n2 = n2.next

            tot += carry

            if tot>9:
                carry = tot // 10
            else:
                carry = 0

            digit = tot % 10


            n3.next = ListNode(digit)
            n3 = n3.next
        
        newNode = newNode.next

        return newNode