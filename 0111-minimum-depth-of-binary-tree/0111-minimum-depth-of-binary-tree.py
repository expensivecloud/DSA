from collections import deque

class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0

        q = deque([root])
        dep = 1

        while q:

            for _ in range(len(q)):
                node = q.popleft()

                # Leaf node
                if not node.left and not node.right:
                    return dep

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            dep += 1