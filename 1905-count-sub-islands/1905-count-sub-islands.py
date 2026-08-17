from collections import deque

class Solution(object):
    def countSubIslands(self, grid1, grid2):
        n = len(grid1)
        m = len(grid2[0])

        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        visited = [[-1] * m for _ in range(n)]
        islands = 0

        for i in range(n):
            for j in range(m):

                # Find an unvisited island in grid2
                if grid2[i][j] == 1 and visited[i][j] == -1:

                    q = deque([(i, j)])
                    visited[i][j] = 1

                    subIsland = True

                    while q:

                        x, y = q.popleft()

                        if grid1[x][y] == 0:
                            subIsland = False

                        for dx, dy in dirs:
                            nx = x + dx
                            ny = y + dy

                            if (0 <= nx < n and
                                0 <= ny < m and
                                grid2[nx][ny] == 1 and
                                visited[nx][ny] == -1):

                                q.append((nx, ny))
                                visited[nx][ny] = 1

                    if subIsland:
                        islands += 1

        return islands