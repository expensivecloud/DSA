"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """

        if not node:
            return None

        clones = {}

        clones[node] = Node(node.val)

        q = deque([node])

        while q:

            curr = q.popleft()

            for nei in curr.neighbors:

                if nei not in clones:
                    clones[nei] = Node(nei.val)
                    q.append(nei)

                clones[curr].neighbors.append(clones[nei])

        return clones[node]