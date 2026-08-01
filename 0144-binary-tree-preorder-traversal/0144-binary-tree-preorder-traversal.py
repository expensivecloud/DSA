# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        ans = []

        def Preorder(node):
            if node is None:
                return

            ans.append(node.val)
            Preorder(node.left)
            Preorder(node.right)

        Preorder(root)
        return ans

        


