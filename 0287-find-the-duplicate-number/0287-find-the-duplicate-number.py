class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=set()
        
        for c in nums:
            if c in s:
                return c
            else:
                s.add(c)