class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        binary = str(bin(n))

        prev = -1
        ans = 0

        for i in range(len(binary)):
            if binary[i] == '1':
                if prev != -1:
                    ans = max(ans, i - prev)
                prev = i

        return ans