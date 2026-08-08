class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head:
            return None

        temp = head
        n = 0

        while temp:
            n += 1
            temp = temp.next

        k = k % n

        if k == 0:
            return head

        br_p = n - k

        tempp = head

        for i in range(br_p - 1):
            tempp = tempp.next

        nxt = tempp.next
        dummy = nxt

        tempp.next = None

        while nxt.next:
            nxt = nxt.next

        nxt.next = head

        return dummy