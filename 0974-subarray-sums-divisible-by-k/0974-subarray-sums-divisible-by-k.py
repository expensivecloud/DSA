class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        curr = 0
        ans = 0

        mp = {0: 1}

        for num in nums:
            curr += num

            rem = curr % k

            if rem in mp:
                ans += mp[rem]

            mp[rem] = mp.get(rem, 0) + 1

        return ans