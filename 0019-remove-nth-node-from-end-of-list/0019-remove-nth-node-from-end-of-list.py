# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        length = 0

        temp = head

        while temp:
            length += 1
            temp = temp.next

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy

        for _ in range(length - n):
            prev = prev.next

        prev.next = prev.next.next

        return dummy.next