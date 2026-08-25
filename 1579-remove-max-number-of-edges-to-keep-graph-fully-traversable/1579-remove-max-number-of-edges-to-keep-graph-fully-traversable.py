class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)
        self.components = n

    def findP(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.findP(self.parent[x])

        return self.parent[x]

    def union(self, a, b):
        pa = self.findP(a)
        pb = self.findP(b)

        if pa == pb:
            return False

        if self.size[pa] < self.size[pb]:
            pa, pb = pb, pa

        self.parent[pb] = pa
        self.size[pa] += self.size[pb]

        self.components -= 1

        return True


class Solution(object):
    def maxNumEdgesToRemove(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """

        alice = DSU(n)
        bob = DSU(n)

        used = 0

        # Type 3 first
        for typ, u, v in edges:
            if typ == 3:

                a = alice.union(u, v)
                b = bob.union(u, v)

                if a or b:
                    used += 1

        for typ, u, v in edges:
            if typ == 1:
                if alice.union(u, v):
                    used += 1

        for typ, u, v in edges:
            if typ == 2:
                if bob.union(u, v):
                    used += 1

        if alice.components != 1 or bob.components != 1:
            return -1

        return len(edges) - used