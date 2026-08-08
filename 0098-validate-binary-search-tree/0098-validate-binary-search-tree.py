class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        def check(node, low, high):
            if not node:
                return 0

            if node.val <= low or node.val >= high:
                return -1

            lh = check(node.left, low, node.val)
            rh = check(node.right, node.val, high)

            if lh == -1 or rh == -1:
                return -1

            return 0

        t = check(root, float('-inf'), float('inf'))

        return t == 0