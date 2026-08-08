# Definition for a binary tree node.
# class TreeNode(object):
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """

        self.prev = None

        def flatt(node):
            if not node:
                return

            flatt(node.right)
            flatt(node.left)

            node.right = self.prev
            node.left = None

            self.prev = node

        flatt(root)
