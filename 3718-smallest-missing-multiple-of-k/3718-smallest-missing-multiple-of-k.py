class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nooms = set(nums)
        num = k

        while True:
            if num not in nooms:
                return num
            num += k

        

