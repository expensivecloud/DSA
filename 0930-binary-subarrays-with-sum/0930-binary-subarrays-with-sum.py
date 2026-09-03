class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        curr = 0
        ans = 0

        mp = {0: 1}

        for num in nums:
            curr += num

            if curr - goal in mp:
                ans += mp[curr - goal]

            mp[curr] = mp.get(curr, 0) + 1

        return ans
        