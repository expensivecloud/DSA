from collections import deque

class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        n = len(grid)
        m = len(grid[0])

        # Start or end is blocked
        if grid[0][0] == 1 or grid[n-1][m-1] == 1:
            return -1

        dirs = [
            (1, 0), (1, 1), (0, 1), (-1, 0),
            (0, -1), (1, -1), (-1, -1), (-1, 1)
        ]

        q = deque([(0, 0)])
        visited = [[False] * m for _ in range(n)]
        visited[0][0] = True

        steps = 1

        while q:

            for _ in range(len(q)):
                x, y = q.popleft()

                if x == n - 1 and y == m - 1:
                    return steps

                for dx, dy in dirs:
                    nx = x + dx
                    ny = y + dy

                    if (0 <= nx < n and
                        0 <= ny < m and
                        visited[nx][ny] == False and
                        grid[nx][ny] == 0):

                        visited[nx][ny] = True
                        q.append((nx, ny))

            steps += 1

        return -1