from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        dr = [(1,0),(-1,0),(0,1),(0,-1)]

        q = deque()
        fresh = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if grid[i][j] == 1:
                    fresh += 1

                if grid[i][j] == 2:
                    q.append([i,j,0])

        ans = 0

        while q:
            x,y,t = q.popleft()
            ans = max(ans,t)

            for dx,dy in dr:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1:
                    grid[nx][ny] = 2
                    fresh -= 1
                    q.append([nx,ny,t+1])


        return ans if fresh == 0 else -1

