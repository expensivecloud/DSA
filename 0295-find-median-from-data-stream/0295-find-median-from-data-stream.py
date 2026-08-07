class MedianFinder(object):

    def __init__(self):
        self.nums = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """       
        left = 0
        right = len(self.nums)

        while left < right:
            mid = (left + right) // 2

            if self.nums[mid] < num:
                left = mid + 1
            else:
                right = mid

        self.nums.insert(left, num)
            
    def findMedian(self):
        """
        :rtype: float
        """
        n = len(self.nums)

        if n % 2 == 1:
            return self.nums[n // 2]

        return (self.nums[n // 2 - 1] + self.nums[n // 2]) / 2.0
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()