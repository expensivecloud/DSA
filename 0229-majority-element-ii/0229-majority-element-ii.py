class Solution(object):
    def majorityElement(self, nums):
        candidate1 = None
        candidate2 = None
        count1 = 0
        count2 = 0

        # First pass: find candidates
        for num in nums:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        # Second pass: verify
        count1 = 0
        count2 = 0

        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1

        ans = []
        threshold = len(nums) // 3

        if count1 > threshold:
            ans.append(candidate1)

        if count2 > threshold:
            ans.append(candidate2)

        return ans