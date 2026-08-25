class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        n = len(edges)

        parent = list(range(n + 1))
        size = [1] * (n + 1)

        def findP(node):
            if parent[node] != node:
                parent[node] = findP(parent[node])

            return parent[node]

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

        for u, v in edges:

            if not union(u, v):
                return [u, v]