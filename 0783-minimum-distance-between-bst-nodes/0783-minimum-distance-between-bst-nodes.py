from collections import deque

class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        q = deque([root])
        values = []

        while q:
            node = q.popleft()
            values.append(node.val)

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)

        values.sort()

        min_diff = float('inf')

        for i in range(1, len(values)):
            min_diff = min(min_diff, values[i] - values[i - 1])

        return min_diff
