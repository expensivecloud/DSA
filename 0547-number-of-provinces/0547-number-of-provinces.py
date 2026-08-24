from collections import deque

class Solution(object):
    def findCircleNum(self, isConnected):

        n = len(isConnected)

        parent = list(range(n))
        size = [1] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a,b):
            pa = find(a)
            pb = find(b)

            if pa == pb:
                return False

            if size[pa] < size[pb]:
                pa, pb = pb, pa

            parent[pb] = pa
            size[pa] += size[pb]

            return True

        provinces = n

        for i in range(n):
            for j in range(i+1,n):

                if isConnected[i][j] == 1:

                    if union(i,j):
                        provinces -= 1

        return provinces

                