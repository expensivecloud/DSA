class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """

        n1set = set(nums1)
        n2set = set(nums2)

        ans1 = []
        ans2 = []

        for x in n1set:
            if x not in n2set:
                ans1.append(x)

        for x in n2set:
            if x not in n1set:
                ans2.append(x)

        return [ans1, ans2]