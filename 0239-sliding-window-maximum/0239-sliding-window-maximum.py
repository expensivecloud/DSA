import heapq

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

        heap = []
        ans = []

        while j < n:

            # Add current element to max heap
            heapq.heappush(heap, (-nums[j], j))

            # Window size < k
            if j - i + 1 < k:
                j += 1

            # Window size == k
            elif j - i + 1 == k:

                # Remove elements outside the window
                while heap and heap[0][1] < i:
                    heapq.heappop(heap)

                # Maximum is at top
                ans.append(-heap[0][0])

                # Slide window
                i += 1
                j += 1

        return ans