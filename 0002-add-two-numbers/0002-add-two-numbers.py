# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):

        num1 = []
        num2 = []

        # Store digits
        while l1:
            num1.append(str(l1.val))
            l1 = l1.next

        while l2:
            num2.append(str(l2.val))
            l2 = l2.next

        num1 = num1[::-1]
        num2 = num2[::-1]

        n1 = int("".join(num1))
        n2 = int("".join(num2))

        total = n1 + n2

        digits = list(str(total))[::-1]

        dummy = ListNode(0)
        curr = dummy

        for d in digits:
            curr.next = ListNode(int(d))
            curr = curr.next

        return dummy.next