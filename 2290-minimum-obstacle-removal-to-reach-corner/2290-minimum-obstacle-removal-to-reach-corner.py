import heapq

class Solution(object):
    def minimumObstacles(self, grid):

        n = len(grid)
        m = len(grid[0])

        dist = [[float('inf')] * m for _ in range(n)]
        dist[0][0] = 0

        pq = [(0, 0, 0)]   # obstacles, x, y

        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        while pq:

            d, x, y = heapq.heappop(pq)

            if x == n - 1 and y == m - 1:
                return d

            if d > dist[x][y]:
                continue

            for dx, dy in dirs:

                nx = x + dx
                ny = y + dy

                if 0 <= nx < n and 0 <= ny < m:

                    weight = grid[nx][ny]

                    new_dist = d + weight

                    if new_dist < dist[nx][ny]:

                        dist[nx][ny] = new_dist

                        heapq.heappush(
                            pq,
                            (new_dist, nx, ny)
                        )

        return -1