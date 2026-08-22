from collections import deque

class Solution(object):
    def shortestAlternatingPaths(self, n, redEdges, blueEdges):
        """
        :type n: int
        :type redEdges: List[List[int]]
        :type blueEdges: List[List[int]]
        :rtype: List[int]
        """

        graph = [[] for _ in range(n)]

        for u, v in redEdges:
            graph[u].append((v, 'r'))

        for u, v in blueEdges:
            graph[u].append((v, 'b'))

        ans = [-1] * n
        ans[0] = 0

        q = deque()

        # Start with both colors
        q.append((0, 'r'))
        q.append((0, 'b'))

        visited = [[False, False] for _ in range(n)]

        visited[0][0] = True
        visited[0][1] = True

        distance = 0

        while q:

            # Process one BFS level
            for _ in range(len(q)):

                node, current_color = q.popleft()

                # We can only take the opposite color
                if current_color == 'r':
                    next_color = 'b'
                    color_index = 1
                else:
                    next_color = 'r'
                    color_index = 0

                for nei, edge_color in graph[node]:

                    if edge_color != next_color:
                        continue

                    if visited[nei][color_index]:
                        continue

                    visited[nei][color_index] = True

                    if ans[nei] == -1:
                        ans[nei] = distance + 1

                    q.append((nei, next_color))

            distance += 1

        return ans