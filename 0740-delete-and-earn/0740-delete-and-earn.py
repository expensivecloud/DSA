class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = max(nums)

        points = [0] * (n + 1)

        for num in nums:
            points[num] += num

        dp = [0] * (n + 1)

        dp[0] = 0

        if n >= 1:
            dp[1] = points[1]

        for i in range(2, n + 1):
            dp[i] = max(
                points[i] + dp[i-2],
                dp[i-1]
            )

        return dp[n]