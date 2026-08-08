# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        nums = []

        def dfs(node):
            if not node:
                return 

            dfs(node.left)
            nums.append(node.val)
            dfs(node.right)

        dfa(root)

        return nums[k-1]