class Solution(object):
    def findOrder(self, numCourses, prerequisites):
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
        
        ans = []
        while q:
            node = q.popleft()
            ans.append(node)

            for nri in graph[node]:
                indegree[nri] -= 1

                if indegree[nri] == 0:
                    q.append(nri)

        if len(ans) != numCourses:
            return []

        return ans