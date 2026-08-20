from collections import deque

class Solution(object):
    def minimumObstacles(self, grid):

        n = len(grid)
        m = len(grid[0])

        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        dist = [[float('inf')] * m for _ in range(n)]
        dist[0][0] = 0

        dq = deque([(0, 0)])

        while dq:

            x, y = dq.popleft()

            for dx, dy in dirs:

                nx = x + dx
                ny = y + dy

                if 0 <= nx < n and 0 <= ny < m:

                    new_dist = dist[x][y] + grid[nx][ny]

                    if new_dist < dist[nx][ny]:

                        dist[nx][ny] = new_dist

                        if grid[nx][ny] == 0:
                            dq.appendleft((nx, ny))
                        else:
                            dq.append((nx, ny))

        return dist[n-1][m-1]