import heapq

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        i, j = 0, 0
        n = len(nums)

        heap = []
        res = []

        while j < n:

            heapq.heappush(heap, (-nums[j], j))

            if j - i + 1 < k:
                j += 1

            elif j - i + 1 == k:

                # Remove elements that are outside the window
                while heap and heap[0][1] < i:
                    heapq.heappop(heap)

                # Maximum
                res.append(-heap[0][0])

                i += 1
                j += 1

        return res