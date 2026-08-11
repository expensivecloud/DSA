class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [-1] * n

        dp[0] = 0
        dp[1] = 1

        for i in range(2,n):
            dp[i] = max(dp[i-1],dp[i-2])

        return dp[n-1]