class Solution(object):
    def sumDivisibleByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        mp = {}

        for i in range(len(nums)):
            mp[nums[i]] = 1 + mp.get(nums[i], 0)

        sumo = 0

        for key, values in mp.items():
            if values % k == 0:
                v = key * values
                sumo += v

        return sumo