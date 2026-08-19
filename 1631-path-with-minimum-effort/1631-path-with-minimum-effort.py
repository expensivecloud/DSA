import heapq
class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        n = len(heights)
        m = len(heights[0])

        dist = [[float('inf')]*m for _ in range(n)]
        dist[0][0] = 0

        dirs = [(1,0),(0,1),(-1,0),(0,-1)]

        pq = [(0,0,0)]

        while pq:
            d,x,y = heapq.heappop(pq)

            if d > dist[x][y]:
                continue
            
            for dx,dy in dirs:
                nx = x+dx
                ny = y+dy

                if 0 <= nx < n and 0 <= ny < m:
                    weight = abs(heights[nx][ny] - heights[x][y])
                    new_dist = max(d, weight)

                    if new_dist < dist[nx][ny]:
                        dist[nx][ny] = new_dist
                        heapq.heappush(pq,(new_dist,nx,ny))

        return dist[n-1][m-1] 

            