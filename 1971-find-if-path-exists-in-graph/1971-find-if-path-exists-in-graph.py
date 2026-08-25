class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """

        parent = list(range(n))
        size = [1] * n

        def findP(node):
            if parent[node] != node:
                parent[node] = findP(parent[node])
            return parent[node]

        def union(a, b):
            pa = findP(a)
            pb = findP(b)

            if pa == pb:
                return

            if size[pa] < size[pb]:
                pa, pb = pb, pa

            parent[pb] = pa
            size[pa] += size[pb]

        for u, v in edges:
            union(u, v)

        return findP(source) == findP(destination)