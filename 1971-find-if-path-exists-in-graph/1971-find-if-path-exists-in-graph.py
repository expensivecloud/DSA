from collections import deque

class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """

        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        q = deque([source])
        visited = [False] * n
        visited[source] = True

        while q:
            node = q.popleft()

            if node == destination:
                return True

            for nxt in graph[node]:

                if not visited[nxt]:
                    visited[nxt] = True
                    q.append(nxt)

        return False