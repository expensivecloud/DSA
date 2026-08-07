from collections import deque

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """

        queue = deque([(p, q)])

        while queue:
            left, right = queue.popleft()

            # Both nodes are None
            if not left and not right:
                continue

            # One is None, the other isn't
            if not left or not right:
                return False

            # Values are different
            if left.val != right.val:
                return False

            # Compare corresponding children
            queue.append((left.left, right.left))
            queue.append((left.right, right.right))

        return True