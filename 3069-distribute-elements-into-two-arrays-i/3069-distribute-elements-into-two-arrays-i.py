class Solution(object):
    def resultArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr1 = [nums[0]]
        arr2 = [nums[1]]

        last_1 = nums[0]
        last_2 = nums[1]

        for i in range(2,len(nums)):
            if last_1 > last_2:
                arr1.append(nums[i])
                last_1 = nums[i]
            else:
                arr2.append(nums[i])
                last_2 = nums[i]

        return arr1+arr2

