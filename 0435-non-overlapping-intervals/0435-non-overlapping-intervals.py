class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x: x[1])

        count = 0
        last_end = float('-inf')

        for st,et in intervals:
            if st >= last_end:
                last_end = et
            else:
                count += 1

        return count