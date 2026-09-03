class Solution(object):
    def subarraySum(self, nums, k):
        curr = 0
        ans = 0

        mp = {0: 1}

        for num in nums:
            curr += num

            if curr - k in mp:
                ans += mp[curr - k]

            mp[curr] = mp.get(curr, 0) + 1

        return ans
        