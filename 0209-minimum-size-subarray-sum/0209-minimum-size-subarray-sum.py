class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, 0
        total = 0
        ans = float('inf')

        while right < len(nums):

            total += nums[right]

            while total >= target:
                ans = min(ans, right - left + 1)

                total -= nums[left]
                left += 1

            right += 1

        if ans == float('inf'):
            return 0

        return ans