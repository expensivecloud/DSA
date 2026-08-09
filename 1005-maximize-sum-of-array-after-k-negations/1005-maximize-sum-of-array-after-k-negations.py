class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()

        i = 0

        while i < len(nums) and k > 0:
            if nums[i] < 0:
                nums[i] = -nums[i]
                k -= 1
                i += 1
            else:
                break

        nums.sort()

        if k % 2 != 0:
            nums[0] = -nums[0]

        return sum(nums)