# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        nums = []

        def f(node):
            if not node:
                return

            f(node.left)
            nums.append(node.val)
            f(node.right)

        f(root)

        freq = {}

        for num in nums:
            freq[num] = freq.get(num,0) + 1

        maxi = max(freq.values())

        res = []
        for num in freq:
            if freq[num] == maxi:
                res.append(num)

        return res