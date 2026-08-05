class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        res = []

        for num in nums1:
            found = False
            ans = -1

            for x in nums2:
                if x == num:
                    found = True
                elif found and x > num:
                    ans = x
                    break

            res.append(ans)

        return res