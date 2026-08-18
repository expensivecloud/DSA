from collections import deque

class Solution(object):
    def connect(self, root):
        if not root:
            return None

        q = deque([root])

        while q:
            level = []

            for _ in range(len(q)):
                node = q.popleft()

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

                level.append(node)

            for i in range(len(level) - 1):
                level[i].next = level[i + 1]

            level[-1].next = None

        return root