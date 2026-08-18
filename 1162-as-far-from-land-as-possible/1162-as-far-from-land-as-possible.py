from collections import deque

class Solution(object):
    def maxDistance(self, grid):
        n = len(grid)
        m = len(grid[0])

        q = deque()

        # Start BFS from every land cell
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    q.append((i, j))

        # All land or all water
        if len(q) == 0 or len(q) == n * m:
            return -1

        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        dist = -1

        while q:
            for _ in range(len(q)):
                x, y = q.popleft()

                for dx, dy in dirs:
                    nx = x + dx
                    ny = y + dy

                    if (0 <= nx < n and
                        0 <= ny < m and
                        grid[nx][ny] == 0):

                        grid[nx][ny] = 1
                        q.append((nx, ny))

            dist += 1

        return dist