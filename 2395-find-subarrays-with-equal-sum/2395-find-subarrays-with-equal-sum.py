class Solution(object):
    def findSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        seen = set()

        for i in range(len(nums) - 1):
            curr = nums[i] + nums[i + 1]

            if curr in seen:
                return True

            seen.add(curr)

        return False