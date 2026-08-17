from collections import deque

class Solution(object):
    def solve(self, board):
        if not board:
            return

        n = len(board)
        m = len(board[0])

        q = deque()

        # Left and right borders
        for i in range(n):
            if board[i][0] == "O":
                board[i][0] = "S"
                q.append((i, 0))

            if board[i][m - 1] == "O":
                board[i][m - 1] = "S"
                q.append((i, m - 1))

        # Top and bottom borders
        for j in range(m):
            if board[0][j] == "O":
                board[0][j] = "S"
                q.append((0, j))

            if board[n - 1][j] == "O":
                board[n - 1][j] = "S"
                q.append((n - 1, j))

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            x, y = q.popleft()

            for dx, dy in dirs:
                nx = x + dx
                ny = y + dy

                if (0 <= nx < n and
                    0 <= ny < m and
                    board[nx][ny] == "O"):

                    board[nx][ny] = "S"
                    q.append((nx, ny))

        for i in range(n):
            for j in range(m):

                if board[i][j] == "O":
                    board[i][j] = "X"

                elif board[i][j] == "S":
                    board[i][j] = "O"