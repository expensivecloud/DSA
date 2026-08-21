from collections import deque

class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """

        n = len(rooms)

        visited = [False] * n
        visited[0] = True

        q = deque([0])

        while q:

            room = q.popleft()

            for key in rooms[room]:

                if not visited[key]:
                    visited[key] = True
                    q.append(key)

        for i in range(n):
            if not visited[i]:
                return False

        return True