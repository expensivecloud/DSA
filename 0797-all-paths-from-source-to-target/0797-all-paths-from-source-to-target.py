class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """

        n = len(graph)
        res = []
        path = []

        def dfs(u):
            path.append(u)

            if u == n - 1:
                res.append(path[:])
            else:
                for v in graph[u]:
                    dfs(v)

            path.pop()

        dfs(0)

        return res