class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        if not obstacleGrid:
            return 0

        n = len(obstacleGrid)
        m = len(obstacleGrid[0])

        dp = [[0] * m for _ in range(n)]

        # Destination itself is blocked
        if obstacleGrid[n-1][m-1] == 1:
            return 0

        # Last column
        for i in range(n-1, -1, -1):
            if obstacleGrid[i][m-1] == 1:
                break
            dp[i][m-1] = 1

        # Last row
        for j in range(m-1, -1, -1):
            if obstacleGrid[n-1][j] == 1:
                break
            dp[n-1][j] = 1

        # DP
        for i in range(n-2, -1, -1):
            for j in range(m-2, -1, -1):

                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i+1][j] + dp[i][j+1]

        return dp[0][0]