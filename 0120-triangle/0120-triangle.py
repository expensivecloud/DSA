class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """

        dp = []
        n = len(triangle)

        for i in range(n):
            dp.append([-1] * (i + 1))

        for i in range(n):
            dp[n-1][i] = triangle[n-1][i]

        for i in range(n-2, -1, -1):
            for j in range(len(triangle[i])):
                dp[i][j] = triangle[i][j] + min(
                    dp[i+1][j],
                    dp[i+1][j+1]
                )

        return dp[0][0]