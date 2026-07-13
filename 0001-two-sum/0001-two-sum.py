class Solution(object):
    def twoSum(self, nums, target):
    
        low = 0
        high = len(nums) - 1

        arr=[]
        for i in range (len(nums)):
            arr.append((nums[i],i))

        arr.sort()

        while(low < high):
            curr = arr[low][0] + arr[high][0]

            if curr == target:
                return [arr[low][1], arr[high][1]]
            
            if curr < target:
                low+=1
            if curr > target:
                high-=1
        