from collections import deque

class Solution(object):
    def maxAreaOfIsland(self, grid):

        n = len(grid)
        m = len(grid[0])

        visited = [[-1] * m for _ in range(n)]
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        max_ar = 0

        for i in range(n):
            for j in range(m):

                if grid[i][j] == 1 and visited[i][j] == -1:

                    q = deque([(i, j)])
                    visited[i][j] = 1
                    ar = 1

                    while q:
                        x, y = q.popleft()

                        for dx, dy in dirs:

                            nx = x + dx
                            ny = y + dy

                            if (0 <= nx < n and
                                0 <= ny < m and
                                grid[nx][ny] == 1 and
                                visited[nx][ny] == -1):

                                q.append((nx, ny))
                                visited[nx][ny] = 1
                                ar += 1

                    max_ar = max(max_ar, ar)

        return max_ar