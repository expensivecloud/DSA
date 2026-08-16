from collections import deque

class Solution(object):
    def numIslands(self, grid):
        n = len(grid)
        m = len(grid[0])

        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        islands = 0

        for i in range(n):
            for j in range(m):

                if grid[i][j] == "1":

                    islands += 1

                    grid[i][j] = "0"
                    q = deque([(i, j)])

                    while q:
                        x, y = q.popleft()

                        for dx, dy in dirs:
                            nx = x + dx
                            ny = y + dy

                            if (0 <= nx < n and
                                0 <= ny < m and
                                grid[nx][ny] == "1"):

                                grid[nx][ny] = "0"
                                q.append((nx, ny))

        return islands