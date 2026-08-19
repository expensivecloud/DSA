import heapq

class Solution(object):
    def maxProbability(self, n, edges, succProb, start_node, end_node):

        graph = [[] for _ in range(n)]

        for i in range(len(edges)):
            u = edges[i][0]
            v = edges[i][1]
            prob = succProb[i]

            graph[u].append((v, prob))
            graph[v].append((u, prob))

        dist = [0.0] * n
        dist[start_node] = 1.0

        pq = [(-1.0, start_node)]

        while pq:

            neg_prob, u = heapq.heappop(pq)
            prob = -neg_prob

            if prob < dist[u]:
                continue

            if u == end_node:
                return prob

            for v, edge_prob in graph[u]:

                new_prob = prob * edge_prob

                if new_prob > dist[v]:
                    dist[v] = new_prob
                    heapq.heappush(pq, (-new_prob, v))

        return 0.0