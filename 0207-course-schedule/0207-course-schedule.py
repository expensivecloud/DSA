class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for v,u in prerequisites:
            graph[u].append(v)
            indegree[v] += 1

        q = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        ans = 0
        while q:
            node = q.popleft()
            ans += 1

            for nri in graph[node]:
                indegree[nri] -= 1

                if indegree[nri] == 0:
                    q.append(nri)

        return ans == numCourses