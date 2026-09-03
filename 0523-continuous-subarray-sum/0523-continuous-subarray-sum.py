class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        curr = 0

        mp = {0: -1}

        for i in range(len(nums)):
            curr += nums[i]

            rem = curr % k

            if rem in mp:
                if i - mp[rem] >= 2:
                    return True
            else:
                mp[rem] = i

        return False