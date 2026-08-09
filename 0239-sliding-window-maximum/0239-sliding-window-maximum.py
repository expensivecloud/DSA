from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        i = 0
        j = 0

        dq = deque()
        res = []

        while j < len(nums):

            # Remove smaller elements from the back
            while dq and nums[dq[-1]] <= nums[j]:
                dq.pop()

            # Add current index
            dq.append(j)

            # Window size < k
            if j - i + 1 < k:
                j += 1

            # Window size == k
            elif j - i + 1 == k:

                # Remove elements outside the window
                if dq[0] < i:
                    dq.popleft()

                # Maximum is at the front
                res.append(nums[dq[0]])

                # Slide window
                i += 1
                j += 1

        return res