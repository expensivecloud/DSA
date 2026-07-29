class Solution(object):
    def sortColors(self, nums):
        zeros = 0
        ones = 0
        twos = 0

        for num in nums:
            if num == 0:
                zeros += 1
            elif num == 1:
                ones += 1
            else:
                twos += 1
                
        i = 0

        for _ in range(zeros):
            nums[i] = 0
            i += 1

        for _ in range(ones):
            nums[i] = 1
            i += 1

        for _ in range(twos):
            nums[i] = 2
            i += 1