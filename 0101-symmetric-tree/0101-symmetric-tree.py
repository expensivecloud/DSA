class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        if not root:
            return True

        leftsub = root.left
        rightsub = root.right

        def dfs(p, q):
            if not p and not q:
                return True

            if not p or not q:
                return False

            if p.val != q.val:
                return False

            return (dfs(p.left, q.right) and
                    dfs(p.right, q.left))

        return dfs(leftsub, rightsub)