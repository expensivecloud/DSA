class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        mp = {}

        for right in range(len(nums)):
            if nums[right] in mp:
                left = mp[nums[right]]

                if right - left <= k:
                    return True

            mp[nums[right]] = right

        return False