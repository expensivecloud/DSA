# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        val = root.val
        q = deque([root])

        while q:
            node = q.popleft()

            if node.val != val:
                return False

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)

        return True