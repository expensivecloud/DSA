class Solution(object):
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """

        parent = list(range(n))
        size = [1] * n

        def findP(x):
            if parent[x] != x:
                parent[x] = findP(parent[x])
            return parent[x]

        def union(a, b):
            pa = findP(a)
            pb = findP(b)

            if pa == pb:
                return False

            if size[pa] < size[pb]:
                pa, pb = pb, pa

            parent[pb] = pa
            size[pa] += size[pb]

            return True

        extra = 0
        components = n

        for u, v in connections:

            if union(u, v):
                components -= 1
            else:
                extra += 1

        ans = extra - components + 1

        if ans >= 0:
            return components - 1

        return -1