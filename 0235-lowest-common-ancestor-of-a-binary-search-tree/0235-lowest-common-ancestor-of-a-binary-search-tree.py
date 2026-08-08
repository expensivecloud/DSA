# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return 

        curr = root.val
        #if both on left go left
        if curr < p.val and curr < q.val:
            return self.lowestCommonAncestor(root.right,p,q)
        #if bothh on right go right
        if curr > p.val and curr > q.val:
            return self.lowestCommonAncestor(root.left,p,q)
        #else lca
        return root