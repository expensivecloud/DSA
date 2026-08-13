class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)

        mp = {}

        for i in range(n):
            mp[nums[i]] = mp.get(nums[i], 0) + 1

        ans = 0

        for x in mp:
            if x + 1 in mp:
                ans = max(ans, mp[x] + mp[x + 1])

        return ans