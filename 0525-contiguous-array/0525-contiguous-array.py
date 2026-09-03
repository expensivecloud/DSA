class Solution(object):
    def findMaxLength(self, nums):
        mp = {0: -1}

        curr = 0
        ans = 0

        for i in range(len(nums)):

            if nums[i] == 0:
                curr -= 1
            else:
                curr += 1

            if curr in mp:
                ans = max(ans, i - mp[curr])
            else:
                mp[curr] = i

        return ans