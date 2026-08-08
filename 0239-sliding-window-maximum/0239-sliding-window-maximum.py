from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        n = len(nums)

        i = 0
        j = 0

        dq = deque()
        ans = []

        while j < n:

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
                while dq and dq[0] < i:
                    dq.popleft()

                # Front contains maximum
                ans.append(nums[dq[0]])

                # Slide window
                i += 1
                j += 1

        return ans