import heapq

class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        n = len(grid)
        m = len(grid[0])

        visited = [[False] * m for _ in range(n)]
        visited[0][0] = True

        dirs = [(0,1), (1,0), (0,-1), (-1,0)]

        pq = [(grid[0][0], 0, 0)]

        while pq:

            time, x, y = heapq.heappop(pq)

            if x == n - 1 and y == m - 1:
                return time

            for dx, dy in dirs:

                nx = x + dx
                ny = y + dy

                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:

                    visited[nx][ny] = True

                    new_time = max(time, grid[nx][ny])

                    heapq.heappush(pq, (new_time, nx, ny))