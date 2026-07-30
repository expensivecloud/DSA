# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        pal_str = ""

        while head:
            pal_str += str(head.val)
            head = head.next

        return pal_str == pal_str[::-1]

        