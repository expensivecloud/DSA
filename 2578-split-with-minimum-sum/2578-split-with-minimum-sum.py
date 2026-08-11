class Solution(object):
    def splitNum(self, num):
        """
        :type num: int
        :rtype: int
        """

        ns = str(num)
        ns = sorted(ns)

        num1 = ""
        num2 = ""

        for i in range(len(ns)):
            if i % 2 == 0:
                num1 += ns[i]
            else:
                num2 += ns[i]

        return int(num1) + int(num2)