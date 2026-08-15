class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        arr = []
        for row in matrix:
            arr += row

        left = 0
        right = len(arr) - 1
        while left<=right:
            mid = (left+right)//2

            if arr[mid] == target:
                return True

            if arr[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return False