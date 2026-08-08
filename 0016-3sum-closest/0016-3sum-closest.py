class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)

        min_diff = float('inf')
        best_sum = 0

        for i in range(n):
            left = i + 1
            right = n-1

            while left < right:
                sumo = nums[left] + nums[right] + nums[i]
                diff = abs(target-sumo)

                if min_diff > diff:
                    min_diff = diff
                    best_sum = sumo

                if sumo == target:
                    return sumo

                if sumo > target:
                    right -= 1
                else:
                    left += 1
        
        return best_sum