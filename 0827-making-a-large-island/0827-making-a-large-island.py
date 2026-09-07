class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        n = len(grid)

        parent = list(range(n * n))
        size = [1] * (n * n)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            pa = find(a)
            pb = find(b)

            if pa == pb:
                return

            if size[pa] < size[pb]:
                pa, pb = pb, pa

            parent[pb] = pa
            size[pa] += size[pb]

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for i in range(n):
            for j in range(n):

                if grid[i][j] == 0:
                    continue

                curr = i * n + j

                for dx, dy in dirs:
                    ni = i + dx
                    nj = j + dy

                    if 0 <= ni < n and 0 <= nj < n:
                        if grid[ni][nj] == 1:

                            neighbor = ni * n + nj
                            union(curr, neighbor)

        ans = 0

        for i in range(n):
            for j in range(n):

                if grid[i][j] == 1:
                    root = find(i * n + j)
                    ans = max(ans, size[root])

        for i in range(n):
            for j in range(n):

                if grid[i][j] == 1:
                    continue

                total = 1
                seen = set()

                for dx, dy in dirs:
                    ni = i + dx
                    nj = j + dy

                    if 0 <= ni < n and 0 <= nj < n:

                        if grid[ni][nj] == 1:

                            root = find(ni * n + nj)

                            if root not in seen:
                                seen.add(root)
                                total += size[root]

                ans = max(ans, total)

        return ans