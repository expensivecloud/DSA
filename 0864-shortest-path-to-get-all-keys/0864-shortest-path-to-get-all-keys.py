from collections import deque

class Solution(object):
    def shortestPathAllKeys(self, grid):
        n = len(grid)
        m = len(grid[0])

        keys = ['a', 'b', 'c', 'd', 'e', 'f']
        locks = ['A', 'B', 'C', 'D', 'E', 'F']

        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        # Find starting point and number of keys
        total_keys = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '@':
                    start = (i, j)

                if grid[i][j] in keys:
                    total_keys += 1

        q = deque([(start[0], start[1], "")])
        visited = set([(start[0], start[1], "")])

        steps = 0

        while q:

            for _ in range(len(q)):
                x, y, collected = q.popleft()

                if len(collected) == total_keys:
                    return steps

                for dx, dy in dirs:
                    nx = x + dx
                    ny = y + dy

                    if not (0 <= nx < n and 0 <= ny < m):
                        continue

                    c = grid[nx][ny]

                    if c == '#':
                        continue

                    new_collected = collected

                    if c in keys:
                        if c not in collected:
                            new_collected += c

                    if c in locks:
                        required_key = c.lower()

                        if required_key not in collected:
                            continue

                    state = (nx, ny, new_collected)

                    if state not in visited:
                        visited.add(state)
                        q.append(state)

            steps += 1

        return -1