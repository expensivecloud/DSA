from collections import deque

class Solution(object):
    def numEnclaves(self, grid):
        n = len(grid)
        m = len(grid[0])

        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        q = deque()

        for i in range(n):
            if grid[i][0] == 1:
                q.append((i, 0))
                grid[i][0] = 0

            if grid[i][m - 1] == 1:
                q.append((i, m - 1))
                grid[i][m - 1] = 0

        for j in range(m):
            if grid[0][j] == 1:
                q.append((0, j))
                grid[0][j] = 0

            if grid[n - 1][j] == 1:
                q.append((n - 1, j))
                grid[n - 1][j] = 0

        while q:
            x, y = q.popleft()

            for dx, dy in dirs:
                nx = x + dx
                ny = y + dy

                if (0 <= nx < n and
                    0 <= ny < m and
                    grid[nx][ny] == 1):

                    grid[nx][ny] = 0
                    q.append((nx, ny))

        ans = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    ans += 1

        return ans