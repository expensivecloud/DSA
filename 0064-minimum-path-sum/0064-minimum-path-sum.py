class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        n = len(grid)
        m = len(grid[0])

        dp = [[-1] * m for _ in range(n)]

        dp[n-1][m-1] = grid[n-1][m-1]

        for j in range(m-2, -1, -1):
            dp[n-1][j] = grid[n-1][j] + dp[n-1][j+1]

        for i in range(n-2, -1, -1):
            dp[i][m-1] = grid[i][m-1] + dp[i+1][m-1]

        for i in range(n-2, -1, -1):
            for j in range(m-2, -1, -1):
                dp[i][j] = grid[i][j] + min(dp[i+1][j], dp[i][j+1])

        return dp[0][0]