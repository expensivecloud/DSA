class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        mp = {}

        for i in range(len(nums)):
            if nums[i] in mp:
                if i - mp[nums[i]] <= k:
                    return True

            mp[nums[i]] = i

        return False