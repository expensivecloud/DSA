class Solution(object):
    def friendRequests(self, n, restrictions, requests):
        """
        :type n: int
        :type restrictions: List[List[int]]
        :type requests: List[List[int]]
        :rtype: List[bool]
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

        res = []

        for u, v in requests:

            pu = findP(u)
            pv = findP(v)

            allowed = True

            for x, y in restrictions:

                px = findP(x)
                py = findP(y)

                if (pu == px and pv == py) or (pu == py and pv == px):
                    allowed = False
                    break

            if allowed:
                res.append(True)
                union(u, v)
            else:
                res.append(False)

        return res