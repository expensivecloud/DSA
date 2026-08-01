class Solution(object):
    def sortedSquares(self, nums):

        n = len(nums)
        res = [0] * n

        left = 0
        right = n - 1
        pos = n - 1

        while left <= right:

            l2 = nums[left] ** 2
            r2 = nums[right] ** 2

            if l2 > r2:
                res[pos] = l2
                left += 1
            else:
                res[pos] = r2
                right -= 1

            pos -= 1

        return res
        
        for i in range(len(nums)):
            nums[i] = nums[i] * nums[i]

        return sorted(nums)