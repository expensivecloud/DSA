# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        res = []
        path = []

        def dfs(node,currSum):

            if not node:
                return False

            path.append(node.val)
            currSum += node.val

            if not node.left and not node.right:
                if currSum == targetSum:
                    res.append(path[:])

            dfs(node.left, currSum)
            dfs(node.right, currSum)

            path.pop()

        
        dfs(root,0)
        return res