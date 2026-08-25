class Solution(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """

        parent = list(range(26))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            pa = find(a)
            pb = find(b)

            if pa != pb:
                parent[pb] = pa

        for eq in equations:
            if eq[1:3] == "==":
                a = ord(eq[0]) - ord('a')
                b = ord(eq[3]) - ord('a')

                union(a, b)

        for eq in equations:
            if eq[1:3] == "!=":
                a = ord(eq[0]) - ord('a')
                b = ord(eq[3]) - ord('a')

                if find(a) == find(b):
                    return False

        return True