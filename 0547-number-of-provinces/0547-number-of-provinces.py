from collections import deque

class Solution(object):
    def findCircleNum(self, isConnected):

        n = len(isConnected)

        visited = [False] * n

        provinces = 0

        for i in range(n):

            if not visited[i]:

                provinces += 1

                q = deque([i])
                visited[i] = True

                while q:

                    city = q.popleft()

                    for j in range(n):

                        if isConnected[city][j] == 1 and not visited[j]:

                            visited[j] = True
                            q.append(j)

        return provinces