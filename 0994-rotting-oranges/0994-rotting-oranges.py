from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        n = len(grid)
        m = len(grid[0])

        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        fresh = 0
        q = deque()

        # Add all rotten oranges
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i, j))

        mins = 0

        while q and fresh > 0:

            # Process all oranges at the current minute
            for _ in range(len(q)):

                x, y = q.popleft()

                for dx, dy in dirs:
                    nx = x + dx
                    ny = y + dy

                    if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh -= 1
                        q.append((nx, ny))

            mins += 1

        if fresh > 0:
            return -1

        return mins