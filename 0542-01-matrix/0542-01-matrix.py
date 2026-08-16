from collections import deque

class Solution(object):
    def updateMatrix(self, mat):
        n = len(mat)
        m = len(mat[0])

        dist = [[-1] * m for _ in range(n)]
        q = deque()

        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        # Start BFS from every 0
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    q.append((i, j))

        # One BFS
        while q:
            x, y = q.popleft()

            for dx, dy in dirs:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < n and 0 <= ny < m and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

        return dist