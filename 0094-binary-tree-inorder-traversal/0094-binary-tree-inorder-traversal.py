# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        ans = []

        def Inorder(root,ans):
            if root is None:
                return 

            Inorder(root.left,ans)
            ans.append(root.val)
            Inorder(root.right,ans)

            return

        Inorder(root,ans)
        return ans