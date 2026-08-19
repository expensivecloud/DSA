import heapq

class Solution(object):
    def networkDelayTime(self, times, n, k):

        graph = [[] for _ in range(n + 1)]

        for u, v, weight in times:
            graph[u].append((v, weight))

        dist = [float('inf')] * (n + 1)
        dist[k] = 0

        pq = [(0, k)]

        while pq:
            d, u = heapq.heappop(pq)

            if d > dist[u]:
                continue

            for v, weight in graph[u]:

                new_dist = d + weight

                if new_dist < dist[v]:
                    dist[v] = new_dist
                    heapq.heappush(pq, (new_dist, v))

        ans = max(dist[1:])

        if ans == float('inf'):
            return -1

        return ans