import heapq

class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """

        heap = []
        n = len(score)

        # Put (-score, original_index) into heap
        for i in range(n):
            heapq.heappush(heap, (-score[i], i))

        ans = [""] * n

        rank = 1

        while heap:

            neg_score, index = heapq.heappop(heap)

            if rank == 1:
                ans[index] = "Gold Medal"

            elif rank == 2:
                ans[index] = "Silver Medal"

            elif rank == 3:
                ans[index] = "Bronze Medal"

            else:
                ans[index] = str(rank)

            rank += 1

        return ans