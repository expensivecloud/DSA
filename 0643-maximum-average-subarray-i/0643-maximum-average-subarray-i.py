class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        n = len(nums)

        i = 0
        j = 0
        sumo = 0
        max_sum = float('-inf')

        while j < n:
            sumo += nums[j]

            if j - i + 1 == k:
                if sumo > max_sum:
                    max_sum = sumo

                sumo -= nums[i]
                i += 1

            j += 1

        return float(max_sum) / k